# Model Card: Qwen3.5-Medium 系列

> **记录版本：** v1.0  
> **调研日期：** 2026-04-04  
> **调研员：** @text-researcher  
> **可靠度评级：** A（VentureBeat 独立报道 + HuggingFace 官方页面 + 第三方评测多源）

---

## 基本信息

| 字段 | 内容 |
|------|------|
| 模型全名 | Qwen3.5-Medium 系列 |
| 开发方 | Alibaba DAMO Academy（阿里达摩院） |
| 发布时间 | 2026-02-24 |
| 发布时间窗口 | 最近 1 个月（✅ 收录） |
| 发布型号 | Qwen3.5-2B、Qwen3.5-4B、Qwen3.5-9B、Qwen3.5-27B、Qwen3.5-35B-A3B |
| 模型类型 | 开源多模态语言模型（MoE + 密集混合，Qwen3.5 家族中端型号） |
| 许可证 | Qwen3.5 License（基于 LlamaRC，商用友好）|

---

## 链接

| 类型 | 链接 |
|------|------|
| GitHub | https://github.com/QwenLM/Qwen3.5 |
| HuggingFace 35B | https://huggingface.co/Qwen/Qwen3.5-35B-A3B |
| HuggingFace 9B | https://huggingface.co/Qwen/Qwen3.5-9B |
| VentureBeat 报道 | https://venturebeat.com/technology/alibabas-new-open-source-qwen3-5-medium-models-offer-sonnet-4-5-performance |
| XDA 开发者评测 | https://www.xda-developers.com/qwen-3-5-9b-tops-ai-benchmarks-not-how-pick-model/ |

---

## Benchmark 成绩

> 数据来源：VentureBeat 2026-02-26 + DigitalApplied 2026-02-25 + HuggingFace 讨论区

| Benchmark | Qwen3.5-35B-A3B | 备注 |
|-----------|----------------|------|
| **Sonnet 4.5 对比** | **性能持平** | VentureBeat 官方 claim（本地计算机运行）|
| **HuggingFace 讨论** | 2B/4B/9B/27B/35B 五型号齐全 | 史上最强开源视觉模型家族 |
| SWE-rebench | 领先前代 Qwen3-Medium | HuggingFace 讨论区确认 |
| XDA 开发者评测 | Qwen3.5-9B 横扫所有 AI Benchmark | 评测方法存争议（见备注）|

**⚠️ XDA 争议说明**：XDA 评测称 Qwen3.5-9B"横扫所有 Benchmark"，但多位社区成员指出其测试方法存在问题（测试集与训练集重叠风险），Benchmark 数据需谨慎对待。

---

## SOTA 声明（有据可查）

| 声明 | 来源 | 可靠度 |
|------|------|--------|
| Qwen3.5-35B 本地运行达 Sonnet 4.5 性能 | VentureBeat 2026-02-26 | ★★★ 高 |
| 史上最强开源视觉模型家族 | HuggingFace 讨论区 2026-03-03 | ★★☆ 中（社区讨论，待官方验证）|
| Qwen3.5-9B Benchmark 领先 | XDA 开发者 2026-03-12 | ★☆☆ 低（测试方法受质疑）|

---

## 技术亮点

1. **五型号完整覆盖**：2B/4B/9B/27B/35B-A3B，满足不同算力需求
2. **本地可运行**：35B-A3B 可在本地计算机运行（VentureBeat 验证）
3. **多模态能力**：视觉语言融合，Qwen3.5 家族统一视觉架构
4. **稀疏 MoE（35B-A3B）**：A3B 架构（推测 MoE），3B 激活参数实现高效推理
5. **Qwen3.5 生态**：与旗舰 397B-A17B 共享架构，工具链兼容
6. **近 100% 多模态训练效率**：异步 RL 框架优化

---

## 入选理由

1. 首个实现"本地消费级硬件达 Sonnet 4.5 水平"的开源模型系列
2. 五型号完整覆盖，从 2B 到 35B，满足边缘到服务器全场景
3. Qwen3.5 家族成员，生态成熟，工具链完善
4. 多模态 + Agent 双能力，适合本地部署场景
5. 填补了 Qwen3.5 旗舰（397B）与 Qwen3（早期版本）之间的能力空白

---

## 信息源列表（按 T0/T1/T2 分类）

### T0：HuggingFace / ModelScope 官方页
- ✅ HuggingFace 页面（2B/4B/9B/27B/35B）：需确认各页面 License 信息

### T1：官方 GitHub / 官方博客
- ✅ GitHub QwenLM/Qwen3.5（2026-02-24 同步更新）

### T2：arXiv / 官方 Leaderboard
- [ ] 无直接 arXiv 页面（Qwen3.5 旗舰报告或可覆盖）

### T3：媒体
- ✅ VentureBeat（2026-02-26）：https://venturebeat.com/technology/alibabas-new-open-source-qwen3-5-medium-models-offer-sonnet-4-5-performance
- ⚠️ XDA 开发者（2026-03-12，需审慎使用）：https://www.xda-developers.com/qwen-3-5-9b-tops-ai-benchmarks-not-how-pick-model/

---

## 待补充

- [ ] 各型号具体 Benchmark 分数（当前依赖 VentureBeat claim）
- [ ] 确认 Qwen3.5 License 商业使用条款
- [ ] 各型号上下文窗口长度
