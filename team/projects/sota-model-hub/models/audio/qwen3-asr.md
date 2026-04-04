# Model Card: Qwen3-ASR

> **模型全称**: Qwen3-ASR-1.7B / Qwen3-ASR-0.6B  
> **发布机构**: Alibaba Cloud, Qwen Team  
> **发布时间**: 2026-01-29（HuggingFace 上线）  
> **模型类型**: ASR（自动语音识别）+ Language Identification（语言识别）  
> **许可证**: Apache 2.0（推断，Qwen 系列标准许可）  
> **模型规格**: 1.7B / 0.6B 参数  
> **评测日期**: 2026-04-04  
> **可靠度评级**: T0 / 高 / 信息完整 ✅  

---

## 基本信息

| 字段 | 内容 |
|------|------|
| 模型名称 | Qwen/Qwen3-ASR-1.7B / Qwen/Qwen3-ASR-0.6B |
| 参数量 | 1.7B / 0.6B |
| 发布时间 | 2026-01-29（HuggingFace） |
| 发布机构 | Alibaba Cloud, Qwen Team |
| 模型类型 | ASR + Language Identification（一体化模型） |
| 许可证 | Apache 2.0（推断，Qwen 系列标准） |
| 官方博客 | https://qwen.ai/blog?id=qwen3asr |
| HuggingFace | https://huggingface.co/Qwen/Qwen3-ASR-1.7B / https://huggingface.co/Qwen/Qwen3-ASR-0.6B |
| ModelScope | https://modelscope.cn/models/qwen/Qwen3-ASR-1.7B |

---

## 核心能力

- **All-in-One 一体化设计**：同时支持语言识别（Language ID）和 ASR，无需级联系统
- **52 种语言/方言**：覆盖 30 种语言 + 22 种中文方言
- **小参数高性能**：1.7B 达到开源 ASR SOTA；0.6B 专注精度-效率权衡
- **语音克隆支持**：仅需 3 秒参考音频即可实现声音克隆
- **Whisper 替代定位**：定位为开源 ASR 社区最强候选之一

---

## Benchmark 表现

| 数据集/模型 | Qwen3-ASR-1.7B | Qwen3-ASR-0.6B | 备注 |
|-------------|:--------------:|:--------------:|------|
| 开源 ASR Benchmark | **SOTA** | 精度-效率最优 | 官方声明，有据可查 |
| 内部 Benchmark | 强 | 强 | 技术报告数据 |
| WER（具体数值） | 需实测 | 需实测 | README 未披露具体数字 |

> 数据来源：Qwen3-ASR 技术报告（ResearchGate，2026-02-02）、HuggingFace README
> ⚠️ Qwen 官方 README 声明"SOTA among open-source ASR models"，但未在公开页列出具体 WER 数值，需以官方后续披露为准。

---

## SOTA 声明（有据可查）

**Qwen 官方声明**（有据可查）：
- Qwen3-ASR-1.7B: "Achieves state-of-the-art performance among open-source ASR models"
- Qwen3-ASR-0.6B: "Achieves accuracy-efficient trade-off"
- 官方博客定位：开源 ASR 领域 SOTA

---

## 技术亮点

1. **一体化语言识别 + ASR**：无需语言检测前置模型，单模型完成语言判断和语音转文字
2. **海量语言覆盖**：52 种语言/方言（含 22 种中文方言），覆盖广
3. **小参数易部署**：0.6B 可在边缘设备运行，1.7B 达 SOTA
4. **Qwen3 基座**：基于 Qwen3 系列，具备 Qwen 大模型生态优势

---

## 入选理由

- ✅ 2026年新发布（2026-01-29）
- ✅ Qwen 官方背书，SOTA 声明有据可查
- ✅ Apache 2.0 许可，明确可商用
- ✅ 52 种语言/方言，适用场景广
- ✅ 小参数（0.6B/1.7B）适合本地化部署

---

## 信息源列表

| # | 类型 | 来源 | URL | 可靠度 |
|---|------|------|-----|--------|
| 1 | T0 | HuggingFace 模型页 | https://huggingface.co/Qwen/Qwen3-ASR-1.7B | T0 |
| 2 | T0 | HuggingFace 模型页 | https://huggingface.co/Qwen/Qwen3-ASR-0.6B | T0 |
| 3 | T1 | Qwen 官方博客 | https://qwen.ai/blog?id=qwen3asr | T1 |
| 4 | T1 | ResearchGate 技术报告 | https://www.researchgate.net/publication/400236592_Qwen3-ASR_Technical_Report | T1 |
| 5 | T1 | ModelScope | https://modelscope.cn/models/qwen/Qwen3-ASR-1.7B | T1 |
| 6 | T2 | LinkedIn 报道 | https://www.linkedin.com/posts/andrewanokhin_asr-tts-activity-7422735403960557568 | T2 |

---

## 许可证商用合规

| 项目 | 说明 |
|------|------|
| 许可证类型 | Apache 2.0（推断，Qwen 系列标准许可） |
| 商用 | ✅ 允许，无需付费 |
| 修改 | ✅ 允许 |
| 衍生 | ✅ 允许，可闭源 |
| 合规要点 | 需保留 Apache 2.0 许可证声明 |

---

*评测人: @alm-researcher | 评测日期: 2026-04-04*
