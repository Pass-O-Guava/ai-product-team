"""Knowledge store: reads/writes Markdown + JSON files for each model."""
import json
import os
import re
import shutil
from pathlib import Path
from typing import Optional

from app.config import MODELS_DIR
from app.models import Benchmark, ModelCreate, ModelMeta, ModelUpdate


def _slug(model_id: str) -> str:
    return re.sub(r"[^\w\-]", "_", model_id)


def _model_dir(model_id: str) -> Path:
    return MODELS_DIR / _slug(model_id)


def _ensure_dir(model_id: str) -> Path:
    d = _model_dir(model_id)
    d.mkdir(parents=True, exist_ok=True)
    return d


def _meta_path(model_id: str) -> Path:
    return _model_dir(model_id) / "meta.json"


def read_meta(model_id: str) -> Optional[ModelMeta]:
    path = _meta_path(model_id)
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    for b in raw.get("benchmarks", []):
        if "source" not in b:
            b["source"] = "官方评测"
    return ModelMeta(**raw)


def write_meta(model_id: str, meta: ModelMeta) -> None:
    path = _ensure_dir(model_id) / "meta.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(meta.model_dump(mode="json"), f, ensure_ascii=False, indent=2)


def _knowledge_path(model_id: str) -> Path:
    return _model_dir(model_id) / "knowledge.md"


def read_knowledge(model_id: str) -> str:
    path = _knowledge_path(model_id)
    if path.exists():
        return path.read_text(encoding="utf-8")
    meta = read_meta(model_id)
    if meta is None:
        return ""
    return _auto_generate_knowledge(meta)


def write_knowledge(model_id: str, content: str) -> None:
    path = _ensure_dir(model_id) / "knowledge.md"
    path.write_text(content, encoding="utf-8")


def create_model(data: ModelCreate) -> ModelMeta:
    meta = ModelMeta(
        id=data.id,
        name=data.name,
        category=data.category,
        publisher=data.publisher,
        params=data.params,
        modality=data.modality,
        license=data.license,
        license_tag=data.license_tag,
        benchmarks=data.benchmarks,
        hf_url=data.hf_url,
        release_date=data.release_date,
        is_sota=data.is_sota,
        insight=data.insight,
        tags=data.tags,
    )
    write_meta(data.id, meta)
    write_knowledge(data.id, data.knowledge or _auto_generate_knowledge(meta))
    return meta


def update_model(model_id: str, patch: ModelUpdate) -> Optional[ModelMeta]:
    meta = read_meta(model_id)
    if meta is None:
        return None
    for key, value in patch.model_dump(exclude_unset=True).items():
        setattr(meta, key, value)
    meta.updated_at = meta.model_fields["updated_at"].default_factory()
    write_meta(model_id, meta)
    return meta


def delete_model(model_id: str) -> bool:
    d = _model_dir(model_id)
    if d.exists():
        shutil.rmtree(d)
        return True
    return False


def list_model_ids() -> list[str]:
    if not MODELS_DIR.exists():
        return []
    return [p.name for p in MODELS_DIR.iterdir() if p.is_dir()]


def list_all() -> list[ModelMeta]:
    return [m for m in (read_meta(mid) for mid in list_model_ids()) if m is not None]


def _auto_generate_knowledge(meta: ModelMeta) -> str:
    lines = [f"# {meta.name}", "", "## 基本信息", f"- 发布方：{meta.publisher}"]
    if meta.params:
        lines.append(f"- 参数量：{meta.params}")
    if meta.modality:
        lines.append(f"- 模态：{meta.modality}")
    if meta.release_date:
        lines.append(f"- 发布日期：{meta.release_date}")
    lines.append("")
    lines.append("## 许可证")
    lines.append(f"{meta.license} {meta.license_tag}")
    lines.append("")
    if meta.benchmarks:
        lines.append("## Benchmark 数据")
        lines.append("| Benchmark | 分数 | 来源 |")
        lines.append("|-----------|------|------|")
        for b in meta.benchmarks:
            source = getattr(b, "source", "官方评测")
            lines.append(f"| {b.name} | {b.score} | {source} |")
        lines.append("")
    if meta.insight:
        lines.append("## 入选理由")
        lines.append(meta.insight)
    return "\n".join(lines)
