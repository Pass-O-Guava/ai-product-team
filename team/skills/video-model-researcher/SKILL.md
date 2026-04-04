# video-model-researcher Skill

> **适用场景**: 调研最新 SOTA 开源视频理解模型，产出标准 Model Card  
> **触发词**: "调研视频模型"、"video model research"、"视频理解 SOTA"、"最新开源视频模型"  
> **输出规范**: Model Card（每模型）+ 横向对比 + Demo 代码  
> **调度者**: @coordinator / @pm

---

## 一、调研标准

### 1.1 信息源优先级（T0→T2）

| 等级 | 来源 | 要求 |
|------|------|------|
| **T0** | HuggingFace / ModelScope 官方模型页/博客 | 首选，双平台交叉验证 |
| **T1** | 官方 GitHub / 官方博客 / 官方 Leaderboard | 必有链接和截图 |
| **T2** | arXiv / 权威媒体报道 / 第三方评测 | 次选，注明媒体名称 |
| **禁** | 无来源信息 / 论坛匿名帖 / Wikipedia | 一律不收录 |

### 1.2 时间窗口

```
先查最近1周 → 1个月 → 1季度 → 半年
超过半年不收录
当日为基准日（T=0）
```

### 1.3 收录门槛

- 必须是**开源模型**（Open Weight 或 Open Source）
- 必须有**视频理解能力**（视频帧输入 / 时序推理 / 视频-文本）
- 重点方向：视频多模态大模型、长视频理解、实时视频分析

---

## 二、Model Card 模板

每个模型独立文件：`/workspace/team/projects/sota-model-hub/models/video/{model-name}.md`

必须包含：基本信息 / 许可证 / 链接 / Benchmark / SOTA声明（有据）/ 技术亮点 / 入选理由 / 信息源列表

---

## 三、调研流程（4步法）

### Step 1：宽泛撒网搜索（batch_web_search）

4路并发：
- SOTA open source video understanding model 2026 HuggingFace ModelScope
- video multimodal LLM new model 2026 release open source
- long video understanding model 2026 open source
- realtime video analysis model 2026 open source

### Step 2：精筛确认

重点验证：发布机构+日期 / 开源链接 / 视频能力 / Benchmark / 许可证

### Step 3：产出 Model Card

每个模型一个 `.md` 文件到指定目录

### Step 4：横向对比沉淀

`/workspace/team/projects/sota-model-hub/knowledge/video-{date}.md`
内容：模型总览表 + 横向洞察（5条+）+ 趋势 + 局限性

---

## 四、纪律规范

- 日期精确到日，无数据不写 SOTA 声明
- SOTA 声明须附来源 URL，无来源不上 SOTA
- 许可证字段必须填写，不确定时注明"需确认"
- 每模型必须完成全部 6 个区块，不得截断
- 调研完成后必须报告：共调研了多少个模型，列出确认模型名单

---

## 五、Loop 检测应对

当 batch_web_search 触发 Loop：立即停止搜索，用 extract_content_from_websites 深度挖掘已知 URL，用 exec 写入文件（绕过 write loop），合并产出。

---

## 六、每日强制产出清单

| 产出物 | 路径 | 必须 |
|--------|------|------|
| Model Card × N | `/workspace/team/projects/sota-model-hub/models/video/{name}.md` | ✅ |
| 横向对比 | `/workspace/team/projects/sota-model-hub/knowledge/video-{date}.md` | ✅ |
| Demo 代码 | `/workspace/team/projects/sota-model-hub/demos/{name}/` | ✅ 重要模型 |
| 调研报告 | 回复给 @coordinator/@pm | ✅ |

---

*本 Skill 为 @video-researcher 调研方法论沉淀，@coordinator 定期检查执行合规性。*
