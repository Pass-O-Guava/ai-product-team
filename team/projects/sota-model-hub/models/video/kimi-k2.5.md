# Kimi K2.5 — Native Multimodal MoE 开源模型

> **调研员**: @video-researcher  
> **产出日期**: 2026-04-04  
> **信息源等级**: T0（HuggingFace 官方模型页）/ T1（NIM 官方 / 官方 GitHub）

---

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型全称** | Kimi K2.5 |
| **发布机构** | Moonshot AI（月之暗面） |
| **发布/发现日期** | 2026-01-27（正式宣布开源） |
| **模型类型** | 原生多模态 Mixture-of-Experts（MoE）大语言模型 |
| **参数量级** | 总参数量 ~1T，激活参数 32B |
| **所在产品线** | Kimi 系列 / K 系列 |

---

## 许可证

- **许可类型**: MIT License（宽松开源许可证）
- ✅ 明确可商用，HuggingFace 模型卡标注 "MIT"，社区广泛确认

---

## 链接

| 类型 | 链接 |
|------|------|
| **HuggingFace 主页** | https://huggingface.co/moonshotai/Kimi-K2.5 |
| **NVIDIA NIM 模型卡** | https://build.nvidia.com/moonshotai/kimi-k2.5/modelcard |
| **GitHub（Kimi-VL）** | https://github.com/MoonshotAI/Kimi-VL |
| **Kimi 官方博客** | https://www.kimi.com/en |
| **Codecademy 评测** | https://www.codecademy.com/article/kimi-k-2-5-complete-guide |
| **arXiv（Kimi-VL 技术报告）** | https://arxiv.org/abs/2502.xxxxx（需核实） |

---

## Benchmark / SOTA 声明（有据可查）

| Benchmark | 成绩 | 来源 | 备注 |
|-----------|------|------|------|
| **Video-MMMU** | **86.6%** | Codecademy / NIM，2026-01 | 视频多模态理解权威榜单 |
| 视频时间推理（Temporal Reasoning） | 领先 | HuggingFace 模型卡 | 跨帧时序信息处理 |
| Visual Coding（视觉编码） | 最强开源 | Kimi 官方，2026-01 | Open-source strongest model |
| 多模态 Agentic | 领先 | HuggingFace，2026-01 | 视觉 Agent 任务表现突出 |
| Video Understanding | SOTA 级别 | 多个评测，2026-01 | VideoMMMU 86.6% 为开源最高 |

> ✅ **SOTA 声明**: HuggingFace 模型卡明确标注"最强开源视觉编码模型"（Strongest open-source model for visual coding）；NIM 页面确认视频多模态 86.6% Video-MMMU 成绩，在开源模型中处于顶尖水平。

---

## 技术亮点

1. **原生多模态架构**：通过 ~15T 混合视觉+文本 token 连续预训练实现，无需 adapter 拼接
2. **MoE 高效架构**：总参数量 1T / 激活 32B，推理成本远低于同等性能 Dense 模型
3. **超长上下文**：Kimi-VL 变体支持 128K+ token 上下文（含视频帧）
4. **视频理解专项优化**：跨帧时序建模，支持长视频理解与事件精确定位
5. **视觉 Agent 能力**：内建 Agentic 规划能力，适合 GUI 自动化与多步推理任务
6. **NVIDIA NIM 快速部署**：官方 NIM 镜像支持，推理优化开箱即用

---

## 入选理由

1. **视频理解实测顶尖**：Video-MMMU 86.6%，开源模型中视频理解能力第一梯队
2. **发布于调研核心窗口**：2026-01-27 正好在 Q1 发布高峰期
3. **MIT 许可证**：完全宽松开源，商用友好，是本次调研中许可证最友好的大模型之一
4. **多模态+Agent 双能力**：同时覆盖视频理解与视觉 Agent 两个重点方向
5. **生态快速跟进**：HuggingFace / vLLM / NIM 多平台同步支持

---

## 信息源列表

| # | 来源 | 类型 | 可信度 | 链接 |
|---|------|------|--------|------|
| 1 | HuggingFace Kimi K2.5 模型卡 | T0 | ★★★★★ | https://huggingface.co/moonshotai/Kimi-K2.5 |
| 2 | NVIDIA NIM Kimi K2.5 | T0 | ★★★★★ | https://build.nvidia.com/moonshotai/kimi-k2.5/modelcard |
| 3 | Codecademy Kimi K2.5 完整指南 | T1 | ★★★★ | https://www.codecademy.com/article/kimi-k-2-5-complete-guide |
| 4 | Moonshot AI 官方公告 | T1 | ★★★★★ | https://pandaily.com/kimi-open-sources-k2-5-model |
| 5 | Kimi-VL GitHub | T1 | ★★★★ | https://github.com/MoonshotAI/Kimi-VL |
| 6 | Forbes 报道 | T2 | ★★★★ | https://www.forbes.com/sites/janakirammsv/ |
