# Model Card: Gemma 4

> 视觉-语言多模态模型 | Google DeepMind | 2026年4月2日

---

## 1. 基本信息

| 字段 | 内容 |
|------|------|
| **模型全称** | Gemma 4 |
| **发布方** | Google DeepMind |
| **参数量级** | 4个规格：E2B / E4B / 26B A4B（MoE） / 31B |
| **模态** | **文本 + 图像 + 视频**（全系列原生多模态）；E2B / E4B 额外支持音频 |
| **发布日期** | **2026年4月2日** |
| **开源时间** | 2026年4月2日（同步开源） |
| **许可证** | **Apache 2.0**（全系列，完全开放） |
| **代码仓库** | https://github.com/google-deepmind/gemma（推测）；HuggingFace 全系列上架 |
| **官方文档** | https://ai.google.dev/gemma/docs/core/model_card_4 |
| **官方博客** | https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/ |

---

## 2. 许可证与商用合规

| 许可证 | 商用意况 |
|--------|----------|
| **Apache 2.0** | ✅ 可商用（无任何附加条款，完全开放） |

> **重大变化**：Gemma 4 从此前 Gemma 3 的"半开放"（Gemma Terms）切换为 **Apache 2.0**，是 Google 史上最大程度的开源开放。
>
> **来源**：[Google Blog Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)；[VentureBeat](https://venturebeat.com/technology/google-releases-gemma-4-under-apache-2-0-and-that-license-change-may-matter)；[Ars Technica](https://arstechnica.com/ai/2026/04/google-announces-gemma-4-open-ai-models-switches-to-apache-2-0-license/)

---

## 3. HuggingFace + ModelScope 链接

| 模型规格 | HuggingFace |
|----------|-------------|
| Gemma 4 全系列 | https://huggingface.co/google |
| Gemma 4 E2B | https://huggingface.co/google/gemma-4-E2B |
| Gemma 4 E4B | https://huggingface.co/google/gemma-4-E4B |
| Gemma 4 26B A4B | https://huggingface.co/google/gemma-4-26b-a4b |
| Gemma 4 31B | https://huggingface.co/google/gemma-4-31b |
| Gemma 4 HuggingFace Blog | https://huggingface.co/blog/gemma4 |
| NVIDIA Build (31B-IT) | https://build.nvidia.com/google/gemma-4-31b-it/modelcard |

---

## 4. Benchmark 数据

> ⚠️ **注意**：Gemma 4 于 2026-04-02 发布，官方尚未完整披露所有 benchmark 数据。以下为已确认数据，待持续更新。

### Gemma 4 31B（已披露数据）

| Benchmark | Gemma 4 31B | 说明 |
|-----------|-------------|------|
| **AIME 2026** | **89.2%** | 数学推理高难度测试 |
| **LiveCodeBench v6** | **80.0%** | 编程能力 |
| **Codeforces ELO** | 高分 | 竞赛编程评分 |
| **MMMU（预估）** | 竞争前列 | 大学多学科理解 |

> **来源**：[VentureBeat 报道](https://venturebeat.com/technology/google-releases-gemma-4-under-apache-2-0-and-that-license-change-may-matter)；[NVIDIA Build Model Card](https://build.nvidia.com/google/gemma-4-31b-it/modelcard)

### Gemma 4 系列能力亮点

- **原生链式思维（CoT）**：内置高级推理能力
- **Agentic Workflows**：支持代理任务执行
- **多模态输入**：全系列支持图像/视频理解，E2B/E4B 支持音频
- **140+ 语言**：覆盖全球主要语言

---

## 5. SOTA 声明

**✅ 有量化证据支持的声明（官方 + 第三方）：**

- **Apache 2.0 史上最大开放**：Google 首次将旗舰级 Gemma 模型完全切换至 Apache 2.0
- **AIME 2026 得分 89.2%**：数学推理性能极佳
- **LiveCodeBench v6 得分 80.0%**：编程能力顶级
- **Google 官方声称**：*"most capable open models to date"*（有量化 benchmark 支撑）

> ⚠️ **边界**：Gemma 4 的 VLM 评测（多模态理解 benchmark）具体分数数据在官方完整文档中尚未完全披露，不声称通用 VLM SOTA。但在 **Apache 2.0 开放程度 + 旗舰尺寸 + 全模态支持** 的综合维度上，Gemma 4 处于行业前沿。

---

## 6. 技术亮点

| 亮点 | 描述 |
|------|------|
| **Apache 2.0 全面开放** | 史上最大程度的 Google 开源开放，无使用限制 |
| **四规格覆盖全场景** | E2B（边缘设备）→ E4B → 26B A4B（MoE）→ 31B（旗舰） |
| **原生统一多模态架构** | 统一架构处理文本、图像、视频（+小规格音频） |
| **高级链式思维（CoT）** | 内置高级推理能力，31B 版本 AIME 2026 高达 89.2% |
| **Agentic 支持** | 支持复杂代理工作流 |
| **140+ 语言** | 覆盖全球主要语言 |
| **构建于 Gemini 3 技术** | 借鉴 Google 最强闭源模型的核心技术 |

> **来源**：[Google Blog](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)；[VentureBeat](https://venturebeat.com/technology/google-releases-gemma-4-under-apache-2-0-and-that-license-change-may-matter)；[Wavespeed.ai](https://wavespeed.ai/blog/posts/what-is-google-gemma-4/)

---

## 7. 入选理由

1. **2026年4月2日最新发布**——距调研日期仅2天，是本期调研时间窗口内最新的高影响力 VLM
2. **Google DeepMind 出品**——全球最具影响力 AI 研究机构之一
3. **Apache 2.0 全系列**——商业使用完全无门槛
4. **全模态覆盖**：图像 + 视频 + 文本（+ E2B/E4B 音频），是真正意义的多模态开放模型
5. **旗舰 31B** 在 AIME 2026（89.2%）和编程 benchmark 上有极强表现
6. **四规格策略**：从边缘设备（E2B）到工作站（31B），覆盖完整部署场景

---

## 8. 信息源列表

| 优先级 | 来源 | 链接 |
|--------|------|------|
| T0 | Google AI Gemma 4 官方文档 | https://ai.google.dev/gemma/docs/core/model_card_4 |
| T0 | Google 官方博客 | https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/ |
| T0 | HuggingFace Gemma 4 博客 | https://huggingface.co/blog/gemma4 |
| T0 | Google AI Gemma 4 概览 | https://ai.google.dev/gemma/docs/core |
| T1 | VentureBeat 报道 | https://venturebeat.com/technology/google-releases-gemma-4-under-apache-2-0-and-that-license-change-may-matter |
| T1 | Ars Technica 报道 | https://arstechnica.com/ai/2026/04/google-announces-gemma-4-open-ai-models-switches-to-apache-2-0-license/ |
| T1 | NVIDIA Build Model Card | https://build.nvidia.com/google/gemma-4-31b-it/modelcard |
| T2 | Wavespeed.ai 深度报道 | https://wavespeed.ai/blog/posts/what-is-google-gemma-4/ |
| T3 | Maarten Grootendorst Visual Guide | https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-gemma-4 |

---

*最后更新：2026-04-04 | 调研员：@vlm-researcher | 注：部分 benchmark 精确数据待官方文档完整披露后更新*
