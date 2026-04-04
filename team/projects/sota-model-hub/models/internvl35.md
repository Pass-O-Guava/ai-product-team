# InternVL3.5

> **数据可靠度：A**（上海 AI Lab 官方 arXiv 论文 & GitHub 公告）

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型名称** | InternVL3.5 |
| **发布方** | 上海人工智能实验室（Shanghai AI Lab, OpenGVLab） |
| **参数量级** | 241B 总参数（MoE 架构，活跃参数约 28B-A28B），另有 Core 精简版 |
| **支持的模态** | 文本 + 图像 + 视频 + 多图 + 交错图文 + 音频（部分） |
| **许可协议** | InternVL License（BSD-3-Clause 类，开源可商用） |
| **HuggingFace** | https://huggingface.co/OpenGVLab/InternVL3_5-241B-A28B-Instruct |
| **魔搭 ModelScope** | https://modelscope.cn/models/OpenGVLab/InternVL3.5 |
| **发布年份/版本** | 2025年8月（arXiv 论文 2508.18265，2025年8月25日） |

## 核心能力描述

InternVL3.5 是 InternVL3 的增强版本，引入三大核心技术：

- **Cascade RL（级联强化学习）**：通过两阶段 RL 策略，大幅提升推理能力同时控制幻觉问题
- **ViR（Visual Reasoning Tokens）**：视觉推理 token 机制，增强复杂空间推理和多步推理能力
- **DvD（Dynamic Vision Discretization）**：动态视觉离散化，提升视觉 token 利用效率

**核心能力**：
- 在开源 VLM 中综合能力最强，被评为"当前最佳开源多模态模型"
- 支持多语言视觉理解（中文/英文/其他）
- 视频理解 SOTA（Video-MME 等 benchmark 领先）
- 强化的复杂推理与数学能力
- Core 版（InternVL3.5-Core）以更少活跃参数实现接近满血版性能

## 性能亮点

| 基准 | InternVL3.5 表现 |
|------|----------------|
| MMMU | ~73 分（开源最高之一） |
| MathVista | ~68 分 |
| Video-MME | 开源 SOTA |
| DocVQA | ~97 分 |
| OCRBench | 领先 |

## 适用场景

- 通用视觉问答与推理
- 视频内容理解与摘要
- 复杂文档/报告分析
- 多模态 Agent 与自动化
- 高精度视觉搜索

## 备注

InternVL3.5 是 2025 年下半年最具突破性的开源 VLM，在 Hugging Face 和开源社区中获得极高评价。241B MoE 版本以稀疏激活方式实现高效推理，Core 版则针对资源受限场景进行了优化。其 Cascade RL 方法对后续多模态 RL 研究有重要影响。
