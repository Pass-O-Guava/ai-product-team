# SmolVLM2

> **数据可靠度：A**（HuggingFace 官方博客 & arXiv 论文）

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型名称** | SmolVLM2（Small Vision Language Model v2） |
| **发布方** | HuggingFace（Thomas Sileo 等工程师团队） |
| **参数量级** | 256M / 500M / 2.2B（三种极小规格） |
| **支持的模态** | 文本 + 图像 + 视频（SmolVLM2-500M-Video-Instruct） |
| **许可协议** | Apache 2.0（完全开源，可商用） |
| **HuggingFace** | https://huggingface.co/HuggingFaceTB/SmolVLM2-500M-Video-Instruct <br> https://huggingface.co/HuggingFaceTB/SmolVLM2-2.2B |
| **魔搭 ModelScope** | 暂无（主要在 HuggingFace） |
| **发布年份/版本** | 2025年2月（SmolVLM2 发布），2025年4月（arXiv 论文 2504.05299） |

## 核心能力描述

SmolVLM2 是 HuggingFace 推出的极致轻量级视觉语言模型，主打"小到极致，快到极致"：

- **256M 参数**：最小版本仅需 <1GB 显存即可推理，超越 300 倍大的 Idefics-80B
- **视频理解**：SmolVLM2-500M-Video-Instruct 以极小参数实现接近 2.2B 的视频理解能力
- **多图理解**：支持多图输入，适合图库分析和对比场景
- **内存极致优化**：专为低显存场景设计，可在 CPU + 少量内存下运行
- **HuggingFace 生态集成**：与 Transformers、Inference Endpoints 无缝集成
- **开源数据训练**：基于开放数据集训练，数据来源透明

## 性能亮点

| 基准 | SmolVLM2 表现 |
|------|-------------|
| 显存需求 | <1GB（256M 版） |
| 视频能力 | 500M 接近 2.2B |
| 多图理解 | 支持 |
| 推理速度 | 极快 |

## 适用场景

- 移动端/手机应用
- 浏览器端 WebAI
- IoT 边缘设备
- 快速原型开发
- 教学与学术研究

## 备注

SmolVLM2 证明了"小模型+高质量训练"可以超越"大模型+普通数据"的范式。其 <1GB 显存的特性使得在浏览器（WebGPU）和移动端运行视觉 AI 成为现实，是真正民主化的视觉 AI 工具。适合作为嵌入式视觉组件集成到各类产品中。
