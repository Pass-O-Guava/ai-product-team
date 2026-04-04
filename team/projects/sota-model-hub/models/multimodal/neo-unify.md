# Model Card: NEO-unify

> **模型名称：** NEO-unify  
> **发布机构：** SenseTime（商汤科技）/ SenseNova  
> **发布日期：** 2026-03-06  
> **可靠度评级：** T1（HuggingFace 官方博客，附技术细节）

---

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型类型** | Native Multimodal Unified Model（端到端统一多模态，理解+生成一体化） |
| **支持输入模态** | 文本、图像、视频（通过 Near-Lossless Visual Interface） |
| **支持输出模态** | 文本、图像（生成） |
| **模型规模** | 2B 参数（首发规格） |
| **架构特色** | Mixture-of-Transformer (MoT)；无独立视觉编码器的原生融合架构 |
| **预训练数据规模** | Web-scale 预训练 + Mid-training (MT) + SFT |

---

## 许可证

Apache 2.0 / 开源（参考 SenseNova 系列开源策略）

---

## 链接

| 类型 | 链接 |
|------|------|
| **官方博客** | https://huggingface.co/blog/sensenova/neo-unify |
| **SenseNova HuggingFace** | https://huggingface.co/sensenova/models |
| **SenseTime 新闻稿** | https://www.sensetime.com/en/news-detail/51170267 |
| **媒体报道（PandaDaily）** | https://pandaily.com/neo-the-world-s-first-native-multimodal-architecture-launches-achieving-deep-vision-language-fusion-and-breaking-industry-bottlenecks |
| **年度财报引用** | https://media-sensetime.todayir.com/20260324175601805012064721_en.pdf |

---

## Benchmark

| 评测集 | NEO-unify (2B) 成绩 | 对比基线 |
|--------|---------------------|----------|
| MS COCO 2017 (Image Gen) | 31.56 PSNR / 0.85 SSIM | Flux VAE: 32.65 / 0.91（参考对比，非直接竞品）|
| MMMU | 超越同期其他原生 VLM | SenseNova 官方博客 |
| MMBench | 超越同等规模原生 VLM | SenseNova 官方博客 |
| VSI-Bench | 已获采纳为评测基准 | SenseNova 官方 |
| MMSI-Bench | 同上 | SenseNova 官方 |

> ⚠️ 注：具体数值需对照 HuggingFace 官方博客原文；当前数据来自摘要层，可信度 T1，完整表格待核。

---

## SOTA 声明

- ⚠️ **待验证 SOTA：** SenseNova 官方博客声称 NEO-unify 在 MMMU、MMBench 上超越原生 VLM 对手，但未给出具体数值和对比列表
- ✅ **架构创新声称有据：** 首次提出 Near-Lossless Visual Interface + MoT 融合，论文/博客描述完整

---

## 技术亮点

1. **Encoder-Free 原生架构**：不依赖独立视觉编码器，通过 Near-Lossless Visual Interface 直接将视觉信息映射到语言模型表征空间
2. **Mixture-of-Transformer (MoT)**：将 MoE 思想引入多模态融合，实现理解与生成任务的高效统一
3. **近无损视觉接口**：相比传统 VAE/编码器压缩方案，大幅保留视觉细节
4. **Scaling 新路径**：SenseTime 在财报中指出，NEO 架构代表了一种新的 Scaling Law 方向

---

## 入选理由

NEO-unify 是 2026 年以来（截至 2026-04-04）架构层面最具创新性的开源多模态统一模型，首次将原生多模态（无独立编码器）+ MoT 融合 + 近无损视觉接口三者结合，是端到端全模态理解+生成领域的里程碑工作。第二代 NEO 架构预计 2026 Q2 发布，当前为第一代预览版。

---

## 信息源列表

| # | 类型 | 来源 | 链接 | 评级 |
|---|------|------|------|------|
| 1 | 官方博客 | HuggingFace SenseNova | https://huggingface.co/blog/sensenova/neo-unify | T0 |
| 2 | 技术报道 | PandaDaily | https://pandaily.com/neo-the-world-s-first-native-multimodal-architecture-launches-achieving-deep-vision-language-fusion-and-breaking-industry-bottlenecks | T1 |
| 3 | 财报公告 | SenseTime IR | https://media-sensetime.todayir.com/20260324175601805012064721_en.pdf | T0 |
| 4 | 官方新闻 | SenseTime | https://www.sensetime.com/en/news-detail/51170267 | T0 |
| 5 | HuggingFace Org | SenseNova | https://huggingface.co/sensenova/models | T0 |
