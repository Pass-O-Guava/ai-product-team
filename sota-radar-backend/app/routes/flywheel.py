"""Knowledge flywheel trigger routes."""
import asyncio
import json
import threading
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from fastapi import APIRouter, BackgroundTasks, HTTPException

from app.config import RunState, RUNS_DIR
from app.models import FlywheelTrigger, FlywheelTriggerResponse, RunStatus
from app.services import status_manager as sm
from app.services.openclaw_client import OpenClawClient


router = APIRouter(prefix="/flywheel", tags=["Flywheel"])


# ─── Run status persistence helpers ───────────────────────────────────────────

def _run_dir(run_id: str) -> Path:
    d = RUNS_DIR / run_id
    if not d.exists():
        d.mkdir(parents=True, exist_ok=True)
    return d


def _status_path(run_id: str) -> Path:
    return _run_dir(run_id) / "status.json"


def save_run_status(run_id: str, data: dict[str, Any]) -> None:
    """Persist run status to a standalone JSON file (used by background thread)."""
    path = _status_path(run_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Load existing file if present, then merge
    existing: dict[str, Any] = {}
    if path.exists():
        try:
            raw = path.read_text(encoding="utf-8")
            if raw.strip():
                existing = json.loads(raw)
        except (json.JSONDecodeError, OSError):
            pass
    existing.update(data)
    path.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")


# ─── Background flywheel executor ─────────────────────────────────────────────

def _run_flywheel_with_openclaw(run_id: str, model_ids: list[str], force: bool) -> None:
    """
    Background task that runs the OpenClaw-powered flywheel cycle.
    Updates step statuses and final run status via status_manager.
    """
    client = OpenClawClient()

    try:
        # Step 1: trigger — mark as started
        sm.advance_step(run_id, "trigger", f"OpenClaw flywheel started for {len(model_ids)} models")

        # Step 2: dispatch — confirm OpenClaw availability
        available = client.is_available()
        if not available:
            raise RuntimeError("OpenClaw CLI is not available on this system.")
        sm.advance_step(run_id, "dispatch", "OpenClaw agent dispatched")

        # Step 3: research — run subagent for each model
        if model_ids:
            from app.services import knowledge_store as store
            results_map: dict[str, Any] = {}
            for mid in model_ids:
                meta = store.read_meta(mid)
                research = client.run_research_task(mid)
                qc = client.run_qc_task(mid, research.get("output", {}))
                results_map[mid] = {
                    "name": meta.name if meta else mid,
                    "category": meta.category if meta else "Unknown",
                    "is_sota": meta.is_sota if meta else False,
                    "research": research,
                    "qc": qc,
                }
            sm.advance_step(run_id, "research", f"Researched {len(results_map)} models via OpenClaw subagents")
        else:
            results_map = {}
            sm.advance_step(run_id, "research", "No models to research")

        # Step 4: qc_review — mark done (QC is embedded in step 3 per-model)
        sm.advance_step(run_id, "qc_review", "QC review complete")

        # Step 5: archive — placeholder for future git-sync
        sm.advance_step(run_id, "archive", "Synced to git (stub)")

        # Step 6: self_review — placeholder for future self-improvement
        sm.advance_step(run_id, "self_review", "Skill self-improvement complete (stub)")

        # Step 7: complete
        sm.advance_step(run_id, "complete", "Report generated")
        sm.complete_run(
            run_id,
            {
                "models_updated": len(model_ids),
                "results": results_map,
                "finished_at": datetime.utcnow().isoformat(),
            },
        )

    except Exception as exc:
        sm.fail_run(run_id, str(exc))
        save_run_status(run_id, {"status": "FAILED", "error": str(exc)})


# ─── Routes ───────────────────────────────────────────────────────────────────

@router.post("/trigger", response_model=FlywheelTriggerResponse)
def trigger_flywheel(body: FlywheelTrigger):
    # Validate model IDs if provided
    if body.model_ids:
        from app.services import knowledge_store as store
        for mid in body.model_ids:
            if store.read_meta(mid) is None:
                raise HTTPException(status_code=404, detail=f"Model not found: {mid}")

    run_id = str(uuid.uuid4())
    sm.create_run(run_id=run_id, model_ids=body.model_ids)
    sm.start_run(run_id)

    # Run OpenClaw-powered flywheel in a background thread so HTTP response is immediate
    thread = threading.Thread(
        target=_run_flywheel_with_openclaw,
        args=(run_id, body.model_ids, body.force),
        daemon=True,
    )
    thread.start()

    return FlywheelTriggerResponse(run_id=run_id, status="started")


@router.get("/status/{run_id}", response_model=RunStatus)
def get_flywheel_status(run_id: str):
    status = sm.get_run(run_id)
    if status is None:
        raise HTTPException(status_code=404, detail="Run not found")
    return status
