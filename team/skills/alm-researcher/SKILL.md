# ALM Researcher Skill

> 音频-语言模型（Audio-Language Model）调研专项技能  
> 版本: 1.0.0 | 日期: 2026-04-04  

---

## 一、调研标准

### 信息源优先级（强制分级）

| 等级 | 来源 | 要求 |
|------|------|------|
| T0（必须） | HuggingFace 官方页 + ModelScope 官方页 | 每模型至少一个 T0 |
| T1（优先） | 官方 GitHub / 博客 / 技术报告 | 至少一个 T1 |
| T2（参考） | arXiv / 第三方媒体 / 社区 | 辅助验证 |

> ⚠️ 无来源标注的信息一律不采信

### 时间窗口（强制）

优先级：1周 > 1个月 > 1季度 > 半年  
超过半年的模型"原则上不收录"；若有 2026 新 checkpoint 则单独标注版本日期。

### SOTA 声明标准

| 情况 | 是否可写 SOTA |
|------|:------------:|
| 官方 README/Blog 明确声明 | ✅ 附来源 |
| 第三方有链接测试达到 SOTA | ✅ 附链接 |
| 自己推断/猜测 | ❌ 禁止 |
| 仅定性描述无数据 | ⚠️ 写"有据可查的 SOTA 定位" |

---

## 二、Model Card 9 个必须字段

1. 基本信息（名称/参数量/发布时间/机构/许可证）
2. 链接（HF / MS / GitHub / arXiv / 博客）
3. Benchmark 数据（数值 + 来源 URL）
4. SOTA 声明（来源 + 可信度）
5. 技术亮点（3-5 个创新点）
6. 入选理由
7. 信息源列表（T0 + T1 至少各一）
8. 许可证商用合规
9. 评测人和日期

---

## 三、每日强制产出

| # | 产出 | 路径 |
|---|------|------|
| 1 | 每个模型 Model Card | `models/audio/{model-name}.md` |
| 2 | 知识横向对比 | `knowledge/alm-{date}.md` |
| 3 | Skill 方法论 | `skills/alm-researcher/SKILL.md` |
| 4 | Demo 代码 | `demos/{model-name}/` |

---

## 四、Model Card 命名规范

- 全小写，空格用连字符 -
- 版本号保留（如 personaplex-7b-v1）
- 示例：`covo-audio-chat.md` `qwen3-asr.md`

---

## 五、调研 SOP

### 第一步：搜索（15 分钟）
```
必跑 Query：
1. "{model-name} 2026 HuggingFace ModelScope release"
2. "{model-name} benchmark SOTA 2026"
3. "open source audio language model ALM 2026"
4. HuggingFace daily papers audio language model 2026
```

### 第二步：提取详情（15 分钟/模型）
- HuggingFace 模型页 README（参数/许可证/Benchmark）
- ModelScope 交叉验证
- GitHub Releases（发布日期）
- arXiv 技术报告（技术细节）

### 第三步：筛选（5 分钟）
- [ ] 发布时间 ≤ 6个月？
- [ ] 至少有 T0 来源？
- [ ] 开源（非仅 API）？
- [ ] 许可证明确？
- [ ] 有可验证 Benchmark？

### 第四步：撰写 Model Card（15 分钟/模型）
### 第五步：横向对比（10 分钟）
### 第六步：Demo 代码（20 分钟/模型）

---

## 六、合规检查清单

```
[ ] 日期精确到"日"（YYYY-MM-DD）
[ ] 无数据不上 SOTA 声明
[ ] 可靠度评级与数据完整性匹配
[ ] 许可证商用判断有据可查
[ ] 所有声明附 URL 或来源说明
```

---

## 七、常见陷阱与规避

| 陷阱 | 规避 |
|------|------|
| 第三方夸大 SOTA | 以官方 README/Blog 为准 |
| 旧版本当新模型 | 核查 GitHub Releases 日期 |
| 许可证误判 | 读取 HuggingFace License 部分 |
| Benchmark 张冠李戴 | 区分论文报告 vs 第三方测试 |
| 仅 T2 支撑重要结论 | 至少补一个 T0/T1 |

---

## 八、版本历史

| 版本 | 日期 | 更新 |
|------|------|------|
| 1.0.0 | 2026-04-04 | 初始版本 |

*Skill 版本: 1.0.0 | 维护人: @alm-researcher*
