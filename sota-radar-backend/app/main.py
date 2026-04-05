"""FastAPI application entry point."""
import sys
from pathlib import Path

# Ensure app root is on path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from app.config import CORS_ORIGINS, PORT
from app.routes import flywheel, knowledge, status

app = FastAPI(
    title="SOTA Radar V4 API",
    version="0.1.0",
    description="Backend API for SOTA Radar — knowledge store, flywheel, and status.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(knowledge.router, prefix="/api/v1")
app.include_router(flywheel.router, prefix="/api/v1")
app.include_router(status.router, prefix="/api/v1")


@app.get("/health")
def health():
    return {"status": "ok", "service": "sota-radar-backend"}


@app.get("/")
def root():
    return {"message": "SOTA Radar V4 API", "version": "0.1.0"}

@app.get("/api/v1/runs")
def list_all_runs(limit: int = Query(20, ge=1, le=100), offset: int = Query(0, ge=0)):
    from app.services import status_manager as sm
    runs = sm.list_runs(limit=limit, offset=offset)
    return {"runs": runs, "total": len(runs)}
