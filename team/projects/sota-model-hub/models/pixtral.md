# Pixtral

> **数据可靠度：A**（Mistral AI 官方博客 & HuggingFace）

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型名称** | Pixtral 12B（Mistral 视觉语言模型） |
| **发布方** | Mistral AI（法国） |
| **参数量级** | 12B（活跃参数，含专用视觉编码器） |
| **支持的模态** | 文本 + 图像 |
| **许可协议** | Apache 2.0（完全开源，可商用） |
| **HuggingFace** | https://huggingface.co/mistralai/pixtral-12b-2409 |
| **魔搭 ModelScope** | https://modelscope.cn/models/mistralai/pixtral-12b |
| **发布年份/版本** | 2024年9月（Pixtral 12B 首发），2024年11月（Pixtral Large） |

## 核心能力描述

Pixtral 是 Mistral AI 首款开源视觉语言模型：

- **独立视觉编码器**：Mistral 团队自研视觉编码器（非第三方），专为 Pixtral 训练
- **文本能力不妥协**：与纯文本版 Mistral 7B 性能相当，视觉增强不降低语言能力
- **12B 均衡规模**：性能与效率的最佳平衡点，部署成本适中
- **Pixtral Large**：2024年11月发布更大版本，性能进一步提升
- **Snowflake 集成**：2025年4月已集成至 Snowflake Cortex AI，企业级可用性高
- **原生支持多图**：支持多图输入和对比分析

## 性能亮点

| 基准 | Pixtral 12B 表现 |
|------|----------------|
| 视觉理解 | 与 GPT-4V 差距缩小 |
| 文本能力 | Mistral 7B 水平（无损） |
| 多图理解 | 支持 |
| 企业集成 | Snowflake 生产可用 |

## 适用场景

- 企业视觉 AI 应用
- 多语言欧洲市场（Mistral 欧洲背景）
- 与 Mistral 生态系统集成
- 中等规模视觉推理任务
- 数据隐私敏感行业（可私有部署）

## 备注

Pixtral 的最大特点是 Apache 2.0 许可证——这是目前最宽松的开源许可证之一，无使用限制。Mistral AI 作为欧洲最重要的开源 AI 公司，其模型的合规性受到欧洲企业青睐。Pixtral 在保持语言能力不下降的同时加入视觉能力，是务实设计的体现。
