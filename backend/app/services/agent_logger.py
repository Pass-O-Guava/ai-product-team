"""
Agent Execution Logger — 记录所有 OpenClaw Agent 调用，提供可观测性。
每条记录包含：agent_id / 输入参数 / 实际输出 / 执行时长 / 状态 / step归属
"""
import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from app.config import DATA_DIR

LOG_DIR = DATA_DIR / "agent_logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)


class AgentLogEntry:
    """单次 Agent 调用记录"""

    def __init__(
        self,
        agent_id: str,
        task: str,
        params: Optional[dict[str, Any]] = None,
        run_id: Optional[str] = None,
        step_name: Optional[str] = None,
    ):
        self.id = str(uuid.uuid4())
        self.agent_id = agent_id
        self.task = task
        self.params = params or {}
        self.run_id = run_id
        self.step_name = step_name
        self.started_at = datetime.utcnow()
        self.finished_at: Optional[datetime] = None
        self.output: Optional[str] = None   # 实际输出（截取前2000字）
        self.error: Optional[str] = None
        self.status: str = "running"  # running | success | error | timeout

    def complete(self, output: Any, status: str = "success") -> None:
        self.finished_at = datetime.utcnow()
        self.status = status
        # 截取输出前2000字防过大
        text = str(output)
        self.output = text[:2000] if len(text) > 2000 else text
        if len(text) > 2000:
            self.output += f"\n... [截断，原始长度 {len(text)} 字]"
        self._save()

    def fail(self, error: str) -> None:
        self.finished_at = datetime.utcnow()
        self.status = "error"
        self.error = str(error)[:500]
        self._save()

    def duration_ms(self) -> Optional[int]:
        if self.finished_at and self.started_at:
            return int((self.finished_at - self.started_at).total_seconds() * 1000)
        return None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "agent_id": self.agent_id,
            "task": self.task,
            "params": self.params,
            "run_id": self.run_id,
            "step_name": self.step_name,
            "started_at": self.started_at.isoformat(),
            "finished_at": self.finished_at.isoformat() if self.finished_at else None,
            "duration_ms": self.duration_ms(),
            "output": self.output,
            "error": self.error,
            "status": self.status,
        }

    def _log_path(self) -> Path:
        # 按 run_id + 日期分目录
        date_str = self.started_at.strftime("%Y-%m-%d")
        run_str = self.run_id or "orphaned"
        d = LOG_DIR / date_str / run_str
        d.mkdir(parents=True, exist_ok=True)
        return d / f"{self.id}.json"

    def _save(self) -> None:
        path = self._log_path()
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)


# ─── 全局日志记录器（内存缓存）────────────────────────────────────────────────

class AgentLogger:
    """所有 Agent 调用的统一日志管理器"""

    def _log_file_for(run_id: str, agent_id: str, log_id: str) -> Path:
        date_str = datetime.utcnow().strftime("%Y-%m-%d")
        d = LOG_DIR / date_str / (run_id or "orphaned")
        d.mkdir(parents=True, exist_ok=True)
        return d / f"{log_id}.json"

    def invoke(
        agent_id: str,
        task: str,
        params: Optional[dict[str, Any]] = None,
        run_id: Optional[str] = None,
        step_name: Optional[str] = None,
        executor=None,  # callable(task, params) -> output
    ) -> dict[str, Any]:
        """
        包装一次 Agent 调用：记录输入 → 执行 → 记录输出/错误 → 返回。
        executor 是实际执行函数，默认用 openclaw_client。
        """
        entry = AgentLogEntry(
            agent_id=agent_id,
            task=task,
            params=params,
            run_id=run_id,
            step_name=step_name,
        )
        # 先写 running 状态
        entry._save()

        if executor is None:
            from app.services.openclaw_client import client
            executor = lambda t, p: client.invoke(t, p)

        try:
            output = executor(task, params)
            entry.complete(output, status="success")
            return {"log_id": entry.id, "status": "success", "output": output}
        except Exception as exc:
            entry.fail(str(exc))
            return {
                "log_id": entry.id,
                "status": "error",
                "error": str(exc),
                "output": None,
            }

    @staticmethod
    def get_logs(run_id: str, limit: int = 50) -> list[dict]:
        """读取指定 run 的所有 agent 日志"""
        date_str = datetime.utcnow().strftime("%Y-%m-%d")
        run_dir = LOG_DIR / date_str / run_id
        if not run_dir.exists():
            return []
        logs = []
        for f in sorted(run_dir.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)[:limit]:
            try:
                with open(f, encoding="utf-8") as fp:
                    logs.append(json.load(fp))
            except Exception:
                pass
        return logs

    @staticmethod
    def get_all_logs(date: Optional[str] = None, limit: int = 100) -> list[dict]:
        """读取所有日志（可按日期过滤）"""
        date_str = date or datetime.utcnow().strftime("%Y-%m-%d")
        logs = []
        for run_dir in (LOG_DIR / date_str).iterdir():
            if not run_dir.is_dir():
                continue
            for f in sorted(run_dir.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)[:20]:
                try:
                    with open(f, encoding="utf-8") as fp:
                        logs.append(json.load(fp))
                except Exception:
                    pass
            if len(logs) >= limit:
                break
        return sorted(logs, key=lambda x: x["started_at"], reverse=True)[:limit]

    @staticmethod
    def list_runs_with_logs() -> list[str]:
        """返回有日志的 run_id 列表"""
        date_str = datetime.utcnow().strftime("%Y-%m-%d")
        run_dir = LOG_DIR / date_str
        if not run_dir.exists():
            return []
        return [d.name for d in run_dir.iterdir() if d.is_dir()]
