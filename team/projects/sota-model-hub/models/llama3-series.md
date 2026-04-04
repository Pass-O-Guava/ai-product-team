# Llama 3.1 / 3.2 / 3.3

> **数据可靠度：A**（Meta AI 官方博客 & HuggingFace）

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型名称** | Llama 3.1 / Llama 3.2 / Llama 3.3 |
| **发布方** | Meta AI（Facebook） |
| **参数量级** | Llama 3.1: 8B / 70B / 405B；Llama 3.2: 1B / 3B / 11B(V) / 90B(V)；Llama 3.3: 70B |
| **支持的模态** | 文本（Llama 3.2 含 Vision 版本） |
| **许可协议** | Llama 3.1/3.2/3.3 Community License（商业使用需申请） |
| **HuggingFace** | https://huggingface.co/meta-llama <br> https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct |
| **魔搭 ModelScope** | https://modelscope.cn/models/meta-llama |
| **发布年份/版本** | Llama 3.1: 2024年7月；Llama 3.2: 2024年9月；Llama 3.3: 2025年5月 |

## 核心能力

- **Llama 3.1（2024年7月）**：405B 参数旗舰，128K 上下文，8语言支持，开源 LLM 里程碑
- **Llama 3.2（2024年9月）**：轻量 1B/3B（边缘移动端优化）+ Vision 版本 11B/90B
- **Llama 3.3（2025年5月）**：70B 多语言优化版，性能接近 Llama 3.1 405B，成本更低
- **Llama Stack**：标准化部署框架，支持 Ollama、vLLM 等主流推理后端
- **Llama Guard**：内置安全过滤，支持内容安全检测

## 性能亮点

| 基准 | Llama 3.1-405B | Llama 3.3-70B |
|------|---------------|---------------|
| MMLU | ~87 | ~86 |
| HumanEval | ~89 | ~88 |
| 上下文 | 128K | 128K |

## 适用场景

通用对话、企业 AI 应用、研究基准、模型蒸馏、Llama 生态定制

## 备注

Llama 系列是开源 AI 最重要的品牌，Meta 持续推动 Llama 3.x 的迭代更新。Llama 3.3 以 70B 参数接近 405B 的能力，是当前最具性价比的开源选择之一。Llama 3.2 Vision 版本（11B/90B）使 Llama 正式进入多模态领域。
