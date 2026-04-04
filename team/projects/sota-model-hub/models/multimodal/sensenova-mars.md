# Model Card: SenseNova-MARS

> **模型名称：** SenseNova-MARS  
> **发布机构：** SenseTime（商汤科技）/ OpenSenseNova  
> **正式开源日期：** 2026-01-30  
> **可靠度评级：** T1（GitHub 官方 + arXiv 论文 + 新闻多源印证）

---

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型类型** | Multimodal Agentic Reasoning & Search（多模态智能体推理搜索） |
| **支持输入模态** | 文本、图像、视频（动态视觉推理 + 交错视觉理解） |
| **支持输出模态** | 文本、工具调用（搜索/推理链） |
| **规格版本** | SenseNova-MARS-8B / SenseNova-MARS-32B |
| **基础架构** | Hybrid Transformer-Mamba（混合 SSM） |
| **核心能力** | 自主规划步骤、调用多工具（文图搜索）、解决复杂跨模态任务 |

---

## 许可证

开源（OpenSenseNova 社区开源，GitHub 仓库可查）

---

## 链接

| 类型 | 链接 |
|------|------|
| **GitHub 仓库** | https://github.com/OpenSenseNova/SenseNova-MARS |
| **arXiv 论文** | https://arxiv.org/abs/2512.24330 |
| **arXiv HTML** | https://arxiv.org/html/2512.24330v2 |
| **HuggingFace Paper** | https://huggingface.co/papers/2512.24330 |
| **官方发布报道（英）** | https://blog.meetneura.ai/sensenova-mars-agentic-vlm/ |
| **官方发布报道（中）** | https://news.aibase.com/news/25115 |
| **OpenReview** | https://openreview.net/pdf?id=oQTEYI28zK |

---

## Benchmark

| 评测集 | SenseNova-MARS 成绩 | 说明 |
|--------|---------------------|------|
| 开源搜索 benchmark | SOTA | 官方声称 |
| 细粒度图像理解 | SOTA | 官方声称 |
| VSI-Bench | 已获采纳为官方评测集 | SenseNova 官方 |
| MMSI-Bench | 同上 | SenseNova 官方 |
| **8B vs GPT-5** | 8B 参数版超越强闭源模型 | OpenReview 论文 |

> ⚠️ 注：具体 Benchmark 数值需查阅 arXiv 论文原文；当前声明来自官方报道，可信度 T1。

---

## SOTA 声明

- ⚠️ **待验证 SOTA：** 官方声称 8B 版本超越 GPT-5 等强闭源模型，但具体 Benchmark 数值未在官方博客/新闻稿中完整列出，需参考 OpenReview 论文表格
- ✅ **开源 Agentic VLM 首屈一指：** 多源印证为 2026-01 时间窗口内最具影响力的开源多模态 Agent 模型

---

## 技术亮点

1. **动态视觉推理（Dynamic Visual Reasoning）**：不仅理解静态图像，还能进行时序/空间动态推理
2. **混合 Transformer-Mamba 架构**：结合 Transformer 的表达力与 Mamba SSM 的高效长序列建模
3. **多工具自主调用**：内置文图搜索、网页浏览等多模态工具链，支持 Agentic 规划-执行闭环
4. **深度视觉-语言融合**：通过交错视觉推理（Interleaved Visual Reasoning）实现复杂跨模态任务
5. **双规格开源**：8B（端侧）+ 32B（服务器）两步开源，覆盖不同算力场景

---

## 入选理由

SenseNova-MARS 是 2026 年 1 月最具影响力的开源多模态 Agent 模型，是 SenseTime 首次开源 Agentic VLM，混合 Transformer-Mamba 架构在多模态 Agent 领域具有独特性，8B 即可超越 GPT-5 部分能力指标，开源策略对社区意义重大。

---

## 信息源列表

| # | 类型 | 来源 | 链接 | 评级 |
|---|------|------|------|------|
| 1 | GitHub 官方仓库 | OpenSenseNova | https://github.com/OpenSenseNova/SenseNova-MARS | T0 |
| 2 | arXiv 论文 | arXiv | https://arxiv.org/abs/2512.24330 | T0 |
| 3 | 官方发布报道（英） | MeetNeura Blog | https://blog.meetneura.ai/sensenova-mars-agentic-vlm/ | T1 |
| 4 | 官方发布报道（中） | AIbase | https://news.aibase.com/news/25115 | T1 |
| 5 | OpenReview | OpenReview | https://openreview.net/pdf?id=oQTEYI28zK | T1 |
| 6 | Reddit 社区 | r/LocalLLaMA | https://www.reddit.com/r/LocalLLaMA/comments/1qr1p1u/sensetime_have_launched_and_opensourced/ | T2 |
