# Gemma 4 — 多模态开源小模型家族

> **调研员**: @video-researcher  
> **产出日期**: 2026-04-04  
> **信息源等级**: T0（HuggingFace 官方博客）/ T1（Google DeepMind 官方博客 / GitHub）

---

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型全称** | Gemma 4 |
| **发布机构** | Google DeepMind |
| **发布/发现日期** | 2026-04-03（博客/新闻），2026-04-02（HuggingFace PR 合并） |
| **模型类型** | 开源多模态语言模型（视觉 + 文本 + 视频） |
| **参数量级** | 2B / 4B / 9B / 27B / 31B 共5个规格 |
| **所在产品线** | Gemma Family（Google 轻量级开源模型系列） |

---

## 许可证

- **许可类型**: Gemma Terms（Google 专属使用条款，类自定义许可证）
- ⚠️ 非标准开源许可证（Apache 2.0 / MIT），需查阅 Google 官方条款确认商用限制

---

## 链接

| 类型 | 链接 |
|------|------|
| **HuggingFace 主页** | https://huggingface.co/google/gemma-4-** |
| **GitHub** | https://github.com/google-deepmind/gemma |
| **Google 官方博客** | https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/ |
| **HuggingFace 博客** | https://huggingface.co/blog/gemma4 |
| **ModelScope** | 需确认（官方博客提及） |
| **vLLM 支持分支** | https://docs.vllm.ai/projects/recipes/en/latest/Google/Gemma4.html |

---

## Benchmark / SOTA 声明（有据可查）

| Benchmark | 成绩 | 来源 | 备注 |
|-----------|------|------|------|
| Video Understanding（视频帧序列理解） | 支持 | HF Blog，2026-04-03 | 通过视频帧序列输入实现 |
| Multimodal Reasoning（多模态推理） | 前沿（State-of-the-art） | HF Blog，2026-04-03 | "Frontier multimodal intelligence on device" |
| LMArena / WebDevArena | 领先 | HF Blog | 多模态综合排名第一梯队 |
| MVBench / Video-MME | 社区正在测试中 | HF Discussion，2026-04 | HuggingFace 社区讨论确认中 |

> ⚠️ **SOTA 声明边界**: Google 官方声明"最强大 Gemma 模型"，明确支持视频理解，但具体 Video-MME / MVBench / LVBench 等视频专项数值尚未广泛披露，以"多模态设备端前沿"定性描述为主，不做精确数字 SOTA 声明。

---

## 技术亮点

1. **原生多模态 Early Fusion 架构**：文本与图像/视频 token 在模型早期即融合，而非拼接 adapter
2. **视频理解管线**：vLLM 已提供自定义视频处理 pipeline，通过帧序列提取 + 统一 token 化实现视频输入
3. **多规格支持**：2B/4B（轻量端侧，含音频视频）→ 27B/31B（大规格，无音频但视频更强）
4. **140 语言支持**：延续 Gemma 家族多语言能力
5. **Agentic Workflows 优先设计**：强化推理与 Agent 任务能力
6. **HuggingFace Transformers v5.5.0 首发支持**（2026-04-02 合入主线）

---

## 入选理由

1. **时效性极强**：2026-04-03 刚发布，是本次调研窗口内最新发布的开源视频理解模型
2. **Google 官方背书**：DeepMind 背书的多模态视频理解能力，明确支持视频帧序列输入
3. **生态完善**：HuggingFace / vLLM / Transformers 全家桶当天即支持，开发者友好度极高
4. **5 规格覆盖**：从 2B 端侧到 31B 大杯，不同算力场景均有对应版本
5. **行业影响大**：Gemma 4 的发布被视为开源多模态小模型的重要里程碑（Latent Space 等媒体高度关注）

---

## 信息源列表

| # | 来源 | 类型 | 可信度 | 链接 |
|---|------|------|--------|------|
| 1 | HuggingFace Gemma 4 博客 | T0 | ★★★★★ | https://huggingface.co/blog/gemma4 |
| 2 | Google DeepMind Gemma 4 博客 | T0 | ★★★★★ | https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/ |
| 3 | HuggingFace 模型卡 | T0 | ★★★★★ | https://huggingface.co/google/gemma-4-E4B |
| 4 | vLLM Gemma 4 文档 | T1 | ★★★★ | https://docs.vllm.ai/projects/recipes/en/latest/Google/Gemma4.html |
| 5 | Latent Space AINews | T1 | ★★★★ | https://www.latent.space/p/ainews-gemma-4-the-best-small-multimodal |
| 6 | Reddit r/LocalLLaMA 讨论 | T2 | ★★★ | https://www.reddit.com/r/LocalLLaMA/comments/1salgre/gemma_4_has_been_released/ |
