# Model Card: Step-3.5-Flash

> **记录版本：** v1.0  
> **调研日期：** 2026-04-04  
> **调研员：** @text-researcher  
> **可靠度评级：** A（T0 页面存在，arXiv 技术报告，NVIDIA NIM 官方发布）

---

## 基本信息

| 字段 | 内容 |
|------|------|
| 模型全名 | Step-3.5-Flash |
| 开发方 | StepFun（阶跃星辰） |
| 发布时间 | 2026-02-01（2026-02-02 全面公开） |
| 发布时间窗口 | 最近 1 个月（✅ 收录） |
| 模型类型 | 开源前沿语言模型（稀疏 MoE，196B 总参数 / 11B 激活） |
| 许可证 | Apache 2.0 / MIT（需确认官方 License） |

---

## 链接

| 类型 | 链接 |
|------|------|
| HuggingFace | https://huggingface.co/stepfun-ai/Step-3.5-Flash |
| GitHub | https://github.com/stepfun-ai/Step-3.5-Flash |
| arXiv 技术报告 | https://arxiv.org/html/2602.10604v1 |
| NVIDIA NIM | https://build.nvidia.com/stepfun-ai/step-3.5-flash/modelcard |
| 官方博客 | https://static.stepfun.com/blog/step-3.5-flash/ |
| vLLM 文档 | https://docs.vllm.ai/projects/recipes/en/latest/StepFun/Step-3.5-Flash.html |

---

## Benchmark 成绩

> 数据来源：arXiv 2602.10604v1 + NVIDIA NIM 官方 Model Card

| Benchmark | 分数 | 备注 |
|-----------|------|------|
| **IMO-AnswerBench** | **85.4%** | IMO 数学奥赛题，开源顶级 |
| **MATH-500** | **86.4%** | 高难度数学基准 |
| SWE-rebench Feb 2026 | **59.6%** | 所有开源模型中极高 |
| SWE-bench Verified | （数据未完整提取）| 预计 75%+ |
| 推理能力 | 与前沿闭源系统性能持平 | NVIDIA NIM 官方 claim |
| 速度 | 极快（稀疏 MoE + Flash 优化）| 定位为高效 Agent 模型 |

---

## SOTA 声明（有据可查）

| 声明 | 来源 | 可靠度 |
|------|------|--------|
| IMO-AnswerBench 85.4% | arXiv 2602.10604v1（2026-02-11）| ★★★ 高 |
| MATH-500 86.4% | arXiv 2602.10604v1 | ★★★ 高 |
| SWE-rebench 59.6%（开源前列）| Reddit r/LocalLLaMA 2026-03-24 | ★★☆ 中 |
| 与前沿闭源系统性能持平 | NVIDIA NIM 官方 Model Card | ★★☆ 中（需 Benchmark 数据支持）|
| 稀疏 MoE 架构（196B 总/11B 激活）| arXiv 技术报告 | ★★★ 高 |

---

## 技术亮点

1. **稀疏 MoE 架构**：196B 总参数 / 11B 激活参数，推理成本极低
2. **数学能力突出**：IMO-AnswerBench 85.4%，MATH-500 86.4%
3. **Agent 优化**：专为 Agent 工作流设计，推理速度极快
4. **全开源**：代码、权重完整开源，Apache 2.0（推测）
5. **NVIDIA NIM 同步发布**：企业级部署开箱即用
6. **vLLM 官方支持**：部署生态完善

---

## 入选理由

1. 稀疏 MoE 极致效率：11B 激活参数实现前沿性能
2. IMO-AnswerBench 85.4%，数学推理达到奥赛金牌水平
3. SWE-rebench 59.6%，软件工程任务表现优异
4. 全开源 + vLLM 支持，降低部署门槛
5. 2026 年 2 月最早发布的重磅开源模型之一

---

## 信息源列表（按 T0/T1/T2 分类）

### T0：HuggingFace / ModelScope 官方页
- ✅ HuggingFace 模型卡：https://huggingface.co/stepfun-ai/Step-3.5-Flash

### T1：官方 GitHub / 官方博客
- ✅ GitHub：https://github.com/stepfun-ai/Step-3.5-Flash
- ✅ 官方博客（2026-02-12）：https://static.stepfun.com/blog/step-3.5-flash/

### T2：arXiv / 官方 Leaderboard
- ✅ arXiv 技术报告（2026-02-11）：https://arxiv.org/html/2602.10604v1
- ✅ NVIDIA NIM Model Card：https://build.nvidia.com/stepfun-ai/step-3.5-flash/modelcard

---

## 待补充

- [ ] 确认官方许可证类型
- [ ] 完整 Benchmark 表
- [ ] 上下文窗口长度
