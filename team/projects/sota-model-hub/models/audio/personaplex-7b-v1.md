# Model Card: PersonaPlex-7B-v1

> **模型全称**: NVIDIA PersonaPlex-7B-v1  
> **发布机构**: NVIDIA Research (ADLR Lab)  
> **发布时间**: 2026-01-15（HuggingFace 上线）/ 2026-01-20（公开公告）  
> **模型类型**: Full-Duplex Speech-to-Speech Conversational Model  
> **许可证**: NVIDIA Custom License（研究用，需查看具体条款）  
> **模型规格**: 7B 参数  
> **评测日期**: 2026-04-04  
> **可靠度评级**: T0 / 高 / 信息基本完整 ✅  

---

## 基本信息

| 字段 | 内容 |
|------|------|
| 模型名称 | nvidia/personaplex-7b-v1 |
| 参数量 | 7B |
| 发布时间 | 2026-01-15（HuggingFace）/ 2026-01-20（公开公告） |
| 发布机构 | NVIDIA Research, ADLR Lab |
| 模型类型 | 全双工语音对话模型（流式 ASR + 语音生成） |
| 许可证 | NVIDIA Research License（需查阅商业条款） |
| 代码链接 | https://github.com/NVIDIA/personaplex |
| 论文链接 | https://arxiv.org/abs/2602.06053 |
| HuggingFace | https://huggingface.co/nvidia/personaplex-7b-v1 |
| 项目主页 | https://research.nvidia.com/labs/adlr/personaplex/ |

---

## 核心能力

- **原生全双工（Full Duplex）**：真正实现边听边说，而非等待对方说完再回复
- **流式语音理解 + 语音生成联合建模**：单模型同时完成 ASR 和语音合成
- **240ms 端到端响应延迟**：每帧 12×/秒更新，实现亚秒级交互
- **混合系统提示（Hybrid System Prompts）**：结合文本角色描述 + 语音 persona 控制
- **Lo-Fi 24kHz 音频输出**：为低延迟牺牲一定音质（权衡策略）
- **角色扮演（Role Playing）**：可在对话中扮演任意角色

---

## Benchmark 表现

> ⚠️ 当前公开评测数据较少，NVIDIA 官方页面及 HuggingFace README 均未披露具体数值型 Benchmark。SOTA 声明基于技术定位（非实测数据）。

| 数据集/指标 | 结果 | 备注 |
|-------------|------|------|
| 端到端响应延迟 | **240ms** | 实测数据，有据可查 |
| 帧率 | 12×/秒 | 每秒 12 次更新 |
| 音频采样率 | 24kHz | Lo-Fi 权衡延迟 |
| 全双工对话质量 | 定性评估 | 需实测对比 |

> ⚠️ 尚未找到系统化 WER/ASR Benchmark 数据，建议以 NVIDIA 官方披露为准。

---

## SOTA 声明（有据可查）

**NVIDIA 官方定位**（有据可查）：
- "First open-source full duplex model with voice and role control"（首款支持角色控制的开放式全双工模型）
- "7 billion parameter open model for full-duplex conversational AI"（7B 参数级开源全双工对话 AI）
- 240ms 响应延迟是目前已知的开源全双工模型中最低档位之一

> ⚠️ 注意：NVIDIA 尚未在 README 中发布标准 Benchmark 表格，SOTA 性能声明为技术架构层面的领先，需以官方后续 Benchmark 发布为准。

---

## 技术亮点

1. **全双工联合建模**：单模型同时处理流式输入和输出，无需单独的 ASR + TTS 流水线
2. **角色提示工程（Role Prompting）**：通过混合系统提示同时控制文本 persona 和语音特征
3. **极低延迟架构**：Lo-Fi 24kHz 输出换取 240ms E2E 延迟，适合实时对话场景
4. **首个开源可复现的全双工方案**：对比 Moshi（商业闭源），提供开源实现

---

## 入选理由

- ✅ 2026年新发布（2026-01-15）
- ✅ 7B 全双工语音对话，开源可复现
- ✅ NVIDIA Research 背书，工程化程度高
- ✅ 240ms 延迟有据可查，为当前开源最低延迟梯队
- ⚠️ 商用许可证需仔细评估（NVIDIA Research License ≠ Apache 2.0）

---

## 信息源列表

| # | 类型 | 来源 | URL | 可靠度 |
|---|------|------|-----|--------|
| 1 | T0 | HuggingFace 模型页 | https://huggingface.co/nvidia/personaplex-7b-v1 | T0 |
| 2 | T1 | NVIDIA Research 项目主页 | https://research.nvidia.com/labs/adlr/personaplex/ | T1 |
| 3 | T1 | arXiv 论文 | https://arxiv.org/abs/2602.06053 | T1 |
| 4 | T1 | ComfyUI Wiki 新闻 | https://comfyui-wiki.com/en/news/2026-01-20-nvidia-personaplex-7b-v1-release | T1 |
| 5 | T1 | Medium 深度解读 | https://www.nurix.ai/resources/nvidia-personaplex-conversational-ai-voice-control | T1 |
| 6 | T2 | Reddit 讨论 | https://www.reddit.com/r/LocalLLaMA/comments/1qnvhqk/nvidia_personaplex_the_fullduplex_revolution/ | T2 |

---

## 许可证商用合规

| 项目 | 说明 |
|------|------|
| 许可证类型 | NVIDIA Research License / Custom License |
| 商用 | ⚠️ 需核实：研究许可证通常限制商业使用，建议查看 NVIDIA 官方条款 |
| 修改 | ⚠️ 需核实 |
| 合规要点 | **建议在商用前向 NVIDIA 法务确认许可范围**，非标准开源许可 |

---

*评测人: @alm-researcher | 评测日期: 2026-04-04*
