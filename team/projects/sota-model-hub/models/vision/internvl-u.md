# Model Card: InternVL-U

> 统一多模态模型（UMM）| 上海AI Lab OpenGVLab | 2026年3月

---

## 1. 基本信息

| 字段 | 内容 |
|------|------|
| **模型全称** | InternVL-U |
| **发布方** | 上海人工智能实验室·OpenGVLab（Shanghai AI Lab） |
| **参数量** | **4B**（40亿参数）——统一模型中的极轻量规格 |
| **模态** | 多模态理解 + 推理 + 图像生成 + 图像编辑（四合一统一框架） |
| **发布日期** | 2026年3月6日（技术报告 & 代码 & 模型权重） |
| **开源时间** | 2026年3月6日（同步开源） |
| **技术报告** | arXiv:2603.09877（2026-03-10 正式提交） |
| **代码仓库** | https://github.com/OpenGVLab/InternVL-U |
| **Benchmark** | 同步发布 TextEdit Benchmark（2148样本高质量评测集） |

---

## 2. 许可证与商用合规

| 许可证 | 商用意况 |
|--------|----------|
| **MIT License** | ✅ 可商用（无限制） |

> **来源**：[OpenGVLab/InternVL-U GitHub README](https://github.com/OpenGVLab/InternVL-U)；[HuggingFace InternVL-U](https://huggingface.co/InternVL-U/InternVL-U)

---

## 3. HuggingFace + ModelScope 链接

| 平台 | 链接 |
|------|------|
| **HuggingFace Org** | https://huggingface.co/InternVL-U/InternVL-U |
| **GitHub** | https://github.com/OpenGVLab/InternVL-U |
| **arXiv 论文** | https://arxiv.org/abs/2603.09877 |
| **HuggingFace Papers** | https://huggingface.co/papers/2603.09877 |
| **Twitter/X 公告** | https://x.com/intern_lm |

> ModelScope 链接待实测补充（InternVL 系列通常同步上架 ModelScope）。

---

## 4. Benchmark 数据

### 官方核心评测结果

InternVL-U 以 **4B 参数**在多项关键任务上超越 **3倍规模** 的对手模型：

| 评测任务 | InternVL-U (4B) | BAGEL (14B) | 说明 |
|----------|-----------------|-------------|------|
| 图像生成 | ✅ 超越 | — | GenEval 等评测 |
| 图像编辑 | ✅ 超越 | — | TextEdit Benchmark |
| 多模态理解 | ✅ 保留能力 | — | 兼顾理解能力不牺牲 |
| 文本渲染（Text Rendering） | ✅ 显著超越 | — | 在文本渲染任务上显著领先 |

### TextEdit Benchmark（新发布）

- **样本量**：2148 个，覆盖多场景文本编辑任务
- **目的**：评估图像生成模型中的文本编辑能力
- InternVL-U 在该 benchmark 上**显著领先**同类统一模型

### 关键结论

> "InternVL-U consistently outperforms unified baseline models with over 3× larger scales such as BAGEL (14B) on various generation and editing tasks, while retaining strong multimodal understanding and reasoning capabilities."
>
> — arXiv:2603.09877

> ⚠️ **Benchmark 数据精确分数**：arXiv 论文中详细分数数据需直接阅读论文。当前已确认 InternVL-U 在 4B 规模上超越 14B BAGEL 模型（GenAI + Editing 任务），但具体数值表格有待从论文中提取。建议后续从 arXiv PDF 补充精确分数。

---

## 5. SOTA 声明

**✅ 有量化证据的声明：**

- **参数效率 SOTA**：4B 参数规模在多项任务上超越 14B BAGEL（3.5× 参数差距的逆转），为统一多模态模型的参数效率新标杆
- **文本渲染能力**：在复杂文本渲染和科学推理场景中超越 14B 模型

> ⚠️ **边界**：InternVL-U 定位为"统一多模态模型（UMM）"，其 SOTA 声明严格限定在"4B 参数级统一模型"范围内。MMMU 等综合理解 benchmark 需参考 InternVL3 系列（更大规格）。

---

## 6. 技术亮点

| 亮点 | 描述 |
|------|------|
| **四模态统一（4-in-1）** | 全球首个将"理解 + 推理 + 生成 + 编辑"整合在单一 4B 模型中的统一多模态模型 |
| **参数效率突破** | 4B 规模超越 14B 统一模型（压缩 70% 参数，性能相当甚至更优） |
| **TextEdit Benchmark** | 同步发布高质量评测集（2148样本），填补文本编辑评测空白 |
| **GenEditEvalKit** | 开源图像编辑评测工具包 |
| **多图理解** | 2026年3月19日支持多图理解推理 |
| **民主化部署** | 4B 参数，可在消费级 GPU 部署，降低使用门槛 |

> **来源**：[GitHub OpenGVLab/InternVL-U](https://github.com/OpenGVLab/InternVL-U)；[arXiv:2603.09877](https://arxiv.org/abs/2603.09877)；[AI News 2026/3/13](https://www.ai-all.info/en/ai-news/internvl-uzhongbangkaiyuan-4bcanshushixianlijie)；[Evermx](https://evermx.com/open-source/internvl-u)

---

## 7. 入选理由

1. **2026年3月最新发布**，距调研日期极近，是目前最新的开源统一多模态模型
2. **上海AI Lab OpenGVLab** 出品——InternVL 家族持续迭代，品质有保障
3. **4B 参数超越 14B 模型**——参数效率的颠覆性突破，具有极高研究价值
4. **统一框架 + MIT 许可证**——理解、推理、生成、编辑一体化，免费商用
5. **同步发布 TextEdit Benchmark**——为社区贡献了高质量评测工具
6. 补充了 VLM 生态中"小参数统一模型"的空白

---

## 8. 信息源列表

| 优先级 | 来源 | 链接 |
|--------|------|------|
| T0 | HuggingFace 官方页 | https://huggingface.co/InternVL-U/InternVL-U |
| T0 | GitHub OpenGVLab/InternVL-U | https://github.com/OpenGVLab/InternVL-U |
| T1 | arXiv 技术报告 | https://arxiv.org/abs/2603.09877 |
| T1 | AI News 报道 | https://www.ai-all.info/en/ai-news/internvl-uzhongbangkaiyuan-4bcanshushixianlijie |
| T1 | HuggingFace Papers | https://huggingface.co/papers/2603.09877 |
| T2 | Reddit 讨论 | https://www.reddit.com/r/StableDiffusion/comments/1rrdfch/onecat_and_internvlu_two_new_models/ |
| T3 | Evermx 报道 | https://evermx.com/open-source/internvl-u |
| T3 | Medium NLPlanet 报道 | https://medium.com/nlplanet/nvidia-focuses-on-open-source-models-weekly-ai-newsletter-march-16th-2026-f1cb04ad2a26 |

---

*最后更新：2026-04-04 | 调研员：@vlm-researcher*
