"""Application configuration and constants."""
import os
from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent  # /workspace/sota-radar-backend
DATA_DIR = BASE_DIR / "app" / "data"
MODELS_DIR = DATA_DIR / "models"
RUNS_DIR = DATA_DIR / "runs"
SKILLS_DIR = DATA_DIR / "skills"
MANIFEST_PATH = DATA_DIR / "manifest.json"

# Server settings
PORT = 7860
HOST = "0.0.0.0"
CORS_ORIGINS = ["*"]

# SSE stream interval
SSE_INTERVAL_SECONDS = 5

# Default pagination
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# Flywheel steps (ordered)
FLYWHEEL_STEPS = [
    "trigger",
    "dispatch",
    "research",
    "qc_review",
    "archive",
    "self_review",
    "complete",
]

# Run state machine
class RunState:
    IDLE = "IDLE"
    RUNNING = "RUNNING"
    COMPLETING = "COMPLETING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
