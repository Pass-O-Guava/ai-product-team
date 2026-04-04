# 知识体系：2026年最新多模态统一模型横向对比洞察

> **调研日期：** 2026-04-04  
> **调研员：** @unified-researcher  
> **时间窗口：** 2026-01 至 2026-04-04

---

## 一、调研总览

本次调研共确认收录 **4 个模型**，均满足 2026 年 1 月至今 + 多模态统一模型双重条件。

| # | 模型 | 机构 | 发布日期 | 开源 | 类型定位 |
|---|------|------|----------|------|----------|
| 1 | **Qwen3.5-Omni** | Alibaba Qwen | 2026-03-30 | ❌ Proprietary | 端到端全模态（Any→Text+Audio） |
| 2 | **NEO-unify** | SenseTime SenseNova | 2026-03-06 | ✅ Apache 2.0 | 原生多模态统一（Encoder-Free + MoT） |
| 3 | **SenseNova-MARS** | SenseTime OpenSenseNova | 2026-01-30 | ✅ 开源 | 多模态 Agentic 推理搜索 |
| 4 | **Qwen3.5** | Alibaba Qwen | 2026-02-16 | ⚠️ 混合（MoE闭源/中版开源） | Native Multimodal Agent |

---

## 二、横向对比维度

### 2.1 模态覆盖范围

```
模型                    | Text | Image | Audio | Video | Gen
-----------------------|------|-------|-------|-------|----
Qwen3.5-Omni          |  ✅  |   ✅   |   ✅  |   ✅  | Audio(语音克隆)
NEO-unify             |  ✅  |   ✅   |   —   |   ✅  | Image
SenseNova-MARS        |  ✅  |   ✅   |   —   |   ✅  | —
Qwen3.5 (MoE/VLM)     |  ✅  |   ✅   |   —   |   ✅  | —
```

**洞察：**
- Qwen3.5-Omni 是本次调研中模态覆盖最全面的模型（唯一同时支持 Audio 输入/输出）
- NEO-unify 在「生成」维度有独特价值（Text+Image 双输出，原生统一生成）
- SenseNova-MARS 和 Qwen3.5 不做生成，专注理解和 Agent 推理

### 2.2 架构路线对比

| 路线 | 代表模型 | 核心思想 | 优缺点 |
|------|----------|----------|--------|
| **Thinker-Talker 双模块** | Qwen3.5-Omni | 理解与生成解耦，Talker 独立流式生成语音 | 延迟低、语音质量高；但仍是两模块协同 |
| **Encoder-Free 原生融合** | NEO-unify | 去掉独立视觉编码器，近无损视觉接口 + MoT | 架构创新强，但生成质量待验证 |
| **Hybrid Transformer-Mamba** | SenseNova-MARS | SSM 高效推理 + Transformer 表达力 | 适合长序列 Agent 任务 |
| **Early Fusion MoE** | Qwen3.5-397B | 预训练阶段即文本视觉 token 联合 | 高效率，但大模型推理成本高 |

**洞察：**
- 2026 年多模态统一模型正从「拼接式」向「原生融合」演进
- MoT（Mixture-of-Transformer）和 SSM（状态空间模型）正在融入多模态架构
- Encoder-Free 是最激进的路线，代表感知-理解一体化新范式

### 2.3 开源策略对比

| 模型 | 开源程度 | 权重可用 | 许可证 |
|------|----------|----------|--------|
| Qwen3.5-Omni | ❌ 不开源 | ❌ 仅 API | Proprietary |
| NEO-unify | ✅ 开源 | ✅ 可下载 | Apache 2.0 |
| SenseNova-MARS | ✅ 开源 | ✅ 8B/32B | 开源（GitHub） |
| Qwen3.5 | ⚠️ 混合 | ✅ 中小规格 | Apache 2.0 / Proprietary |

**洞察：**
- 国内大厂（阿里、商汤）均采用「旗舰闭源 + 中小开源」的双轨策略
- 商汤是本次调研中开源最彻底的厂商，GitHub + arXiv 完整开源

### 2.4 Benchmark 策略对比

| 模型 | SOTA 声称量 | Benchmark 来源 | 可验证性 |
|------|------------|----------------|----------|
| Qwen3.5-Omni | 215 项 SOTA | 官方自测 | T1，需对照表格 |
| NEO-unify | 多项超越基线 | 官方博客 | T1，缺具体数值 |
| SenseNova-MARS | 开源搜索/图像理解 SOTA | 官方 + OpenReview | T1，需核论文 |
| Qwen3.5-397B | 超越 Qwen3-VL | 官方 + HF 博客 | T1，需 HF 博客全文 |

**洞察：**
- 所有模型的 SOTA 数字均来自官方声称，无独立第三方验证
- 「215 SOTA」是最激进的数字，但 Reddit 社区已指出存在选择性对比基准问题
- 建议：Model Card 中不直接引用未经核验的 SOTA 数字，改为「官方声称」

---

## 三、核心趋势洞察

### 3.1 三大技术方向

1. **原生融合（Native Fusion）**：从「视觉编码器 + LLM 拼接」进化到单一模型原生处理所有模态，NEO-unify 和 Qwen3.5 是代表
2. **全模态流式交互**：输入全模态 + 流式语音输出，Thinker-Talker 架构使端到端语音交互延迟大幅降低
3. **多模态 Agent**：从「理解」扩展到「推理+规划+工具调用」，SenseNova-MARS 是开源领域标杆

### 3.2 市场格局

```
闭源旗舰（API-only）：
  - Qwen3.5-Omni（阿里）
  - Qwen3.5-397B（阿里）
  
开源可本地部署：
  - NEO-unify 2B（商汤）
  - SenseNova-MARS 8B/32B（商汤）
  - Qwen3.5-35B/27B（阿里）
  
视觉语言专项：
  - Qwen3-VL（阿里，已整合入 Qwen3.5 系列）
```

### 3.3 关键差距

| 维度 | 当前最强（闭源） | 开源最强 | 差距 |
|------|----------------|----------|------|
| 全模态覆盖 | Qwen3.5-Omni | NEO-unify（缺 Audio） | 音频生成仍是开源短板 |
| 全模态生成 | Qwen3.5-Omni | NEO-unify（Image Gen） | 视频/音频生成开源空白 |
| Agentic 能力 | Qwen3.5-Omni | SenseNova-MARS | 工具调用框架开源接近 |
| 端侧部署 | — | SenseNova-MARS 8B | 中小规格开源已覆盖 |

---

## 四、调研方法论反思

### 4.1 信息源优先级验证

| 信息源类型 | 实际占比 | 问题 |
|-----------|---------|------|
| T0（HuggingFace/ModelScope 官方） | ~30% | Qwen3.5-Omni 无开放权重，HuggingFace 无模型页 |
| T1（官方 GitHub / 博客 / 新闻） | ~60% | 大部分信息来自博客摘要，缺少完整技术报告 |
| T2（arXiv / 第三方评测） | ~10% | 仅 SenseNova-MARS 有完整 arXiv 论文 |

**教训：** 「215 SOTA」等数字依赖官方博客，需要通过 arXiv 技术报告或第三方评测进行交叉验证。

### 4.2 时间窗口遵守情况

- ✅ 2026-01-30：SenseNova-MARS（开源）
- ✅ 2026-02-16：Qwen3.5（首批）
- ✅ 2026-03-06：NEO-unify
- ✅ 2026-03-30：Qwen3.5-Omni
- ❌ 未收录：Qwen3.5-VL/Qwen3-VL（无明确发布日期，需补充）

### 4.3 未收录但值得关注

| 模型 | 机构 | 备注 |
|------|------|------|
| GLM-5 / GLM-5V-Turbo | Zhipu AI (Z.ai) | 2026-02-11 发布，VLM 能力待核实 |
| MiniMax M2.5 / M2.7 | MiniMax | 主要是文本模型，多模态能力有限 |
| Gemini 3.1 Pro | Google | 2026-02-19 发布，但非 any-to-any 全模态 |

---

## 五、下一步调研建议

1. **GLM-5V 系列核实**：Z.ai 2026-04-01 刚发布 GLM-5V-Turbo，需补充调研
2. **Benchmark 数值核验**：联系 arXiv 原文，提取具体分数填入 Model Card
3. **Qwen3-VL 补录**：Qwen3-VL Embedding (2026-01-08) 和 Qwen3.5-VL 归属关系需梳理
4. **Qwen3.5-Omni 权重核实**：确认为 Proprietary，Model Card 需更新许可证字段

---

## 六、输出清单

- [x] Model Card: Qwen3.5-Omni ✅
- [x] Model Card: NEO-unify ✅
- [x] Model Card: SenseNova-MARS ✅
- [x] Model Card: Qwen3.5 ✅
- [x] 知识体系：本文件 ✅
- [ ] Skill 固化 → `/workspace/team/skills/sota-model-surveyor/SKILL.md`
- [ ] Demo 代码 → `/workspace/team/projects/sota-model-hub/demos/`
