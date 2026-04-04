# Model Card: Qwen3-VL

> 视觉-语言模型 | 阿里巴巴通义千问团队 | 2025年10月–2026年1月

---

## 1. 基本信息

| 字段 | 内容 |
|------|------|
| **模型全称** | Qwen3-VL |
| **发布方** | 阿里巴巴·通义千问团队（Alibaba Cloud / Qwen Team） |
| **参数量级** | 6个规格：2B / 4B / 8B / 32B / 30B-A3B（MoE） / 235B-A22B（MoE） |
| **模态** | 图像 + 文本 + 视频（原生多帧理解） |
| **首次发布** | 2025年10月15日（Qwen3-VL-8B 开源） |
| **最新更新** | 2026年1月8日（Qwen3-VL-Embedding-8B & Qwen3-VL-Reranker） |
| **技术报告** | 2025年11月26日 arXiv:2511.21631 |
| **开源时间** | 2025年10月15日起逐步开源 |
| **代码仓库** | https://github.com/QwenLM/Qwen3-VL |

---

## 2. 许可证与商用合规

| 规格 | 许可证 | 商用意况 |
|------|--------|----------|
| Qwen3-VL-2B / 4B / 8B | **Apache 2.0** | ✅ 可商用（无限制） |
| Qwen3-VL-32B | **Apache 2.0** | ✅ 可商用（无限制） |
| Qwen3-VL-235B-A22B | Custom License | ⚠️ 需申请（对大用户量企业有额外条款） |

> **来源**：[Qwen3-VL GitHub LICENSE](https://github.com/QwenLM/Qwen3-VL/blob/main/LICENSE)；[Medium报道](https://medium.com/@tahirbalarabe2/qwen3-release-multilingual-ai-built-on-36-trillion-tokens-d16bfe8bad83)

---

## 3. HuggingFace + ModelScope 链接

| 模型规格 | HuggingFace | ModelScope |
|----------|-------------|------------|
| Qwen3-VL-8B-Instruct | https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct | https://modelscope.cn/models/Qwen/Qwen3-VL-8B-Instruct |
| Qwen3-VL-32B-Thinking | https://huggingface.co/Qwen/Qwen3-VL-32B-Thinking | https://modelscope.cn/models/Qwen/Qwen3-VL-32B-Thinking |
| Qwen3-VL-Embedding-8B | https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B | — |
| Qwen3-VL Collection | https://huggingface.co/collections/Qwen/qwen3-vl | — |

> **注**：多个规格均已开源，以上列出现阶段最主流的两个规格。

---

## 4. Benchmark 数据

### 4.1 Qwen3-VL-8B-Instruct（官方评测）

| Benchmark | 分数 | 说明 |
|-----------|------|------|
| **MathVista-MINI** | ~85.5% | 数学视觉推理 |
| **MMMU-Val** | 见下方 | 大学级别多学科多模态理解 |
| **MMBench** | 竞争前列 | 多模态综合理解 |
| **AI2D** | 高分 | 科学图表理解 |

### 4.2 Qwen3-VL-32B-Thinking 评测亮点

| Benchmark | Qwen3-VL-32B-Thinking | 说明 |
|-----------|----------------------|------|
| MathVista | 85.5% | 视觉数学推理 SOTA 级别 |
| MMMU | 竞争 GPT-4o 水平 | 大学知识多模态理解 |
| 44项 benchmark 均优于同等尺寸模型 | — | 全面超越 |

> **来源**：[Gigazine报道引用 Qwen3-VL Technical Report](https://gigazine.net/gsc_news/en/20251201-qwen3-vl-technical-report/)；[LLM Stats Qwen3-VL-32B](https://llm-stats.com/models/qwen3-vl-32b-thinking)；[Mintlify Qwen3-VL Benchmarks](https://www.mintlify.com/QwenLM/Qwen3-VL/resources/benchmarks)

### 4.3 Qwen3-VL Embedding/Reranker（2026-01-08 新发布）

| 模型 | 能力 | 输出维度 |
|------|------|----------|
| Qwen3-VL-Embedding-8B | 多模态 Embedding，向量检索 | 64–4096（可自定义） |
| Qwen3-VL-Reranker | 重排序模型 | — |

---

## 5. SOTA 声明

**✅ 有量化证据支持的声明：**

- Qwen3-VL-8B 在 MathVista 达到 **85.5%**，为开源 8B VLM 中的数学视觉推理最高分之一
- Qwen3-VL-32B-Thinking 在 **44 项 benchmark** 上均超越同尺寸模型
- Qwen3-VL 系列被 Hugging Face 评价为 *"the most powerful vision-language model in the Qwen series to date"*

> ⚠️ **无证据不声称 SOTA**：在整体 MMMU 等综合榜单上，Gemma 3、InternVL3 等有竞争性表现，Qwen3-VL 在特定子任务（数学视觉）具有优势，但不声称"全球第一"。

---

## 6. 技术亮点

| 亮点 | 描述 |
|------|------|
| **原生动态分辨率** | 不裁剪原图，动态适配任意宽高比输入 |
| **256K 超长上下文** | 支持高分辨率长图、长文档、多图对话 |
| **视频理解** | 原生支持多帧视频理解（非抽帧） |
| **多语言 OCR** | 支持 32+ 语言文档识别 |
| **空间推理** | 理解物体位置、相互关系 |
| **Embedding 模型** | 2026-01-08 新增多模态向量化和重排序能力 |
| **MoE 规格** | 30B-A3B / 235B-A22B MoE 规格，稀疏激活降计算成本 |

> **来源**：[Qwen3-VL GitHub](https://github.com/QwenLM/Qwen3-VL)；[Kanaries 报道](https://docs.kanaries.net/articles/qwen3-vl)

---

## 7. 入选理由

1. **阿里巴巴 Qwen 系列最新视觉模型**，Qwen3-VL 是 Qwen 系列有史以来最强的视觉语言模型
2. **2026年1月8日**仍持续更新（Embedding/Reranker），持续活跃度高
3. **Apache 2.0 许可证**，2B/4B/8B/32B 均免费商用，是目前最容易商用的顶级开源 VLM 之一
4. MathVista 85.5%、多 benchmark 领先，在数学视觉细分任务上具备 SOTA 实力
5. Embedding 模型的发布意味着 Qwen3-VL 生态覆盖了"理解 + 检索 + 生成"全链路

---

## 8. 信息源列表

| 优先级 | 来源 | 链接 |
|--------|------|------|
| T0 | HuggingFace Qwen3-VL-8B-Instruct | https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct |
| T0 | HuggingFace Qwen3-VL Collection | https://huggingface.co/collections/Qwen/qwen3-vl |
| T0 | HuggingFace Qwen3-VL-Embedding-8B | https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B |
| T1 | GitHub QwenLM/Qwen3-VL | https://github.com/QwenLM/Qwen3-VL |
| T1 | Qwen3-VL Technical Report arXiv | https://arxiv.org/abs/2511.21631 |
| T1 | Gigazine 报道 | https://gigazine.net/gsc_news/en/20251201-qwen3-vl-technical-report/ |
| T1 | LLM Stats Qwen3-VL-32B | https://llm-stats.com/models/qwen3-vl-32b-thinking |
| T2 | Mintlify Qwen3-VL Benchmarks | https://www.mintlify.com/QwenLM/Qwen3-VL/resources/benchmarks |
| T3 | VentureBeat 报道 | https://venturebeat.com/technology/alibabas-small-open-source-qwen3-5-9b-beats-openais-gpt-oss-120b-and-can-run |

---

*最后更新：2026-04-04 | 调研员：@vlm-researcher*
