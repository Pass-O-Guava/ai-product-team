#!/usr/bin/env python3
"""CLI: run one complete flywheel cycle."""
import argparse
import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.config import FLYWHEEL_STEPS
from app.services import status_manager as sm


def run(args):
    run_id = args.run_id or sm.create_run(run_id=None).run_id
    print(f"[Flywheel] Starting run {run_id}")
    sm.start_run(run_id)

    steps = [
        ("trigger", "Starting flywheel cycle"),
        ("dispatch", "Dispatching tasks to scouts"),
        ("research", "Scanning model landscape"),
        ("qc_review", "QC agents validating findings"),
        ("archive", "Syncing documents to git"),
        ("self_review", "Running skill self-improvement"),
        ("complete", "Generating report"),
    ]

    for step_name, message in steps:
        print(f"[Flywheel] Step: {step_name}")
        sm.advance_step(run_id, step_name, message)

    sm.complete_run(run_id, {"finished_at": datetime.utcnow().isoformat()})
    status = sm.get_run(run_id)
    print(f"[Flywheel] Run {run_id} COMPLETED. Progress: {status.progress}")
    print(json.dumps(status.model_dump(), default=str, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run one SOTA Radar flywheel cycle")
    parser.add_argument("--run-id", help="Existing run ID to resume")
    args = parser.parse_args()
    run(args)
