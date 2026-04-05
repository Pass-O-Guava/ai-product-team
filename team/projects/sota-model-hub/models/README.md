# 🤖 SOTA 模型知识库 v0.3（2026-04-05 紧急更新）

> **维护者**：@pm · AI 产品研发团队  
> **数据截止**：2026-04-04（HuggingFace + ModelScope 实地核查）  
> **收录原则**：以最近 3 个月内模型为主；超过 3 个月的标注「静态版本」

---

## 📊 总览

| 模态类别 | 收录数量 | 本次新增 |
|---------|---------|---------|
| 视觉-语言模型（VLM） | 19 个 | +4 |
| 音频-语言模型（ALM） | 3 个 | +1 |
| 视频理解模型 | 4 个 | +1 |
| 多模态统一/端到端模型 | 5 个 | — |
| 纯语言 SOTA 模型 | 13 个 | +8 |
| **合计** | **44 个模型** | **+14** |

> ⚠️ 标注「静态」的模型：超过 3 个月无更新，供历史参考，不建议作为选型首选

---

## 📂 模型索引

### 👁️ 视觉-语言模型（VLM）— 19 个

| # | 模型 | 发布方 | 参数量 | 发布日期 | 许可证 | 状态 |
|---|------|--------|--------|----------|--------|------|
| 1 | **Qwen3-VL-235B-A22B** | 阿里巴巴 | 235B总/22B激活 | 2025-09-23 | Tongyi Qianwen（可商用） | ✅ 最新 |
| 2 | **Kimi K2.5** 🆕 | Moonshot AI | ~200B | 2026-01-27 | **MIT（完全开源）** | ✅ |
| 3 | **InternVL3.5-Flash** 🆕 | 上海AI Lab | 8B/38B/78B | 2025-10-14 | Apache 2.0 | ✅ |
| 4 | InternVL3.5 | 上海AI Lab | 8B/38B/78B | 2025-08-25 | Apache 2.0 | ✅ |
| 5 | Qwen3-VL（通用版） | 阿里巴巴 | 3B/8B/30B | 2025-09-23 | Tongyi Qianwen | ✅ |
| 6 | Qwen2.5-VL | 阿里巴巴 | 3B/7B/32B/72B | 2025-01/03-25 | Tongyi Qianwen | ⚠️ 静态 |
| 7 | InternVL3 | 上海AI Lab | 1B~78B 多规格 | 2025-04 | Apache 2.0 | ⚠️ 静态 |
| 8 | **GLM-5V-Turbo** 🆕 | 智谱AI/Z.ai | — | 2026-04-01 | 🔒 专有（API） | ✅ 最新 |
| 9 | MiniCPM-V 4.5 | OpenBMB | 8B | 2024-11 | BSD | ⚠️ 静态 |
| 10 | GLM-4.6V | 智谱AI | ~9B | 2025-01 | 需确认 | ⚠️ 静态 |
| 11 | LLaVA-OneVision-1.5 | LLaVA-VL | 4B/8B | 2024-12 | MIT | ⚠️ 静态 |
| 12 | Phi-4-Multimodal | 微软 | 8B | 2025-02 | MIT | ⚠️ 静态 |
| 13 | Llama 3.2 Vision | Meta | 11B/90B | 2024-10 | Llama License | ⚠️ 静态 |
| 14 | Phi-4-Reasoning-Vision | 微软 | 15B | 2025-02 | MIT | ⚠️ 静态 |
| 15 | DeepSeek-VL2 | DeepSeek | 3B/16B/27B总 | 2025-03 | DeepSeek License | ⚠️ 静态 |
| 16 | Gemma 3 | Google | 1B~27B | 2025-03 | Gemma T&C | ⚠️ 静态 |
| 17 | Pixtral 12B | Mistral AI | 12B | 2025-03 | Apache 2.0 | ⚠️ 静态 |
| 18 | LLaVA-CoT | PKU-YuanGroup | 11B | 2025-08 | Apache 2.0 | ✅ |
| 19 | SmolVLM2 | HuggingFace | 256M~2.2B | 2025-02 | Apache 2.0 | ⚠️ 静态 |

### 🎧 音频-语言模型（ALM）— 3 个

| # | 模型 | 发布方 | 参数量 | 发布日期 | 许可证 | 状态 |
|---|------|--------|--------|----------|--------|------|
| 20 | **Qwen3-ASR-0.6B** 🆕 | 阿里巴巴 | 0.6B/1.7B | 2026-01-29 | Tongyi Qianwen | ✅ |
| 21 | Qwen2-Audio | 阿里巴巴 | 7B | 2024-09 | Tongyi Qianwen | ⚠️ 静态 |
| 22 | SALMONN | ByteDance | 7B/13B | 2024-08 | CC BY-NC-SA | ⚠️ 静态 |

### 🎬 视频理解模型 — 4 个

| # | 模型 | 发布方 | 参数量 | 发布日期 | 许可证 | 状态 |
|---|------|--------|--------|----------|--------|------|
| 23 | **Cosmos-Reason2**（原R2）🆕 | NVIDIA | 2B/8B/72B | 2025-12-19 | NVIDIA Open | ✅ |
| 24 | **SenseNova-MARS** 🆕 | 商汤科技 | — | 2026-01-29 | 需确认 | ✅ |
| 25 | CogVLM2-Video | THUDM/智谱AI | ~17B | 2025-03 | Apache 2.0 | ⚠️ 静态 |
| 26 | Video-LLaVA | PKU-YuanGroup | 7B | 2025-03 | Apache 2.0 | ⚠️ 静态 |

### 🔮 多模态统一/端到端模型 — 5 个

| # | 模型 | 发布方 | 参数量 | 发布日期 | 许可证 | 状态 |
|---|------|--------|--------|----------|--------|------|
| 27 | Qwen3-Omni | 阿里巴巴 | ~7B | 2025-12 | Tongyi Qianwen | ✅ |
| 28 | Kimi K2.5 | Moonshot AI | ~200B | 2026-01-27 | **MIT** | ✅ |
| 29 | DeepSeek Janus-Pro | DeepSeek | 7B | 2025-01-27 | DeepSeek License | ⚠️ 静态 |
| 30 | Emu3.5 | BAAI | ~20B+ | 2025-06 | 需确认 | ✅ |
| 31 | Show-o2 | Showlab | 1.5B/7B | 2025-04 | Apache 2.0 | ⚠️ 静态 |

### 📝 纯语言 SOTA 模型 — 13 个

| # | 模型 | 发布方 | 参数量 | 发布日期 | 许可证 | 状态 |
|---|------|--------|--------|----------|--------|------|
| 32 | **Qwen3.6-Plus** 🆕 | 阿里巴巴 | — | **2026-04-02** | Tongyi Qianwen | ✅ **最新** |
| 33 | **GLM-5** 🆕 | 智谱AI/Z.ai | — | 2026-02-11 | **MIT（开源）** | ✅ |
| 34 | **Qwen3.5-397B-A17B** 🆕 | 阿里巴巴 | 397B总/17B激活 | 2026-02-16 | Qwen3.5 License | ✅ |
| 35 | **Qwen3.5 系列** 🆕 | 阿里巴巴 | 0.8B~35B | 2026-02-24 | Qwen3.5 License | ✅ |
| 36 | **MiniMax M2.7** 🆕 | MiniMax | — | 2026-03-18 | 🔒 专有 | ✅ |
| 37 | **Qwen3-Coder-Next** 🆕 | 阿里巴巴 | 80B/3B激活 | 2026-02-04 | Tongyi Qianwen | ✅ |
| 38 | **MiniMax M2.5** 🆕 | MiniMax | MoE | 2026-02-12 | Apache 2.0（已开源） | ✅ |
| 39 | **Step-3.5-Flash** 🆕 | StepFun AI | 196B总 | 2026-02-02 | 需确认 | ✅ |
| 40 | DeepSeek-R1 | DeepSeek | 671B总/37B激活 | 2025-01-20 | DeepSeek License | ⚠️ 静态 |
| 41 | DeepSeek-V3 | DeepSeek | 671B总/37B激活 | 2025-01-28 | DeepSeek License | ⚠️ 静态 |
| 42 | Qwen2.5 系列 | 阿里巴巴 | 0.5B~72B | 2024-09 | Tongyi Qianwen | ⚠️ 静态 |
| 43 | Llama 3.3 | Meta | 70B | 2024-12 | Llama License | ⚠️ 静态 |
| 44 | Mistral Small 3 | Mistral AI | 24B | 2025-03 | Apache 2.0 | ⚠️ 静态 |

---

## 🆕 本次新增（14 个）

| 模型 | 日期 | 许可证 | 亮点 |
|------|------|--------|------|
| Qwen3.6-Plus | 2026-04-02 | Tongyi Qianwen | 最新旗舰，刚发布 |
| GLM-5V-Turbo | 2026-04-01 | 🔒专有 | 视觉编程，Agent |
| Kimi K2.5 | 2026-01-27 | **MIT** | 开源多模态 Agent，MIT 许可 |
| Qwen3.5-397B | 2026-02-16 | Qwen3.5 | MoE 超大模型，商用友好 |
| Qwen3.5 系列 | 2026-02-24 | Qwen3.5 | 全规格覆盖，0.8B~35B |
| Qwen3-Coder-Next | 2026-02-04 | Tongyi Qianwen | 编程专用，80B/3B激活 |
| MiniMax M2.7 | 2026-03-18 | 🔒专有 | 闭源旗舰 |
| MiniMax M2.5 | 2026-02-12 | Apache 2.0 | 开源编程，$1/h |
| GLM-5 | 2026-02-11 | **MIT** | 开源基础大模型 |
| Step-3.5-Flash | 2026-02-02 | 需确认 | 极速 MoE |
| Qwen3-ASR-0.6B | 2026-01-29 | Tongyi Qianwen | 语音识别 |
| InternVL3.5-Flash | 2025-10-14 | Apache 2.0 | 快速版 VLM |
| Cosmos-Reason2 | 2025-12-19 | NVIDIA Open | 物理 AI 推理 |
| SenseNova-MARS | 2026-01-29 | 需确认 | 多模态 Agent |

---

## 🏆 v0.3 Top 3 SOTA 推荐

### 1. Qwen3.6-Plus — 最新旗舰（2026-04-02）
> 阿里巴巴 2026 年 4 月 2 日发布，Qwen 系列最新作，具体规格待 HuggingFace 页面确认。代表当前中文开源 LLM 最前沿。

### 2. Kimi K2.5 — 开源多模态 Agent（2026-01-27）
> Moonshot AI 发布，MIT 许可证完全开源，支持视觉+Agent swarm，在 HuggingFace 可直接下载，编程和 Agent 场景接近闭源旗舰水平。

### 3. GLM-5 — 开源新基准（2026-02-11）
> 智谱 AI / Z.ai 发布，**MIT 许可证开源**，200K 上下文，对标 Claude Opus 4.6 水平，同时发布 GLM-5V-Turbo 视觉编程版本。

---

## 📋 许可证速查

| 许可证 | 可商用 | 代表模型 |
|-------|--------|---------|
| MIT | ✅ | Kimi K2.5, GLM-5, Phi-4-Multimodal, InternVL3.5, Step-3.5-Flash |
| Apache 2.0 | ✅ | InternVL3.5, Mistral Small 3, Show-o2, CogVLM2-Video, LLaVA-CoT, MiniMax M2.5 |
| Tongyi Qianwen | ✅ | Qwen3-VL, Qwen3-Omni, Qwen3-Coder-Next, Qwen3.5 系列, Qwen3.6-Plus |
| DeepSeek License | ✅ | DeepSeek-R1, DeepSeek-V3, Janus-Pro |
| Llama License | ⚠️ 需申请 | Llama 3.x |
| CC BY-NC-SA | ❌ | SALMONN, video-SALMONN |
| 🔒 专有 | ❌ | GLM-5V-Turbo, MiniMax M2.7, Gemini 3.1 Pro |

---

*本知识库 v0.3 · 2026-04-05 · 数据来源：HuggingFace + ModelScope 官方页面实地核查*
