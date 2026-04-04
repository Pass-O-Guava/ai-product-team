# Llama 3.2 Vision

> **数据可靠度：A**（Meta 官方博客 & HuggingFace）

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型名称** | Llama 3.2（Vision 多模态版本） |
| **发布方** | Meta AI（Facebook） |
| **参数量级** | 11B / 90B（Vision 版本）；1B / 3B（纯文本轻量版） |
| **支持的模态** | 文本 + 图像（Vision 版本） |
| **许可协议** | Llama 3.2 Community License（商业使用需申请，非完全自由） |
| **HuggingFace** | https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct <br> https://huggingface.co/meta-llama/Llama-3.2-90B-Vision-Instruct |
| **魔搭 ModelScope** | https://modelscope.cn/models/meta-llama/Llama-3.2-11B-Vision |
| **发布年份/版本** | 2024年9月（Llama 3.2 发布） |

## 核心能力描述

Llama 3.2 Vision 是 Meta Llama 3.2 系列中的视觉版本，标志着 Llama 系列正式拥抱多模态：

- **Llama 生态最强多模态**：依托 Llama 3.2 强大的语言基座，Vision 版本具备出色的通用理解能力
- **双规格覆盖**：11B（适合消费者 GPU） 和 90B（适合服务器级部署）
- **指令微调**：基于 RLHF 和 DPO 深度对齐，对话体验流畅自然
- **多语言**：继承 Llama 3 的多语言能力，支持英文及部分其他语言
- **Llama Stack**：支持 Llama Stack 标准化部署，生态完善
- **边缘优化**：1B/3B 纯文本版针对移动端优化，适合手机部署

## 性能亮点

| 基准 | Llama 3.2-90B-Vision |
|------|---------------------|
| MMMU | ~64 分 |
| VQA-v2 | ~85 分 |
| DocVQA | ~91 分 |
| 文本能力 | Llama 3.2 同等水平 |

## 适用场景

- 企业级视觉 AI 应用
- 基于 Llama 生态的定制开发
- 多语言全球化产品
- Llama Stack 标准化部署
- 学术研究基准对比

## 备注

Llama 3.2 Vision 是 Meta Llama 家族首款支持视觉的模型，意义重大。90B 版本提供了与 GPT-4V 正面对抗的能力，而 11B 版本则适合开发者快速实验。虽然许可协议不是完全自由的 Apache 2.0，但对于非商业和多数商业场景免费，是目前最被广泛采用的开源 VLM 基础之一。
