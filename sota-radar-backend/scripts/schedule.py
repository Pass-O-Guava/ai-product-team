#!/usr/bin/env python3
"""Daily scheduled runs: 07:00 and 13:30 UTC+8.

Reads CRON_SCHEDULE from env or defaults to:
  - 07:00  Asia/Shanghai
  - 13:30  Asia/Shanghai

Usage:
  python scripts/schedule.py          # one-shot (for cron testing)
  python scripts/schedule.py --daemon  # daemon loop (for long-running scheduler)
"""
import argparse
import os
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

import pytz

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.services import status_manager as sm

SHanghai = pytz.timezone("Asia/Shanghai")

DEFAULT_SCHEDULES = [
    (7, 0),   # 07:00 UTC+8
    (13, 30), # 13:30 UTC+8
]


def _next_run(hour: int, minute: int) -> datetime:
    now_sh = datetime.now(SHanghai)
    naive_next = now_sh.replace(hour=hour, minute=minute, second=0, microsecond=0)
    # Make it timezone-aware
    if naive_next.tzinfo is None:
        naive_next = SHanghai.localize(naive_next)
    if naive_next <= now_sh:
        naive_next += timedelta(days=1)
    return naive_next.astimezone(pytz.UTC)


def _wait_until(target: datetime) -> None:
    wait_seconds = (target - datetime.now(pytz.UTC)).total_seconds()
    if wait_seconds > 0:
        print(f"[Schedule] Next run at {target.isoformat()} (waiting {wait_seconds:.0f}s)")
        time.sleep(min(wait_seconds, 60))  # sleep max 60s between checks


def _run_cycle() -> str:
    print(f"[Schedule] Triggering flywheel at {datetime.utcnow().isoformat()}")
    # Import here to avoid circular imports at module level
    from app.services import status_manager as sm
    run = sm.create_run()
    print(f"[Schedule] Created run {run.run_id}")
    return run.run_id


def _daemon(schedules):
    print("[Schedule] Daemon started. Press Ctrl+C to stop.")
    while True:
        now_sh = datetime.now(SHanghai)
        # Find next scheduled time
        candidates = []
        for hour, minute in schedules:
            next_t = _next_run(hour, minute)
            candidates.append(next_t)
        next_target = min(candidates)
        _wait_until(next_target)
        # Check if we're within 90 seconds of the target
        diff = abs((datetime.now(pytz.UTC) - next_target).total_seconds())
        if diff < 90:
            try:
                _run_cycle()
            except Exception as e:
                print(f"[Schedule] Run failed: {e}")
        # Sleep a bit before re-evaluating
        time.sleep(30)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--daemon", action="store_true", help="Run as daemon loop")
    args = parser.parse_args()

    schedules = DEFAULT_SCHEDULES

    if args.daemon:
        _daemon(schedules)
    else:
        # One-shot: run immediately if within schedule window, else skip
        now_sh = datetime.now(SHanghai)
        for hour, minute in schedules:
            if now_sh.hour == hour and now_sh.minute - minute < 5:
                _run_cycle()
                return
        print("[Schedule] No schedule window active. Use --daemon for continuous scheduling.")


if __name__ == "__main__":
    main()
