"""Run status + SSE stream routes."""
import asyncio
import json
from datetime import datetime
from typing import AsyncGenerator

from fastapi import APIRouter, Query
from sse_starlette.sse import EventSourceResponse

from app.config import SSE_INTERVAL_SECONDS, RunState
from app.models import CurrentStatus, RunSummary
from app.services import status_manager as sm

router = APIRouter(prefix="/status", tags=["Status"])


async def _sse_stream() -> AsyncGenerator[dict, None]:
    """Yield SSE events every SSE_INTERVAL_SECONDS."""
    last_status = ""
    last_steps = []
    while True:
        status = sm.get_current_status()
        run = status.current_run

        event_type = None
        payload = {}

        if run:
            cur = sm.get_run(run.run_id)
            if cur:
                step_changed = len(cur.steps) != len(last_steps) or any(
                    s.status != last_steps[i].status
                    for i, s in enumerate(cur.steps)
                    if i < len(last_steps)
                )
                if cur.status == RunState.RUNNING and last_status != RunState.RUNNING:
                    event_type = "run_started"
                    payload = {
                        "run_id": cur.run_id,
                        "status": cur.status,
                        "progress": cur.progress,
                        "steps": [{"step": s.step, "status": s.status} for s in cur.steps],
                    }
                elif cur.status == RunState.COMPLETED and last_status != RunState.COMPLETED:
                    event_type = "run_complete"
                    payload = {
                        "run_id": cur.run_id,
                        "status": cur.status,
                        "progress": 1.0,
                        "finished_at": cur.finished_at.isoformat() if cur.finished_at else None,
                    }
                elif cur.status == RunState.FAILED and last_status != RunState.FAILED:
                    event_type = "run_failed"
                    payload = {
                        "run_id": cur.run_id,
                        "status": cur.status,
                        "errors": cur.errors,
                    }
                elif step_changed:
                    # Emit step_complete for the most recently completed step
                    for s in reversed(cur.steps):
                        if s.status == "done" and (
                            not last_steps or
                            any(st.step == s.step and st.status != "done" for st in last_steps)
                        ):
                            event_type = "step_complete"
                            payload = {
                                "run_id": cur.run_id,
                                "step": s.step,
                                "message": s.message,
                                "progress": cur.progress,
                            }
                            break
                last_status = cur.status
                last_steps = list(cur.steps)

        if event_type:
            yield {"event": event_type, "data": json.dumps(payload, ensure_ascii=False)}
        else:
            yield {"event": "ping", "data": json.dumps({"ts": datetime.utcnow().isoformat()}, ensure_ascii=False)}

        await asyncio.sleep(SSE_INTERVAL_SECONDS)


@router.get("/stream")
async def stream_status():
    return EventSourceResponse(_sse_stream())


@router.get("/current", response_model=CurrentStatus)
def get_current_status():
    return sm.get_current_status()

@router.get("/runs")
def list_runs(limit: int = Query(20, ge=1, le=100), offset: int = Query(0, ge=0)):
    runs = sm.list_runs(limit=limit, offset=offset)
    return {"runs": runs, "total": len(runs)}
