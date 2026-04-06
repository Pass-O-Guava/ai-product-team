"""Run status manager: state machine + JSON file persistence."""
import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional

from app.config import FLYWHEEL_STEPS, MODELS_DIR, RUNS_DIR, RunState
from app.models import CurrentStatus, FlywheelStep, RunStatus, RunSummary


# ─── Run directory helpers ────────────────────────────────────────────────────

def _run_dir(run_id: str) -> Path:
    d = RUNS_DIR / run_id
    if d.is_file() or (not d.exists()):
        d.mkdir(parents=True, exist_ok=True)
    return d


def _status_path(run_id: str) -> Path:
    return _run_dir(run_id) / "status.json"


# ─── Serialisation helpers ───────────────────────────────────────────────────

def _dt(v: Optional[datetime]) -> Optional[str]:
    return v.isoformat() if v else None


def _from_dict(d: dict) -> RunStatus:
    steps = [FlywheelStep(**s) for s in d.get("steps", [])]
    return RunStatus(
        run_id=d["run_id"],
        status=d["status"],
        started_at=datetime.fromisoformat(d["started_at"]) if d.get("started_at") else None,
        finished_at=datetime.fromisoformat(d["finished_at"]) if d.get("finished_at") else None,
        progress=float(d.get("progress", 0.0)),
        steps=steps,
        results=d.get("results", {}),
        errors=d.get("errors", []),
    )


# ─── State machine operations ─────────────────────────────────────────────────

def create_run(run_id: Optional[str] = None, model_ids: Optional[list[str]] = None) -> RunStatus:
    run_id = run_id or str(uuid.uuid4())
    steps = [FlywheelStep(step=s) for s in FLYWHEEL_STEPS]
    status = RunStatus(
        run_id=run_id,
        status=RunState.IDLE,
        started_at=None,
        finished_at=None,
        progress=0.0,
        steps=steps,
        results={"model_ids": model_ids or []},
        errors=[],
    )
    _save(status)
    return status


def start_run(run_id: str) -> Optional[RunStatus]:
    status = get_run(run_id)
    if status is None:
        return None
    status.status = RunState.RUNNING
    status.started_at = datetime.utcnow()
    # Mark trigger step as running
    if status.steps:
        status.steps[0].status = "running"
        status.steps[0].started_at = datetime.utcnow()
    _save(status)
    return status


def advance_step(run_id: str, step_name: str, message: str = "") -> Optional[RunStatus]:
    status = get_run(run_id)
    if status is None:
        return None
    for i, step in enumerate(status.steps):
        if step.step == step_name:
            step.status = "done"
            step.finished_at = datetime.utcnow()
            step.message = message
            # Next step becomes running
            if i + 1 < len(status.steps):
                status.steps[i + 1].status = "running"
                status.steps[i + 1].started_at = datetime.utcnow()
            break
    # Progress
    done = sum(1 for s in status.steps if s.status == "done")
    status.progress = round(done / len(status.steps), 3)
    _save(status)
    return status


def complete_run(run_id: str, results: Optional[dict] = None) -> Optional[RunStatus]:
    status = get_run(run_id)
    if status is None:
        return None
    status.status = RunState.COMPLETED
    status.finished_at = datetime.utcnow()
    status.progress = 1.0
    # Mark all steps done
    for step in status.steps:
        if step.status in ("pending", "running"):
            step.status = "done"
            step.finished_at = datetime.utcnow()
    if results:
        status.results.update(results)
    _save(status)
    return status


def fail_run(run_id: str, error: str) -> Optional[RunStatus]:
    status = get_run(run_id)
    if status is None:
        return None
    status.status = RunState.FAILED
    status.finished_at = datetime.utcnow()
    status.errors.append(error)
    # Mark current running step as failed
    for step in status.steps:
        if step.status == "running":
            step.status = "failed"
            step.finished_at = datetime.utcnow()
            step.message = error
            break
    _save(status)
    return status


def get_run(run_id: str) -> Optional[RunStatus]:
    path = _status_path(run_id)
    if not path.exists():
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
        if not raw.strip():
            return None
        return _from_dict(json.loads(raw))
    except (json.JSONDecodeError, OSError):
        return None


def list_runs(limit: int = 20, offset: int = 0) -> list[RunSummary]:
    if not RUNS_DIR.exists():
        return []
    runs = []
    for d in sorted(RUNS_DIR.iterdir(), key=lambda p: p.name, reverse=True):
        s = get_run(d.name)
        if s:
            runs.append(RunSummary(
                run_id=s.run_id,
                status=s.status,
                started_at=s.started_at,
                finished_at=s.finished_at,
                progress=s.progress,
            ))
    return runs[offset : offset + limit]


def get_current_status() -> CurrentStatus:
    """Find the most recent RUNNING or COMPLETING run."""
    all_runs = list_runs(limit=50, offset=0)
    current_run = None
    for r in all_runs:
        if r.status in (RunState.RUNNING, RunState.COMPLETING):
            current_run = r
            break
    if current_run is None and all_runs:
        current_run = all_runs[0]
    today = datetime.utcnow().date().isoformat()
    today_count = sum(
        1 for r in all_runs
        if r.started_at and r.started_at.date().isoformat() == today
    )
    return CurrentStatus(
        state=current_run.status if current_run else RunState.IDLE,
        current_run=current_run,
        today_runs=today_count,
        today_models_updated=0,  # placeholder
    )


def _save(status: RunStatus) -> None:
    path = _status_path(status.run_id)
    data = {
        "run_id": status.run_id,
        "status": status.status,
        "started_at": _dt(status.started_at),
        "finished_at": _dt(status.finished_at),
        "progress": status.progress,
        "steps": [
            {
                "step": s.step,
                "started_at": _dt(s.started_at),
                "finished_at": _dt(s.finished_at),
                "status": s.status,
                "message": s.message,
            }
            for s in status.steps
        ],
        "results": status.results,
        "errors": status.errors,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
