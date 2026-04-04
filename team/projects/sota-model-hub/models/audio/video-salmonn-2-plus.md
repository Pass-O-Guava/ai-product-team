# Model Card: video-SALMONN 2+

> **模型全称**: video-SALMONN 2+ (ByteDance / Tsinghua-EE)  
> **发布机构**: ByteDance & Tsinghua University (EE Department)  
> **论文发布时间**: 2025-06-18（arXiv）  
> **2026 新版本发布时间**: 2026-01-28（HuggingFace 72B audio-aligned）/ 2026-02-15（3B audio-aligned）/ 2026-02-24（minimal inference code）  
> **模型类型**: Audio-Visual Large Language Model（音视频多模态）  
> **许可证**: 研究许可（需查看具体条款）  
> **模型规格**: 3B / 7B / 72B 参数（多规格）  
> **评测日期**: 2026-04-04  
> **可靠度评级**: T1 / 中 / 部分数据待补充 ⚠️  

---

## 基本信息

| 字段 | 内容 |
|------|------|
| 模型名称 | video-SALMONN 2+ |
| 参数量 | 3B / 7B / 72B（三种规格） |
| 论文发布 | 2025-06-18（arXiv） |
| 2026 新版本 | 2026-01-28（72B audio-aligned HF）、2026-02-15（3B audio-aligned）、2026-02-24（minimal inference code） |
| 发布机构 | ByteDance & Tsinghua University EE |
| 模型类型 | 音视频大语言模型（Audio-Visual LLM） |
| 许可证 | 研究许可（需查看具体条款） |
| 代码链接 | https://github.com/bytedance/video-SALMONN-2 |
| 论文链接 | https://arxiv.org/abs/2506.15220 |
| HuggingFace | https://huggingface.co/tsinghua-ee/video-SALMONN-2_plus_72B / https://huggingface.co/tsinghua-ee/video_SALMONN2plus_72B_audioAlign |

---

## ⚠️ 版本说明（重要）

| 版本 | 发布时间 | 内容 |
|------|----------|------|
| video-SALMONN 2（原始） | 2025-06-18 | 论文发布，3B/7B/72B 初始版本 |
| video-SALMONN 2+ Version-2509 | 2025-09-26 | 代码修订，7B/72B 更新 |
| 72B Audio-Aligned | **2026-01-28** | HF 上线，音频对齐版 |
| 3B Audio-Aligned | **2026-02-15** | HF 上线，音频对齐版 |
| Minimal Inference Code | **2026-02-24** | 轻量推理代码发布 |

> 本 Model Card 主要收录 **2026 年发布的新版本（audio-aligned checkpoints + inference code）**。原始论文属 2025年，不符合半年内收录标准，但 2026-01/02 月的 HF checkpoint 属于新发布内容。

---

## 核心能力

- **字幕增强音视频理解（Captioning-Enhanced）**：通过生成高质量字幕增强视频理解
- **音视频联合推理**：同时处理视频画面和音频信号，统一输出
- **低幻觉率**：官方评测中幻觉率显著低于竞品
- **多规格可选**：3B（轻量）、7B（均衡）、72B（旗舰），适应不同算力场景
- **Audio-Aligned 版**：2026 新发布，优化了音频信号对齐质量

---

## Benchmark 表现

| 数据集 | 72B 结果 | 3B/7B 结果 | 备注 |
|--------|----------|-----------|------|
| Video-MME（音视频 QA） | **SOTA** | 各规模领先 | 官方声明，有据可查 |
| 自定义音视频评测集 | 22.9% 总错误率 | — | 低于 GPT-4o / Gemini-1.5-Pro |
| 视频描述质量 | SOTA | 规模领先 | 官方 Leaderboard |

> 数据来源：arXiv 2506.15220（2025-06-18 初版，2025-07-10 更新），HuggingFace Model Card
> ⚠️ 具体 2026 版（audio-aligned）的 Benchmark 数据尚未单独披露，沿用 2025 版数据

---

## SOTA 声明（有据可查）

**官方声明**（有据可查）：
- "video-SALMONN 2+ achieves SOTA on audio-visual QA benchmarks, including Video-MME"
- 72B: "surpasses all open-source competitors"（超越所有开源竞品）
- 3B/7B: "lead their size class"（各自规模级别领先）
- 自定义测试集总错误率 22.9%，优于 GPT-4o 和 Gemini-1.5-Pro

---

## 技术亮点

1. **Captioning-Enhanced 架构**：引入字幕生成模块作为中间表征，提升音视频理解深度
2. **LoRA 微调方案**：低秩适配，降低微调成本
3. **Audio-Aligned 2026 版**：重新对齐音频信号，提升音频理解精度
4. **Minimal Inference Code（2026-02-24）**：极简推理代码，降低部署门槛

---

## 入选理由

- ✅ 2026-01/02 月有新版本发布（audio-aligned checkpoints + inference code）
- ✅ 72B 版本在音视频多模态领域具备 SOTA 潜力
- ✅ 多规格（3B/7B/72B）覆盖边缘到旗舰场景
- ⚠️ 原始论文 2025-06 发布，不符合半年标准，但 2026 HF checkpoint 属新内容
- ⚠️ 许可证未明确，需进一步确认商用合规性

---

## 信息源列表

| # | 类型 | 来源 | URL | 可靠度 |
|---|------|------|-----|--------|
| 1 | T0 | HuggingFace 72B+ | https://huggingface.co/tsinghua-ee/video-SALMONN-2_plus_72B | T0 |
| 2 | T0 | HuggingFace 72B Audio-Aligned | https://huggingface.co/tsinghua-ee/video_SALMONN2plus_72B_audioAlign | T0 |
| 3 | T1 | GitHub 项目页 | https://github.com/bytedance/video-SALMONN-2 | T1 |
| 4 | T1 | arXiv 论文 | https://arxiv.org/abs/2506.15220 | T1 |
| 5 | T1 | HuggingFace Collection | https://huggingface.co/collections/tsinghua-ee/video-salmonn-2 | T1 |
| 6 | T2 | OpenReview | https://openreview.net/forum?id=O2tca5tExP | T2 |

---

## 许可证商用合规

| 项目 | 说明 |
|------|------|
| 许可证类型 | 未明确标注（研究许可，需进一步确认） |
| 商用 | ⚠️ 未明确，建议联系 ByteDance/Tsinghua 获取商业授权 |
| 合规要点 | **建议商用前确认许可范围**，ByteDance 系产品通常有商业化路径但需单独协商 |

---

*评测人: @alm-researcher | 评测日期: 2026-04-04*
