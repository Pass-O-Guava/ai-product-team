# SKILL.md — SOTA Model Surveyor

> **技能名称：** sota-model-surveyor  
> **版本：** 1.0.0  
> **适用场景：** 调研最新 SOTA 模型，产出标准化 Model Card + 知识对比文件  
> **触发词：** 调研 SOTA、模型调研、Model Card、查找最新模型、调研报告  

---

## 技能概述

本技能指导 AI 智能体完成「最新 SOTA 多模态统一模型调研」全流程，从搜索 → 信息提取 → Model Card 撰写 → 知识沉淀，全部标准化输出。

---

## 任务定义

**目标：** 调研指定时间窗口内发布的最新 SOTA 多模态端到端统一模型，产出：
1. 每个模型的标准化 Model Card（`.md` 文件）
2. 横向对比知识体系文件（`.md` 文件）
3. （可选）可运行 Demo 代码（`.py` / `.js`）

---

## 信息源优先级（T0/T1/T2 评级）

| 等级 | 来源 | 用途 |
|------|------|------|
| **T0** | HuggingFace 官方页 / ModelScope 官方页 | 模型规格、下载链接、许可证 |
| **T1** | 官方 GitHub / 官方博客 / 官方新闻稿 | 技术细节、发布时间、Benchmark 声称 |
| **T2** | arXiv 论文 / 官方 Leaderboard | 具体分数、论文深度解读 |
| **❌ 禁用** | 无来源信息 / 第三方转载无原始链接 | 不录入 SOTA 声明 |

---

## 时间窗口规则

优先搜索顺序：
1. **最近 1 周 → 1 个月 → 1 季度 → 最近半年**
2. 超过半年的模型**不收录**
3. 每日调研任务中给出具体截止日期，严格遵守

---

## Model Card 标准化模板

每个模型输出到路径：
```
/workspace/team/projects/sota-model-hub/models/{category}/{model-name}.md
```

内容必须包含：基本信息 / 许可证 / 链接 / Benchmark / SOTA声明（有据/待验证/不可用）/
技术亮点 / 入选理由 / 信息源列表（附T0/T1/T2评级）

---

## 搜索策略（每次调研必执行）

### 步骤 1：批量搜索（5 个查询，并行）

```
Query 1: "{target_model} official release date benchmark HuggingFace ModelScope"
Query 2: "{target_model} technical specifications parameters modalities"
Query 3: "Jan/Feb/Mar 2026 new multimodal unified model release any-to-any"
Query 4: "{competitor} 2026 new release multimodal"
Query 5: "end-to-end multimodal unified model 2026 new release"
```

### 步骤 2：深度提取
对搜索结果中的高优先级链接（HuggingFace / 官方博客 / arXiv）使用 extract_content_from_websites 提取详细内容。

### 步骤 3：信息核实
- 官方博客日期 vs 实际发布日期 → 以官方博客/新闻稿最早时间为准
- SOTA 数字 → 检查是否为官方声称 + 是否有第三方对照
- 许可证 → HuggingFace Model Card 页 / 官方 GitHub README

---

## 输出纪律

| 规则 | 说明 |
|------|------|
| 日期精确到日 | 禁止「2026 年初」等模糊描述 |
| 无数据不上 SOTA | SOTA 声明必须有 Benchmark 表格支撑 |
| 可信度匹配 | 数字完整性差 → 降级 T2，不虚高 |
| 每模型独立文件 | 不合并，所有信息归入单一 .md |
| 完成后报告 | 必须列出：调研模型数 + 模型名单 |

---

## 异常处理

| 情况 | 处理方式 |
|------|----------|
| 搜索无结果 | 扩大时间窗口（半年内），换关键词 |
| 链接 404 / 内容缺失 | 跳过该来源，标记「T2 可信度」|
| SOTA 数字无法核实 | 改为「官方声称」，不作为有据声明 |
| 模型发布日不明确 | 找最早来源（博客/新闻/arXiv）以较早日期为准 |

---

## 输出文件位置约定

```
/workspace/team/projects/sota-model-hub/
├── models/
│   └── {category}/          # 如 multimodal/, text/, vision/
│       ├── {model-1}.md
│       └── {model-2}.md
├── knowledge/
│   └── {category}-{YYYY-MM-DD}.md
└── demos/
    └── {model-name}/        # 每个重要模型一个目录
        └── demo.py / demo.js
```
