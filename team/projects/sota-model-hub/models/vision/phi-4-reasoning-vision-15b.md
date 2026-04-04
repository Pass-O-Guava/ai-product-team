# Model Card: Phi-4-reasoning-vision-15B

> 视觉-语言推理模型 | 微软研究院 | 2026年3月4日

---

## 1. 基本信息

| 字段 | 内容 |
|------|------|
| **模型全称** | Phi-4-reasoning-vision-15B（简称 Phi-4-Reasoning-Vision） |
| **发布方** | 微软研究院（Microsoft Research） |
| **参数量** | 15B（150亿参数） |
| **模态** | 图像 + 文本（多模态推理） |
| **发布日期** | 2026年3月4日 |
| **开源时间** | 2026年3月4日（同步开源） |
| **代码仓库** | https://github.com/microsoft/Phi-4-reasoning-vision-15B |
| **技术报告** | arXiv:2603.03975（2026-03-04） |

---

## 2. 许可证与商用合规

| 许可证 | 商用意况 |
|--------|----------|
| **MIT License** | ✅ 可商用（无限制，无需申请） |

> **来源**：[HuggingFace Phi-4-reasoning-vision-15B](https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B)；[GitHub README](https://github.com/microsoft/Phi-4-reasoning-vision-15B)

---

## 3. HuggingFace + ModelScope 链接

| 平台 | 链接 |
|------|------|
| **HuggingFace** | https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B |
| **GitHub** | https://github.com/microsoft/Phi-4-reasoning-vision-15B |
| **arXiv 技术报告** | https://arxiv.org/abs/2603.03975 |
| **Microsoft 官方博客** | https://www.microsoft.com/en-us/research/blog/phi-4-reasoning-vision-and-the-lessons-of-training-a-multimodal-reasoning-model/ |
| **Azure AI Foundry** | https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-phi-4-reasoning-vision-to-microsoft-foundry/4499154 |

> ModelScope 链接需实测，部分微软模型可能未同步上架。

---

## 4. Benchmark 数据

### 完整官方评测结果

| Benchmark | 分数 | 说明 |
|-----------|------|------|
| **AI2D_TEST** | 84.8 | 科学图表理解 |
| **ChartQA_TEST** | 83.3 | 图表阅读理解 |
| **MathVista_MINI** | 75.2 | 数学视觉推理 |
| **MMMU_VAL** | 54.3 | 大学级别多模态理解 |
| **MMStar** | 64.5 | 多模态事实性/幻觉检测 |
| **HallusionBench** | 64.4 | 视觉幻觉检测 |
| **WeMath** | 50.1 | 数学应用题 |
| **MathVerse_MINI** | 44.9 | 数学图表理解 |
| **MathVision_MINI** | 36.2 | 数学视觉理解（高难） |
| **ScreenSpot_v2_Desktop** | 87.1 | 桌面 UI 理解 |
| **ScreenSpot_v2_Mobile** | 88.6 | 移动端 UI 理解 |
| **ScreenSpot_v2_Web** | 88.8 | 网页 UI 理解 |
| **ZEROBench_sub** | 17.7 | 通用视觉语言评测 |

> **来源**：[GitHub README 官方披露](https://github.com/microsoft/Phi-4-reasoning-vision-15B)；[VentureBeat 报道](https://venturebeat.com/technology/microsoft-built-phi-4-reasoning-vision-15b-to-know-when-to-think-and-when)；[Forbes 报道](https://www.forbes.com/sites/janakirammsv/2026/03/06/microsoft-builds-a-compact-ai-model-that-decides-when-to-think/)

### 对比亮点

- **MathVista 75.2**：领先多款大型多模态模型
- **ScreenSpot 全面 87+**：UI/屏幕理解能力极为突出
- **15B 紧凑规格**：以最小体积实现顶级数学推理能力

---

## 5. SOTA 声明

**✅ 有量化证据的声明：**

- 在 **15B 参数量级**实现了与大型模型（Gemini Pro 1.5等）相当的数学推理能力（MathVista 75.2）
- **UI/屏幕理解 SOTA**：ScreenSpot v2 三项全超 87%，在桌面/移动/网页 UI 任务上表现卓越
- 微软官方声称："compact model that decides when to think"——即在推理时自适应决定是否需要深度思考

> ⚠️ **边界**：Phi-4-reasoning-vision 在 MathVista 等特定 benchmark 上有突出表现，但在 MMMU（54.3）等综合学术 benchmark 上落后于更大模型（如 Qwen3-VL-32B、InternVL3-78B）。**SOTA 声明范围限定在"紧凑模型"（Compact Multimodal Model）类别**。

---

## 6. 技术亮点

| 亮点 | 描述 |
|------|------|
| **自适应推理（Selective Thinking）** | 核心创新——模型学会在简单任务上快速回答，在复杂任务上深度思考，避免"过度思考" |
| **卓越数学推理** | MathVista 75.2，超越多款更大模型 |
| **顶级 UI/屏幕理解** | ScreenSpot 三项均超 87%，可应用于自动化测试、GUI Agent |
| **文档与图表理解** | ChartQA 83.3，可处理收据、表格、图表 |
| **合成数据训练** | 延续 Phi-4 系列传统，以高质量合成数据为核心 |
| **完全开源** | 权重 + 代码 + 技术报告同日发布 |

> **来源**：[Microsoft Research Blog](https://www.microsoft.com/en-us/research/blog/phi-4-reasoning-vision-and-the-lessons-of-training-a-multimodal-reasoning-model/)；[VentureBeat](https://venturebeat.com/technology/microsoft-built-phi-4-reasoning-vision-15b-to-know-when-to-think-and-when)

---

## 7. 入选理由

1. **2026年3月4日最新发布**，距调研日期不足一个月
2. **微软研究院出品**，MIT 许可证，商业可用
3. **"选择性推理"机制**——业界创新的推理策略，有效控制计算成本
4. **UI/屏幕理解领域**，ScreenSpot benchmark 全面领先，具有实际应用价值
5. **15B 紧凑规格**易于部署，在边缘设备和消费级 GPU 上有实际可用性
6. 微软同日发布技术报告（arXiv）、博客、代码仓库，信息完整度极高

---

## 8. 信息源列表

| 优先级 | 来源 | 链接 |
|--------|------|------|
| T0 | HuggingFace 官方页 | https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B |
| T0 | GitHub 官方仓库 | https://github.com/microsoft/Phi-4-reasoning-vision-15B |
| T1 | Microsoft Research 官方博客 | https://www.microsoft.com/en-us/research/blog/phi-4-reasoning-vision-and-the-lessons-of-training-a-multimodal-reasoning-model/ |
| T1 | Azure AI Foundry 公告 | https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-phi-4-reasoning-vision-to-microsoft-foundry/4499154 |
| T2 | arXiv 技术报告 | https://arxiv.org/abs/2603.03975 |
| T2 | VentureBeat 报道 | https://venturebeat.com/technology/microsoft-built-phi-4-reasoning-vision-15b-to-know-when-to-think-and-when |
| T2 | Forbes 报道 | https://www.forbes.com/sites/janakirammsv/2026/03/06/microsoft-builds-a-compact-ai-model-that-decides-when-to-think/ |
| T3 | MLQ.ai 报道 | https://mlq.ai/news/microsoft-releases-phi-4-reasoning-vision-15b-open-weight-multimodal-ai-model/ |

---

*最后更新：2026-04-04 | 调研员：@vlm-researcher*
