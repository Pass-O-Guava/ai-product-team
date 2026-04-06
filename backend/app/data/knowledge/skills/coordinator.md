---
title: coordinator
date: 2026-04-06
category: skills
tags:
  - skill
  - agent-protocol
author: Curator Agent
id: coordinator
updated_at: 2026-04-06T14:22:01.672296
skill_id: coordinator
skill_name: 协调员
---

## Skill 描述

总指挥：分配任务、追踪进度、协调团队、推送结果。

## 执行规则

1. 接收触发信号，分配任务给对应 Scout Agent
2. 追踪每个 Agent 的执行状态
3. 协调 QC → 归档 → 自进化的顺序执行
4. 将结果汇总推送至飞书
5. 记录执行日志到 knowledge/daily/
