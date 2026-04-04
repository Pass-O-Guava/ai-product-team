# SKILL.md — VLM Research Agent Skill

> 用于 @vlm-researcher 子智能体执行 VLM 调研任务的标准化工作流。

## 触发条件

当收到以下任务时，自动加载本 Skill：
- "调研 VLM" / "调研视觉语言模型"
- "写 Model Card" / "产出 Model Card"
- "调研最新 VLM" / "更新 VLM 模型库"
- "SOTA VLM 调研" / "最新开源 VLM"

## 工作流程

### Step 1：信息源优先级

| 优先级 | 来源 | 要求 |
|--------|------|------|
| T0（必须） | HuggingFace 官方页 + ModelScope 官方页 | 无 T0 数据不得声称"已确认" |
| T1（优先） | 官方 GitHub / 官方博客 | 有则补充 |
| T2（参考） | arXiv 论文 / 官方 Leaderboard | 数据引用标注来源 |
| T3（补充） | 权威媒体（有来源标注） | 不得作为唯一数据来源 |

### Step 2：时间窗口

检索顺序：最近1周 → 1个月 → 1季度 → 半年

### Step 3：Model Card 产出

路径：`/workspace/team/projects/sota-model-hub/models/vision/{model-name}.md`

必须包含：基本信息 / 许可证与商用合规 / HuggingFace+ModelScope链接 / Benchmark数据 / SOTA声明（有证据）/ 技术亮点 / 入选理由 / 信息源列表

### Step 4：额外交付物（每日强制）

1. 横向对比洞察：`/workspace/team/projects/sota-model-hub/knowledge/vlm-{date}.md`
2. Skill 沉淀：`/workspace/team/skills/vlm-researcher-skill/SKILL.md`
3. Demo 代码：`/workspace/team/projects/sota-model-hub/demos/{model-name}.py`

### Step 5：报告格式

完成调研后回复：
```
共调研了 N 个模型：
1. {模型名} — {发布日期} — {一句话定位}
...
```

## 数据质量控制

- 无来源标注的数据不得使用
- 无具体分数不得声称 SOTA
- 日期必须精确到日（无则标注待确认）
- SOTA 声明必须附量化证据，标注适用范围

## Demo 代码规范

每个 Demo 必须：
1. 可直接运行（依赖 pip install 明确标注）
2. 包含模型下载 + 推理完整流程
3. 附输入输出示例
4. 标注最低硬件要求（显存）
5. 提供 HuggingFace Transformers 调用方式

## Skill 版本

| 版本 | 日期 | 内容 |
|------|------|------|
| 1.0.0 | 2026-04-04 | 初始版本：Qwen3-VL / Phi-4-vision / InternVL-U / Gemma 4 |
