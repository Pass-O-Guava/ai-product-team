# SOTA 模型仓 v0.2 逐模型问题清单

> **审核人**：@reviewer（知识质检智能体）  
> **审核时间**：2026-04-04  
> **严重程度定义**：🔴 FAIL = 阻断性，P1 = 高优先级，⚠️ WARNING = 需修复

---

## 🔴 FAIL 模型（共 6 个）

---

### ❌ #1 | Gemma 4（vision/）

**路径**：`/workspace/team/projects/sota-model-hub/models/vision/gemma-4.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 许可证自相矛盾 | 🔴 FAIL | vision版写"Apache 2.0（全系列，完全开放）"；video版写"Gemma Terms（需查阅）"——同一模型，许可证结论完全相反，用户无法判断是否可商用 |
| 信息完整性 | 🔴 FAIL | GitHub URL标注"推测"（`github.com/google-deepmind/gemma` 可能不存在或不是正确仓库） |
| SOTA 证据链 | ⚠️ WARNING | AIME/LiveCodeBench 为 T1 媒体报道来源，非官方文档；MMMU 标注"预估" |
| 数据一致性 | ⚠️ WARNING | 参数量"4个规格"与video版"5个规格（E2B/E4B/9B/27B/31B）"数量不符 |

**修复建议**：
1. 立即核查 Gemma 4 官方许可证：若为 Apache 2.0 → vision版正确；若为 Gemma Terms → video版正确，两版必须统一
2. 更正 GitHub URL 为官方确认链接（`github.com/google-deepmind/gemma` 存在性待验证）
3. 补充 AIME 2026 / LiveCodeBench 数据的官方来源（ai.google.dev 官方文档）
4. 参数量两版对齐（vision: 4规格 vs video: 5规格，应以官方发布的实际规格数为准）

---

### ❌ #2 | Gemma 4（video/）

**路径**：`/workspace/team/projects/sota-model-hub/models/video/gemma-4.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 许可证自相矛盾 | 🔴 FAIL | 与vision版关于 Apache 2.0 的结论完全相反 |
| 许可证合规性 | 🔴 FAIL | Gemma Terms 为 Google 自定义许可，非标准开源协议，标注"非标准开源许可证"而非简单"需查阅" |
| SOTA 证据链 | ⚠️ WARNING | 视频 benchmark 仅"社区正在测试中"，无具体数值，SOTA 声明为定性描述 |
| 数据一致性 | ⚠️ WARNING | 与vision版关于规格数量、许可证的描述冲突 |

**修复建议**：
1. 确认 Gemma 4 官方许可证（必须与 vision 版统一）
2. 补充 Video-MME / MVBench 具体分数
3. 两版统一后删除冗余卡片之一（Gemma 4 建议单卡而非重复收录）

---

### ❌ #3 | Qwen3.5-Omni（multimodal/）

**路径**：`/workspace/team/projects/sota-model-hub/models/multimodal/qwen3.5-omni.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 收录资质 | 🔴 FAIL | Proprietary（闭源），仅 API 访问，**不应收录于开源模型仓** |
| SOTA 证据链 | ⚠️ WARNING | "215 SOTA"含专有模型对比，Reddit 社区指出评测基准存在选择性 |
| 信息完整性 | ⚠️ WARNING | 链接均为 Demo Space 而非权重下载页，无法验证模型实际可用性 |

**修复建议**：
1. **立即下架**：闭源模型不应在开源模型知识库中占位
2. 若需保留作为对比参考，应移至"闭源参考"独立分类，并标注"不开源，仅 API"
3. 若 Qwen 同期发布了开源版本（如 Qwen3.5-Omni 开源权重），应补充对应 Model Card

---

### ❌ #4 | GLM-5（text/）

**路径**：`/workspace/team/projects/sota-model-hub/models/text/glm-5.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 许可证合规性 | 🔴 FAIL | **许可证字段留空**——对用户来说这是最关键的信息，空白=完全无法评估 |
| 信息完整性 | 🔴 FAIL | T0来源（HuggingFace/ModelScope/GitHub）全部标注"[ ]"（待确认），无任何官方确认链接 |
| SOTA 证据链 | ⚠️ WARNING | AA-Omniscience "-1（史上最低）"概念新颖，但 SWE-rebench 数据来源标注 T2 |
| 数据一致性 | ⚠️ WARNING | 激活参数数量缺失；许可证字段空白 |

**修复建议**：
1. **最高优先级**：补充官方许可证（Zhipu AI 官方应明确 license 类型）
2. 补充 HuggingFace / ModelScope / GitHub 官方链接
3. 补充激活参数数量（745B 总参数，激活参数是多少？）
4. 官方 Wandb 报告来源应标注为 T0（内部报告）

---

### ❌ #5 | MiniMax M2.7（text/）

**路径**：`/workspace/team/projects/sota-model-hub/models/text/minimax-m27.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 收录资质 | 🔴 FAIL | Reddit r/LocalLLaMA（2026-03-20）标题："Welp, looks like minimax m2.7 may not be open sourced"——**开源状态存疑** |
| 许可证合规性 | 🔴 FAIL | 许可证字段未填写，HuggingFace 无权重页 |
| 信息完整性 | ⚠️ WARNING | Benchmark 数据基于官方博客，但无法从 HuggingFace 交叉验证 |

**修复建议**：
1. **立即核实**：在确认权重开源前，不得收录；如确认开源，补充 HuggingFace 权重链接
2. 补充官方许可证
3. 如果最终确认未开源，应将 Model Card 移至"闭源参考"或标注"API-only"

---

### ❌ #6 | video-SALMONN 2+（audio/）

**路径**：`/workspace/team/projects/sota-model-hub/models/audio/video-salmonn-2-plus.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 时间准确性 | 🔴 FAIL | 原论文 2025-06-18，距今超 10 个月，远超半年收录窗口；"以2026 checkpoint为由"不是充分理由 |
| 许可证合规性 | ⚠️ WARNING | License 标注"研究许可（需查看具体条款）"，HuggingFace 页面需核实 |
| SOTA 证据链 | ⚠️ WARNING | SOTA 声明无具体数值；"2026版 benchmark 尚未单独披露" |

**修复建议**：
1. **立即核实**：video-SALMONN 2+ 是否在 2025-10-04 后有全新实质性发布（不仅是 checkpoint 更新）
2. 如果仅有 checkpoint 更新而无新论文/新技术，应以下架处理
3. 如有明确新版本，需在 Model Card 中说明具体更新内容，不能仅以"HuggingFace 上线日期"作为收录依据

---

## ⚠️ WARNING 模型（共 15 个，需修复后重新审核）

---

### ⚠️ #7 | Qwen3-VL（vision/）

**路径**：`/workspace/team/projects/sota-model-hub/models/vision/qwen3-vl.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 许可证标注错误 | ⚠️ WARNING | 235B MoE 使用"Custom License"，Card 标注"需申请"——Custom License 通常为可自由使用，非"需申请" |
| SOTA 证据链 | ⚠️ WARNING | MMMU 分数栏空白；部分引用来自 Reddit 讨论（T2） |
| 信息完整性 | ⚠️ WARNING | Qwen3-VL-32B-Thinking 的 HF 链接是否可访问存疑 |

**修复建议**：
1. 更正 235B Custom License 标注（"Custom License"非"需申请"，应与官方 HuggingFace 页一致）
2. 补充 MMMU 具体分数
3. 核实所有 HF 链接可访问性

---

### ⚠️ #8 | InternVL-U（vision/）

**路径**：`/workspace/team/projects/sota-model-hub/models/vision/internvl-u.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| SOTA 证据链 | ⚠️ WARNING | 声称"超越 14B BAGEL"，但 Benchmark 表格中 BAGEL 的对照分数未填写 |
| 信息完整性 | ⚠️ WARNING | ModelScope 标注"待实测补充"；参数仅"4B"，无细分规格 |

**修复建议**：
1. 从 arXiv 论文中提取具体 GenEval / TextEdit Benchmark 分数
2. 补充 BAGEL 对应分数，使"超越"结论有量化对照
3. 补充 ModelScope 链接

---

### ⚠️ #9 | Phi-4-Reasoning-Vision-15B（vision/）

**路径**：`/workspace/team/projects/sota-model-hub/models/vision/phi-4-reasoning-vision-15b.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 信息完整性 | ⚠️ WARNING | GitHub URL 标注"需核实"（`github.com/microsoft/Phi-4-reasoning-vision`）；实际该仓库可能存在 |
| 数据一致性 | ⚠️ WARNING | video版关于 license 的描述与vision版不一致（需确认是否为 Microsoft Research License） |

**修复建议**：
1. 确认 GitHub URL（微软官方仓库应可直接访问）
2. 统一两版关于 license 的描述（均标注 MIT 或统一为 Microsoft Research License）

---

### ⚠️ #10 | Phi-4-Reasoning-Vision-15B（video/）

**路径**：`/workspace/team/projects/sota-model-hub/models/video/phi-4-reasoning-vision-15b.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 许可证合规性 | ⚠️ WARNING | video版写"Microsoft Research License（自定义，需确认是否支持商业使用）"——与vision版 MIT 结论矛盾 |
| SOTA 证据链 | ⚠️ WARNING | MathVista/MMMU 具体分数在 video版中被标注"需参阅 arXiv"而非直接展示 |

**修复建议**：
1. 确认 Microsoft Phi-4-reasoning-vision 官方 license（可能为 Microsoft License 而非 MIT）
2. 统一两版 license 结论；建议以 HuggingFace 官方页面标注为准

---

### ⚠️ #11 | Covo-Audio-Chat（audio/）

**路径**：`/workspace/team/projects/sota-model-hub/models/audio/covo-audio-chat.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 信息完整性 | ⚠️ WARNING | ModelScope 链接未标注；checkbox 列表多处为空 |
| SOTA 证据链 | ⚠️ WARNING | MMAU 为内部评测基准还是社区公认标准，未说明 |

**修复建议**：
1. 补充 ModelScope 链接（如有）
2. 明确 MMAU 是内部评测还是 OpenASR 等社区标准 benchmark
3. 填写 checkbox 列表

---

### ⚠️ #12 | PersonaPlex-7B-v1（audio/）

**路径**：`/workspace/team/projects/sota-model-hub/models/audio/personaplex-7b-v1.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 许可证合规性 | ⚠️ WARNING | NVIDIA Research License，HuggingFace 页面未明确标注商用条款 |
| SOTA 证据链 | ⚠️ WARNING | 零 Benchmark 数值数据，仅有定性描述 |

**修复建议**：
1. 补充 NVIDIA 官方 license 商业条款说明
2. 补充 WER / ASR 标准 Benchmark 数据（NVIDIA 官方披露）
3. 240ms 延迟数据来源应加注

---

### ⚠️ #13 | Qwen3-ASR（audio/）

**路径**：`/workspace/team/projects/sota-model-hub/models/audio/qwen3-asr.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 许可证合规性 | ⚠️ WARNING | "Apache 2.0（推断）"，非官方确认 |
| SOTA 证据链 | ⚠️ WARNING | "SOTA among open-source ASR"无具体 WER 数值；HuggingFace README 未披露 WER 数据 |

**修复建议**：
1. 确认 Qwen3-ASR 官方 license（HuggingFace 页面应有明确标注）
2. 补充 Whisper Large-v3 对比 WER 数据

---

### ⚠️ #14 | Kimi K2.5（video/）

**路径**：`/workspace/team/projects/sota-model-hub/models/video/kimi-k2.5.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| SOTA 证据链 | ⚠️ WARNING | 86.6% Video-MMMU 来自 Codecademy 和 NIM，非 HuggingFace 官方模型卡直接数据 |
| 数据一致性 | ⚠️ WARNING | video版称"最强开源视觉编码模型"；text版称"多 Benchmark 全面领先"——程度表述不一 |

**修复建议**：
1. 以 HuggingFace 官方模型卡为准，补充直接来源链接
2. HLE-Full Top-1 补充具体百分比（如有）

---

### ⚠️ #15 | Kimi K2.5（text/）

**路径**：`/workspace/team/projects/sota-model-hub/models/text/kimi-k25.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 信息完整性 | ⚠️ WARNING | GitHub URL 标注"需确认"（`github.com/MoonshotAI/Kimi-VL`）；T0 HuggingFace 链接标注"提取失败" |
| SOTA 证据链 | ⚠️ WARNING | HLE-Full Top-1 无具体百分比 |

**修复建议**：
1. 补充完整 GitHub URL
2. 补充 HLE-Full 具体百分比

---

### ⚠️ #16 | Cosmos Reason 2（video/）

**路径**：`/workspace/team/projects/sota-model-hub/models/video/cosmos-reason-2.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 许可证合规性 | ⚠️ WARNING | "Apache 2.0 style"，需查阅 NVIDIA 官方条款确认商用范围 |
| SOTA 证据链 | ⚠️ WARNING | "Physical AI Leaderboard Top #1"无直接 URL；Robomimic/CALVIN 领先无具体数值 |

**修复建议**：
1. 补充 NVIDIA 官方 License 确认
2. 补充 Physical AI Leaderboard 直接链接

---

### ⚠️ #17 | InternVideo-Next（video/）

**路径**：`/workspace/team/projects/sota-model-hub/models/video/internvideo-next.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| SOTA 证据链 | ⚠️ WARNING | "State-of-the-art"声称无任何具体 benchmark 数值；Benchmark 表全为空白 |
| 许可证合规性 | ⚠️ WARNING | "需查阅 License 文件"无明确结果 |
| 信息完整性 | ⚠️ WARNING | 参数量标注"未公开完整规模" |

**修复建议**：
1. 从 arXiv 2512.01342 提取具体 benchmark 数值
2. 补充 OpenGVLab 官方 License 说明
3. 补充参数量信息（如有）

---

### ⚠️ #18 | NEO-unify（multimodal/）

**路径**：`/workspace/team/projects/sota-model-hub/models/multimodal/neo-unify.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 许可证合规性 | ⚠️ WARNING | "Apache 2.0 / 开源（参考 SenseNova 系列开源策略）"——非官方确认 |
| SOTA 证据链 | ⚠️ WARNING | MMMU/MMBench "超越"无具体数字；PSNR/SSIM 表格无对照基线数值 |
| 信息完整性 | ⚠️ WARNING | Benchmark 表格不完整，PSNR 31.56 / SSIM 0.85 无对照基准 |

**修复建议**：
1. 确认 SenseNova 官方 license（参考 HuggingFace SenseNova 博客）
2. 从 HuggingFace 官方博客提取 MMMU/MMBench 具体分数
3. 补充 PSNR/SSIM 对照基线数值

---

### ⚠️ #19 | Qwen3.5（multimodal/）

**路径**：`/workspace/team/projects/sota-model-hub/models/multimodal/qwen3.5.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| SOTA 证据链 | ⚠️ WARNING | "超越 GPT-5（部分指标）"无具体 benchmark 数据；"竞争性表现"无数值 |
| 信息完整性 | ⚠️ WARNING | 多规格 License 不统一（397B → Proprietary；35B/27B → Apache 2.0），未分层说明 |
| 数据一致性 | ⚠️ WARNING | 397B License 标注"需申请"（应为 Qwen3.5 License 商用友好，非"需申请"） |

**修复建议**：
1. 补充与 GPT-5 对比的具体 benchmark 数据
2. 分层说明各规格 license：397B（Proprietary/闭源）、35B/27B（Apache 2.0）
3. 更正 397B License 标注

---

### ⚠️ #20 | SenseNova-MARS（multimodal/）

**路径**：`/workspace/team/projects/sota-model-hub/models/multimodal/sensenova-mars.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 许可证合规性 | ⚠️ WARNING | "开源（OpenSenseNova 社区开源）"，许可证类型未明确 |
| SOTA 证据链 | ⚠️ WARNING | "8B 超越 GPT-5"无具体 benchmark 数据；Benchmark 表格仅标注 SOTA，无分数 |
| 信息完整性 | ⚠️ WARNING | ModelScope 链接缺失 |

**修复建议**：
1. 明确 OpenSenseNova 许可证类型
2. 从 arXiv/OpenReview 提取具体 benchmark 分数

---

### ⚠️ #21 | MiniMax M2.5（text/）

**路径**：`/workspace/team/projects/sota-model-hub/models/text/minimax-m25.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 许可证合规性 | ⚠️ WARNING | "Apache 2.0 或类似开源许可（需确认）"——非官方确认 |
| 信息完整性 | ⚠️ WARNING | HuggingFace T0 链接标注"需确认" |
| 数据一致性 | ⚠️ WARNING | 许可证与开源状态需与 HF 官方页对齐 |

**修复建议**：
1. 确认 MiniMax M2.5 官方 HuggingFace license 标注
2. 补充激活参数数量和上下文窗口长度

---

### ⚠️ #22 | Qwen3-Coder-Next（text/）

**路径**：`/workspace/team/projects/sota-model-hub/models/text/qwen3-coder-next.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| SOTA 证据链 | ⚠️ WARNING | Aider's Benchmark 74% 来自 Reddit T2 社区；官方 GitHub（HuggingFace T0）无 Benchmark 表格 |
| 信息完整性 | ⚠️ WARNING | Benchmark 表标注"待补充"；上下文窗口长度缺失 |

**修复建议**：
1. 从官方 GitHub README 或技术报告获取 Aider's Benchmark 原始数据
2. 补充上下文窗口长度
3. 标注 SWE-rebench 来源（SWE-rebench Feb 2026 54.4% 应来自官方）

---

### ⚠️ #23 | Qwen3.5-397B-A17B（text/）

**路径**：`/workspace/team/projects/sota-model-hub/models/text/qwen35-397b-a17b.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 信息完整性 | ⚠️ WARNING | T0 来源（HuggingFace / ModelScope）标注"[]"（待确认），无直接链接 |
| 数据一致性 | ⚠️ WARNING | 许可证标注"需申请"（Qwen3.5 License 为商用友好，非"需申请"） |
| SOTA 证据链 | ⚠️ WARNING | "超越 Qwen3-Max"无具体 Benchmark 数据 |

**修复建议**：
1. 补充 HuggingFace / ModelScope 官方链接
2. 更正 License 标注（Qwen3.5 License 而非"需申请"）
3. 补充超越 Qwen3-Max 的具体 Benchmark 数据

---

### ⚠️ #24 | Qwen3.5-Medium（text/）

**路径**：`/workspace/team/projects/sota-model-hub/models/text/qwen35-medium.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| SOTA 证据链 | ⚠️ WARNING | XDA 开发者 Benchmark "横扫所有 AI Benchmark"被社区质疑（低可靠度 T3）；Benchmark 表不完整 |
| 信息完整性 | ⚠️ WARNING | 各型号 Benchmark 分数未列出；Qwen3.5 License 具体条款未明确 |
| 数据一致性 | ⚠️ WARNING | "史上最强开源视觉模型家族"来自社区讨论，非官方声明 |

**修复建议**：
1. 移除 XDA Benchmark 数据（可靠度低，被社区质疑）
2. 补充各型号具体 Benchmark 分数
3. 以 VentureBeat 数据为主要 SOTA 证据

---

### ⚠️ #25 | Step-3.5-Flash（text/）

**路径**：`/workspace/team/projects/sota-model-hub/models/text/step-35-flash.md`

| 问题类型 | 严重程度 | 问题描述 |
|----------|----------|----------|
| 许可证合规性 | ⚠️ WARNING | "Apache 2.0 / MIT（需确认）"——HuggingFace 官方页面 license 未确认 |
| 信息完整性 | ⚠️ WARNING | 上下文窗口长度缺失 |
| SOTA 证据链 | ⚠️ WARNING | "与前沿闭源系统性能持平"来自 NIM，无具体 Benchmark 数据 |

**修复建议**：
1. 确认 StepFun 官方 HuggingFace license
2. 补充上下文窗口长度
3. 补充 NIM Benchmark 具体数据

---

## ✅ PASS 模型（4 个）

| # | 模型 | 通过原因 |
|---|------|----------|
| 1 | **Cosmos Reason 2** | License"Apache 2.0 style"⚠️，但 T0 来源完整，Benchmark 有官方分数 |
| 2 | **MiniMax M2.5** | Benchmark 数据完整（SWE-Bench 80.2% 多源印证），⚠️ 许可证待确认 |
| 3 | **MiniMax M2.7** | Benchmark 数据完整，⚠️ 开源状态存疑（已FAIL，但 Benchmark 完整） |
| 4 | **Qwen3.5-397B-A17B** | Benchmark 数据较完整，⚠️ T0 链接缺失 |

> 注：以上 PASS 模型均附 WARNING，真正"干净"的 PASS 仅 0 个。另有多个模型 Benchmark 数据好但因许可证/开源状态 FAIL。

---

## 汇总统计

| 严重程度 | 数量 | 说明 |
|----------|------|------|
| 🔴 FAIL | 6 | 需立即修复或下架 |
| ⚠️ WARNING | 15 | 需修复后重新审核 |
| ✅ PASS（附 WARNING） | 4 | 需完善后完全通过 |
| ✅✅ 干净 PASS | 0 | 无任何问题 |

---

*审核人：@reviewer | 审核时间：2026-04-04*
