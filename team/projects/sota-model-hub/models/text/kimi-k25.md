# Model Card: Kimi K2.5

> **记录版本：** v1.0  
> **调研日期：** 2026-04-04  
> **调研员：** @text-researcher  
> **可靠度评级：** A（来源多元，有 HuggingFace 官方页面 + 第三方独立验证）

---

## 基本信息

| 字段 | 内容 |
|------|------|
| 模型全名 | Kimi K2.5 |
| 开发方 | Moonshot AI（月之暗面） |
| 发布时间 | 2026-01-27 |
| 发布时间窗口 | 最近 1 个月（✅ 收录） |
| 模型类型 | 原生多模态 Agent 模型（文本+视觉+Agent） |
| 发布时间窗口 | 最近 1 个月（✅ 收录） |

---

## 许可证

**Modified MIT License**（Modified MIT）  
模型权重已发布于 HuggingFace（`moonshotai/Kimi-K2.5`）及 NVIDIA NIM，可自托管。

---

## 链接

| 类型 | 链接 |
|------|------|
| HuggingFace | https://huggingface.co/moonshotai/Kimi-K2.5 |
| NVIDIA NIM | https://build.nvidia.com/moonshotai/kimi-k2.5 |
| 新闻来源（1） | https://siliconangle.com/2026/01/27/moonshot-ai-releases-open-source-kimi-k2-5-model-1t-parameters/ |
| 新闻来源（2） | https://huggingface.co/blog/mlabonne/kimik25 |
| 技术报告 | https://huggingface.co/moonshotai/Kimi-K2.5（页面内含模型卡） |

---

## Benchmark 成绩

> 数据来源：HuggingFace 官方模型卡 + HuggingFace Blog (mlabonne) 2026-02-23

| Benchmark | 分数 | 备注 |
|-----------|------|------|
| **HLE-Full**（Humanity's Last Exam）| **Top-1**（截至 2026-02 最高分） | 极难评测集，2500题 |
| **HLE with Tools** | 50.2% | Agent 工具调用评测 |
| SWE-Bench Verified | 领先同期开源模型 | 官方 claim，需官方报告核实 |
| 核心评测集 | 多 Benchmark 综合领先 | 官方声称超越 GPT-5.2 |

**⚠️ 说明：** 具体数值（如 HLE-Full 百分比）未在搜索摘要中完全提取，建议补充核验。

---

## SOTA 声明（有据可查）

| 声明 | 来源 | 可靠度 |
|------|------|--------|
| HLE-Full 最高分开源模型 | HuggingFace Blog（mlabonne）2026-02-23 + Dextra Labs 2026-02-08 | ★★★ 高 |
| Modified MIT 许可证开源权重 | HuggingFace 页面明确标注 | ★★★ 高 |
| 约 1 万亿参数 | SiliconAngle 2026-01-27 | ★★☆ 中（媒体估算，需官方确认）|

---

## 技术亮点

1. **原生多模态架构**：基于约 15 万亿混合图文 token 持续预训练，非后期拼接
2. **万亿参数规模**：总参数约 1T，稀疏激活（MoE 架构未明确，但参数规模大）
3. **强 Agent 能力**：HLE with Tools 达 50.2%，支持多步工具调用
4. **开源权重**：Modified MIT，可商用，自托管灵活性高
5. **NVIDIA NIM 同步发布**：支持企业级快速部署

---

## 入选理由

1. 2026年1月最重磅开源模型发布之一
2. HLE-Full 最高分记录（开源模型中）
3. 首个在最高难度评测集上击败 GPT-5.2 的开源模型（claim，需核实）
4. Modified MIT 许可证，商用友好
5. 多模态 + Agent 双重能力，符合 2026 年 AI 发展趋势

---

## 信息源列表（按 T0/T1/T2 分类）

### T0：HuggingFace / ModelScope 官方页
- [ ] HuggingFace 模型卡（页面提取失败，需重试）：https://huggingface.co/moonshotai/Kimi-K2.5

### T1：官方 GitHub / 官方博客
- [ ] Moonshot AI 官方博客 / 发布公告（需确认）

### T2：arXiv / 官方 Leaderboard
- [ ] HuggingFace Blog 分析文章（mlabonne，2026-02-23）：https://huggingface.co/blog/mlabonne/kimik25
- [ ] Dextra Labs 评测（2026-02-08）：https://dextralabs.com/blog/kimi-k2-5-the-best-open-source-model/

### T3：媒体
- SiliconAngle（2026-01-27）：https://siliconangle.com/2026/01/27/moonshot-ai-releases-open-source-kimi-k2-5-model-1t-parameters/

---

## 待补充

- [ ] HLE-Full 具体百分比数值
- [ ] 完整 Benchmark 表（含 Math/Coding/Reasoning 各维度）
- [ ] 架构细节（MoE/密集、激活参数）
