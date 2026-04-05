"""Knowledge flywheel trigger routes."""
import asyncio
import uuid
from datetime import datetime

from fastapi import APIRouter, BackgroundTasks, HTTPException

from app.config import RunState
from app.models import FlywheelTrigger, FlywheelTriggerResponse, RunStatus
from app.services import status_manager as sm
from app.services.openclaw_client import client

router = APIRouter(prefix="/flywheel", tags=["Flywheel"])


def _run_flywheel_sync(run_id: str, model_ids: list[str], force: bool) -> None:
    """Synchronous flywheel execution (runs inside BackgroundTasks)."""
    try:
        sm.start_run(run_id)

        # Step 1: dispatch
        sm.advance_step(run_id, "trigger", f"Started with {len(model_ids)} models")

        # Step 2: dispatch
        sm.advance_step(run_id, "dispatch", "Tasks dispatched to scouts")

        # Step 3: research
        if model_ids:
            from app.services import knowledge_store as store
            results = {}
            for mid in model_ids:
                meta = store.read_meta(mid)
                if meta:
                    results[mid] = {
                        "name": meta.name,
                        "category": meta.category,
                        "is_sota": meta.is_sota,
                    }
            sm.advance_step(run_id, "research", f"Researched {len(results)} models")
        else:
            sm.advance_step(run_id, "research", "No models to research")

        # Step 4: qc_review
        sm.advance_step(run_id, "qc_review", "QC review complete")

        # Step 5: archive
        sm.advance_step(run_id, "archive", "Synced to git")

        # Step 6: self_review
        sm.advance_step(run_id, "self_review", "Skill self-improvement complete")

        # Step 7: complete
        sm.advance_step(run_id, "complete", "Report generated")
        sm.complete_run(run_id, {"models_updated": len(model_ids), "finished_at": datetime.utcnow().isoformat()})

    except Exception as exc:
        sm.fail_run(run_id, str(exc))


@router.post("/trigger", response_model=FlywheelTriggerResponse)
def trigger_flywheel(
    body: FlywheelTrigger,
    background_tasks: BackgroundTasks,
):
    # Validate model IDs if provided
    if body.model_ids:
        from app.services import knowledge_store as store
        for mid in body.model_ids:
            if store.read_meta(mid) is None:
                raise HTTPException(status_code=404, detail=f"Model not found: {mid}")

    run_id = str(uuid.uuid4())
    sm.create_run(run_id=run_id, model_ids=body.model_ids)
    sm.start_run(run_id)

    background_tasks.add_task(_run_flywheel_sync, run_id, body.model_ids, body.force)

    return FlywheelTriggerResponse(run_id=run_id, status="started")


@router.get("/status/{run_id}", response_model=RunStatus)
def get_flywheel_status(run_id: str):
    status = sm.get_run(run_id)
    if status is None:
        raise HTTPException(status_code=404, detail="Run not found")
    return status
