# InternVL3

> **数据可靠度：A**（上海 AI Lab 官方 GitHub & arXiv 论文）

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型名称** | InternVL3（InternVL3 系列） |
| **发布方** | 上海人工智能实验室（Shanghai AI Lab, OpenGVLab） |
| **参数量级** | 1B / 8B / 14B / 38B / 78B（含视觉编码器总量） |
| **支持的模态** | 文本 + 图像 + 视频 + 多图 + 交错图文 |
| **许可协议** | InternVL License（BSD-3-Clause 类，开源可商用） |
| **HuggingFace** | https://huggingface.co/OpenGVLab/InternVL3-8B <br> https://huggingface.co/OpenGVLab/InternVL3-14B <br> https://huggingface.co/OpenGVLab/InternVL3-38B <br> https://huggingface.co/OpenGVLab/InternVL3-78B |
| **魔搭 ModelScope** | https://modelscope.cn/models/OpenGVLab/InternVL3 |
| **发布年份/版本** | 2025年4月（论文发布），2025年4月~8月（各规模陆续开源） |

## 核心能力描述

InternVL3 是上海 AI Lab 推出的第三代InternVL系列，引入**原生多模态预训练（Native Multimodal Pretraining）**范式：

- **原生多模态预训练**：不再依赖独立 LLM + 视觉编码器的拼接，而是从底层统一建模，训练效率与效果大幅提升
- **超大视觉编码器**：基于改进的 ViT 架构（InternViT），具备更强的视觉表征能力
- **超强推理**：引入推理链机制，在视觉数学、复杂推理任务上表现突出
- **视频理解**：支持长视频理解，时间戳定位与事件追踪能力显著提升
- **多语言**：支持中英双语及多语言理解
- **Agent 能力**：可作为视觉 Agent 执行工具调用、任务规划

## 性能亮点

| 基准 | InternVL3-78B 表现 |
|------|------------------|
| MMMU | ~72 分（开源最高） |
| MathVista | ~66 分 |
| VQA-v2 | ~86 分 |
| DocVQA | ~96 分 |

## 适用场景

- 高精度文档/表单理解
- 复杂视觉推理与数学
- 长视频内容分析
- 多模态检索与 RAG
- 企业级视觉 AI 系统

## 备注

InternVL3 系列是目前开源社区公认的顶级 VLM 选项，78B 版本在多项 benchmark 上可与 GPT-4V 相媲美。上海 AI Lab 提供了从 1B 到 78B 的全规格覆盖，开发者可根据硬件条件灵活选择。其中 8B/14B 版本对消费级 GPU 友好，推理成本低。
