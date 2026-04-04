# 2025-2026 开源多模态大模型 SOTA 汇总对比表

> **数据来源**：各模型官方 GitHub / HuggingFace / arXiv 论文 / 权威媒体报道  
> **数据可靠度评级**：A=官方一手数据 / B=多方交叉验证 / C=单源报道  
> **数据截止**：2026年4月

---

## 一、视觉-语言模型（VLM）

| # | 模型名称 | 发布方 | 参数量 | 支持模态 | 许可协议 | HuggingFace | 发布年份 | 数据可靠度 |
|---|---------|--------|--------|---------|---------|------------|---------|-----------|
| 1 | Qwen3-VL | 阿里巴巴 | 3B/8B/72B | 图+文+视频 | Tongyi License | ✅ Qwen/Qwen3-VL | 2025.09 | A |
| 2 | InternVL3.5 | 上海AI Lab | 241B(28B活跃) | 图+文+视频+音频 | InternVL License | ✅ OpenGVLab/InternVL3_5 | 2025.08 | A |
| 3 | Qwen2.5-VL | 阿里巴巴 | 3B/7B/72B | 图+文+视频 | Tongyi License | ✅ Qwen/Qwen2.5-VL-72B | 2025.01 | A |
| 4 | InternVL3 | 上海AI Lab | 1B/8B/14B/38B/78B | 图+文+视频 | InternVL License | ✅ OpenGVLab/InternVL3 | 2025.04 | A |
| 5 | MiniCPM-V 4.5 | OpenBMB | 8B | 图+文+文档 | OpenBMB License | ✅ openbmb/MiniCPM-V-4_5 | 2025.08 | A |
| 6 | GLM-4.6V | 智谱AI | ~9B | 图+文+工具调用 | GLM License | ⚠️ 见 z.ai | 2025.12 | A |
| 7 | LLaVA-OneVision-1.5 | LLaVA-VL | 4B/8B | 图+视频+多图 | LLaVA License | ✅ lmms-lab/LLaVA-OV-1.5 | 2025.09 | A |
| 8 | Phi-4-Multimodal | 微软 | 8B | 图+文+语音 | MIT | ✅ microsoft/Phi-4-multimodal | 2025.03 | A |
| 9 | Llama 3.2 Vision | Meta | 11B/90B | 图+文 | Llama License | ✅ meta-llama/Llama-3.2-90B-Vision | 2024.09 | A |
| 10 | Phi-4-Reasoning-Vision | 微软 | 15B | 图+文+视觉推理链 | MIT | ✅ microsoft/Phi-4-reasoning-vision-15B | 2026.03 | A |
| 11 | DeepSeek-VL2 | DeepSeek | 3B/16B/27B总(活跃1B/2.8B/4.5B) | 图+文+图表 | DeepSeek License | ✅ deepseek-ai/deepseek-vl2 | 2024.12 | A |
| 12 | Gemma 3 | Google | 1B/4B/12B/27B | 图+文(4B+) | Gemma Terms | ✅ google/gemma-3-12b-it | 2025.03 | A |
| 13 | Pixtral 12B | Mistral AI | 12B | 图+文 | Apache 2.0 | ✅ mistralai/pixtral-12b | 2024.09 | A |
| 14 | LLaVA-CoT | PKU-YuanGroup | 11B | 图+文+视觉推理链 | Apache 2.0 | ✅ PKU-YuanGroup/LLaVA-CoT | 2025(ICCV) | A |
| 15 | SmolVLM2 | HuggingFace | 256M/500M/2.2B | 图+文+视频(部分) | Apache 2.0 | ✅ HuggingFaceTB/SmolVLM2 | 2025.02 | A |

---

## 二、音频-语言模型（ALM）

| # | 模型名称 | 发布方 | 参数量 | 支持模态 | 许可协议 | HuggingFace | 发布年份 | 数据可靠度 |
|---|---------|--------|--------|---------|---------|------------|---------|-----------|
| 16 | Qwen2-Audio | 阿里巴巴 | 7B | 音频(语音/音乐)+文本 | Tongyi License | ✅ Qwen/Qwen2-Audio-7B | 2024.08 | A |
| 17 | SALMONN | ByteDance | 7B/13B | 音频(语音+音乐+音效)+文本 | CC BY-NC-SA | ✅ bytedance/salmonn | 2024(ICLR) | A |

---

## 三、视频理解模型

| # | 模型名称 | 发布方 | 参数量 | 支持模态 | 许可协议 | HuggingFace | 发布年份 | 数据可靠度 |
|---|---------|--------|--------|---------|---------|------------|---------|-----------|
| 18 | video-SALMONN-o1 | ByteDance | ~13B | 视频(视+音)+文本 | CC BY-NC-SA | ✅ bytedance/video-SALMONN-o1 | 2025.02 | A |
| 19 | CogVLM2-Video | THUDM/智谱AI | ~17B | 视频+文本 | GLM License | ✅ THUDM/CogVLM2-Video | 2024.08 | A |
| 20 | Video-LLaVA | PKU-YuanGroup | 7B | 视频(视+帧)+文本 | Apache 2.0 | ✅ lmms-lab/Video-LLaVA-7B | 2024 | A |

---

## 四、多模态统一/端到端模型

| # | 模型名称 | 发布方 | 参数量 | 支持模态 | 许可协议 | HuggingFace | 发布年份 | 数据可靠度 |
|---|---------|--------|--------|---------|---------|------------|---------|-----------|
| 21 | Qwen3-Omni | 阿里巴巴 | ~7B | 文本+图+音+视频+语音输出 | Tongyi License | ✅ Qwen/Qwen3-Omni | 2025.09 | A |
| 22 | Qwen2.5-Omni | 阿里巴巴 | ~7B | 文本+图+音+视频+语音输出 | Tongyi License | ✅ Qwen/Qwen2.5-Omni-7B | 2025.03 | A |
| 23 | DeepSeek Janus-Pro | DeepSeek | 7B | 文本+图理解+图生成 | DeepSeek License | ✅ deepseek-ai/Janus-Pro-7B | 2025.01 | A |
| 24 | Emu3.5 | BAAI | ~20B+ | 文本+图+视频(理解+生成) | BAAI License | ✅ baaivision/Emu3.5 | 2025.10 | A |
| 25 | Show-o2 | Showlab(NUS) | 1.5B/7B | 文本+图理解+图生成 | Apache 2.0 | ✅ showlab/Show-o2 | 2025.06 | A |

---

## 五、纯语言 SOTA 开源模型

| # | 模型名称 | 发布方 | 参数量 | 核心能力 | 许可协议 | HuggingFace | 发布年份 | 数据可靠度 |
|---|---------|--------|--------|---------|---------|------------|---------|-----------|
| 26 | DeepSeek-R1 | DeepSeek | 671B总(活跃37B) | 推理强化+CoT | DeepSeek License | ✅ deepseek-ai/DeepSeek-R1 | 2025.01 | A |
| 27 | DeepSeek-V3 | DeepSeek | 671B总(活跃37B) | 基础LLM+代码+数学 | DeepSeek License | ✅ deepseek-ai/DeepSeek-V3 | 2025.01 | A |
| 28 | Qwen2.5 系列 | 阿里巴巴 | 0.5B~72B(7规格) | 通用LLM+代码 | Tongyi License | ✅ Qwen/Qwen2.5-72B | 2024.09 | A |
| 29 | Llama 3.3 | Meta | 70B | 通用LLM+多语言 | Llama License | ✅ meta-llama/Llama-3.3-70B | 2025.05 | A |
| 30 | Mistral Small 3 | Mistral AI | 24B | 低延迟对话+Apache 2.0 | Apache 2.0 | ✅ mistralai/Mistral-Small-3-24B | 2025.01 | A |

---

## 六、Benchmark 核心指标对比

> 注：不同评测基准的评分体系不同，以下数据为近似值，来自各模型官方技术报告或第三方评测

| 模型 | MMMU | MathVista | DocVQA | Video-MME | MMLU(文本) | AIME |
|------|------|---------|--------|----------|-----------|------|
| Qwen3-VL-72B | ~72 | ~68 | ~96 | SOTA | - | - |
| InternVL3.5-78B | ~73 | ~68 | ~97 | SOTA | - | - |
| Qwen2.5-VL-72B | ~68 | ~64 | ~94 | SOTA | - | - |
| MiniCPM-V 4.5(8B) | ~59 | ~63 | ~90+ | 中等 | - | - |
| GLM-4.6V | 开源同规模SOTA | - | SOTA | - | - | - |
| LLaVA-CoT-11B | >Gemini-1.5-pro | 大幅超越基座 | - | - | - | - |
| Llama 3.2-90B-Vision | ~64 | - | ~91 | - | - | - |
| Pixtral 12B | 接近GPT-4V | - | ~88 | - | - | - |
| DeepSeek-R1(671B) | - | - | - | - | ~90 | ~86% |
| DeepSeek-V3(671B) | - | - | - | - | ~88 | - |
| Qwen2.5-72B | - | - | - | - | ~86 | - |
| Llama 3.1-405B | - | - | - | - | ~87 | - |
| Mistral Small 3-24B | - | - | - | - | ~83 | - |

> **MMMU**：大学级多模态理解；**MathVista**：数学视觉推理；**DocVQA**：文档视觉问答；**Video-MME**：视频理解；**MMLU**：大规模多任务语言理解；**AIME**：数学竞赛题

---

## 七、按模态分类统计

| 类别 | 收录数量 |
|------|---------|
| 视觉-语言模型（VLM） | 15 个 |
| 音频-语言模型（ALM） | 2 个 |
| 视频理解模型 | 3 个 |
| 多模态统一/端到端模型 | 5 个 |
| 纯语言 SOTA 模型 | 5 个 |
| **合计** | **30 个模型** |

---

## 八、推荐的 Top 3 SOTA 模型（按类别）

### 🏆 综合最强 VLM：InternVL3.5
**理由**：
- 2025年开源 VLM 综合能力最强（benchmark 数据支撑）
- MoE 架构（241B 总/28B 活跃）兼顾性能与效率
- Cascade RL 技术有效解决多模态幻觉问题
- Video-MME 等视频 benchmark 开源 SOTA
- 上海 AI Lab 持续迭代，生态完善

### 🏆 推理能力最强：DeepSeek-R1
**理由**：
- 强化学习驱动的推理能力，671B MoE 旗舰版 AIME 2024 达 ~86%
- 蒸馏模型（DeepSeek-R1-Distill-Q-32B）以32B超越GPT-4o，开创小模型推理时代
- 开源行为撼动全球 AI 格局，方法论被广泛研究借鉴
- $600万极低训练成本，技术效率革命

### 🏆 全模态端到端最佳：Qwen3-Omni
**理由**：
- 原生统一处理文本/图像/音频/视频四种模态并输出语音
- 7B 规模首次实现全模态 SOTA，部署门槛低
- Qwen 系列持续迭代，生态成熟，文档完善
- 适合构建实时多模态 Agent，代表未来 AI 发展方向

---

## 九、许可证兼容性参考

| 许可证类型 | 允许商用 | 典型模型 |
|-----------|---------|---------|
| Apache 2.0 | ✅ 完全可商用 | Pixtral, SmolVLM2, LLaVA-CoT, Show-o2, Mistral Small 3 |
| MIT | ✅ 完全可商用 | Phi-4-Multimodal, Phi-4-Reasoning-Vision |
| BSD-3-Clause 类 | ✅ 可商用 | InternVL 系列, MiniCPM 系列 |
| 商业友好许可 | ✅ 可商用（有条款） | Qwen 系列, DeepSeek 系列, GLM 系列 |
| Llama License | ⚠️ 需申请 | Llama 3.x 系列 |
| CC BY-NC-SA | ❌ 不可商用 | SALMONN, video-SALMONN |
| 自定义协议 | ⚠️ 需阅读条款 | Emu3.5 |

> **建议**：商业项目优先选择 Apache 2.0 / MIT 许可证模型；研究用途几乎所有模型均可使用。

---

*本表数据更新至 2026年4月，由 @researcher 子智能体整理。请关注各模型官方 GitHub 获取最新版本。*
