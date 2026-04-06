"""
Knowledge Asset Manager — OpenClaw 风格 Markdown 知识资产管理。
核心原则：
  1. 一切知识资产皆是 .md 文件
  2. 文件名即索引（包含日期/类型/标识）
  3. YAML frontmatter 提供结构化元数据
  4. Curator（归档员）是唯一写入口，其他 Agent 只读
  5. 目录即分类：models / skills / daily / weekly / team

知识体系：
  knowledge/
  ├── models/          # 每模型一 MD（模型卡）
  ├── skills/          # 每技能一 MD（Skill 文档）
  ├── daily/           # 每日研究日志
  ├── weekly/          # 每周综合报告
  └── team/            # 团队规范与 SOP
"""
import re
import uuid
from datetime import datetime, date
from pathlib import Path
from typing import Any, Optional

from app.config import DATA_DIR

KNOWLEDGE_DIR = DATA_DIR / "knowledge"
MANIFEST_PATH  = KNOWLEDGE_DIR / "_manifest.json"

CATEGORIES = ["models", "skills", "daily", "weekly", "team"]
SUBCATEGORIES: dict[str, list[str]] = {
    "models":  ["vlm", "text", "video", "embedding", "unified", "alm"],
    "skills":  ["researcher", "reviewer", "archiver", "coordinator", "self-review"],
    "daily":   [],
    "weekly":  [],
    "team":    ["handbook", "sop", "research-standard"],
}

# ─── Frontmatter 解析 ──────────────────────────────────────────────────────

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
TAG_RE = re.compile(r"\btag[s]?:\s*(.*)", re.I)
DATE_RE = re.compile(r"\bdate[s]?:\s*(.*)", re.I)


def _load_manifest() -> dict:
    if not MANIFEST_PATH.exists():
        return {"entries": [], "version": "1.0"}
    import json
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        return json.load(f)


def _save_manifest(manifest: dict) -> None:
    import json
    KNOWLEDGE_DIR.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)


def _parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    lines = m.group(1).splitlines()
    meta: dict[str, Any] = {}
    for line in lines:
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        meta[key.strip()] = val.strip().strip('"').strip("'")
    body = text[m.end():]
    return meta, body


def _make_frontmatter(meta: dict) -> str:
    lines = ["---"]
    for k, v in meta.items():
        if isinstance(v, list):
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---\n")
    return "\n".join(lines)


# ─── 文件命名规范 ──────────────────────────────────────────────────────────

def _slugify(name: str) -> str:
    """把名称转为合法文件名 slug"""
    import urllib.parse
    s = name.lower().replace(" ", "-").replace("/", "-")
    return re.sub(r"[^a-z0-9\-]", "", s)


def make_path(category: str, title: str, date_str: Optional[str] = None) -> Path:
    """
    生成标准知识文件路径。
    例: knowledge/daily/2026-04-06.md
        knowledge/models/qwen3-vl-2026-04-06.md
        knowledge/skills/researcher-2026-04-06.md
    """
    today = date_str or date.today().isoformat()
    slug = _slugify(title)
    ext = ".md"

    if category == "daily":
        # 每日日志：一个文件一天
        return KNOWLEDGE_DIR / "daily" / f"{today}.md"
    elif category == "weekly":
        return KNOWLEDGE_DIR / "weekly" / f"{today}-{slug}{ext}"
    elif category == "models":
        return KNOWLEDGE_DIR / "models" / f"{slug}-{today}{ext}"
    elif category == "skills":
        return KNOWLEDGE_DIR / "skills" / f"{slug}{ext}"
    else:
        return KNOWLEDGE_DIR / category / f"{today}-{slug}{ext}"


def _entry_from_path(path: Path) -> dict[str, Any]:
    """从文件路径提取 entry 元数据（不解析内容）"""
    rel = path.relative_to(KNOWLEDGE_DIR)
    parts = rel.parts
    category = parts[0] if len(parts) > 1 else "root"
    name = path.stem
    mtime = datetime.fromtimestamp(path.stat().st_mtime).isoformat()

    # 尝试解析 frontmatter
    try:
        text = path.read_text(encoding="utf-8")
        meta, _ = _parse_frontmatter(text)
        return {
            "path": str(rel),
            "category": meta.get("category", category),
            "title": meta.get("title", name),
            "date": meta.get("date", mtime[:10]),
            "tags": meta.get("tags", []),
            "author": meta.get("author", ""),
            "updated_at": mtime,
            "size_kb": round(path.stat().st_size / 1024, 1),
        }
    except Exception:
        return {
            "path": str(rel), "category": category,
            "title": name, "date": mtime[:10],
            "tags": [], "author": "", "updated_at": mtime,
            "size_kb": round(path.stat().st_size / 1024, 1),
        }


# ─── 核心 CRUD 操作 ────────────────────────────────────────────────────────

def write(
    category: str,
    title: str,
    content_body: str,
    tags: Optional[list[str]] = None,
    author: str = "Curator Agent",
    date_str: Optional[str] = None,
    extra_meta: Optional[dict[str, Any]] = None,
    update: bool = True,
) -> dict[str, Any]:
    """
    写入或更新一个知识资产 MD 文件。
    update=True: 追加到已有文件；update=False: 覆盖。
    """
    if category not in CATEGORIES:
        raise ValueError(f"Invalid category: {category}")

    path = make_path(category, title, date_str)
    path.parent.mkdir(parents=True, exist_ok=True)

    meta: dict[str, Any] = {
        "title": title,
        "date": date_str or date.today().isoformat(),
        "category": category,
        "tags": tags or [],
        "author": author,
        "id": path.stem,
        "updated_at": datetime.utcnow().isoformat(),
    }
    if extra_meta:
        meta.update(extra_meta)

    if update and path.exists():
        # 追加模式：读取旧内容，追加新 section
        old_text = path.read_text(encoding="utf-8")
        _, old_body = _parse_frontmatter(old_text)
        old_meta, _ = _parse_frontmatter(old_text)
        # 更新时间
        old_meta["updated_at"] = datetime.utcnow().isoformat()
        if tags:
            existing_tags = set(old_meta.get("tags", []))
            old_meta["tags"] = list(existing_tags | set(tags))
        meta = old_meta

        # 追加新内容块
        new_block = f"\n\n## {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} 更新\n\n{content_body}"
        full_body = old_body.rstrip() + new_block
    else:
        full_body = content_body

    # 写文件
    full_text = _make_frontmatter(meta) + full_body
    path.write_text(full_text, encoding="utf-8")

    # 更新 manifest
    _upsert_manifest_entry(_entry_from_path(path))

    return {"path": str(path.relative_to(KNOWLEDGE_DIR)), "size_kb": round(path.stat().st_size / 1024, 1)}


def read(path_or_slug: str) -> dict[str, Any]:
    """
    读取一个知识文件。
    参数可以是相对路径（knowledge/daily/2026-04-06.md）或 slug（2026-04-06）。
    """
    # 尝试直接路径
    direct = KNOWLEDGE_DIR / path_or_slug
    if direct.exists():
        path = direct
    else:
        # 模糊匹配：在所有子目录中找
        found = list(KNOWLEDGE_DIR.rglob(f"*{path_or_slug}*.md"))
        if not found:
            raise FileNotFoundError(f"知识文件未找到: {path_or_slug}")
        path = found[0]

    text = path.read_text(encoding="utf-8")
    meta, body = _parse_frontmatter(text)
    rel = path.relative_to(KNOWLEDGE_DIR)
    return {
        "path": str(rel),
        "meta": meta,
        "body": body.strip(),
        "word_count": len(body.split()),
    }


def list_entries(
    category: Optional[str] = None,
    tag: Optional[str] = None,
    limit: int = 50,
) -> list[dict[str, Any]]:
    """
    列出知识资产（支持按分类/标签过滤）。
    不解析文件内容，只读文件列表 + frontmatter 高效过滤。
    """
    manifest = _load_manifest()
    entries = manifest.get("entries", [])

    # 过滤
    if category:
        entries = [e for e in entries if e.get("category") == category]
    if tag:
        entries = [e for e in entries if tag in e.get("tags", [])]

    # 按日期倒序
    entries.sort(key=lambda e: e.get("date", ""), reverse=True)
    return entries[:limit]


def search(keyword: str, limit: int = 20) -> list[dict[str, Any]]:
    """
    全文关键词搜索（基于文件名 + 路径 + tags）。
    深度内容搜索由 LLM 提供语义检索。
    """
    import urllib.parse
    kw = keyword.lower()
    results = []

    for path in KNOWLEDGE_DIR.rglob("*.md"):
        # 跳过 manifest 自身
        if path.name.startswith("_"):
            continue
        rel = str(path.relative_to(KNOWLEDGE_DIR)).lower()
        if kw in rel:
            try:
                results.append(_entry_from_path(path))
            except Exception:
                pass
        else:
            # 读 frontmatter tags
            try:
                text = path.read_text(encoding="utf-8")
                meta, _ = _parse_frontmatter(text)
                if kw in str(meta.get("tags", [])).lower() or kw in meta.get("title", "").lower():
                    results.append(_entry_from_path(path))
            except Exception:
                pass

    return sorted(results, key=lambda e: e.get("updated_at", ""), reverse=True)[:limit]


def _upsert_manifest_entry(entry: dict[str, Any]) -> None:
    """更新 manifest 索引（插入或更新已有条目）。"""
    manifest = _load_manifest()
    entries = manifest.get("entries", [])
    path_key = entry.get("path", "")

    # 更新或追加
    updated = False
    for i, e in enumerate(entries):
        if e.get("path") == path_key:
            entries[i] = {**e, **entry}
            updated = True
            break
    if not updated:
        entries.append(entry)

    # 裁剪到最近 500 条
    entries = sorted(entries, key=lambda x: x.get("date", ""), reverse=True)[:500]
    manifest["entries"] = entries
    manifest["updated_at"] = datetime.utcnow().isoformat()
    manifest["total"] = len(entries)
    _save_manifest(manifest)


# ─── 快捷写入函数 ─────────────────────────────────────────────────────────

def write_daily_log(
    content: str,
    date_str: Optional[str] = None,
    tags: Optional[list[str]] = None,
) -> dict:
    """
    写入每日研究日志。
    每日只保留一个文件，多次调用追加内容。
    """
    return write(
        category="daily",
        title=f"每日研究日志 {date_str or date.today().isoformat()}",
        content_body=content,
        tags=tags or ["daily", "research-log"],
        author="Curator Agent",
        date_str=date_str,
        update=True,
    )


def write_model_card(
    model_id: str,
    model_name: str,
    benchmark_data: str,
    analysis: str,
    tags: Optional[list[str]] = None,
) -> dict:
    """写入或更新一个模型的知识卡。"""
    body = f"\n## 基本信息\n\n- **模型名称**: {model_name}\n- **模型 ID**: {model_id}\n\n## Benchmark 数据\n\n{benchmark_data}\n\n## 分析\n\n{analysis}\n"
    return write(
        category="models",
        title=model_id,
        content_body=body,
        tags=tags or ["model-card", "sota"],
        extra_meta={"model_id": model_id, "model_name": model_name},
        update=False,
    )


def write_skill_doc(
    skill_id: str,
    skill_name: str,
    description: str,
    rules: str,
    changelog: Optional[str] = None,
) -> dict:
    """写入或更新一个 Skill 文档。"""
    body = f"\n## Skill 描述\n\n{description}\n\n## 执行规则\n\n{rules}\n"
    if changelog:
        body += f"\n## 变更历史\n\n{changelog}\n"
    return write(
        category="skills",
        title=skill_id,
        content_body=body,
        tags=["skill", "agent-protocol"],
        extra_meta={"skill_id": skill_id, "skill_name": skill_name},
        update=False,
    )


# ─── 知识体系健康度报告 ────────────────────────────────────────────────────

def health_report() -> dict:
    """返回知识库健康度报告（供前端展示）。"""
    manifest = _load_manifest()
    entries = manifest.get("entries", [])
    total = len(entries)

    by_category: dict[str, int] = {}
    by_tag: dict[str, int] = {}
    recent_dates: set[str] = set()

    for e in entries:
        by_category[e.get("category", "unknown")] = by_category.get(e.get("category", "unknown"), 0) + 1
        for tag in e.get("tags", []):
            by_tag[tag] = by_tag.get(tag, 0) + 1
        recent_dates.add(e.get("date", "")[:7])  # YYYY-MM

    total_files = sum(1 for _ in KNOWLEDGE_DIR.rglob("*.md"))

    return {
        "total_assets": total,
        "total_files": total_files,
        "by_category": by_category,
        "top_tags": sorted(by_tag.items(), key=lambda x: x[1], reverse=True)[:10],
        "active_months": len(recent_dates),
        "manifest_version": manifest.get("version", "1.0"),
        "last_updated": manifest.get("updated_at", ""),
    }
