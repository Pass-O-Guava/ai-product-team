"""
Knowledge Flywheel — 真实的智能体协作调度路由（含完整执行日志）。
每个步骤对应一个 OpenClaw Agent 调用，结果写入状态文件。
Agent 输出作为"证据"记录到 DAG Step Message 中。
"""
import uuid
from datetime import datetime
from typing import Any

from fastapi import APIRouter, BackgroundTasks, HTTPException

from app.models import FlywheelTrigger, FlywheelTriggerResponse, RunStatus
from app.services import status_manager as sm
from app.services.self_evolution import (
    get_evolution_log,
    get_next_iteration,
    get_skills_index,
    run_self_evolution,
)
from app.services.agent_logger import AgentLogger

router = APIRouter(prefix="/flywheel", tags=["Flywheel"])


# ─── Agent 调用（含日志）────────────────────────────────────────────────────

def _coa(
    task: str,
    params: dict[str, Any] | None = None,
    run_id: str = "",
    step_name: str = "",
) -> dict[str, Any]:
    """
    调用 OpenClaw Agent，结果记录到 agent_logger。
    返回 {log_id, status, output/error}，不抛异常。
    """
    return AgentLogger.invoke(
        agent_id=task,
        task=task,
        params=params,
        run_id=run_id,
        step_name=step_name,
    )


def _step(run_id: str, name: str, message: str = "") -> None:
    """推进 DAG 到指定步骤（写入状态文件）。"""
    sm.advance_step(run_id, name, message)


# ─── Flywheel 真实执行流程 ─────────────────────────────────────────────────

def _run_flywheel_sync(run_id: str, model_ids: list[str], force: bool) -> None:
    started_at = datetime.utcnow().isoformat()

    try:
        # ── Step 0: trigger ────────────────────────────────────────────────
        _step(run_id, "trigger", f"🚀 知识飞轮启动 · run_id={run_id} · {started_at}")

        # ── Step 1: dispatch — Coordinator ─────────────────────────────────
        _step(run_id, "dispatch", "⏳ Coordinator 正在分配任务…")
        dispatch_res = _coa("coordinator", {
            "action": "dispatch", "model_ids": model_ids, "run_id": run_id,
        }, run_id=run_id, step_name="dispatch")

        if dispatch_res.get("status") == "success":
            out = dispatch_res.get("output", {})
            ev = str(out)[:100] if out else "任务已分配"
        else:
            ev = f"⚠️ Agent异常: {dispatch_res.get('error', 'unknown')[:80]}"
        _step(run_id, "dispatch", f"✅ 任务已分配 | {ev}")

        # ── Step 2: research — 各类 Scout Agent ──────────────────────────────
        _step(run_id, "research", "⏳ Scout Agents 正在调研模型…")
        from app.services import knowledge_store as store
        all_ids = store.list_all_ids() if hasattr(store, "list_all_ids") else []
        targets = model_ids if model_ids else all_ids[:10]

        category_agents = {
            "Text": "text-researcher", "VLM": "vlm-researcher",
            "ALM": "alm-researcher", "Video": "video-researcher",
            "Unified": "unified-researcher", "Embedding": "embedding-researcher",
        }

        research_results = {}
        for mid in targets:
            meta = getattr(store, "read_meta", lambda *_: None)(mid) if hasattr(store, "read_meta") else None
            cat = getattr(meta, "category", "Text") if meta else "Text"
            agent = category_agents.get(cat, "text-researcher")
            r = _coa(agent, {"model_id": mid, "run_id": run_id}, run_id=run_id, step_name="research")
            research_results[mid] = {
                "status": "done" if r.get("status") == "success" else "error",
                "output": r.get("output", "")[:150] if r else "",
                "log_id": r.get("log_id", ""),
                "error": r.get("error", ""),
            }

        done = [k for k, v in research_results.items() if v["status"] == "done"]
        ev_parts = [f"{k}[{v['status']}]" for k, v in list(research_results.items())[:4]]
        ev_str = "; ".join(ev_parts) + (f"…（共{len(research_results)}个）" if len(research_results) > 4 else "")
        _step(run_id, "research", f"✅ 调研完成 {len(done)}/{len(targets)} 个 | {ev_str}")

        # ── Step 3: qc_review — QC Agent ───────────────────────────────────
        _step(run_id, "qc_review", "⏳ QC Agent 正在进行质量审查…")
        qc_res = _coa("qc-agent", {
            "action": "qc_review", "model_ids": done, "run_id": run_id,
        }, run_id=run_id, step_name="qc_review")

        qc_out = qc_res.get("output", {}) if qc_res.get("status") == "success" and isinstance(qc_res.get("output"), dict) else {}
        qc_passed    = qc_out.get("passed", [])
        qc_failed    = qc_out.get("failed", [])
        qc_rejected  = qc_out.get("rejected", [])
        qc_mistakes  = qc_out.get("mistakes", [])

        if qc_res.get("status") == "success":
            p0_names = ", ".join([str(r.get("model_id", r.get("id", "?"))) for r in qc_rejected[:3]])
            qc_ev = (f"通过{len(qc_passed)}个，"
                       f"P0拦截{len(qc_rejected)}个"
                       + (f" [{p0_names}]" if p0_names else ""))
        else:
            qc_ev = f"⚠️ Agent异常: {qc_res.get('error', '')[:80]}"
        _step(run_id, "qc_review", f"✅ {qc_ev}")

        # ── Step 4: archive — Archiver ──────────────────────────────────────
        _step(run_id, "archive", "⏳ Archiver 正在同步文档到 GitHub…")
        arch_res = _coa("archiver", {
            "action": "archive", "model_ids": qc_passed, "run_id": run_id,
        }, run_id=run_id, step_name="archive")

        if arch_res.get("status") == "success":
            arch_ev = str(arch_res.get("output", ""))[:100] or "文档已同步"
        else:
            arch_ev = f"⚠️ Agent异常: {arch_res.get('error', '')[:80]}"
        _step(run_id, "archive", f"✅ {arch_ev}")

        # ── Step 4b: 写入知识库 Markdown ─────────────────────────────────
        _step(run_id, "knowledge_write", "📝 正在写入知识库…")
        kw_ok = []
        from datetime import date as _date
        for mid in (qc_passed or []):
            try:
                from app.services import knowledge_store as ks
                meta = getattr(ks, "read_meta", lambda _: None)(mid) if hasattr(ks, "read_meta") else None
                if meta:
                    bench = "\n".join([f"- {b.get('name','')}: {b.get('score','')}"
                                        for b in getattr(meta, "benchmarks", [])]) or "（暂无Benchmark数据）"
                    analysis = (f"通过 QC 审核（run_id={run_id}）。"
                                f"许可证：{getattr(meta,'license_tag','unknown')}。"
                                f"发布方：{getattr(meta,'publisher','unknown')}。"
                                f"参数量：{getattr(meta,'params','unknown')}。")
                    from app.services.knowledge_manager import write_model_card
                    write_model_card(
                        model_id=mid,
                        model_name=getattr(meta, "name", mid),
                        benchmark_data=bench,
                        analysis=analysis,
                        tags=["model-card", getattr(meta, "category", "unknown").lower(), f"run:{run_id[:8]}"],
                    )
                    kw_ok.append(mid)
            except Exception as e:
                pass
        kw_msg = f"知识卡写入完成：{len(kw_ok)} 个模型" if kw_ok else "无模型需写入"
        _step(run_id, "knowledge_write", f"✅ {kw_msg}")

        # ── Step 5: self_review — Skills 自进化 ────────────────────────────
        _step(run_id, "self_review", "⏳ SelfReview Agent 正在分析失误模式…")
        evolution_result = run_self_evolution(
            run_id=run_id,
            recent_mistakes=qc_mistakes,
            total入库=len(qc_passed),
            p0_rate=len(qc_rejected) / max(len(qc_passed), 1),
        )

        if evolution_result["triggered"]:
            ev_msg = (f"🔄 Skills 自进化已触发！"
                        f"原因：{evolution_result['trigger_reason']}。"
                        f"更新 Skills：{', '.join(evolution_result['skills_updated'])}。"
                        f"发现 {len(evolution_result['patterns_found'])} 个失误模式。")
        else:
            ev_msg = f"⏭️ 未达到触发阈值（{evolution_result['trigger_reason']}）"
        _step(run_id, "self_review", ev_msg)

        # ── Step 6: complete ───────────────────────────────────────────────
        sm.complete_run(run_id, {
            "models_researched": len(research_results),
            "models_passed": len(qc_passed),
            "models_rejected": len(qc_rejected),
            "p0_count": len(qc_rejected),
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
    if body.model_ids:
        from app.services import knowledge_store as store
        for mid in body.model_ids:
            if store.read_meta(mid) is None:
                raise HTTPException(status_code=404, detail=f"Model not found: {mid}")

    run_id = str(uuid.uuid4())
    sm.create_run(run_id=run_id, model_ids=body.model_ids)
    background_tasks.add_task(_run_flywheel_sync, run_id, body.model_ids, body.force)
    return FlywheelTriggerResponse(run_id=run_id, status="started")


@router.get("/status/{run_id}", response_model=RunStatus)
def get_flywheel_status(run_id: str):
    status = sm.get_run(run_id)
    if status is None:
        raise HTTPException(status_code=404, detail="Run not found")
    return status


@router.get("/logs/{run_id}")
def get_run_logs(run_id: str):
    """返回指定 run 的所有 Agent 执行日志（供前端展示）。"""
    logs = AgentLogger.get_logs(run_id)
    return {"run_id": run_id, "logs": logs, "count": len(logs)}


@router.get("/evolution/status")
def get_evolution_status():
    index = get_skills_index()
    log = get_evolution_log()
    return {
        "skills_index": index,
        "recent_evolutions": log[:5],
        "next_iteration": get_next_iteration(),
    }
