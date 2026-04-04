# Model Card: MiniMax M2.5

> **记录版本：** v1.0  
> **调研日期：** 2026-04-04  
> **调研员：** @text-researcher  
> **可靠度评级：** A（多源交叉验证，Benchmark 数据来自官方发布 + 独立评测）

---

## 基本信息

| 字段 | 内容 |
|------|------|
| 模型全名 | MiniMax M2.5 |
| 开发方 | MiniMax（稀宇科技） |
| 发布时间 | 2026-02-12 |
| 发布时间窗口 | 最近 1 个月（✅ 收录） |
| 模型类型 | 开源前沿语言模型（MoE，文本 + Agent） |
| 许可证 | Apache 2.0 或类似开源许可（需确认官方许可证） |

---

## 链接

| 类型 | 链接 |
|------|------|
| HuggingFace | https://huggingface.co/minimax-io/MiniMax-M2.5 |
| 官方博客 | https://venturebeat.com/technology/minimaxs-new-open-m2-5-and-m2-5-lightning-near-state-of-the-art-while/ |
| 第三方分析 | https://huggingface.co/blog/mlabonne/minimax-m25 |
| 评测汇总 | https://llm-stats.com/models/minimax-m2.5 |

---

## Benchmark 成绩

> 数据来源：VentureBeat 2026-02-12 + HuggingFace Blog (mlabonne) 2026-02-17

| Benchmark | 分数 | 备注 |
|-----------|------|------|
| **SWE-Bench Verified** | **80.2%** | 开源模型最高分，与 Claude Opus 4.6 持平 |
| **Multi-SWE-Bench** | **51.3%** | **开源第一** |
| **BrowseComp** | 76.3% | 网页搜索与理解 |
| **BFCL**（工具调用） | 76.8% | 开源顶级 |
| **Coding Benchmark** | 37.4 | （对比 MiniMax M2: 29.2）|
| 推理速度 | 达 Claude Opus 4.6 速度水平 | VentureBeat 2026-02-12 |

---

## SOTA 声明（有据可查）

| 声明 | 来源 | 可靠度 |
|------|------|--------|
| 开源模型 SWE-Bench Verified 最高分 80.2% | VentureBeat（官方数据）+ HuggingFace Blog 交叉验证 | ★★★ 高 |
| Multi-SWE-Bench 开源第一（51.3%） | llm-stats.com 排行榜 | ★★★ 高 |
| 工具调用 BFCL 76.8% | VentureBeat + mlabonne 验证 | ★★★ 高 |
| 推理速度与 Claude Opus 4.6 持平 | VentureBeat 官方 claim | ★★☆ 中（需实测验证）|
| API 价格：$1/小时 | VentureBeat（官方数据）| ★★★ 高 |

---

## 技术亮点

1. **SWE-Bench 80.2%**：首个开源模型在软件工程评测集上突破 80%，与闭源前沿模型持平
2. **Multi-SWE-Bench 开源第一**：多文件软件工程任务表现最佳
3. **极低成本**：API 价格约 $1/小时，比 Claude 低约 20 倍
4. **强工具调用能力**：BFCL 76.8%，支持复杂 Agent 工作流
5. **高推理速度**：达闭源旗舰模型速度水平

---

## 入选理由

1. SWE-Bench Verified 80.2% 是 2026 年开源模型最重要的里程碑之一
2. Multi-SWE-Bench 开源第一，工程任务能力最强
3. 性价比极高（$1/小时 vs Claude Opus $20+/小时）
4. 开源可自托管，Apache 2.0 许可（推测，需确认）
5. 验证了开源模型可达前沿闭源水平

---

## 信息源列表（按 T0/T1/T2 分类）

### T0：HuggingFace / ModelScope 官方页
- [ ] HuggingFace 模型卡（需确认完整 URL）

### T1：官方 GitHub / 官方博客
- [ ] MiniMax 官方技术博客（需确认官方报告）

### T2：arXiv / 官方 Leaderboard
- [ ] HuggingFace Blog（mlabonne，2026-02-17）：https://huggingface.co/blog/mlabonne/minimax-m25

### T3：媒体
- VentureBeat（2026-02-12）：https://venturebeat.com/technology/minimaxs-new-open-m2-5-and-m2-5-lightning-near-state-of-the-art-while/

---

## 待补充

- [ ] 确认官方许可证（Apache 2.0 / MIT / 其他）
- [ ] 完整参数规模信息
- [ ] 上下文窗口长度
