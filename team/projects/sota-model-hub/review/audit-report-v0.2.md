# SOTA 模型仓 v0.2 知识质检审核报告

> **审核人**：@reviewer（知识质检智能体）  
> **审核时间**：2026-04-04  
> **数据截止**：2026年4月  
> **审核标准**：与 v0.1 同等标准，宁缺毋滥

---

## 一、审核范围

### 1.1 模型清单（共 25 个 Model Card，21 个独立模型）

| 序号 | 模型名称 | 类别 | 来源卡片 |
|------|----------|------|----------|
| 1 | Gemma 4 | vision / video | 2 张卡片（跨类别） |
| 2 | InternVL-U | vision | 1 张卡片 |
| 3 | Qwen3-VL | vision | 1 张卡片 |
| 4 | Phi-4-Reasoning-Vision-15B | vision / video | 2 张卡片（跨类别） |
| 5 | Covo-Audio-Chat | audio | 1 张卡片 |
| 6 | PersonaPlex-7B-v1 | audio | 1 张卡片 |
| 7 | Qwen3-ASR | audio | 1 张卡片 |
| 8 | video-SALMONN 2+ | audio | 1 张卡片 |
| 9 | Kimi K2.5 | video / text | 2 张卡片（跨类别） |
| 10 | Cosmos Reason 2 | video | 1 张卡片 |
| 11 | InternVideo-Next | video | 1 张卡片 |
| 12 | NEO-unify | multimodal | 1 张卡片 |
| 13 | Qwen3.5-Omni | multimodal | 1 张卡片 |
| 14 | Qwen3.5 | multimodal | 1 张卡片 |
| 15 | SenseNova-MARS | multimodal | 1 张卡片 |
| 16 | GLM-5 | text | 1 张卡片 |
| 17 | MiniMax M2.5 | text | 1 张卡片 |
| 18 | MiniMax M2.7 | text | 1 张卡片 |
| 19 | Qwen3-Coder-Next | text | 1 张卡片 |
| 20 | Qwen3.5-397B-A17B | text | 1 张卡片 |
| 21 | Qwen3.5-Medium | text | 1 张卡片 |
| 22 | Step-3.5-Flash | text | 1 张卡片 |

> **注**：Gemma 4、Phi-4-Reasoning-Vision-15B、Kimi K2.5 各出现 2 次（分属不同类别），Qwen3.5 出现 2 次（multimodal 和 text 均收录）。实际独立模型 21 个，Model Card 共 25 张。

---

## 二、审核维度通过率

### 2.1 维度1：时间准确性

| 评级 | 数量 | 占比 |
|------|------|------|
| ✅ PASS | 20 | 80% |
| ⚠️ WARNING | 4 | 16% |
| 🔴 FAIL | 1 | 4% |

**通过率：80%**

**WARNING 列表**：
- `video-SALMONN 2+`：原论文 2025-06-18，超出半年窗口，仅以"2026年checkpoint"为由收录，理由不充分
- `video/Gemma 4`：发布/开源时间与 `vision/Gemma 4` 不一致（vision: 4月2日 vs video: 4月2日博客/4月3日新闻稿）
- `video/InternVideo-Next`：发布时间仅标注"2025-12"，精确日期未填
- `GLM-5`：发布时间仅填"2026-02-10"，未区分首发公告日期与技术报告日期

---

### 2.2 维度2：许可证合规性

| 评级 | 数量 | 占比 |
|------|------|------|
| ✅ PASS | 8 | 32% |
| ⚠️ WARNING | 13 | 52% |
| 🔴 FAIL | 4 | 16% |

**通过率：32%**

**WARNING 列表**（13个，许可证信息未经官方确认）：
- `InternVL-U`：MIT ✅，但 ModelScope 链接标注"待实测补充"
- `Qwen3-VL`：2B/4B/8B/32B → Apache 2.0 ✅；235B MoE → "Custom License"被错误标注为"需申请"（Custom License 通常可自由使用）⚠️
- `Covo-Audio-Chat`：CC BY 4.0 ✅，但 ModelScope 未标注
- `PersonaPlex-7B-v1`：NVIDIA Research License，HuggingFace 页面需核实 ⚠️
- `Qwen3-ASR`：Apache 2.0 **（推断）**，非官方确认 ⚠️
- `Kimi K2.5 (video)`：MIT ✅，video版同vision
- `Cosmos Reason 2`："Apache 2.0 style"，需查阅 NVIDIA 官方条款 ⚠️
- `InternVideo-Next`：需查阅 License 文件 ⚠️
- `NEO-unify`："参考 SenseNova 系列开源策略"，非官方确认 ⚠️
- `Qwen3.5-Omni`：Proprietary ⚠️（不应收录入开源模型仓）
- `Qwen3.5`：35B/27B → Apache 2.0 ✅；397B → "需申请"（实为 Qwen3.5 License，商用友好，非"需申请"）⚠️
- `SenseNova-MARS`："开源（OpenSenseNova 社区开源）"，许可证类型未明确 ⚠️
- `MiniMax M2.5`："Apache 2.0 或类似开源许可（需确认）" ⚠️
- `MiniMax M2.7`：待确认 ⚠️
- `Qwen3.5-397B-A17B`：Qwen3.5 License（商用友好）⚠️
- `Qwen3.5-Medium`：Qwen3.5 License ⚠️
- `Step-3.5-Flash`："Apache 2.0 / MIT（需确认）" ⚠️

**FAIL 列表**（4个）：
- `GLM-5`：许可证字段**留空**，无任何标注（空白=无法评估）
- `video/Gemma 4`：License 标注为"Gemma Terms"，需查阅官方条款
- `Qwen3.5-Omni`：Proprietary，闭源模型不应收录
- `MiniMax M2.7`：Reddit（2026-03-20）质疑权重开源状态，**开源状态存疑**

---

### 2.3 维度3：SOTA 声明证据链

| 评级 | 数量 | 占比 |
|------|------|------|
| ✅ PASS | 7 | 28% |
| ⚠️ WARNING | 13 | 52% |
| 🔴 FAIL | 5 | 20% |

**通过率：28%**

**PASS 列表**（有量化分数+来源）：
- `vision/Gemma 4`：AIME 2026 89.2%，LiveCodeBench v6 80.0%（T1来源）
- `Phi-4-Reasoning-Vision-15B`：8项具体 benchmark 分数（AI2D 84.8、ChartQA 83.3等），来源完整
- `video/Kimi K2.5`：Video-MMMU 86.6%，来源 NIM/Codecademy（T1）
- `Cosmos Reason 2`：Physical AI Leaderboard #1，NVIDIA CES 2026 官方声明
- `MiniMax M2.5`：SWE-Bench 80.2%，Multi-SWE-Bench 51.3%，多源印证
- `MiniMax M2.7`：Terminal Bench 2.0 57.0%，GDPval-AA ELO 1495（官方）
- `Qwen3.5-397B-A17B`：AIME 2026 91.3%，HMMT 94.8%（T1来源）

**WARNING 列表**（13个，证据不完整）：
- `InternVL-U`：声称超越 14B BAGEL，但表格中无 BAGEL 对应分数对照；GenEval/TextEdit 分数未填
- `Qwen3-VL`：声称 MathVista 85.5%，但 MMMU 分数栏空白；部分数据引用 Reddit 来源（T2）
- `Covo-Audio-Chat`：MMAU 75.30%，但 MMAU 是否为社区公认 benchmark 存疑
- `video-SALMONN 2+`：声称"总错误率 22.9%，优于 GPT-4o/Gemini-1.5-Pro"，但无原始对比数据
- `video/Gemma 4`：视频 benchmark 无具体分数，"LMArena 领先"无数据支撑
- `InternVideo-Next`：声称"SOTA"，但无任何 benchmark 数值
- `NEO-unify`：声称"超越原生 VLM"，但 MMMU/MMBench 均为"超越"无具体数字
- `Qwen3.5-Omni`："215 SOTA"声称含专有模型对比；Reddit 用户指出评测基准有选择性
- `Qwen3.5`：声称"超越 GPT-5 部分指标"，无具体 benchmark 数据
- `SenseNova-MARS`：声称"8B 超越 GPT-5"，无具体分数
- `GLM-5`：AA-Omniscience "-1（史上最低）"概念独特但来源（SWE-rebench）标注为 T2
- `Kimi K2.5 (text)`：HLE-Full "Top-1"无具体百分比
- `Qwen3.5-Medium`：XDA Benchmark 数据被社区质疑为低可靠度（T3）

**FAIL 列表**（5个，零证据 SOTA 声明）：
- `Qwen3-VL`：235B MoE "Custom License"标注错误，且多项关键 benchmark 空白
- `Qwen3.5-Omni`：Proprietary 模型，SOTA 声明中含专有模型对比，不可比
- `video/Gemma 4`：license 与 vision 版冲突，benchmark 无数值，"SOTA"定性描述无支撑
- `video-SALMONN 2+`：超出时间窗口，收录依据不充分
- `Qwen3-Coder-Next`：Aider's 74% 来自 T2 社区，官方 GitHub/HF（T0/T1）无 benchmark 表格

---

### 2.4 维度4：信息完整性

| 评级 | 数量 | 占比 |
|------|------|------|
| ✅ PASS | 10 | 40% |
| ⚠️ WARNING | 12 | 48% |
| 🔴 FAIL | 3 | 12% |

**通过率：40%**

**PASS 列表**（字段完整，T0/T1来源）：
- `Phi-4-Reasoning-Vision-15B`：完整 benchmark 表，8个数据集均有分数，来源完整
- `video/Kimi K2.5`：链接完整，MIT 标注清晰
- `Cosmos Reason 2`：GitHub/HF/NIM/博客均有
- `MiniMax M2.5`：Benchmark 完整，价格信息有
- `MiniMax M2.7`：Benchmark 完整，价格信息有
- `Qwen3.5-397B-A17B`：Benchmark 数据较完整
- `Qwen3.5-Medium`：链接列表完整
- `Step-3.5-Flash`：T0/T1 来源均有
- `NEO-unify`：链接列表较完整
- `SenseNova-MARS`：GitHub/arXiv/OpenReview 均完整

**WARNING 列表**（12个）：
- `vision/Gemma 4`：GitHub URL 标注"推测"（不准确），架构/训练数据缺失
- `InternVL-U`：ModelScope 未标注，参数仅"4B"，架构细节缺失
- `Qwen3-VL`：HF链接中 32B-Thinking 链接存疑，235B License 标注错误
- `Covo-Audio-Chat`：ModelScope 缺失，checkbox 待填
- `Qwen3-ASR`：License 仅"推断"，非确认
- `video-SALMONN 2+`：版本信息混乱
- `video/Gemma 4`：架构/训练数据缺失
- `InternVideo-Next`：参数量"未公开完整规模"
- `Qwen3.5`：Benchmark 数据仅"竞争性表现"，无具体数字
- `GLM-5`：T0来源链接全部缺失
- `Qwen3-Coder-Next`：Benchmark 表"待补充"
- `Qwen3.5-Omni`：Proprietary，链接为 Demo 而非权重

**FAIL 列表**（3个）：
- `GLM-5`：T0来源全部空白（HuggingFace/ModelScope/GitHub均未确认），许可证留空
- `MiniMax M2.7`：开源状态存疑（Reddit 质疑）
- `Qwen3.5-Omni`：Proprietary，模型权重不可用

---

### 2.5 维度5：数据一致性

| 评级 | 数量 | 占比 |
|------|------|------|
| ✅ PASS | 8 | 32% |
| ⚠️ WARNING | 13 | 52% |
| 🔴 FAIL | 4 | 16% |

**通过率：32%**

**WARNING/FAIL 问题列表**：
- **Gemma 4 许可证冲突**（严重）：vision版明确写"Apache 2.0（全系列）"；video版写"Gemma Terms（需查阅）"——同一模型，许可证结论完全相反
- **Phi-4-Reasoning-Vision 许可证差异**：vision版写"MIT License ✅"；video版写"Microsoft Research License，需确认是否支持商业使用"——存在矛盾
- **Kimi K2.5 SOTA 程度差异**：video版称"最强开源视觉编码模型"；text版仅说"多 Benchmark 全面领先"——程度描述不一致
- **InternVL-U 评分表缺失对照值**：Benchmark 表格有 PSNR 31.56/SSIM 0.85，但对照基线数值未填
- **Qwen3-VL License 标注错误**：235B Custom License ≠ "需申请"（Custom License 通常免费使用）
- **GLM-5 激活参数缺失**：745B 总参数，激活参数数量未填
- **MiniMax M2.5 许可证待确认**：Apache 2.0 仅"推测"
- **Qwen3-Coder-Next Benchmark 来源混乱**：Aider's 74% 来自 T2，官方 T0 链接中无此数据

---

## 三、典型问题汇总

### 3.1 最严重问题（Top 5）

| 排名 | 问题 | 影响模型数 | 严重程度 |
|------|------|-----------|----------|
| #1 | **许可证字段空白**（GLM-5 许可证留空） | 1 | 阻断性 |
| #2 | **许可证自相矛盾**（Gemma 4 vision版 vs video版） | 1 | 阻断性 |
| #3 | **Proprietary 模型收录于开源仓**（Qwen3.5-Omni） | 1 | 阻断性 |
| #4 | **开源状态存疑**（MiniMax M2.7 被质疑未开源） | 1 | 阻断性 |
| #5 | **超出时间窗口**（video-SALMONN 2+ 原论文 2025-06） | 1 | 高 |

### 3.2 高频问题模式

| 问题模式 | 出现次数 | 说明 |
|----------|----------|------|
| 许可证"需确认/需核实" | 13 | 超过半数模型许可证未经官方确认 |
| Benchmark 空白或无具体分数 | 9 | SOTA 声明缺乏量化支撑 |
| 可靠度评级虚高 | 4 | 标注 A/B 级但 T0 链接缺失 |
| 跨类别卡片不一致 | 3 | 同一模型在不同类别出现，信息矛盾 |

---

## 四、各维度通过率一览

| 维度 | PASS | WARNING | FAIL | 通过率 |
|------|------|---------|------|--------|
| 1. 时间准确性 | 20 | 4 | 1 | 80% |
| 2. 许可证合规性 | 8 | 13 | 4 | 32% |
| 3. SOTA 证据链 | 7 | 13 | 5 | 28% |
| 4. 信息完整性 | 10 | 12 | 3 | 40% |
| 5. 数据一致性 | 8 | 13 | 4 | 32% |

---

## 五、总体评分

**综合评分：4.8 / 10**

> 相比 v0.1（5.2/10）**下降 0.4 分**，主要原因是：
> 1. 新增模型中 Proprietary 模型混入（Gemma 4 license 严重冲突、Qwen3.5-Omni 闭源混入）
> 2. 许可证"需确认"现象严重（52% 模型未确认许可证）
> 3. SOTA 证据链通过率仅 28%，与 v0.1 同等水平
> 4. 部分模型开源状态存疑（MiniMax M2.7）

---

*审核人：@reviewer | 审核时间：2026-04-04*
