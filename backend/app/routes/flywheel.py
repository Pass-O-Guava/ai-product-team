"""
Knowledge Flywheel — 真实的智能体协作调度路由。
每个步骤对应一个 OpenClaw Agent 调用，结果写入状态文件。
"""
import asyncio
import uuid
from datetime import datetime
from typing import Any

from fastapi import APIRouter, BackgroundTasks, HTTPException

from app.config import RunState
from app.models import (
    FlywheelTrigger,
    FlywheelTriggerResponse,
    RunStatus,
)
from app.services import status_manager as sm
from app.services.self_evolution import (
    get_evolution_log,
    get_next_iteration,
    get_skills_index,
    run_self_evolution,
)
from app.services.openclaw_client import client

router = APIRouter(prefix="/flywheel", tags=["Flywheel"])


# ─── Agent Invocations ────────────────────────────────────────────────────────

def _coa(task: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    """
    调用 OpenClaw Agent（通过 subprocess CLI）。
    失败时不抛异常，只记录错误。
    """
    try:
        return client.invoke(task, params)
    except Exception as exc:
        return {"error": str(exc)}


def _step(run_id: str, name: str, message: str = "") -> None:
    """推进到指定步骤（写入状态文件）。"""
    sm.advance_step(run_id, name, message)


# ─── Flywheel 真实执行流程 ────────────────────────────────────────────────────

def _run_flywheel_sync(run_id: str, model_ids: list[str], force: bool) -> None:
    """
    真实的知识飞轮执行流程。
    每个步骤顺序执行，对应一个 OpenClaw Agent 调用。
    """
    started_at = datetime.utcnow().isoformat()

    try:
        # ── Step 0: trigger ────────────────────────────────────────────────
        _step(run_id, "trigger", f"知识飞轮启动 · run_id={run_id} · {started_at}")

        # ── Step 1: dispatch — Coordinator 分配任务 ──────────────────────────
        _step(run_id, "dispatch", "Coordinator 正在分配调研任务…")
        dispatch_result = _coa("coordinator", {
            "action": "dispatch",
            "model_ids": model_ids,
            "run_id": run_id,
        })
        dispatch_summary = dispatch_result.get("output", "") or str(dispatch_result)
        _step(run_id, "dispatch", f"任务已分配：{dispatch_summary[:80]}")

        # ── Step 2: research — 各类模型 Scout Agent 并行调研 ─────────────────
        _step(run_id, "research", "Scout Agents 正在调研…")

        # 按模型类别分组，触发对应的 Scout Agent
        category_agents: dict[str, str] = {
            "Text":     "text-researcher",
            "VLM":      "vlm-researcher",
            "ALM":      "alm-researcher",
            "Video":    "video-researcher",
            "Unified":  "unified-researcher",
            "Embedding": "embedding-researcher",
        }

        research_results: dict[str, Any] = {}
        # 从 manifest 获取模型列表（如果没有指定 model_ids）
        from app.services import knowledge_store as store
        all_models = store.list_all_ids() if hasattr(store, "list_all_ids") else []

        targets = model_ids if model_ids else all_models[:10]  # 最多10个

        for mid in targets:
            meta = store.read_meta(mid) if hasattr(store, "read_meta") else None
            if not meta:
                continue
            cat = getattr(meta, "category", "Text") if meta else "Text"
            agent = category_agents.get(cat, "text-researcher")
            r = _coa(agent, {"model_id": mid, "run_id": run_id})
            research_results[mid] = {
                "agent": agent,
                "status": "done" if "error" not in r else "error",
                "output": r.get("output", "")[:200] if r else "",
            }

        researched = [k for k, v in research_results.items() if v["status"] == "done"]
        _step(run_id, "research", f"调研完成：{len(researched)}/{len(targets)} 个模型")

        # ── Step 3: qc_review — QC Agent 质检 ─────────────────────────────
        _step(run_id, "qc_review", "QC Agent 正在进行质量审查…")
        qc_result = _coa("qc-agent", {
            "action": "qc_review",
            "model_ids": researched,
            "run_id": run_id,
        })
        qc_passed = qc_result.get("passed", [])
        qc_failed = qc_result.get("failed", [])
        qc_rejected = qc_result.get("rejected", [])

        # 读取质检拦截记录（用于 Truth Filter）
        qc_summary = (
            f"通过{qc_result.get('passed_count', len(qc_passed))}个，"
            f"P0拦截{qc_result.get('p0_count', len(qc_rejected))}个，"
            f"P1拦截{qc_result.get('p1_count', len(qc_failed))}个"
        )
        _step(run_id, "qc_review", qc_summary)

        # ── Step 4: archive — Archiver 归档到 GitHub ────────────────────────
        _step(run_id, "archive", "Archiver 正在同步文档到 GitHub…")
        archive_result = _coa("archiver", {
            "action": "archive",
            "model_ids": qc_passed,
            "run_id": run_id,
        })
        archive_summary = archive_result.get("output", "") or "文档已同步"
        _step(run_id, "archive", str(archive_summary)[:100])

        # ── Step 5: self_review — Skills 自进化 ────────────────────────────
        _step(run_id, "self_review", "SelfReview Agent 正在分析失误模式…")

        # 从质检结果中提取失误记录
        recent_mistakes = qc_result.get("mistakes", [])
        total入库 = len(qc_passed)
        p0拦截数 = len(qc_rejected)
        p0_rate = p0拦截数 / max(total入库, 1)

        evolution_result = run_self_evolution(
            run_id=run_id,
            recent_mistakes=recent_mistakes,
            total入库=total入库,
            p0_rate=p0_rate,
        )

        if evolution_result["triggered"]:
            ev_msg = (
                f"触发 Skills 自进化！原因：{evolution_result['trigger_reason']}。"
                f"更新 Skills：{', '.join(evolution_result['skills_updated'])}。"
                f"发现 {len(evolution_result['patterns_found'])} 个失误模式。"
            )
        else:
            ev_msg = f"未达到触发阈值。{evolution_result['trigger_reason']}"
        _step(run_id, "self_review", ev_msg)

        # ── Step 6: complete ────────────────────────────────────────────────
        sm.complete_run(run_id, {
            "models_researched": len(researched),
            "models_passed": len(qc_passed),
            "models_rejected": len(qc_rejected),
            "p0_count": p0拦截数,
            "skills_updated": evolution_result["skills_updated"],
            "evolution_triggered": evolution_result["triggered"],
            "evolution_reason": evolution_result["trigger_reason"],
            "iteration": evolution_result["iteration"],
            "finished_at": datetime.utcnow().isoformat(),
        })

    except Exception as exc:
        sm.fail_run(run_id, str(exc))


# ─── Routes ───────────────────────────────────────────────────────────────────

@router.post("/trigger", response_model=FlywheelTriggerResponse)
def trigger_flywheel(body: FlywheelTrigger, background_tasks: BackgroundTasks):
    """触发一轮知识飞轮（异步执行，立即返回 run_id）。"""
    # 前置验证：如果指定了 model_ids，验证它们存在
    if body.model_ids:
        from app.services import knowledge_store as store
        for mid in body.model_ids:
            if store.read_meta(mid) is None:
                raise HTTPException(status_code=404, detail=f"Model not found: {mid}")

    run_id = str(uuid.uuid4())
    sm.create_run(run_id=run_id, model_ids=body.model_ids)

    background_tasks.add_task(
        _run_flywheel_sync, run_id, body.model_ids, body.force
    )

    return FlywheelTriggerResponse(run_id=run_id, status="started")


@router.get("/status/{run_id}", response_model=RunStatus)
def get_flywheel_status(run_id: str):
    """查询指定 run 的详细状态。"""
    status = sm.get_run(run_id)
    if status is None:
        raise HTTPException(status_code=404, detail="Run not found")
    return status


@router.get("/evolution/status")
def get_evolution_status():
    """查询 Skills 自进化状态（供前端展示）。"""
    index = get_skills_index()
    log = get_evolution_log()
    next_iter = get_next_iteration()
    return {
        "skills_index": index,
        "recent_evolutions": log[:5],
        "next_iteration": next_iter,
    }
