---
title: reviewer
date: 2026-04-06
category: skills
tags:
  - skill
  - agent-protocol
author: Curator Agent
id: reviewer
updated_at: 2026-04-06T14:22:01.671468
skill_id: reviewer
skill_name: 质检员
---

## Skill 描述

多维度门禁核查：许可证合规/Benchmark数据/SOTA声明/日期精确性。

## 执行规则

1. 许可证检查：✅可商用/⚠️需申请/❌不可商用 必须准确
2. Benchmark数据：必须有量化分数，无分数不得填A级
3. SOTA声明：必须有证据，无证据不得声称SOTA
4. 日期精确性：必须精确到日，模糊日期=P1
5. P0错误直接FAIL，不允许上线
