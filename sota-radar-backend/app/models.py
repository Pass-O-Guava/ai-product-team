"""Pydantic data models."""
from datetime import datetime
from typing import Any, Literal, Optional

from pydantic import BaseModel, Field


# ─── Benchmark ────────────────────────────────────────────────────────────────
class Benchmark(BaseModel):
    name: str
    score: str
    source: str = "官方评测"


# ─── Model Meta ───────────────────────────────────────────────────────────────
class ModelMeta(BaseModel):
    id: str
    name: str
    category: Literal["VLM", "ALM", "Video", "Text", "Embedding", "Unified"]
    publisher: str
    params: str
    modality: str
    license: str
    license_tag: Literal["✅可商用", "⚠️需申请", "❌不可商用"]
    benchmarks: list[Benchmark] = Field(default_factory=list)
    hf_url: str = ""
    release_date: str
    is_sota: bool = True
    insight: str = ""
    tags: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.utcnow())
    updated_at: datetime = Field(default_factory=lambda: datetime.utcnow())


# ─── Full Model (meta + knowledge) ────────────────────────────────────────────
class ModelDetail(BaseModel):
    meta: ModelMeta
    knowledge: str = ""


# ─── Paginated response ────────────────────────────────────────────────────────
class ModelListResponse(BaseModel):
    models: list[ModelMeta]
    total: int
    page: int
    page_size: int


# ─── Create / Update ──────────────────────────────────────────────────────────
class ModelCreate(BaseModel):
    id: str
    name: str
    category: Literal["VLM", "ALM", "Video", "Text", "Embedding", "Unified"]
    publisher: str
    params: str = ""
    modality: str = ""
    license: str = ""
    license_tag: Literal["✅可商用", "⚠️需申请", "❌不可商用"] = "✅可商用"
    benchmarks: list[Benchmark] = Field(default_factory=list)
    hf_url: str = ""
    release_date: str = ""
    is_sota: bool = True
    insight: str = ""
    tags: list[str] = Field(default_factory=list)
    knowledge: str = ""


class ModelUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    publisher: Optional[str] = None
    params: Optional[str] = None
    modality: Optional[str] = None
    license: Optional[str] = None
    license_tag: Optional[str] = None
    benchmarks: Optional[list[Benchmark]] = None
    hf_url: Optional[str] = None
    release_date: Optional[str] = None
    is_sota: Optional[bool] = None
    insight: Optional[str] = None
    tags: Optional[list[str]] = None


# ─── Flywheel ─────────────────────────────────────────────────────────────────
class FlywheelTrigger(BaseModel):
    model_ids: list[str] = Field(default_factory=list)
    force: bool = False


class FlywheelTriggerResponse(BaseModel):
    run_id: str
    status: str = "started"


class FlywheelStep(BaseModel):
    step: str
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    status: Literal["pending", "running", "done", "failed"] = "pending"
    message: str = ""


class RunStatus(BaseModel):
    run_id: str
    status: str  # IDLE / RUNNING / COMPLETING / COMPLETED / FAILED
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    progress: float = 0.0  # 0.0 – 1.0
    steps: list[FlywheelStep] = Field(default_factory=list)
    results: dict[str, Any] = Field(default_factory=dict)
    errors: list[str] = Field(default_factory=list)


class RunSummary(BaseModel):
    run_id: str
    status: str
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    progress: float = 0.0


class CurrentStatus(BaseModel):
    state: str
    current_run: Optional[RunSummary] = None
    today_runs: int = 0
    today_models_updated: int = 0


# ─── SSE Event ───────────────────────────────────────────────────────────────
class SSEEvent(BaseModel):
    event: Literal["run_started", "step_complete", "run_complete", "run_failed"]
    data: dict[str, Any]
