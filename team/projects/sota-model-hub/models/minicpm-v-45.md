# MiniCPM-V 4.5

> **数据可靠度：A**（Nature 论文 & OpenBMB 官方 GitHub）

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型名称** | MiniCPM-V 4.5（代号：小猛犸视觉） |
| **发布方** | 面壁智能（OpenBMB），清华大学 NLP 实验室孵化 |
| **参数量级** | 8B（活跃参数，端侧友好） |
| **支持的模态** | 文本 + 图像 + 文档 + 图表 + 屏幕截图 |
| **许可协议** | OpenBMB License（BSD-3-Clause 类，开源可商用） |
| **HuggingFace** | https://huggingface.co/openbmb/MiniCPM-V-4_5 |
| **魔搭 ModelScope** | https://modelscope.cn/models/OpenBMB/MiniCPM-V-4_5 |
| **发布年份/版本** | 2025年8月~9月（arXiv 2509.18154，Nature 论文 2025年7月发表） |

## 核心能力描述

MiniCPM-V 4.5 是面壁智能打造的高效视觉-语言模型，以仅 8B 参数在多项 benchmark 上超越 GPT-4o：

- **超高效率**：仅 8B 参数，推理显存需求低，可在消费级 GPU（RTX 3090）上流畅运行
- **任意分辨率**：基于 LLaVA-UHD 架构，支持任意宽高比图像，最高 1.8M 像素（1344×1344）
- **SOTA 性能**：Nature 公开发表论文，8B 参数超越 GPT-4o 等专有模型
- **强 OCR 能力**：在 OCRBench 等评测中达到开源领先水平
- **多场景切换**：支持 OCR 模式、推理模式、上下文模式自动切换
- **中文友好**：针对中文视觉理解深度优化，中文 OCR 和问答效果出色

## 性能亮点

| 基准 | MiniCPM-V 4.5（8B）表现 |
|------|------------------------|
| OpenCompass VLM Rank | 超越 Qwen2.5-VL-72B |
| MMMU | ~59 分 |
| MathVista | ~63 分 |
| OCRBench | 开源领先 |

## 适用场景

- 端侧/移动端视觉 AI 部署
- 高精度中文 OCR
- 移动文档扫描与理解
- 低显存环境的多模态应用
- 中文视觉问答

## 备注

MiniCPM-V 4.5 是"小模型大能力"的典型代表，Nature 公开发表论文证明了其方法论的有效性。8B 参数在消费级硬件上即可运行，大幅降低多模态 AI 应用门槛，特别适合移动端和边缘计算场景。
