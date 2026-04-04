# DeepSeek-R1

> **数据可靠度：A**（DeepSeek 官方博客 & 技术报告）

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型名称** | DeepSeek-R1 |
| **发布方** | 深度求索（DeepSeek AI） |
| **参数量级** | 671B 总（MoE，活跃 37B）；蒸馏版：7B/8B/14B/32B/70B |
| **支持的模态** | 文本（推理强化） |
| **许可协议** | DeepSeek License（允许商业使用） |
| **HuggingFace** | https://huggingface.co/deepseek-ai/DeepSeek-R1 <br> https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B |
| **魔搭 ModelScope** | https://modelscope.cn/models/deepseek-ai/DeepSeek-R1 |
| **发布年份/版本** | 2025年1月20日 |

## 核心能力描述

DeepSeek-R1 是深度求索推出的推理专用大模型，通过强化学习（RL）实现了突破性的推理能力：

- **强化学习推理**：不依赖 SFT 标注的推理链数据，通过 GRPO 强化学习自主涌现推理能力
- **蒸馏能力卓越**：将推理能力蒸馏到小模型，DeepSeek-R1-Distill-Q-32B 超越 GPT-4o 和 Claude-3.5-Sonnet
- **671B MoE 旗舰**：全尺寸版本活跃参数仅 37B，推理成本极低
- **多版本覆盖**：提供从 7B 到 671B 的全系列蒸馏版
- **Chain-of-Thought**：内置显式推理链，复杂问题分解能力极强
- **开源影响深远**：开源后引发全球 AI 社区强烈反响，被誉为"开源推理模型分水岭"

## 性能亮点

| 基准 | DeepSeek-R1-671B |
|------|-----------------|
| AIME 2024 | ~86% |
| MATH-500 | ~97% |
| MMLU | ~90% |

## 适用场景

复杂数学求解、代码生成、逻辑推理、科学研究辅助、CoT 对话应用

## 备注

DeepSeek-R1 是 2025 年最具影响力的开源 AI 模型之一，其 RL 驱动的推理能力提升方法论被业界广泛研究。开源行为对闭源厂商形成巨大竞争压力，是开源 AI 发展的重要里程碑。
