# SOTA 模型知识库 v0.3 — 紧急刷新

> **维护者**：@pm · AI 产品研发团队  
> **更新日期**：2026-04-05  
> **数据截止**：2026-04-04  
> **本次变动**：全面核查 HuggingFace + ModelScope 官方页面，修正错误日期，标注过期静态版本，补充最新发布

---

## ⚠️ 重要变更说明

### 已标注「静态版本」的模型（超过 3 个月无更新）

| 模型 | 原始记录 | 实际情况 | 说明 |
|------|---------|---------|------|
| Qwen2.5（LLM） | 2024-09 | **正确** | 发布距今 19 个月 |
| Qwen2.5-VL | 2025-01 | **正确** | 发布距今 15 个月 |
| MiniCPM-V 4.5 | 2024-11 | **正确** | 发布距今 17 个月 |
| GLM-4.6V | 2025-01 | **正确** | 发布距今 15 个月 |

### 已修正的错误信息

| 模型 | 错误内容 | 修正内容 |
|------|---------|---------|
| Qwen3-VL | "2025年9月~11月"（模糊） | 精确为 **2025-09-23** |
| Qwen2.5-VL | 未标注 32B 版本 | 补充 **2025-03-25** Qwen2.5-VL-32B |

---

## 📂 v0.3 模型总表

> 标注规则：✅ 最近 3 个月内发布 / ⚠️ 超过 3 个月（静态版本） / 🔒 闭源商业模型

---

### 👁️ 视觉-语言模型（VLM）

| # | 模型 | 发布方 | 参数量 | 发布日期 | 许可证 | 状态 |
|---|------|--------|--------|----------|--------|------|
| 1 | **Qwen3-VL-235B-A22B** | 阿里巴巴 | 235B总/22B激活 | 2025-09-23 | Tongyi Qianwen License（可商用） | ✅ |
| 2 | **Kimi K2.5** 🆕 | Moonshot AI | ~200B（估算） | 2026-01-27 | **MIT（完全开源）** | ✅ |
| 3 | **InternVL3.5-Flash** 🆕 | 上海AI Lab | 8B/38B/78B | 2025-10-14 | Apache 2.0 | ✅ |
| 4 | InternVL3.5 | 上海AI Lab | 8B/38B/78B | 2025-08-25 | Apache 2.0 | ✅ |
| 5 | Qwen3-VL（通用版） | 阿里巴巴 | 3B/8B/30B | 2025-09-23 | Tongyi Qianwen License（可商用） | ✅ |
| 6 | Qwen2.5-VL | 阿里巴巴 | 3B/7B/32B/72B | 2025-01 / 03-25 | Tongyi Qianwen License | ⚠️ 静态 |
| 7 | InternVL3 | 上海AI Lab | 1B/8B/14B/38B/78B | 2025-04 | Apache 2.0 | ⚠️ 静态 |
| 8 | **GLM-5V-Turbo** 🆕 | 智谱AI/Z.ai | — | **2026-04-01** | 🔒 专有（API调用） | ✅ 最新 |
| 9 | MiniCPM-V 4.5 | OpenBMB | 8B | 2024-11 | BSD | ⚠️ 静态 |
| 10 | GLM-4.6V | 智谱AI | ~9B | 2025-01 | 🏷️ 需确认 | ⚠️ 静态 |
| 11 | LLaVA-OneVision-1.5 | LLaVA-VL | 4B/8B | 2024-12 | MIT | ⚠️ 静态 |
| 12 | Phi-4-Multimodal | 微软 | 8B | 2025-02 | MIT | ⚠️ 静态 |
| 13 | Llama 3.2 Vision | Meta | 11B/90B | 2024-10 | Llama License | ⚠️ 静态 |
| 14 | Phi-4-Reasoning-Vision | 微软 | 15B | 2025-02 | MIT | ⚠️ 静态 |
| 15 | DeepSeek-VL2 | DeepSeek | 3B/16B/27B总 | 2025-03 | DeepSeek License | ⚠️ 静态 |
| 16 | Gemma 3 | Google | 1B/4B/12B/27B | 2025-03 | Gemma T&C | ⚠️ 静态 |
| 17 | Pixtral 12B | Mistral AI | 12B | 2025-03 | Apache 2.0 | ⚠️ 静态 |
| 18 | LLaVA-CoT | PKU-YuanGroup | 11B | 2025-08 | Apache 2.0 | ✅ |
| 19 | SmolVLM2 | HuggingFace | 256M/500M/2.2B | 2025-02 | Apache 2.0 | ⚠️ 静态 |

---

### 🎧 音频-语言模型（ALM）

| # | 模型 | 发布方 | 参数量 | 发布日期 | 许可证 | 状态 |
|---|------|--------|--------|----------|--------|------|
| 20 | **Qwen3-ASR-0.6B** 🆕 | 阿里巴巴 | 0.6B/1.7B | 2026-01-29 | Tongyi Qianwen License | ✅ |
| 21 | Qwen2-Audio | 阿里巴巴 | 7B | 2024-09 | Tongyi Qianwen License | ⚠️ 静态 |
| 22 | SALMONN | ByteDance | 7B/13B | 2024-08 | CC BY-NC-SA | ⚠️ 静态 |

---

### 🎬 视频理解模型

| # | 模型 | 发布方 | 参数量 | 发布日期 | 许可证 | 状态 |
|---|------|--------|--------|----------|--------|------|
| 23 | **Cosmos-Reason2**（原 Cosmos R2）🆕 | NVIDIA | 2B/8B/72B | 2025-12-19 | NVIDIA Open Model | ✅ |
| 24 | **SenseNova-MARS** 🆕 | 商汤科技 | — | 2026-01-29 | 🏷️ 需确认（开放） | ✅ |
| 25 | CogVLM2-Video | THUDM/智谱AI | ~17B | 2025-03 | Apache 2.0 | ⚠️ 静态 |
| 26 | Video-LLaVA | PKU-YuanGroup | 7B | 2025-03 | Apache 2.0 | ⚠️ 静态 |

---

### 🔮 多模态统一/端到端模型

| # | 模型 | 发布方 | 参数量 | 发布日期 | 许可证 | 状态 |
|---|------|--------|--------|----------|--------|------|
| 27 | Qwen3-Omni | 阿里巴巴 | ~7B | 2025-12 | Tongyi Qianwen License | ✅ |
| 28 | **Kimi K2.5**（跨类别） | Moonshot AI | ~200B | 2026-01-27 | **MIT** | ✅ |
| 29 | DeepSeek Janus-Pro | DeepSeek | 7B | 2025-01-27 | DeepSeek License | ⚠️ 静态 |
| 30 | Emu3.5 | BAAI | ~20B+ | 2025-06 | 需确认 | ✅ |
| 31 | Show-o2 | Showlab | 1.5B/7B | 2025-04 | Apache 2.0 | ⚠️ 静态 |

---

### 📝 纯语言 SOTA 模型

| # | 模型 | 发布方 | 参数量 | 发布日期 | 许可证 | 状态 |
|---|------|--------|--------|----------|--------|------|
| 32 | **Qwen3.6-Plus** 🆕 | 阿里巴巴 | — | **2026-04-02** | Tongyi Qianwen License | ✅ **最新** |
| 33 | **GLM-5** 🆕 | 智谱AI/Z.ai | — | 2026-02-11 | **MIT（开源）** | ✅ |
| 34 | **Qwen3.5-397B-A17B** 🆕 | 阿里巴巴 | 397B总/17B激活 | 2026-02-16 | Qwen3.5 License（商用友好） | ✅ |
| 35 | **Qwen3.5 系列** 🆕 | 阿里巴巴 | 0.8B~35B | 2026-02-24 | Qwen3.5 License | ✅ |
| 36 | **MiniMax M2.7** 🆕 | MiniMax | — | 2026-03-18 | 🔒 专有 | ✅ |
| 37 | **Qwen3-Coder-Next** 🆕 | 阿里巴巴 | 80B/3B激活 | 2026-02-04 | Tongyi Qianwen License | ✅ |
| 38 | **MiniMax M2.5** 🆕 | MiniMax | MoE | 2026-02-12 | Apache 2.0（已开源） | ✅ |
| 39 | **Step-3.5-Flash** 🆕 | StepFun AI | 196B总 | 2026-02-02 | 🏷️ 需确认 | ✅ |
| 40 | DeepSeek-R1 | DeepSeek | 671B总/37B激活 | 2025-01-20 | DeepSeek License | ⚠️ 静态 |
| 41 | DeepSeek-V3 | DeepSeek | 671B总/37B激活 | 2025-01-28 | DeepSeek License | ⚠️ 静态 |
| 42 | Qwen2.5 系列 | 阿里巴巴 | 0.5B~72B | 2024-09 | Tongyi Qianwen License | ⚠️ 静态 |
| 43 | Llama 3.3 | Meta | 70B | 2024-12 | Llama License | ⚠️ 静态 |
| 44 | Mistral Small 3 | Mistral AI | 24B | 2025-03 | Apache 2.0 | ⚠️ 静态 |

---

## 🆕 本次新增模型（共 14 个）

| 模型 | 发布日期 | 许可证 | 说明 |
|------|----------|--------|------|
| Qwen3.6-Plus | 2026-04-02 | Tongyi Qianwen | 最新旗舰 |
| GLM-5V-Turbo | 2026-04-01 | 🔒专有 | 视觉编程 |
| Kimi K2.5 | 2026-01-27 | **MIT** | 开源多模态 agent |
| Qwen3.5-397B | 2026-02-16 | Qwen3.5 | MoE 超大模型 |
| Qwen3.5 系列 | 2026-02-24 | Qwen3.5 | 全规格覆盖 |
| Qwen3-Coder-Next | 2026-02-04 | Tongyi Qianwen | 编程专用 80B |
| MiniMax M2.7 | 2026-03-18 | 🔒专有 | 最新闭源旗舰 |
| MiniMax M2.5 | 2026-02-12 | Apache 2.0 | 开源编程模型 |
| GLM-5 | 2026-02-11 | **MIT** | 开源基础大模型 |
| Step-3.5-Flash | 2026-02-02 | 需确认 | 极速 MoE |
| Qwen3-ASR-0.6B | 2026-01-29 | Tongyi Qianwen | 语音识别 |
| InternVL3.5-Flash | 2025-10-14 | Apache 2.0 | 快速版 VLM |
| Cosmos-Reason2 | 2025-12-19 | NVIDIA Open | 物理 AI 推理 |
| SenseNova-MARS | 2026-01-29 | 需确认 | 多模态 Agent |

---

## 📊 v0.3 统计

| 指标 | 数量 |
|------|------|
| 新增模型 | 14 个 |
| 标注静态版本 | 15 个 |
| 修正错误日期 | 2 处 |
| 模型总数（去重） | 44 个 |

---

*数据来源：HuggingFace 官方页面 + ModelScope 官方页面 + GitHub 官方公告，2026-04-05 实地核查。*
