# NVIDIA Cosmos Reason 2 — 物理 AI 推理视觉语言模型

> **调研员**: @video-researcher  
> **产出日期**: 2026-04-04  
> **信息源等级**: T0（HuggingFace / NVIDIA 官方）/ T1（GitHub / CES 2026 公告）

---

## 基本信息

| 字段 | 内容 |
|------|------|
| **模型全称** | Cosmos Reason 2 |
| **发布机构** | NVIDIA |
| **发布/发现日期** | 2025-12-19（首批模型发布）/ 2026-01-05（CES 2026 正式公告） |
| **模型类型** | 推理型视觉语言模型（Reasoning VLM），面向物理 AI / 机器人 |
| **参数量级** | 2B / 8B 两个规格 |
| **所在产品线** | NVIDIA Cosmos 系列（物理世界基础模型） |

---

## 许可证

- **许可类型**: NVIDIA Cosmos License（Apache 2.0 style，部分开放）
- ✅ NVIDIA 官方称为"open, customizable"，Apache 2.0 风格开放
- ⚠️ 需查阅 NVIDIA 官方条款确认完整商用授权范围

---

## 链接

| 类型 | 链接 |
|------|------|
| **GitHub** | https://github.com/nvidia-cosmos/cosmos-reason2 |
| **HuggingFace** | https://huggingface.co/nvidia/cosmos-reason2-8B |
| **NVIDIA NIM** | https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard |
| **官方博客** | https://huggingface.co/blog/nvidia/nvidia-cosmos-reason-2-brings-advanced-reasoning |
| **CES 2026 公告** | https://forums.developer.nvidia.com/t/nvidia-cosmos-announcements-at-ces-2026/356629 |
| **Datature 微调教程** | https://datature.com/blog/finetuning-your-own-cosmos-reason2-model |

---

## Benchmark / SOTA 声明（有据可查）

| Benchmark | 成绩 | 来源 | 备注 |
|-----------|------|------|------|
| **Physical AI Leaderboard** | **Top #1** | NVIDIA CES 2026，2026-01-06 | 物理 AI 推理榜单第一 |
| Physical Common Sense | Leaderboard Topping | NVIDIA 博客，2026-01 | 物理常识推理最强 |
| Embodied Reasoning | SOTA | NVIDIA GitHub，2025-12 | 机器人/具身推理 |
| Robomimic / CALVIN | 领先 | NVIDIA 官方，2026-01 | 机器人操作基准 |
| Open-source Physical AI VLM | #1 | HuggingFace NIM，2026-01 | 开源物理 AI VLM 第一 |

> ✅ **SOTA 声明**: NVIDIA CES 2026 官方公告确认"topping the Physical AI leaderboard"；HuggingFace NIM 页面标题即为"leaderboard-topping reasoning VLM"。有官方来源支撑，声明有效。

---

## 技术亮点

1. **Chain-of-Thought 推理**：内置推理 token，逐 token 思考物理交互逻辑，适合机器人规划
2. **物理世界常识理解**：对物体重量、碰撞、运动轨迹、材质等物理属性有强理解能力
3. **双规格开放**：2B（边缘高效部署）+ 8B（最强推理能力）
4. **物理 AI 生态**：专为机器人、具身智能、自动驾驶等物理世界 AI 场景设计
5. **视频时间戳精确感知**：支持事件时间戳精准定位，适合长视频时序推理
6. **微调友好**：Datature 等平台已提供微调教程，支持定制化物理推理场景

---

## 入选理由

1. **官方 SOTA 认证**：NVIDIA 明确声称"Leaderboard-topping"，Physical AI 榜单第一
2. **视频时间推理专长**：时序理解+物理推理双重能力，切中长视频理解重点方向
3. **生态完善**：GitHub / HuggingFace / NIM 多平台同步，Apache 2.0 风格许可证
4. **调研窗口合规**：2025-12-19 发布，距今约 4 个月，在半年窗口内
5. **机器人+视频双赛道**：同时覆盖实时视频分析（机器人视觉）和长视频理解两个重点

---

## 信息源列表

| # | 来源 | 类型 | 可信度 | 链接 |
|---|------|------|--------|------|
| 1 | NVIDIA Cosmos Reason 2 GitHub | T0 | ★★★★★ | https://github.com/nvidia-cosmos/cosmos-reason2 |
| 2 | HuggingFace NIM 模型卡 | T0 | ★★★★★ | https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard |
| 3 | HuggingFace 官方博客 | T0 | ★★★★★ | https://huggingface.co/blog/nvidia/nvidia-cosmos-reason-2-brings-advanced-reasoning |
| 4 | NVIDIA CES 2026 公告 | T1 | ★★★★★ | https://forums.developer.nvidia.com/t/nvidia-cosmos-announcements-at-ces-2026/356629 |
| 5 | NVIDIA 官方文档 | T1 | ★★★★ | https://docs.nvidia.com/cosmos/latest/reason2/index.html |
| 6 | Datature 微调指南 | T2 | ★★★ | https://datature.com/blog/finetuning-your-own-cosmos-reason2-model |
