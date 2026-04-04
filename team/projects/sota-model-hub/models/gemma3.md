# Gemma 3

> **数据可靠度：A**（Google DeepMind 官方博客）

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型名称** | Gemma 3（全系列，含视觉版本 Gemma-3-Variants） |
| **发布方** | Google DeepMind |
| **参数量级** | 1B / 4B / 12B / 27B（四种文本版，4B 及以上有视觉多模态版） |
| **支持的模态** | 文本 + 图像（4B 及以上版本支持） |
| **许可协议** | Gemma Terms of Use（允许商业使用，有使用限制条款） |
| **HuggingFace** | https://huggingface.co/google/gemma-3-4b-it <br> https://huggingface.co/google/gemma-3-12b-it |
| **魔搭 ModelScope** | https://modelscope.cn/models/google/gemma-3 |
| **发布年份/版本** | 2025年3月（正式发布），2025年8月（模型卡更新） |

## 核心能力描述

Gemma 3 是 Google 轻量级开源模型 Gemma 系列的第三代：

- **多语言领先**：支持中文、英文等 140+ 语言，是当前开源模型中多语言覆盖最广的之一
- **128K 超长上下文**：原生支持 128K token 上下文，适合长文档处理
- **多模态支持**：4B 及以上版本支持图像理解，在视觉任务上表现优异
- **高效率**：针对单 GPU 推理优化，12B 版本可在一张消费级 GPU 上运行
- **多平台支持**：支持 vLLM、Ollama、HuggingFace Transformers 等主流推理框架
- **多格式支持**：支持 PyTorch、JAX、Transformers 等框架
- **Gemini 2.0 技术下放**：继承 Gemini 系列最新训练技术

## 性能亮点

| 基准 | Gemma-3-27B 表现 |
|------|-----------------|
| MMLU | ~87 分（领先开源） |
| 多语言 | 140+ 语言支持 |
| 推理效率 | 单 GPU 可运行 27B |
| 视觉理解 | 4B+ 版本可用 |

## 适用场景

- 多语言全球化应用
- 长文本处理与分析
- 单 GPU 部署场景
- 移动/边缘设备（1B/4B）
- 学术研究与模型比较基准

## 备注

Gemma 3 是 Google 推动开源 AI 的重要举措，1B~27B 的全规格覆盖使得从手机到服务器的全场景部署成为可能。其 140+ 语言支持对国际化应用极具吸引力，是当前最具影响力的开源 LLM 之一。
