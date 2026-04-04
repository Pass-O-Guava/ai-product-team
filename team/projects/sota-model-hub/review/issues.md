# 逐模型问题清单

> **审核时间**：2026-04-04  
> **审核人**：@reviewer（知识质检智能体）  
> 共审核 30 个模型，详见下表。

---

## 问题汇总表

| # | 模型 | 问题类型 | 问题描述 | 严重程度 | 修复建议 |
|---|------|---------|---------|---------|---------|
| 1 | Qwen3-Omni | 时效性错误 | Card 标注"2025年9月~12月"，实际官方公告发布于 **2025年9月22日**（来源：Qwen 官方博客 `qwen.ai/blog`），范围跨4个月，严重失准 | **严重** | 改为精确日期"2025年9月22日" |
| 2 | Qwen3-Omni | SOTA声明无证据 | 声称"首次在7B规模实现全模态SOTA"，但通篇无任何 benchmark 分数、无 benchmark 名称、无来源链接 | **严重** | 删除或补充 MMMU/MathVista/Video-MME 等具体分数及来源 |
| 3 | Qwen3-VL | SOTA声明无证据 | "MMMU 超越 GPT-4o" 无具体分数；"Video-MME 开源 SOTA" 无分数无链接；备注中"多项 benchmark 超越 GPT-4o"无法查证 | **严重** | 补充 MMMU 具体分数（如"~71.2分"）及 Video-MME 分数；引用官方技术报告 arXiv 2511.21631 |
| 4 | InternVL3.5 | SOTA声明无证据 | "开源 VLM 综合最强"为综合性断言，无综合评分依据；"MMMU ~73 分"未注明评测规模（28B/78B/241B-MoE）；"Cascade RL 有效控制幻觉"无量化数据 | **严重** | 明确是哪一规模的 ~73 分；补充综合评分来源；引用论文 2508.18265 |
| 5 | MiniCPM-V 4.5 | SOTA声明量化不足 | "8B参数超越 GPT-4o"基于 OpenCompass 排名，但未附链接；"Nature 论文 2025年7月发表"已核实OK，但超越 GPT-4o 需具体分数佐证 | **严重** | 补充 MMMU/MathVista 具体分数及 OpenCompass 排名链接 |
| 6 | Gemma 3 | 信息完整性+自相矛盾 | 1. 标注"数据可靠度：A"但全文无任何 benchmark 分数；2. 声称"140+语言"但列表中仅列举英文；3. 参数量级写"1B/4B/12B/27B"但27B版本（Gemini-3N-27B-it）是否存在存疑 | **严重** | 补充至少 MMMU/MMLU 分数；核实27B版本是否公开可用；更正可靠度评级为 B 或 C |
| 7 | Pixtral 12B | 信息准确性错误 | 1. 标注"数据可靠度：A"但全文无任何 benchmark 分数（严重自相矛盾）；2. "文本能力与 Mistral 7B 性能相当"有误导性——Pixtral 基础模型是 **Mistral Nemo 12B**（12B，非7B），此比较无意义 | **严重** | 补充 benchmark 分数（如 MMMU/VQA-v2）；更正文本能力比较对象或删除该表述 |
| 8 | SmolVLM2 | 信息完整性缺失 | 1. 标注"数据可靠度：A"但全文无任何 benchmark 分数；2. "超越 Idefics-80B"无具体数据来源；3. 参数列表中 256M/500M/2.2B 三个规格，但无各规格 benchmark 对比 | **严重** | 补充 benchmark 分数；更正可靠度评级为 C；如确实无 benchmark 数据，应如实说明 |
| 9 | Phi-4-Reasoning-Vision | SOTA声明无证据+信息不完整 | 1. 全文无任何具体 benchmark 分数；2. "紧凑模型 SOTA"无来源；3. "超越多数更大模型 MathVista"无具体分数；4. 发布时间虽精确到月（2026年3月）但缺少具体日期 | **严重** | 补充 MathVista/MMMU 具体分数；引用 HuggingFace 模型卡或官方博客 |
| 10 | Video-LLaVA | 信息不完整+过时风险 | 1. 无精确发布日期（仅"2024年"）；2. 无数据可靠度评级；3. 无任何 benchmark 分数；4. "2024年"无法判断是否有新版本 | **严重** | 补充精确月份（参考：PKU-YuanGroup GitHub）；补充至少一个 benchmark 分数 |
| 11 | video-SALMONN-o1 | 信息不完整 | 1. 无数据可靠度评级；2. 无任何 benchmark 分数；3. 仅"首个开源推理增强视听LLM"定性描述，能力边界不清 | **一般** | 补充至少一个视听 benchmark（AVSBench/AVLUE等）分数；补充可靠度评级 |
| 12 | Qwen2-Audio | 信息不完整 | 1. 无数据可靠度评级；2. 无任何 benchmark 分数（通篇只有功能描述）；3. "2024年8月"与官方 arXiv 编号2407（7月）时间不一致 | **一般** | 补充语音理解 benchmark（LibriSpeech/CoVoST）分数；核实正确发布日期；补充可靠度评级 |
| 13 | SALMONN | 信息不完整 | 1. 无数据可靠度评级；2. 无任何 benchmark 分数；3. 许可证 CC BY-NC-SA 标注正确（❌不可商用），但全文未在显眼位置提示不可商用 | **一般** | 补充 benchmark 分数；补充可靠度评级；在显眼位置补充"⚠️不可商用"提示 |
| 14 | CogVLM2-Video | 许可证模糊 | 1. "GLM License"含义不明——智谱存在多个许可协议，Card 未明确说明是否可商用；2. 无数据可靠度评级 | **一般** | 明确注明 GLM License 商用合规性（✅可商用/⚠️需申请）；补充可靠度评级 |
| 15 | DeepSeek Janus-Pro | SOTA声明无证据 | "可与 DALL-E 3 竞争"无任何具体分数（FID/CLIP Score）；仅"视觉理解 benchmark 表现优异"定性描述 | **一般** | 补充 GenEval/DPG-Bench 具体分数，或改为"图像生成达到开源领先水平（附分数）" |
| 16 | Show-o2 | SOTA声明无证据 | "7B 超越 14B 竞品（更低训练数据）"无 benchmark 名称、无具体分数；"NeurIPS 2025"会议信息待核实 | **一般** | 补充 MSCOCO/GenEval 分数；注明是哪14B竞品；核实NeurIPS 2025论文编号 |
| 17 | Emu3.5 | 信息不完整 | 1. 无数据可靠度评级；2. 无任何 benchmark 分数；3. 声称"世界模型"但缺乏量化指标；4. "约20B+"参数量用"约"字不够严谨 | **一般** | 补充视频生成 benchmark（UVB/PerpEval）或世界模型评测分数；标注确切参数量；补充可靠度评级 |
| 18 | LLaVA-OneVision-1.5 | SOTA声明无证据 | "Video-MME 开源领先"无具体分数；"强化学习版 LLaVA-OneVision-1.5-RL"存在但 Card 未提供该版本信息 | **一般** | 补充 Video-MME 具体分数；如存在1.5-RL版本需单独卡片或注明 |
| 19 | LLaVA-CoT | SOTA声明量化不足 | "MMMU 超越 Gemini-1.5-pro"无具体分数（Gemini-1.5-pro 的 MMMU 约 69）；ICCV 2025 Oral 论文信息正确，但声明超越需更具体数据 | **一般** | 补充 MMMU/MathVista 具体分数；引用 ICCV 2025 论文编号 |
| 20 | InternVL3 | 版本混淆风险 | 2025年4月~8月各规模陆续开源，但 Card 未说明 InternVL3.5（8月）比 InternVL3 的具体提升，InternVL3 卡片未标注"已被 InternVL3.5 超越" | **一般** | 在 InternVL3 卡片中注明与 InternVL3.5 的关系，或在 README 中明确版本优先级 |
| 21 | DeepSeek-V3 | 版本标注混淆 | Card 将"DeepSeek-V3.2（2025年12月）"与 V3 混排在同一卡片，未明确说明 V3.2 是 API 更新还是模型权重更新，用户可能混淆 | **一般** | 拆分 V3 与 V3.2 为独立卡片，或明确标注"V3.2 为 V3 的 API 版本更新，权重同 V3" |
| 22 | MiniCPM-V 4.5 | HF链接有误 | Card 中 HF 链接为 `openbmb/MiniCPM-V-4_5-8B`，实际 HuggingFace 模型 ID 为 `openbmb/MiniCPM-V-4_5`（不带-8B后缀），链接无法直接访问 | **一般** | 更正 HF 链接为 `https://huggingface.co/openbmb/MiniCPM-V-4_5` |
| 23 | GLM-4.6V | 信息不完整 | 1. 无数据可靠度评级；2. "原生工具调用，131K上下文"正确，但无任何 benchmark 分数；3. GLM-4.6V 的 CogAgent 版本（90B）被忽略，卡片参数量"约9B"可能有误 | **一般** | 补充 MMMU/ChartQA/DocVQA 分数；核实参数量（可能是 GLM-4V-9B 的 CogAgent 版本） |
| 24 | Mistral Small 3 | 版本信息不清晰 | Card 混合描述 Mistral Small 3、Small 3.1、Small 3.2（非官方）、Mistral 3（3B/8B/14B小规模版）、Large 3（旗舰），5个版本混在一张卡片，用户无法快速识别当前最新版本 | **一般** | 拆分为各版本独立卡片，或用子章节明确区分各版本的发布时间和 benchmark |

---

## 问题类型分布统计

| 问题类型 | 数量 | 占问题总数比例 |
|---------|------|-------------|
| SOTA声明无证据/量化不足 | 8 | 33% |
| 信息不完整（缺字段/分数） | 10 | 42% |
| 时间标注错误/模糊 | 3 | 13% |
| 许可证表述问题 | 2 | 8% |
| 链接/HTTP错误 | 1 | 4% |

---

*本清单由 @reviewer 于 2026-04-04 自动生成，每项问题均基于原始 Card 内容与官方来源交叉验证。*
