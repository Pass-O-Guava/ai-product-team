"""OpenClaw agent wrapper using subprocess."""
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Optional

# Base path for imports
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # /workspace/sota-radar-backend


class OpenClawClient:
    """Thin wrapper around the OpenClaw CLI for agent invocation."""

    def __init__(self, binary: str = "openclaw"):
        self.binary = binary

    def invoke(self, task: str, params: Optional[dict[str, Any]] = None) -> dict[str, Any]:
        """
        Invoke an OpenClaw agent/task via CLI.
        Returns parsed JSON output, or raises RuntimeError.
        """
        args = [self.binary, "invoke", task]
        if params:
            args.append("--params")
            args.append(json.dumps(params))
        try:
            result = subprocess.run(
                args,
                capture_output=True,
                text=True,
                timeout=120,
            )
            if result.returncode != 0:
                raise RuntimeError(f"OpenClaw error: {result.stderr.strip()}")
            out = result.stdout.strip()
            if out:
                try:
                    return json.loads(out)
                except json.JSONDecodeError:
                    return {"output": out}
            return {}
        except subprocess.TimeoutExpired:
            raise RuntimeError(f"OpenClaw invoke timed out after 120s: {task}")
        except FileNotFoundError:
            raise RuntimeError(f"OpenClaw binary not found: {self.binary}")

    def is_available(self) -> bool:
        """Check whether the OpenClaw CLI is accessible."""
        try:
            subprocess.run(
                [self.binary, "--version"],
                capture_output=True,
                timeout=5,
            )
            return True
        except Exception:
            return False

    # ─── Flywheel: subagent tasks ────────────────────────────────────────────

    def run_research_task(self, model_id: str, task_type: str = "research") -> dict[str, Any]:
        """
        Run a research task via OpenClaw subagent (--local mode).
        The subagent inspects the model's HuggingFace / ModelScope pages and
        updates the knowledge file in the local store.
        """
        prompt = (
            f'你是一个专业的AI模型调研员。请对模型 "{model_id}" 进行调研：\n'
            "1. 检查该模型在 HuggingFace 和 ModelScope 上的最新信息\n"
            "2. 核实参数量、许可证、Benchmark 数据\n"
            "3. 如有必要，更新模型知识库文件（位于 /workspace/sota-radar-backend/app/data/models/{model_id}/knowledge.md）\n"
            "\n输出格式（仅 JSON，无其他内容）：\n"
            '{"findings": "...", "sota_claim": true/false, "confidence": "high/medium/low"}'
        ).format(model_id=model_id)

        try:
            result = subprocess.run(
                [self.binary, "agent", "--local", "--message", prompt, "--json"],
                capture_output=True,
                text=True,
                timeout=300,
            )
            stdout = result.stdout.strip()
            stderr = result.stderr.strip()

            # Try to parse JSON from stdout
            output = {}
            if stdout:
                try:
                    output = json.loads(stdout)
                except json.JSONDecodeError:
                    output = {"raw": stdout}

            return {
                "model_id": model_id,
                "output": output,
                "stdout": stdout,
                "error": stderr if result.returncode != 0 else "",
                "returncode": result.returncode,
            }
        except subprocess.TimeoutExpired:
            return {
                "model_id": model_id,
                "output": {},
                "stdout": "",
                "error": f"Research task timed out after 300s for model {model_id}",
                "returncode": -1,
            }
        except FileNotFoundError:
            return {
                "model_id": model_id,
                "output": {},
                "stdout": "",
                "error": f"OpenClaw binary not found: {self.binary}",
                "returncode": -1,
            }

    def run_qc_task(self, model_id: str, findings: dict) -> dict[str, Any]:
        """
        Run a QC check on research findings via OpenClaw subagent (--local mode).
        """
        findings_str = json.dumps(findings, ensure_ascii=False, indent=2)

        prompt = (
            f'请对以下模型调研结果进行质检。\n'
            f'模型：{model_id}\n'
            f'调研结果：{findings_str}\n\n'
            "检查项：\n"
            "1. 数据准确性（来源是否可靠）\n"
            "2. 日期是否为最新\n"
            "3. SOTA 声明是否有量化证据\n"
            "4. 许可证标注是否正确\n\n"
            "输出格式（仅 JSON，无其他内容）：\n"
            '{"passed": true/false, "issues": ["issue1", ...], "verdict": "pass/fail"}'
        )

        try:
            result = subprocess.run(
                [self.binary, "agent", "--local", "--message", prompt, "--json"],
                capture_output=True,
                text=True,
                timeout=180,
            )
            stdout = result.stdout.strip()
            stderr = result.stderr.strip()

            output = {}
            if stdout:
                try:
                    output = json.loads(stdout)
                except json.JSONDecodeError:
                    output = {"raw": stdout}

            return {
                "model_id": model_id,
                "qc_result": output,
                "stdout": stdout,
                "error": stderr if result.returncode != 0 else "",
                "returncode": result.returncode,
            }
        except subprocess.TimeoutExpired:
            return {
                "model_id": model_id,
                "qc_result": {},
                "stdout": "",
                "error": f"QC task timed out after 180s for model {model_id}",
                "returncode": -1,
            }
        except FileNotFoundError:
            return {
                "model_id": model_id,
                "qc_result": {},
                "stdout": "",
                "error": f"OpenClaw binary not found: {self.binary}",
                "returncode": -1,
            }


def run_full_flywheel_cycle(model_ids: Optional[list[str]] = None) -> dict[str, Any]:
    """
    Run a complete flywheel cycle:
      1. Get list of models to research (from knowledge store or provided list)
      2. For each model: run research task → run QC task
      3. Return consolidated results
    """
    import uuid
    from datetime import datetime

    client_local = OpenClawClient()
    run_id = str(uuid.uuid4())
    started_at = datetime.utcnow().isoformat()

    # Get all model IDs from knowledge store if none provided
    if not model_ids:
        try:
            # Dynamic import to avoid circular refs at module level
            from app.services.knowledge_store import list_model_ids
            model_ids = list_model_ids()
        except Exception:
            model_ids = []

    results: list[dict[str, Any]] = []
    for mid in model_ids:
        # Step 1: Research
        research = client_local.run_research_task(mid)
        # Step 2: QC
        qc = client_local.run_qc_task(mid, research.get("output", {}))
        results.append({
            "model_id": mid,
            "research": research,
            "qc": qc,
        })

    finished_at = datetime.utcnow().isoformat()
    return {
        "run_id": run_id,
        "started_at": started_at,
        "finished_at": finished_at,
        "models_processed": len(results),
        "results": results,
        "status": "COMPLETED",
    }


# ─── Module-level convenience helpers (backward-compatible) ───────────────────

def run_research_task(model_id: str, task_type: str = "research") -> dict[str, Any]:
    return client.run_research_task(model_id, task_type)


def run_qc_task(model_id: str, findings: dict) -> dict[str, Any]:
    return client.run_qc_task(model_id, findings)


def run_full_flywheel_cycle(model_ids: Optional[list[str]] = None) -> dict[str, Any]:
    return run_full_flywheel_cycle(model_ids)


# Global singleton (kept for backward compat)
client = OpenClawClient()
