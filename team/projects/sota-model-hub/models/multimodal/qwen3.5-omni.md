# Model Card: Qwen3.5-Omni

> **模型名称：** Qwen3.5-Omni  
> **发布机构：** Alibaba Cloud / Qwen Team  
> **发布日期：** 2026-03-30  
> **可靠度评级：** T1（官方博客 + GitHub，模型为 Proprietary）

---

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型类型** | Native Omni-Modal（任意模态输入 → 文本/语音输出） |
| **支持输入模态** | 文本、图像、音频、视频、实时流 |
| **支持输出模态** | 文本、语音（流式）、音频克隆 |
| **系列规格** | Qwen3.5-Omni-Plus / Flash / Light（三档） |
| **上下文窗口** | 256K tokens |
| **语音支持** | 113 种语言/方言识别；语音生成覆盖多语言 |
| **架构** | Thinker-Talker 双模块：Thinker 负责理解，Talker 负责语音流式生成 |

---

## 许可证

Proprietary（闭源）；可通过 Qwen Chat（网页）和 API 访问，不开放权重下载。

---

## 链接

| 类型 | 链接 |
|------|------|
| **官方博客** | https://qwen.ai/blog?id=qwen3.5-omni |
| **Hugging Face** | https://huggingface.co/spaces/Qwen/Qwen3.5-Omni-Online-Demo |
| **Hugging Face 离线 Demo** | https://huggingface.co/spaces/Qwen/Qwen3.5-Omni-Offline-Demo |
| **GitHub（对应旧版 Qwen3-Omni）** | https://github.com/QwenLM/Qwen3-Omni |
| **评测报道** | https://www.marktechpost.com/2026/03/30/alibaba-qwen-team-releases-qwen3-5-omni-a-native-multimodal-model-for-text-audio-video-and-realtime-interaction/ |

---

## Benchmark

| 评测集 | Qwen3.5-Omni-Plus 成绩 | 对比 |
|--------|------------------------|------|
| **SOTA 数量** | 215 项任务达到 SOTA | 涵盖音频/音视频理解、推理、交互 |
| MMLU-Redux | 94.2 | vs Qwen3.5-Plus 94.3 |
| C-Eval | 92.0 | vs Qwen3.5-Plus 92.3 |
| **vs Gemini-3.1-Pro** | 超越 | 215 项 benchmark 中多项胜出 |
| 音频理解 | SOTA（22/36 项子集开源对比） | 开源领域排名第一 |
| 视频理解 | 领先竞品 | 400 秒 720P 视频输入 |

> 注：「215 SOTA」为官方博客声称，可信度评级 T1，需对照具体评测表格逐一验证。部分 Reddit 用户指出评测对比基准存在选择性。

---

## SOTA 声明

- ✅ **有据 SOTA（215 benchmark，SOTA 级别）：** 官方博客明确列出 215 项音频/音视频理解 benchmark 声称 SOTA  
- ⚠️ **注意：** 该「215 SOTA」数字含专有模型对比；开源可比范围为 Qwen3-Omni 在 36 个音频 benchmark 中取得 22 项总体 SOTA、32 项开源 SOTA（旧版数据）

---

## 技术亮点

1. **Thinker-Talker 原生多模态架构**：Thinker 模块统一处理文本、图像、音频、视频 token；Talker 模块直接从文本语义流式生成语音，无 ASR/TTS 级联延迟
2. **超长上下文**：256K tokens，可处理 10+ 小时音频、400+ 秒 720P 视频（1 FPS）
3. **原生语音克隆**：支持从短音频参考中克隆音色，零样本
4. **端到端流式交互**：实时流输入 + 流式输出，延迟低于传统级联 Pipeline

---

## 入选理由

Qwen3.5-Omni 是 2026 年以来（截至 2026-04-04）技术指标最完整、评测范围最广的端到端全模态模型，在语音/视频理解 Benchmark 上覆盖了此前开源与闭源模型的最大评测集，架构上首次实现了 Thinker-Talker 统一建模，是当前全模态（Any-to-Text + Any-to-Audio）领域的标志性工作。

---

## 信息源列表

| # | 类型 | 来源 | 链接 | 评级 |
|---|------|------|------|------|
| 1 | 官方博客 | Qwen.ai | https://qwen.ai/blog?id=qwen3.5-omni | T0 |
| 2 | 新闻报道 | MarkTechPost | https://www.marktechpost.com/2026/03/30/alibaba-qwen-team-releases-qwen3-5-omni/ | T1 |
| 3 | 官方 GitHub（Qwen3-Omni v1） | GitHub | https://github.com/QwenLM/Qwen3-Omni | T0 |
| 4 | 社区讨论 | Reddit r/LocalLLaMA | https://www.reddit.com/r/LocalLLaMA/comments/1s8d5zo/qwen35omni_sota_on_215_benchmarks/ | T2 |
| 5 | 官方 HF Space | Hugging Face | https://huggingface.co/spaces/Qwen/Qwen3.5-Omni-Online-Demo | T0 |
| 6 | 技术解读 | Analytics Vidhya | https://www.analyticsvidhya.com/blog/2026/03/qwen3-5-omni-ai-model/ | T1 |
| 7 | 评测报道 | BuildFastWithAI | https://www.buildfastwithai.com/blogs/qwen3-5-omni-multimodal-ai-review | T1 |
| 8 | Reddit 讨论 | Reddit r/LocalLLaMA | https://www.reddit.com/r/LocalLLaMA/comments/1s8apue/qwen35omni_results_have_been_published/ | T2 |
