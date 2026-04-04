# LLaVA-OneVision-1.5

> **数据可靠度：A**（LLaVA 官方 GitHub & HuggingFace）

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型名称** | LLaVA-OneVision-1.5（LLaVA-Next-OneVision） |
| **发布方** | LLaVA-VL 团队（主导：微软 & 威斯康星大学麦迪逊分校） |
| **参数量级** | 4B / 8B（两种规格，另有 72B MoE 版本） |
| **支持的模态** | 文本 + 图像 + 视频 + 多图 + 交错图文 |
| **许可协议** | LLaVA License（BSD-3-Clause，可商用） |
| **HuggingFace** | https://huggingface.co/lmms-lab/LLaVA-OneVision-1.5-4B-Instruct <br> https://huggingface.co/lmms-lab/LLaVA-OneVision-1.5-8B-Instruct |
| **魔搭 ModelScope** | https://modelscope.cn/models/lmms-lab/LLaVA-OneVision |
| **发布年份/版本** | 2025年9月（LLaVA-OneVision-1.5 正式发布） |

## 核心能力描述

LLaVA-OneVision-1.5 是 LLaVA 系列的最新里程碑，主打"全开源 Democratized Training"：

- **全开源数据与训练**：完全开源训练数据（LLaVA-OneVision-Data）和训练代码，降低多模态研究门槛
- **任意视觉输入**：支持单图、多图、视频、交错图文等多种输入格式的统一处理
- **高性价比**：4B 版本即可实现超越更大模型的效果，训练成本仅 ~$16,000（A100 GPU）
- **视频理解**：在 Video Understanding benchmark 上达到开源 SOTA
- **学术友好**：数据集和训练代码全开源，适合学术研究二次开发
- **强化学习版**：LLaVA-OneVision-1.5-RL 基于 RL 进一步提升

## 性能亮点

| 基准 | LLaVA-OneVision-1.5-8B |
|------|----------------------|
| MMMU | ~61 分 |
| MathVista | ~59 分 |
| Video-MME | 开源领先 |
| 训练成本 | ~$16,000（完全可复现） |

## 适用场景

- 多模态学术研究
- 低成本视觉模型训练
- 视频理解应用
- 多图/文档分析
- 开源社区定制开发

## 备注

LLaVA-OneVision-1.5 的最大贡献在于"完全民主化"——不仅开源模型权重，还开源了训练数据和完整训练流程。这使得任何研究团队都可以基于此训练自己的视觉模型，对于推动多模态 AI 研究民主化具有重要意义。
