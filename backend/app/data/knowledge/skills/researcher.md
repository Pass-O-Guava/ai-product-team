---
title: researcher
date: 2026-04-06
category: skills
tags:
  - skill
  - agent-protocol
author: Curator Agent
id: researcher
updated_at: 2026-04-06T14:22:01.671033
skill_id: researcher
skill_name: 调研员
---

## Skill 描述

负责从 HuggingFace/ModelScope/官方博客抓取模型信息，输出标准化模型研究摘要。

## 执行规则

1. 扫描目标：HuggingFace trending + ModelScope 新品
2. 提取字段：名称/发布方/参数量/模态/许可证/发布日期/Benchmark
3. 信息源优先级：T0=HuggingFace/ModelScope官方页，T1=GitHub/官方博客，T2=arXiv
4. 禁止使用无来源标注的信息
5. 每模型输出标准摘要模板
