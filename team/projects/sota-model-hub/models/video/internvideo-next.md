# InternVideo-Next — 通用视频基础模型

> **调研员**: @video-researcher  
> **产出日期**: 2026-04-04  
> **信息源等级**: T0（HuggingFace / GitHub OpenGVLab）/ T1（arXiv）

---

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型全称** | InternVideo-Next |
| **发布机构** | Shanghai AI Lab（OpenGVLab） |
| **发布/发现日期** | 2025-12（技术报告与预训练权重正式发布） |
| **模型类型** | 通用视频基础模型（Video Foundation Model） |
| **参数量级** | 未公开完整规模（基于 InternVideo 生态，系列含 6B+ 参数编码器） |
| **所在产品线** | InternVideo 系列（OpenGVLab 视频理解系列） |

---

## 许可证

- **许可类型**: 需查阅 OpenGVLab 官方条款（基于开源协议，非商业限制）
- ⚠️ OpenGVLab 部分模型采用自定义许可证，建议查阅 GitHub 仓库 License 文件

---

## 链接

| 类型 | 链接 |
|------|------|
| **GitHub（InternVideo 集合页）** | https://github.com/opengvlab/internvideo |
| **arXiv 技术报告** | https://arxiv.org/abs/2512.01342（2025-12-01 初版） |
| **arXiv HTML 最新版** | https://arxiv.org/html/2512.01342v2（4 days ago，2026-04） |
| **HuggingFace OpenGVLab Collection** | https://huggingface.co/collections/OpenGVLab/internvideo2 |
| **arXiv 摘要页面** | https://tldr.takara.ai/p/2512.01342 |

---

## Benchmark / SOTA 声明（有据可查）

| Benchmark | 成绩 | 来源 | 备注 |
|-----------|------|------|------|
| **Video Understanding（全任务）** | **SOTA** | arXiv 2512.01342，2025-12 | 官方技术报告声明 |
| Video Recognition | State-of-the-art | GitHub，2025-12 | 视频动作识别 |
| Video-Text | State-of-the-art | GitHub，2025-12 | 视频-文本多模态 |
| 开源视频理解 | 领先 | arXiv，2025-12 | 相比 InternVideo2.5 有显著提升 |

> ✅ **SOTA 声明**: 技术报告摘要原文："achieves state-of-the-art results across benchmarks"；GitHub 官方仓库明确标注"State-of-the-art"。arXiv HTML 版最近更新（2026-04），说明项目仍在活跃维护中。

---

## 技术亮点

1. **无标签视频预训练**：基于大规模无标注公开视频自监督预训练，降低数据依赖
2. **通用视频理解能力**：支持视频动作识别、时序理解、视频-文本多模态等多种任务
3. **Scaling 路径清晰**：官方明确表示提供了"可扩展路径"（scalable path toward world understanding）
4. **Video Foundation Model 定位**：不同于 VLM，专注视频表示学习，适合作为视频编码器接入多模态系统
5. **OpenGVLab 生态**：与 InternVideo / InternVL 形成完整视频+图像+语言多模态家族
6. **开源预训练权重**：官方 GitHub 同步发布权重，方便研究社区复现与微调

---

## 入选理由

1. **官方 SOTA 声明**：技术报告明确声明"state-of-the-art across benchmarks"
2. **发布时间合规**：2025-12 发布，在半年窗口内（距今约 4 个月）
3. **OpenGVLab 权威发布**：上海 AI Lab 是视频理解领域顶级开源团队，GitHub Stars 超 7k
4. **视频理解专项**：专注视频基础模型，是视频多模态大模型的重要底层编码器
5. **活跃维护**：arXiv HTML 版于 2026-04 刚更新，说明仍在持续优化

---

## 信息源列表

| # | 来源 | 类型 | 可信度 | 链接 |
|---|------|------|--------|------|
| 1 | arXiv 技术报告 2512.01342 | T0 | ★★★★★ | https://arxiv.org/abs/2512.01342 |
| 2 | OpenGVLab InternVideo GitHub | T0 | ★★★★★ | https://github.com/opengvlab/internvideo |
| 3 | HuggingFace OpenGVLab Collection | T0 | ★★★★★ | https://huggingface.co/collections/OpenGVLab/internvideo2 |
| 4 | Semantic Scholar 摘要 | T1 | ★★★★ | https://www.semanticscholar.org/paper/InternVideo2 |
| 5 | Reddit r/MachineLearning 讨论 | T2 | ★★★ | https://www.reddit.com/r/MachineLearning/comments/1ekpgd8/ |
