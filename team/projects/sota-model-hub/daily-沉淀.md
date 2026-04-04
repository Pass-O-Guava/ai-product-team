# 每日沉淀规范（强制执行）

> 每位调研智能体每天必须完成沉淀，不得跳过。
> 这是调研工作的正式产出之一，不是一次性动作。
> @coordinator 负责监督执行，@pm 验收。

---

## 沉淀产出清单（每日必做）

### 沉淀1️⃣：模型知识体系
**文件路径**：`/workspace/team/projects/sota-model-hub/knowledge/{category}-knowledge-{date}.md`

**内容要求**：
- 今日调研的模型技术架构分析（不是 Model Card，是深度分析）
- 多个模型的横向对比洞察
- 技术趋势判断（有依据）
- 踩过的坑和纠正（真实记录）
- 对后续调研的启示

**格式**：
```markdown
## 今日认知

### 新学到的东西
- ...

### 横向对比发现
- ...

### 技术趋势
- ...

### 下次调研要注意什么
- ...
```

---

### 沉淀2️⃣：工作方法和技能方式
**文件路径**：`/workspace/team/skills/{skill-name}/SKILL.md`

**内容要求**：
- 调研过程中发现的高效方法 → 固化为 Skill
- 踩过的坑 → 固化为检查清单
- 工具使用技巧 → 固化为操作指南
- 每次调研至少沉淀 1 个新 Skill 或更新 1 个已有 Skill

**Skill 模板**：
```markdown
# {技能名称}

## 何时使用
## 核心步骤
## 常见错误（踩坑记录）
## 示例
```

---

### 沉淀3️⃣：产品级 Demo 代码
**文件路径**：`/workspace/team/projects/sota-model-hub/demos/{model-name}-{date}.py`

**内容要求**：
- 每个重要模型配套一个可运行的 Demo
- 代码必须能实际调用模型（HuggingFace API 或开源权重）
- 包含：模型加载 → 核心功能演示 → 结果输出
- 附带 requirements.txt 或 pip install 命令
- 代码必须经过实测（不能是伪代码）

**Demo 标准**：
- Python，≤100行，突出核心能力
- 有注释说明关键步骤
- 运行方式清晰（python demo.py 即可跑通）

---

## 每日沉淀检查清单

@coordinator 每日检查以下所有项：

- [ ] 今日调研了多少个模型？
- [ ] 沉淀1（知识体系）完成了吗？路径在哪？
- [ ] 沉淀2（工作方法/Skill）完成了吗？路径在哪？
- [ ] 沉淀3（Demo代码）完成了吗？路径在哪？
- [ ] 沉淀内容是否已推送到 GitHub？

**有任何一项未完成，@coordinator 必须向 @pm 报告原因并给出补完计划。**

---

## 与 GitHub 推送绑定

每日沉淀必须当天推送 GitHub：
```bash
git add team/projects/sota-model-hub/knowledge/
git add team/projects/sota-model-hub/demos/
git add team/skills/
git commit -m "沉淀: {日期} {内容摘要}"
git push origin main
```

---

*本文件为强制规范，所有调研智能体必须遵守。*
*由 @pm 于 2026-04-04 建立。*
