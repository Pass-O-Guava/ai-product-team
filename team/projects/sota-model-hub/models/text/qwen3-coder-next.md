# Model Card: Qwen3-Coder-Next

> **记录版本：** v1.0  
> **调研日期：** 2026-04-04  
> **调研员：** @text-researcher  
> **可靠度评级：** A（GitHub + HuggingFace 官方 + 第三方多源验证）

---

## 基本信息

| 字段 | 内容 |
|------|------|
| 模型全名 | Qwen3-Coder-Next |
| 开发方 | Alibaba DAMO Academy |
| 发布时间 | 2026-02-02 |
| 发布时间窗口 | 最近 1 个月（✅ 收录） |
| 模型类型 | 专用代码生成 / Agent 模型（MoE，80B 总 / 3B 激活）|
| 许可证 | Qwen3.5 License（商用友好）|

---

## 链接

| 类型 | 链接 |
|------|------|
| HuggingFace | https://huggingface.co/Qwen/Qwen3-Coder-Next |
| 官方博客 | https://qwen.ai/blog?id=qwen3-coder-next |
| arXiv 技术报告 | https://huggingface.co/papers/2603.00729 |

---

## Benchmark 成绩

> 数据来源：Qwen 官方博客 2026-02-02 + Reddit r/LocalLLaMA + SWE-rebench

| Benchmark | 分数 | 备注 |
|-----------|------|------|
| **Aider's Benchmark** | **74%** | 代码编辑能力极强 |
| **SWE-rebench Jan 2026** | **40.0%** | 开源模型中第三高 |
| **SWE-rebench Feb 2026** | **54.4%** | 随评测更新显著提升 |
| Terminal-Bench | 竞争性表现 | Agent 终端任务 |
| 推理速度 | 40-45 tok/s（单请求）| HuggingFace 讨论区实测 |

---

## SOTA 声明（有据可查）

| 声明 | 来源 | 可靠度 |
|------|------|--------|
| Aider's benchmark 74% | 技术报告（社群来源）| ★★☆ 中 |
| SWE-rebench 40.0% / 54.4% | Reddit r/LocalLLaMA 2026-02/03 | ★★☆ 中 |
| 达 Claude Sonnet 4.5 级别代码能力（3B 激活）| 第三方（Dev.to 2026-02-04）| ★★☆ 中 |

---

## 技术亮点

1. **极小激活参数**：3B 激活参数实现 Sonnet 4.5 级别代码能力
2. **专注代码 Agent**：Terminal-Bench、SWE-Bench 全面覆盖
3. **极速推理**：40-45 tok/s（单请求），70 tok/s 总吞吐
4. **Qwen3.5 架构**：共享 Qwen3.5 家族技术红利
5. **本地可运行**：消费级 GPU 可部署

---

## 入选理由

1. 3B 激活达 Sonnet 4.5 级代码能力，性价比极高
2. SWE-rebench 54.4%（Feb），软件工程能力开源顶级
3. Aider's 74%，代码编辑能力突出
4. Qwen 生态成熟，支持 vLLM/Ollama 部署
5. 专注代码 Agent，差异化定位清晰

---

## 信息源列表

### T0
- ✅ HuggingFace：https://huggingface.co/Qwen/Qwen3-Coder-Next

### T1
- ✅ 官方博客（2026-02-02）：https://qwen.ai/blog?id=qwen3-coder-next
- ✅ arXiv 技术报告：https://huggingface.co/papers/2603.00729

### T3
- Dev.to（2026-02-04）：https://dev.to/sienna/qwen3-coder-next-the-complete-2026-guide-to-running-powerful-ai-coding-agents-locally-1k95

---

## 待补充

- [ ] 完整 Benchmark 数值表
- [ ] 上下文窗口长度
