# SKILL.md — SOTA Model Researcher

> **技能名称：** SOTA Model Researcher  
> **版本：** v1.0  
> **适用任务：** 调研最新 SOTA 开源语言模型，产出标准化 Model Card  
> **调用方：** @coordinator（调度者）  
> **执行者：** @text-researcher（纯语言模型调研员）

---

## 触发条件

当 coordinator 下发以下类型任务时激活本技能：
- "调研 XX 年最新 SOTA 开源模型"
- "调研 XX 月发布的语言模型"
- "产出 Model Card"
- "补充知识体系"

---

## 调研标准

### 时间窗口优先级
1. 最近 1 周
2. 最近 1 个月
3. 最近 1 季度
4. 最近半年
5. 超过半年的 Reasoning 模型有重大突破可例外

### 信息源优先级（T0→T2）

| 等级 | 来源 | 要求 |
|------|------|------|
| **T0** | HuggingFace / ModelScope 官方页面 | 必须有，至少 1 个 |
| **T1** | 官方 GitHub / 官方博客 | 必须有，至少 1 个 |
| **T2** | arXiv / 官方 Leaderboard | 至少有 |
| **T3** | 科技媒体（TechCrunch/VentureBeat等）| 可选，辅助 |
| **禁止** | 无来源信息 | 不收录 |

### 收录门槛
- 必须有明确的**发布时间**（精确到日）
- 必须有至少 T0 或 T1 来源
- 无数据不得写 SOTA 声明

---

## Model Card 模板

每个模型输出一个 `.md` 文件，保存至：
`/workspace/team/projects/sota-model-hub/models/text/{model-name}.md`

内容必须包含：

```markdown
# Model Card: {模型名}

## 基本信息
- 模型全名 / 开发方 / 发布时间 / 许可证

## 链接
- HuggingFace / GitHub / 官方博客（按 T0→T2 排列）

## Benchmark 成绩
- 表格：Benchmark | 分数 | 备注
- 标注数据来源

## SOTA 声明（有据可查）
- 每条 claim 标注来源和可靠度星级

## 技术亮点
- 3~5 条技术特色

## 入选理由
- 为什么收录

## 信息源列表（按 T0/T1/T2 分类）
- 标注 ✅（已确认）/ ⚠️（待核实）

## 待补充
- 已知数据缺口
```

---

## 调研流程

### 第一步：批量搜索（batch_web_search）

按优先级搜索：
```
1. 最近1周："{model-name} release date 2026"
2. 最近1月："{model-name} benchmark open source"
3. 趋势搜索："open source LLM leaderboard {month} 2026"
```

每批最多 10 个查询，分批执行。

### 第二步：提取官方页面（extract_content_from_websites）

对 T0/T1 来源批量提取：
- HuggingFace 模型页面（benchmark 数据）
- GitHub README（技术细节）
- 官方博客（发布公告）

### 第三步：交叉验证

- Benchmark 数据至少 2 个独立来源
- 发布信息与官方页面交叉核对
- 许可证信息以官方 License 文件为准

### 第四步：撰写 Model Card

按模板产出，每条 claim 严格对应来源。

---

## 每日沉淀要求

每次调研任务完成后，**必须**额外产出：

### 1. 知识体系文件
路径：`/workspace/team/projects/sota-model-hub/knowledge/text-{date}.md`

内容：
- 横向对比表（Benchmark 对比、架构对比）
- 洞察分析（3~5 条）
- 推荐选型指南
- 数据质量说明

### 2. Demo 代码（可选，视任务规模）

路径：`/workspace/team/projects/sota-model-hub/demos/`

每个重要模型配套：
- `inference_{model-name}.py`（推理 Demo）
- `requirements.txt`

---

## 可靠度评级规则

| 评级 | 含义 | 标准 |
|------|------|------|
| A | 高可靠 | T0 官方页面 + 至少 1 个 T1/T2 交叉验证 |
| B | 中可靠 | 有 T0 或 T1，数值需核实 |
| C | 低可靠 | 仅 T3 来源，无官方确认 |

---

## 禁止事项

1. ❌ 无来源信息写入 Model Card
2. ❌ 日期模糊（"最近"、"近期"不可接受，必须精确到日）
3. ❌ 将"传闻"作为 SOTA 声明
4. ❌ 合并不同模型为一个卡片
5. ❌ 跳过调研直接用历史数据

---

## 汇报格式

调研完成后向 coordinator 报告：

```
共调研了 N 个模型，名单：
1. {模型名} — {发布时间} — {一句话定位}
2. ...
```

同时告知：
- 哪些模型数据不完整（需后续跟进）
- 哪些模型开源状态存疑（需额外核实）
