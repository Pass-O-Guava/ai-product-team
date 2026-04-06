---
title: archiver
date: 2026-04-06
category: skills
tags:
  - skill
  - agent-protocol
author: Curator Agent
id: archiver
updated_at: 2026-04-06T14:22:01.671870
skill_id: archiver
skill_name: 归档员
---

## Skill 描述

将审核通过的模型同步至文档体系，更新 GitHub 仓库。

## 执行规则

1. 写入 knowledge/models/{model_id}.md
2. 更新 knowledge/daily/{date}.md 每日日志
3. Git commit 并推送到 main 分支
4. 推送后更新 manifest 索引
5. 所有文件使用 UTF-8 编码
