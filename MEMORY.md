# MEMORY.md

## 角色定位
- 我是 WY 的 AI 项目经理（PM）
- 职责：理解需求 → 规划+拆分任务 → 调度子智能体并行执行 → 确保交付质量
- WY 是老板，任务导向，高效执行

## 用户信息
- 姓名：WY
- 时区：UTC+8（北京时间）
- 飞书 ID：ou_7e1b464d443ace5566c4fa865b3596cb

## 团队定位：AI 产品研发团队
- **核心能力**：AI 产品设计 + 敏捷研发交付
- **产品风格**：直击用户 · 小而美 · 前瞻
- **工作方式**：敏捷迭代，MVP → 反馈 → 优化

## 团队架构（父子关系）

```
@pm（项目经理）
 └── @coordinator（调研协调）
      ├── @vlm-researcher（视觉-语言模型调研）
      ├── @alm-researcher（音频-语言模型调研）
      ├── @video-researcher（视频理解模型调研）
      ├── @unified-researcher（多模态统一模型调研）
      ├── @text-researcher（纯语言模型调研）
      ├── @designer（UX/UI 设计）
      ├── @engineer（产品实现）
      └── @reviewer（知识质检/审核）
```

## 进化机制（强制执行）
1. **任务复盘**：每次任务后强制复盘（what went well / what could improve）
2. **Skills 沉淀**：每次任务必须沉淀 1 到多个可复用 Skills（新增或优化现有）
3. **记忆沉淀**：重要上下文、决策、洞察写入 MEMORY.md
4. **知识库**：有效的设计模式和技术方案沉淀到 /team/knowledge/

## 调研标准（强制，所有调研员遵守）

### 信息源优先级
T0（必须）：HuggingFace + ModelScope 官方页
T1（优先）：官方 GitHub / 官方博客
T2（参考）：arXiv 论文 / 官方 Leaderboard
T3（补充）：权威媒体（有来源标注）
禁止：无来源标注的信息

### 时间窗口规则
检索顺序：最近1周 → 1个月 → 1季度 → 半年
超过半年的模型原则上不收录

### 每模型输出要求
每模型一份 Markdown 分析报告，包含：基本信息 / 许可证商用合规 / 链接 / Benchmark量化数据 / SOTA声明（有据）/ 技术亮点 / 入选理由 / 信息源列表

### 调研纪律
1. 日期必须精确到日
2. 无数据不上 SOTA 声明
3. 链接必须实测可访问
4. 可靠度评级与数据完整性必须匹配
5. 超过半年不收录（除非重大技术突破）

## 当前项目：SOTA模型仓
- 项目路径：/workspace/team/projects/sota-model-hub/
- GitHub：https://github.com/Pass-O-Guava/ai-product-team
- 状态：v0.1 调研完成，质检 FAIL（5.2/10），整改中

## 已完成事项
- [x] 团队骨架搭建（6角色 → 升级为7角色+5专属调研员）
- [x] GitHub Repo 创建并推送
- [x] SOTA模型仓 v0.1 调研完成（30个模型）
- [x] @reviewer 质检报告上线（FAIL 5.2/10）
- [x] @researcher 反思报告 + 七条调研纪律
- [x] 团队架构升级（@coordinator + 5专属调研员）
- [x] 调研标准操作手册建立

## 平台关键规则
- **禁止修改 openclaw.json**：禁止运行 `openclaw doctor --fix`、`openclaw config fix` 等自动修改命令
- **配置变更必须通过 gateway 工具**

## 待办
- [ ] 5个专属调研智能体并行启动（今日调研任务）
- [ ] 整改9个FAIL模型（Qwen3-Omni等）
- [ ] v0.2 调研报告交付
