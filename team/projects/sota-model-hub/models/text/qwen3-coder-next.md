# Qwen3-Coder-Next

> **数据可靠度：A**（Qwen 官方 GitHub + HuggingFace 官方页面）
> **调研日期**：2026-04-05

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型名称** | Qwen3-Coder-Next |
| **发布方** | 阿里巴巴通义实验室（Qwen Team） |
| **参数量级** | 80B 总参数 / **3B 激活参数**（MoE） |
| **支持的模态** | 文本（编程专用） |
| **许可协议** | Tongyi Qianwen License（可商用） |
| **HuggingFace** | https://huggingface.co/Qwen/Qwen3-Coder-Next |
| **魔搭 ModelScope** | https://modelscope.cn/models/Qwen/Qwen3-Coder-Next |
| **发布日期** | **2026-02-04** |
| **官方博客** | https://qwen.ai/blog?id=qwen3-coder-next |

## 核心能力

- **80B MoE 架构**：总参数 80B，每次推理仅激活 3B，推理成本极低
- **编程专项优化**：基于 800K 可验证编程题训练，覆盖代码生成、补全、Debug、测试生成
- **Agent 友好**：支持 OpenClaw、Claude Code、Cline、Web 开发、浏览器自动化等场景
- **多语言**：支持 Python、JavaScript、TypeScript、Go、Rust 等主流语言
- **Benchmark 领先**：HumanEval、MBPP、LiveCodeBench 等编程基准达到开源 SOTA

## 许可证与商用合规

✅ **可商用**（Tongyi Qianwen License，阿里巴巴商业友好许可）

## Benchmark 参考

| Benchmark | 成绩 | 来源 |
|-----------|------|------|
| HumanEval | ~85%+ | 官方 GitHub |
| MBPP | ~80%+ | 官方 GitHub |

## 入选理由

2026 年 2 月发布的最新开源编程模型，80B MoE 架构以极低推理成本达到顶级编程能力，是当前开源编程模型综合实力最强之一，特别适合本地 AI 编程助手场景。

## 信息源

- Qwen 官方博客：https://qwen.ai/blog?id=qwen3-coder-next
- HuggingFace：https://huggingface.co/Qwen/Qwen3-Coder-Next
- GitHub：https://github.com/QwenLM/Qwen3.5
- The Decoder 报道：https://the-decoder.com/alibabas-qwen3-coder-next-delivers-solid-coding-performance-in-a-compact-package/
