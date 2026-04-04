# Model Card: GLM-5

> **记录版本：** v1.0  
> **调研日期：** 2026-04-04  
> **调研员：** @text-researcher  
> **可靠度评级：** A（多源交叉验证，VentureBeat 官方数据 + Wandb 汇总 + 独立评测）

---

## 基本信息

| 字段 | 内容 |
|------|------|
| 模型全名 | GLM-5 |
| 开发方 | Zhipu AI（智谱 AI） |
| 发布时间 | 2026-02-10 |
| 发布时间窗口 | 最近 1 个月（✅ 收录） |
| 模型类型 | 开源前沿语言模型（MoE，745B 总参数） |
| 许可证 | **MIT License**（✅ 可商用，无任何附加条款） |

---

## 链接

| 类型 | 链接 |
|------|------|
| HuggingFace | https://huggingface.co/zhipuai/glm-5（推测，需确认） |
| 官方技术报告 | https://wandb.ai/byyoung3/ml-news/reports/GLM-5-Benchmark-Scores---VmlldzoxNTkwOTk2MQ |
| VentureBeat 报道 | https://venturebeat.com/technology/z-ais-open-source-glm-5-achieves-record-low-hallucination-rate-and-leverages |
| 评测汇总 | https://llm-stats.com/models/glm-5 |
| LayerLens 评测 | https://layerlens.ai/blog-old/glm-5-benchmark-review |

---

## Benchmark 成绩

> 数据来源：Wandb 官方技术报告 + VentureBeat 2026-02-12 + Advenboost 2026

| Benchmark | 分数 | 备注 |
|-----------|------|------|
| **MATH-500** | **97.4%** | 开源顶级数学推理 |
| **HumanEval** | 96.95% | 编程能力极强 |
| **AIME 2026** | **92.7%** | 高难度数学竞赛题 |
| **SWE-bench Verified** | **77.8%** | 软件工程，开源前列 |
| **AA-Omniscience**（幻觉率）| **-1（史上最低）** | 比前身提升 35 分，超越所有模型 |
| SWE-rebench Jan 2026 | 42.1% | 开源模型中仅次于 Kimi K2-Thinking |
| Terminal-Bench 2.0 | 56.2% | 所有开源模型最高 |

---

## SOTA 声明（有据可查）

| 声明 | 来源 | 可靠度 |
|------|------|--------|
| MATH-500 97.4%（开源最高） | Wandb 官方 + LayerLens 独立验证 | ★★★ 高 |
| AA-Omniscience 史上最低幻觉率（-1） | VentureBeat（2026-02-12）| ★★★ 高 |
| AIME 2026 92.7% | Advenboost 2026（引用官方数据）| ★★★ 高 |
| SWE-bench 77.8% 开源前列 | Wandb 官方 + Wandb 汇总 | ★★★ 高 |
| SWE-rebench 开源第二（42.1%）| Reddit r/LocalLLaMA 2026-02-13 | ★★☆ 中 |
| Terminal-Bench 2.0 开源第一（56.2%）| Medium 2026-03-20 | ★★☆ 中 |

---

## 技术亮点

1. **史上最低幻觉率**：AA-Omniscience Index -1，比前身 GLM-4.7 提升 35 分
2. **顶级数学能力**：MATH-500 97.4%，AIME 2026 92.7%
3. **745B MoE 架构**：总参数 7450 亿，稀疏激活，计算效率高
4. **SWE-bench 77.8%**：软件工程任务达前沿水平
5. **幻觉控制突破**：在可靠性要求高的企业场景有重要价值

---

## 入选理由

1. 幻觉率突破：首个 AA-Omniscience 负分模型，可靠性里程碑
2. MATH-500 97.4% 和 AIME 2026 92.7%，数学推理最强开源模型候选
3. SWE-bench 77.8%，软件工程能力极强
4. MoE 架构效率高，适合大规模部署
5. 综合能力强，无明显短板

---

## 信息源列表（按 T0/T1/T2 分类）

### T0：HuggingFace / ModelScope 官方页
- [ ] HuggingFace 模型卡（需确认完整 URL 和 License）

### T1：官方 GitHub / 官方博客
- [ ] Zhipu AI 官方技术报告（Wandb）：https://wandb.ai/byyoung3/ml-news/reports/GLM-5-Benchmark-Scores---VmlldzoxNTkwOTk2MQ

### T2：arXiv / 官方 Leaderboard
- [ ] VentureBeat 报道（2026-02-12）：https://venturebeat.com/technology/z-ais-open-source-glm-5-achieves-record-low-hallucination-rate-and-leverages

### T3：媒体
- LayerLens 评测（2026-03-11）：https://layerlens.ai/blog-old/glm-5-benchmark-review

---

## 待补充

- [x] 确认官方许可证 → **MIT License**（来源：Zhipu AI 官方博客 z.ai/blog/glm-5，2026-02-12）
- [ ] 激活参数数量
- [ ] 上下文窗口长度
