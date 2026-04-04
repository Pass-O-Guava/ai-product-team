# Model Card: Qwen3.5

> **模型名称：** Qwen3.5（系列）  
> **发布机构：** Alibaba Cloud / Qwen Team  
> **发布日期：** 2026-02-16（首批）；2026-03-09（扩展）  
> **可靠度评级：** T1（官方 GitHub + HuggingFace + 官方博客，多源印证）

---

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型类型** | Native Multimodal Agent（大系列，含纯文本 + VLM 多规格） |
| **支持输入模态（VLM 版）** | 文本、图像、视频（Qwen3.5-VL 版本） |
| **支持输出模态** | 文本 |
| **系列规格** | Qwen3.5-397B-A17B（MoE，400B 总参，22B 激活）、Qwen3.5-35B-A3B、Qwen3.5-27B、Qwen3.5-0.8B 等 |
| **架构** | MoE（Qwen3.5-397B）/ Dense（中小规格）；原生 Early Fusion 多模态训练 |
| **上下文窗口** | 128K（部分版本）~ 256K（待确认） |
| **核心定位** | "Native Multimodal Agent"——面向 Agent 工程、长程任务、复杂代码 |

---

## 许可证

多版本：
- Qwen3.5-397B-A17B：**Proprietary**（闭源，仅 API 访问）
- Qwen3.5-35B-A3B、Qwen3.5-27B：**Apache 2.0**（开源权重，HuggingFace 可下载）

---

## 链接

| 类型 | 链接 |
|------|------|
| **官方博客** | https://qwen.ai/blog?id=qwen3.5 |
| **官方 GitHub** | https://github.com/QwenLM/Qwen3.5 |
| **HuggingFace 系列页** | https://huggingface.co/collections/Qwen/qwen35 |
| **ModelScope 397B** | https://www.modelscope.ai/models/Qwen/Qwen3.5-397B-A17B |
| **NVIDIA 开发者博客** | https://developer.nvidia.com/blog/develop-native-multimodal-agents-with-qwen3-5-vlm-using-nvidia-gpu-accelerated-endpoints/ |
| **评测报道** | https://medium.com/data-science-in-your-pocket/qwen-3-5-explained-architecture-upgrades-over-qwen-3-benchmarks-and-real-world-use-cases-af38b01e9888 |
| **Qwen3-VL GitHub** | https://github.com/QwenLM/Qwen3-VL |

---

## Benchmark

| 评测集 | Qwen3.5-397B-A17B 成绩 | 说明 |
|--------|------------------------|------|
| MMLU | 竞争性表现 | 超越 Qwen3-235B-A22B（官方）|
| MMMU | 竞争性表现 | 超越 Qwen3-VL（官方）|
| 编程 benchmark | 领先（Agentic Coding） | 涵盖前端开发、仓库级问题解决 |
| **vs Qwen3-VL** | 全面超越 | 多模态评测集 |
| **vs GPT-5（部分指标）** | 部分胜出 | 官方声称 |

> ⚠️ 注：具体分数需查阅 Qwen 官方技术报告；HuggingFace 博客（2026-02-17）中有 Qwen3.5-397B-A17B 详细评测。

---

## SOTA 声明

- ⚠️ **部分有据 SOTA：** 官方声称 Qwen3.5-397B 在编程、Agentic 任务、MMMU 等超越 Qwen3-VL；多规格对比数据需对照 HF 官方博客
- ✅ **多规格开源**（35B/27B 等）：Apache 2.0，具体 Benchmark 对比在 HF 页面有列表

---

## 技术亮点

1. **Native Multimodal Agent 定位**：非后期拼接，而是从预训练阶段即实现 Early Fusion（早期融合），文本与视觉 token 联合训练
2. **MoE 高效激活**：397B 总参 / 22B 激活参数，以低成本实现接近 Dense-400B 级性能
3. **Agentic Coding 专项强化**：从前端 Web 开发到仓库级复杂代码理解全面增强
4. **全系列开源**：从 0.8B 到 397B 完整覆盖，Apache 2.0 许可（中小规格）
5. **VLM 版本独立发布**：Qwen3.5-VL（视觉语言）通过 Qwen3-VL 系列页单独管理

---

## 入选理由

Qwen3.5 是 2026 年 2 月发布的最大规模多模态开源/可访问模型系列，MoE 架构 + Early Fusion 多模态训练使其成为原生多模态 Agent 的标杆，其中开源中小规格（35B/27B）提供了可直接本地部署的高质量多模态选项。

---

## 信息源列表

| # | 类型 | 来源 | 链接 | 评级 |
|---|------|------|------|------|
| 1 | 官方博客 | Qwen.ai | https://qwen.ai/blog?id=qwen3.5 | T0 |
| 2 | 官方 GitHub | QwenLM | https://github.com/QwenLM/Qwen3.5 | T0 |
| 3 | HuggingFace 博客 | HuggingFace (mlabonne) | https://huggingface.co/blog/mlabonne/qwen35 | T1 |
| 4 | NVIDIA 开发者博客 | NVIDIA | https://developer.nvidia.com/blog/develop-native-multimodal-agents-with-qwen3-5-vlm/ | T1 |
| 5 | ModelScope | ModelScope | https://www.modelscope.ai/models/Qwen/Qwen3.5-397B-A17B | T0 |
| 6 | 技术评测 | Medium | https://medium.com/data-science-in-your-pocket/qwen-3-5-explained-architecture-upgrades-over-qwen-3-benchmarks-and-real-world-use-cases-af38b01e9888 | T1 |
