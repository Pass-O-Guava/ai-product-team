# Model Card: MiniMax M2.7

> **记录版本：** v1.0  
> **调研日期：** 2026-04-04  
> **调研员：** @text-researcher  
> **可靠度评级：** B（官方博客存在，Benchmark 数据多源，但**权重开放状态存疑**，需核实）

---

## 基本信息

| 字段 | 内容 |
|------|------|
| 模型全名 | MiniMax M2.7 |
| 开发方 | MiniMax（稀宇科技）|
| 发布时间 | 2026-03-18 |
| 发布时间窗口 | 最近 1 个月（✅ 收录）|
| 模型类型 | 自进化前沿语言模型（文本 + Agent）|
| 许可证 | **待确认**（Reddit 讨论质疑是否真正开源权重）|

---

## ⚠️ 重要说明：开源状态存疑

Reddit r/LocalLLaMA（2026-03-20）有讨论标题"Welp, looks like minimax m2.7 may not be open sourced"，提示 M2.7 可能仅通过 API 提供，未开放权重。建议核实后再正式收录。

---

## 链接

| 类型 | 链接 |
|------|------|
| 官方博客（MiniMax.io）| https://www.minimax.io/news/minimax-m27-en |
| 官方模型页 | https://www.minimax.io/models/text/m27 |
| OpenRouter | https://openrouter.ai/minimax/minimax-m2.7/benchmarks |
| Wavespeed AI 报道 | https://wavespeed.ai/blog/posts/minimax-m2-7-self-evolving-agent-model-features-benchmarks-2026 |
| Towards AI 报道 | https://pub.towardsai.net/minimax-m2-7-built-itself-heres-how-to-use-it-like-a-pro-27529761d9a7 |

---

## Benchmark 成绩

> 数据来源：MiniMax 官方博客 2026-03-18 + OpenRouter + Wavespeed AI

| Benchmark | 分数 | 备注 |
|-----------|------|------|
| **SWE-Pro** | **56.2%** | 软件工程（进阶版），开源顶级 |
| **Terminal Bench 2.0** | **57.0%** | 终端 Agent 任务，开源最高 |
| **GDPval-AA ELO** | **1495** | 开源模型最高 ELO |
| Toolathon Benchmark | 46.3% | 多工具推理任务 |
| PinchBench | 领先 | 开放测试集 |

---

## SOTA 声明（有据可查）

| 声明 | 来源 | 可靠度 |
|------|------|--------|
| GDPval-AA ELO 1495，开源最高 | MiniMax 官方博客 2026-03-18 | ★★★ 高 |
| Terminal Bench 2.0 开源第一（57.0%）| OpenRouter 2026-03-18 | ★★★ 高 |
| SWE-Pro 56.2% | OpenRouter 官方数据 | ★★★ 高 |
| 自进化能力（首个自进化训练）| MiniMax 官方博客 | ★★☆ 中（概念性声明，需技术细节）|

---

## 技术亮点

1. **首个自进化模型**：模型能分析自身失败、修改测试框架、自我迭代（概念性突破）
2. **GDPval-AA ELO 1495**：开源最高 ELO 评分
3. **Terminal Bench 2.0 57.0%**：开源最高，终端 Agent 能力最强
4. **SWE-Pro 56.2%**：软件工程进阶任务表现突出
5. **100 TPS 推理速度**：极高吞吐量
6. **$0.30/M 输入价格**：低成本 API

---

## 入选理由

1. GDPval-AA 开源最高 ELO（1495），综合智能领先
2. Terminal Bench 2.0 开源第一，Agent 能力突破
3. 自进化训练范式，AI 训练方法论创新
4. 最新发布（2026-03-18），时间窗口内最高版本 MiniMax 模型
5. ⚠️ **前提：需确认权重是否真正开源**（待核实）

---

## 信息源列表

### T1：官方 GitHub / 官方博客
- ✅ MiniMax 官方博客（2026-03-18）：https://www.minimax.io/news/minimax-m27-en
- ✅ 官方模型页：https://www.minimax.io/models/text/m27

### T2
- ✅ OpenRouter（2026-03-18）：https://openrouter.ai/minimax/minimax-m2.7/benchmarks

### T3
- Wavespeed AI（2026-03-21）：https://wavespeed.ai/blog/posts/minimax-m2-7-self-evolving-agent-model-features-benchmarks-2026
- ⚠️ Reddit 质疑帖（2026-03-20）："minimax m2.7 may not be open sourced"

---

## 待补充

- [ ] **【关键】确认 M2.7 权重是否已开源（当前状态：存疑）**
- [ ] 确认官方许可证
- [ ] 完整参数规模信息
- [ ] 上下文窗口长度
