# Qwen2.5-VL

> **数据可靠度：A**（官方博客 & HuggingFace 官方页面）

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型名称** | Qwen2.5-VL |
| **发布方** | 阿里巴巴通义实验室（Alibaba Cloud, Qwen Team） |
| **参数量级** | 3B / 7B / 72B（三种规格） |
| **支持的模态** | 文本 + 图像 + 视频（动态分辨率、多帧处理） |
| **许可协议** | Tongyi Qianwen License（阿里巴巴商业友好许可，开源可商用，限制输出合规） |
| **HuggingFace** | https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct <br> https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct <br> https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct |
| **魔搭 ModelScope** | https://modelscope.cn/models/Qwen/Qwen2.5-VL |
| **发布年份/版本** | 2025年1月（正式发布），2025年3月（32B 强化学习版本） |

## 核心能力描述

Qwen2.5-VL 是阿里巴巴 Qwen 系列新一代旗舰视觉-语言模型，相比前代 Qwen2-VL 有显著提升：

- **超长视频理解**：原生支持超长视频（小时级）处理，可进行持续视频理解与问答
- **动态分辨率（Dynamic Resolution）**：将图像映射为任意分辨率的视觉 token，无固定分辨率限制，适配各类图片比例
- **增强的 OCR 和文档理解**：在文档理解、表格解析、数学公式识别等任务上达到 SOTA 水准
- **多语言支持**：支持中文、英文等 32+ 语言，覆盖全球主要语种
- **Agent 能力**：可作为视觉 Agent，支持工具调用、网页操作等复杂任务
- **强化学习版本**：Qwen2.5-VL-32B-Instruct 通过强化学习进一步提升数学和推理能力，超越更大的 72B 模型

## 性能亮点

| 基准 | Qwen2.5-VL-72B |
|------|---------------|
| MMMU（大学级多模态推理） | ~68 分 |
| MathVista（数学视觉） | ~64 分 |
| Video-MME（视频理解） | SOTA |

## 适用场景

- 视频理解与长视频分析
- 多语言图文理解与翻译
- 复杂文档（PDF/PPT/截图）解析
- 视觉 Agent 与自动化操作
- 视觉问答与推理

## 备注

Qwen2.5-VL 是 2025 年上半年最具影响力的开源 VLM 之一，72B 版本在多项权威评测中超越 GPT-4o mini，尤其在中文和多语言场景下优势明显。32B 强化学习版以更小参数量超越 72B 基础版，展现了 RL Scaling 的潜力。
