# Model Card: Covo-Audio-Chat

> **模型全称**: Tencent Covo-Audio-Chat  
> **发布机构**: Tencent AI Lab  
> **发布时间**: 2026-02-10（HuggingFace 上线） / 2026-03-26（公开公告）  
> **模型类型**: End-to-End Large Audio Language Model (LALM)  
> **许可证**: CC BY 4.0（可商用）  
> **模型规格**: 7B 参数  
> **评测日期**: 2026-04-04  
> **可靠度评级**: T0 / 高 / 信息完整 ✅  

---

## 基本信息

| 字段 | 内容 |
|------|------|
| 模型名称 | Covo-Audio-Chat |
| 参数量 | 7B |
| 发布时间 | 2026-02-10（HuggingFace）/ 2026-03-26（公开公告） |
| 发布机构 | Tencent AI Lab |
| 模型类型 | 端到端音频-语言模型（Speech LLM） |
| 许可证 | CC BY 4.0 |
| 代码链接 | https://github.com/Tencent/Covo-Audio |
| 论文链接 | https://arxiv.org/abs/2602.09823 |
| HuggingFace | https://huggingface.co/tencent/Covo-Audio-Chat |
| ModelScope | 未明确标注（腾讯系通常同步） |

---

## 核心能力

- **原生全双工交互（Native Full-Duplex）**：支持同时听和说，可实现自然打断与平滑话术切换
- **端到端连续音频处理**：直接处理连续音频流，无需中间 ASR 模块
- **音频生成**：同时输出文本和音频，无需 TTS 模块
- **实时推理管线**：配套开源推理 pipeline，支持低延迟部署
- **语音定制**：支持语音克隆和声音风格控制

---

## Benchmark 表现

| 数据集 | 指标 | 说明 |
|--------|------|------|
| MMAU（音频理解） | **75.30%** | 官方技术报告披露 |
| 预训练基础模型 | 强语音-文本理解和语义推理能力 | 技术报告数据 |

> ⚠️ 数据来源：Tencent 技术报告（arXiv 2602.09823，2026-01-27 提交），可靠度 T1

---

## SOTA 声明（有据可查）

**Tencent 技术报告声明**：预训练基础模型在 MMAU 音频理解任务上达到 75.30%，在同类端到端语音语言模型中处于领先水平。

> ⚠️ 需注意：MMAU 是内部或自定义评测基准，非社区公认 Leaderboard（如 OpenASR）。SOTA 声明基于厂商自测，建议以实际业务评测为准。

---

## 技术亮点

1. **JEPA 架构用于实时隐含特征学习**（技术报告提及）
2. **层次化三模态语音-文本交织（Hierarchical Tri-modal Speech-Text Interleaving）**：深度跨模态对齐
3. **高斯 Splatting 用于 3D 空间环境建模**（技术报告提及）
4. **CC BY 4.0 许可**：明确可商用，门槛低

---

## 入选理由

- ✅ 2026年新发布（2026-02-10 HF 上线）
- ✅ 7B 端到端音频语言模型，全双工可商用
- ✅ CC BY 4.0 明确商用许可
- ✅ 配套完整开源推理管线（降低部署门槛）
- ✅ 涵盖音频理解 + 生成双重能力

---

## 信息源列表

| # | 类型 | 来源 | URL | 可靠度 |
|---|------|------|-----|--------|
| 1 | T0 | HuggingFace 模型页 | https://huggingface.co/tencent/Covo-Audio-Chat | T0 |
| 2 | T1 | arXiv 技术报告 | https://arxiv.org/abs/2602.09823 | T1 |
| 3 | T1 | MarkTechPost 新闻报道 | https://www.marktechpost.com/2026/03/26/tencent-ai-open-sources-covo-audio/ | T1 |
| 4 | T2 | Reddit 讨论 | https://www.reddit.com/r/machinelearningnews/comments/1s40y97/tencent_ai_open_sources_covoaudio/ | T2 |
| 5 | T1 | WinBuzzer 新闻 | https://www.newsbreak.com/winbuzzer-com-302470011/4559659100571-tencent-releases-covo-audio-open-source-7b-speech-ai-model | T1 |

---

## 许可证商用合规

| 项目 | 说明 |
|------|------|
| 许可证类型 | CC BY 4.0（Creative Commons Attribution 4.0） |
| 商用 | ✅ 允许，需注明来源 |
| 修改 | ✅ 允许 |
| 衍生 | ✅ 允许 |
| 合规要点 | 使用时必须署名（Attribution），提供许可证副本或链接 |

---

*评测人: @alm-researcher | 评测日期: 2026-04-04*
