"""Model knowledge CRUD routes."""
import math
from typing import Optional

from fastapi import APIRouter, HTTPException, Query

from app.config import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE
from app.models import ModelCreate, ModelDetail, ModelListResponse, ModelMeta, ModelUpdate
from app.services import knowledge_store as store

router = APIRouter(prefix="/models", tags=["Knowledge"])


def _filter_models(
    models: list[ModelMeta],
    category: Optional[str] = None,
    license: Optional[str] = None,
    search: Optional[str] = None,
) -> list[ModelMeta]:
    result = models
    if category and category != "全部":
        result = [m for m in result if m.category == category]
    if license and license != "全部":
        result = [m for m in result if m.license_tag == license]
    if search:
        q = search.lower()
        result = [
            m
            for m in result
            if q in m.name.lower() or q in m.publisher.lower() or q in m.insight.lower()
        ]
    return result


@router.get("", response_model=ModelListResponse)
def list_models(
    category: Optional[str] = Query(None),
    license: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    sort: Optional[str] = Query("最近更新"),
    page: int = Query(1, ge=1),
    page_size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE),
):
    all_models = store.list_all()
    filtered = _filter_models(all_models, category, license, search)

    if sort == "名称 A-Z":
        filtered = sorted(filtered, key=lambda m: m.name)
    elif sort == "Benchmark评分":
        filtered = sorted(
            filtered,
            key=lambda m: max([float(b.score.strip("%~")) for b in m.benchmarks], default=0.0),
            reverse=True,
        )
    elif sort == "参数量":
        def _parse_params(m: ModelMeta) -> float:
            import re
            txt = m.params
            nums = re.findall(r"[\d.]+", txt)
            return float(nums[0]) if nums else 0.0
        filtered = sorted(filtered, key=_parse_params, reverse=True)
    else:  # 最近更新
        filtered = sorted(filtered, key=lambda m: m.updated_at, reverse=True)

    total = len(filtered)
    start = (page - 1) * page_size
    page_items = filtered[start : start + page_size]

    return ModelListResponse(
        models=page_items,
        total=total,
        page=page,
        page_size=page_size,
    )


@router.get("/{model_id}", response_model=ModelDetail)
def get_model(model_id: str):
    meta = store.read_meta(model_id)
    if meta is None:
        raise HTTPException(status_code=404, detail="Model not found")
    knowledge = store.read_knowledge(model_id)
    return ModelDetail(meta=meta, knowledge=knowledge)


@router.get("/{model_id}/knowledge", response_model=dict)
def get_knowledge(model_id: str):
    if store.read_meta(model_id) is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return {"model_id": model_id, "knowledge": store.read_knowledge(model_id)}


@router.put("/{model_id}", response_model=ModelMeta)
def put_model(model_id: str, patch: ModelUpdate):
    updated = store.update_model(model_id, patch)
    if updated is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return updated


@router.post("", response_model=ModelMeta, status_code=201)
def post_model(data: ModelCreate):
    existing = store.read_meta(data.id)
    if existing is not None:
        raise HTTPException(status_code=409, detail="Model with this ID already exists")
    return store.create_model(data)


@router.delete("/{model_id}", status_code=204)
def delete_model(model_id: str):
    if not store.delete_model(model_id):
        raise HTTPException(status_code=404, detail="Model not found")
