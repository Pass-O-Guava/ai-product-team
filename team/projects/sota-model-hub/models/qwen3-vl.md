# Qwen3-VL

> **数据可靠度：A**（GitHub 官方公告 & 多家权威媒体报道）

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型名称** | Qwen3-VL |
| **发布方** | 阿里巴巴通义实验室（Alibaba Cloud, Qwen Team） |
| **参数量级** | 3B / 8B / 72B（三种规格）；另有 MoE 架构版本 |
| **支持的模态** | 文本 + 图像 + 视频 + 多图 + 交错图文（Interleaved） |
| **许可协议** | Tongyi Qianwen License（阿里巴巴商业友好许可，可商用） |
| **HuggingFace** | https://huggingface.co/Qwen/Qwen3-VL |
| **魔搭 ModelScope** | https://modelscope.cn/models/Qwen/Qwen3-VL |
| **发布年份/版本** | **2025-09-23**（首发）；2025-10-29（Qwen3-VL-235B-A22B-Instruct GGUF） |

## 核心能力描述

Qwen3-VL 是 Qwen 系列的第三代视觉-语言模型，相比 Qwen2.5-VL 带来全面升级：

- **256K 超长上下文**：支持 256K token 上下文窗口，可一次性理解海量图文交错内容
- **原生空间智能（Spatial Intelligence）**：增强对空间关系、三维布局的理解，适用于图表分析和场景推理
- **原生视频理解**：支持长达数小时的视频流理解，具备更强的时间推理能力
- **更强推理能力**：引入思维链（Chain-of-Thought）强化，复杂推理任务表现大幅提升
- **多语言 OCR**：支持 32+ 语言的文档 OCR 与理解
- **Qwen3-VL-Embedding**：同步开源了多模态嵌入模型，支持视觉语义检索
- **视频字幕与问答**：视频理解 benchmark 达到开源 SOTA

## 性能亮点

| 基准 | Qwen3-VL-72B 表现 |
|------|------------------|
| MMMU | 超越 GPT-4o |
| Video-MME | 开源 SOTA |
| MathVista | 大幅超越 Qwen2.5-VL |
| 多语言 OCR | 32+ 语言领先 |

## 适用场景

- 超长文档/视频的端到端理解
- 海量图文数据库的语义检索
- 空间推理与图表深度分析
- 多语言企业级视觉文档处理
- 多模态 Agent 系统

## 备注

Qwen3-VL 是截至 2025 年末最强的开源 VLM，72B 版本在多项 benchmark 上超越 GPT-4o 和 Claude-3.5 Sonnet，在中文场景下优势尤为突出。其超长上下文和空间推理能力使其成为复杂企业级应用的理想选择。
