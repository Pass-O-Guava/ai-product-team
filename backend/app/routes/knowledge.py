"""
Knowledge API — 知识资产管理路由（OpenClaw 风格 Markdown 知识库）。
所有知识资产通过 Curator Agent 统一管理。
"""
import uuid
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException, Query

from app.services.knowledge_manager import (
    health_report,
    list_entries,
    read,
    search,
    write,
    write_daily_log,
    write_model_card,
    write_skill_doc,
    CATEGORIES,
)

router = APIRouter(prefix="/api/v1/knowledge", tags=["Knowledge"])


# ─── 读取接口 ───────────────────────────────────────────────────────────

@router.get("/list")
def list_knowledge(
    category: Optional[str] = Query(None, description="分类：models/skills/daily/weekly/team"),
    tag: Optional[str] = Query(None, description="标签过滤"),
    limit: int = Query(50, ge=1, le=200),
):
    """列出知识资产（支持分类/标签过滤）。"""
    if category and category not in CATEGORIES:
        raise HTTPException(status_code=400, detail=f"Invalid category. Options: {CATEGORIES}")
    return {
        "entries": list_entries(category=category, tag=tag, limit=limit),
        "total": len(list_entries(category=category, tag=tag, limit=limit)),
    }


@router.get("/read/{path:path}")
def read_knowledge(path: str):
    """
    读取指定知识文件。
    path: 相对路径，如 'models/qwen3-vl-2026-04-06.md' 或 '2026-04-06'
    """
    try:
        return read(path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Knowledge asset not found: {path}")


@router.get("/search")
def search_knowledge(
    q: str = Query(..., min_length=1, description="搜索关键词"),
    limit: int = Query(20, ge=1, le=50),
):
    """
    关键词全文搜索（文件名 + tags + 标题）。
    语义搜索由 LLM 提供深度检索能力。
    """
    return {
        "query": q,
        "results": search(keyword=q, limit=limit),
        "count": len(search(keyword=q, limit=limit)),
    }


@router.get("/health")
def knowledge_health():
    """知识库健康度报告（供前端仪表盘展示）。"""
    return health_report()


# ─── 写入接口（仅 Curator Agent 可用）──────────────────────────────────

@router.post("/write")
def write_knowledge(body: dict):
    """
    写入任意知识资产。
    body: { category, title, content, tags?, author?, date?, update? }
    """
    try:
        result = write(
            category=body["category"],
            title=body["title"],
            content_body=body["content"],
            tags=body.get("tags"),
            author=body.get("author", "Curator Agent"),
            date_str=body.get("date"),
            update=body.get("update", True),
        )
        return {"ok": True, **result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/daily")
def append_daily(body: dict):
    """
    追加每日研究日志（追加模式，自动去重同日期）。
    body: { content, date?, tags? }
    """
    result = write_daily_log(
        content=body["content"],
        date_str=body.get("date"),
        tags=body.get("tags"),
    )
    return {"ok": True, **result}


@router.post("/models")
def upsert_model_card(body: dict):
    """
    写入或更新模型知识卡（幂等写入）。
    body: { model_id, model_name, benchmark_data, analysis, tags? }
    """
    result = write_model_card(
        model_id=body["model_id"],
        model_name=body["model_name"],
        benchmark_data=body.get("benchmark_data", ""),
        analysis=body.get("analysis", ""),
        tags=body.get("tags"),
    )
    return {"ok": True, **result}


@router.post("/skills")
def upsert_skill_doc(body: dict):
    """
    写入或更新 Skill 文档。
    body: { skill_id, skill_name, description, rules, changelog? }
    """
    result = write_skill_doc(
        skill_id=body["skill_id"],
        skill_name=body["skill_name"],
        description=body.get("description", ""),
        rules=body.get("rules", ""),
        changelog=body.get("changelog"),
    )
    return {"ok": True, **result}


# ─── 批量操作 ────────────────────────────────────────────────────────────

@router.post("/bulk")
def bulk_write(items: list[dict]):
    """
    批量写入多个知识资产。
    用于飞轮运转后一次性写入多个模型卡/Skill 更新。
    items: [{ category, title, content, tags?, date? }, ...]
    """
    results = []
    for item in items:
        try:
            r = write(
                category=item["category"],
                title=item["title"],
                content_body=item["content"],
                tags=item.get("tags"),
                date_str=item.get("date"),
                update=item.get("update", False),
            )
            results.append({**r, "ok": True})
        except Exception as exc:
            results.append({"ok": False, "title": item.get("title"), "error": str(exc)})
    return {"results": results, "ok_count": sum(1 for r in results if r.get("ok"))}
