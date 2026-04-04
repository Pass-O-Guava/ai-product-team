// Enhanced OpenClaw Report - fully compilable C# Program
using DocumentFormat.OpenXml;
using DocumentFormat.OpenXml.Packaging;
using DocumentFormat.OpenXml.Wordprocessing;
using System;
using System.Collections.Generic;
using System.IO;
using A  = DocumentFormat.OpenXml.Drawing;
using DW = DocumentFormat.OpenXml.Drawing.Wordprocessing;
using PIC = DocumentFormat.OpenXml.Drawing.Pictures;

static class Program
{
    static readonly string imgCover  = "/workspace/imgs/cover_hero.png";
    static readonly string imgArch   = "/workspace/imgs/arch_three_layers.png";
    static readonly string imgTools  = "/workspace/imgs/tools_skills.png";
    static readonly string imgSec    = "/workspace/imgs/security_wasm.png";
    static readonly string imgTrends = "/workspace/imgs/trends_2026.png";
    static readonly string imgMcp    = "/workspace/imgs/mcp_diagram.png";
    static readonly string imgAgent  = "/workspace/imgs/agentic_ai_2026.jpg";

    const long EmuPerPx96 = 9525L;
    const int  ImgWidthPx  = 660;
    const long ImgWidthEmu = ImgWidthPx * EmuPerPx96;

    static uint _imgSeq = 1;
    static MainDocumentPart? _mainPart = null;

    static Drawing MkDrawing(string relId, long cx, long cy, uint id, string name)
    {
        var docProps = new DW.DocProperties { Id = id, Name = name };

        var picture = new PIC.Picture(
            new PIC.NonVisualPictureProperties(
                new PIC.NonVisualDrawingProperties { Id = 0U, Name = name },
                new PIC.NonVisualPictureDrawingProperties()),
            new PIC.BlipFill(
                new A.Blip { Embed = relId, CompressionState = A.BlipCompressionValues.Print },
                new A.Stretch(new A.FillRectangle())),
            new PIC.ShapeProperties(
                new A.Transform2D(new A.Offset { X = 0L, Y = 0L }, new A.Extents { Cx = cx, Cy = cy }),
                new A.PresetGeometry(new A.AdjustValueList()) { Preset = A.ShapeTypeValues.Rectangle }));

        var graphic = new A.Graphic(new A.GraphicData { Uri = "http://schemas.openxmlformats.org/drawingml/2006/picture" });
        graphic.AppendChild(picture);

        var inline = new DW.Inline(
            new DW.Extent { Cx = cx, Cy = cy },
            new DW.EffectExtent { LeftEdge = 0L, TopEdge = 0L, RightEdge = 0L, BottomEdge = 0L },
            docProps,
            new DW.NonVisualGraphicFrameDrawingProperties(new A.GraphicFrameLocks { NoChangeAspect = true }),
            graphic)
        { DistanceFromTop = 0U, DistanceFromBottom = 0U, DistanceFromLeft = 0U, DistanceFromRight = 0U };

        return new Drawing(inline);
    }

    static void AddImg(Body body, string imgPath, long heightEmu, string caption)
    {
        try
        {
            var ext = Path.GetExtension(imgPath).ToLowerInvariant();
            var imgType = ext switch { ".png" => ImagePartType.Png, ".jpg" or ".jpeg" => ImagePartType.Jpeg, ".gif" => ImagePartType.Gif, ".bmp" => ImagePartType.Bmp, _ => ImagePartType.Png };
            var imgPart = _mainPart!.AddImagePart(imgType);
            using (var s = File.OpenRead(imgPath)) imgPart.FeedData(s);
            var relId = _mainPart.GetIdOfPart(imgPart);
            uint id = 100 + _imgSeq++;

            var drawing = MkDrawing(relId, ImgWidthEmu, heightEmu, id, Path.GetFileName(imgPath));

            var p = new Paragraph(new ParagraphProperties(new Justification { Val = JustificationValues.Center }, new SpacingBetweenLines { Before = "200", After = "0" }));
            p.AppendChild(new Run(drawing));
            body.AppendChild(p);

            var cp = new Paragraph(new ParagraphProperties(new Justification { Val = JustificationValues.Center }, new SpacingBetweenLines { Before = "0", After = "200" }));
            cp.AppendChild(new Run(new RunProperties(new FontSize { Val = "18" }, new Color { Val = "555555" }, new Italic()), new Text("图：" + caption)));
            body.AppendChild(cp);
        }
        catch (Exception ex) { Console.WriteLine($"[WARN] {imgPath}: {ex.Message}"); }
    }

    static void H1(Body b, string t, RunProperties? rPr = null)
    {
        rPr ??= new RunProperties(new Bold(), new FontSize { Val = "36" }, new Color { Val = "2F5496" });
        var p = new Paragraph(new ParagraphProperties(new ParagraphStyleId { Val = "Heading1" }));
        p.AppendChild(new Run(rPr, new Text(t))); b.AppendChild(p);
    }
    static void H2(Body b, string t)
    {
        var p = new Paragraph(new ParagraphProperties(new ParagraphStyleId { Val = "Heading2" }));
        p.AppendChild(new Run(new RunProperties(new Bold(), new FontSize { Val = "28" }, new Color { Val = "2F5496" }), new Text(t))); b.AppendChild(p);
    }
    static void P(Body b, string t)
    {
        if (string.IsNullOrWhiteSpace(t)) { b.AppendChild(new Paragraph()); return; }
        var p = new Paragraph(new ParagraphProperties(new SpacingBetweenLines { After = "160", Line = "276", LineRule = LineSpacingRuleValues.Auto }));
        p.AppendChild(new Run(new RunProperties(new FontSize { Val = "21" }, new Color { Val = "333333" }), new Text(t) { Space = SpaceProcessingModeValues.Preserve })); b.AppendChild(p);
    }
    static void B(Body b, string t)
    {
        var p = new Paragraph(new ParagraphProperties(new SpacingBetweenLines { After = "120", Line = "276", LineRule = LineSpacingRuleValues.Auto }, new Indentation { Left = "360", Hanging = "180" }));
        p.AppendChild(new Run(new RunProperties(new FontSize { Val = "21" }, new Color { Val = "333333" }), new Text("• " + t) { Space = SpaceProcessingModeValues.Preserve })); b.AppendChild(p);
    }
    static void PB(Body b) { b.AppendChild(new Paragraph(new Run(new Break { Type = BreakValues.Page }))); }

    static void Tbl(Body b, string[] headers, string[][] rows)
    {
        var corpBlue = "2F5496"; var darkGray = "333333"; var altBlue = "E8F0FA";
        var tbl = new Table();
        tbl.AppendChild(new TableProperties(new TableWidth { Width = "5000", Type = TableWidthUnitValues.Pct },
            new TableBorders(new TopBorder { Val = BorderValues.Single, Size = 8, Color = corpBlue }, new BottomBorder { Val = BorderValues.Single, Size = 8, Color = corpBlue },
                new LeftBorder { Val = BorderValues.Single, Size = 4, Color = "AAAAAA" }, new RightBorder { Val = BorderValues.Single, Size = 4, Color = "AAAAAA" },
                new InsideHorizontalBorder { Val = BorderValues.Single, Size = 4, Color = "CCCCCC" }, new InsideVerticalBorder { Val = BorderValues.Single, Size = 4, Color = "CCCCCC" })));
        var tg = new TableGrid();
        for (int i = 0; i < headers.Length; i++) tg.AppendChild(new GridColumn { Width = (5000 / headers.Length).ToString() });
        tbl.AppendChild(tg);

        var hr = new TableRow();
        foreach (var h in headers) { var tc = new TableCell(); tc.AppendChild(new TableCellProperties(new Shading { Fill = corpBlue })); var cp = new Paragraph(new ParagraphProperties(new Justification { Val = JustificationValues.Center })); cp.AppendChild(new Run(new RunProperties(new Bold(), new FontSize { Val = "20" }, new Color { Val = "FFFFFF" }), new Text(h))); tc.AppendChild(cp); hr.AppendChild(tc); }
        tbl.AppendChild(hr);

        for (int ri = 0; ri < rows.Length; ri++)
        {
            var tr = new TableRow(); string fill = ri % 2 == 0 ? "FFFFFF" : altBlue;
            for (int ci = 0; ci < rows[ri].Length; ci++) { var tc = new TableCell(); tc.AppendChild(new TableCellProperties(new Shading { Fill = fill })); var cp = new Paragraph(); cp.AppendChild(new Run(new RunProperties(new FontSize { Val = "20" }, new Color { Val = darkGray }), new Text(rows[ri][ci]) { Space = SpaceProcessingModeValues.Preserve })); tc.AppendChild(cp); tr.AppendChild(tc); }
            tbl.AppendChild(tr);
        }
        b.AppendChild(tbl);
        b.AppendChild(new Paragraph(new SpacingBetweenLines { Before = "0", After = "160" }));
    }

    static void Caption(Body b, string t)
    {
        var p = new Paragraph(new ParagraphProperties(new SpacingBetweenLines { Before = "0", After = "200" }));
        p.AppendChild(new Run(new RunProperties(new FontSize { Val = "18" }, new Color { Val = "555555" }, new Italic()), new Text("表：" + t))); b.AppendChild(p);
    }

    static long ImgH() => (long)(ImgWidthEmu * 0.5625);

    static void Main()
    {
        var corpBlue = "2F5496"; var darkGray = "333333";
        Console.WriteLine("Generating Enhanced OpenClaw Report...");

        using var doc = WordprocessingDocument.Create("/workspace/OpenClaw技术研究报告_图文版.docx", WordprocessingDocumentType.Document);
        var mainPart = doc.AddMainDocumentPart();
        _mainPart = mainPart;
        mainPart.Document = new Document(new Body());
        var b = mainPart.Document.Body!;

        // Styles
        var sp = mainPart.AddNewPart<StyleDefinitionsPart>();
        var styles = new Styles();
        var ns = new Style { Type = StyleValues.Paragraph, StyleId = "Normal", Default = true };
        ns.AppendChild(new StyleName { Val = "Normal" });
        ns.AppendChild(new StyleParagraphProperties(new SpacingBetweenLines { After = "160", Line = "276", LineRule = LineSpacingRuleValues.Auto }));
        ns.AppendChild(new StyleRunProperties(new RunFonts { Ascii = "Calibri", HighAnsi = "Calibri", EastAsia = "SimSun", ComplexScript = "Arial" }, new FontSize { Val = "21" }, new Color { Val = darkGray }));
        styles.AppendChild(ns);

        var h1s = new Style { Type = StyleValues.Paragraph, StyleId = "Heading1" };
        h1s.AppendChild(new StyleName { Val = "heading 1" }); h1s.AppendChild(new BasedOn { Val = "Normal" });
        h1s.AppendChild(new StyleParagraphProperties(new SpacingBetweenLines { Before = "480", After = "120" }, new KeepNext(), new OutlineLevel { Val = 0 }));
        h1s.AppendChild(new StyleRunProperties(new Bold(), new FontSize { Val = "36" }, new Color { Val = corpBlue }));
        styles.AppendChild(h1s);

        var h2s = new Style { Type = StyleValues.Paragraph, StyleId = "Heading2" };
        h2s.AppendChild(new StyleName { Val = "heading 2" }); h2s.AppendChild(new BasedOn { Val = "Normal" });
        h2s.AppendChild(new StyleParagraphProperties(new SpacingBetweenLines { Before = "280", After = "80" }, new KeepNext(), new OutlineLevel { Val = 1 }));
        h2s.AppendChild(new StyleRunProperties(new Bold(), new FontSize { Val = "28" }, new Color { Val = corpBlue }));
        styles.AppendChild(h2s);

        sp.Styles = styles; sp.Styles.Save();

        // ── COVER ──
        AddImg(b, imgCover, ImgH(), "OpenClaw AI Agent 技术研究报告封面图");
        var cp2 = new Paragraph(new ParagraphProperties(new Justification { Val = JustificationValues.Center }, new SpacingBetweenLines { Before = "300", After = "80" }));
        cp2.AppendChild(new Run(new RunProperties(new Bold(), new FontSize { Val = "52" }, new Color { Val = corpBlue }), new Text("技术研究报告"))); b.AppendChild(cp2);
        cp2 = new Paragraph(new ParagraphProperties(new Justification { Val = JustificationValues.Center }, new SpacingBetweenLines { Before = "0", After = "600" }));
        cp2.AppendChild(new Run(new RunProperties(new FontSize { Val = "24" }, new Color { Val = "888888" }), new Text("2026年最新版  |  OpenClaw研究组  |  2026年4月"))); b.AppendChild(cp2);
        PB(b);

        // ── 一、研究背景 ──
        H1(b, "一、研究背景");
        H2(b, "1.1  AI Agent 发展趋势");
        P(b, "2026年被称为\"通用AI智能体元年\"。以OpenClaw为代表的开源自主Agent框架正在重塑人机协作方式。与传统聊天机器人不同，OpenClaw被设计为\"永远在线\"的数字工作者——它持续运行在用户本地硬件上，通过消息应用（飞书、WhatsApp、Telegram等）随时待命，主动执行任务而非被动应答。");
        AddImg(b, imgAgent, ImgH(), "图1-1  2026年企业级AI Agent工作流示意图");
        H2(b, "1.2  OpenClaw 的诞生与定位");
        P(b, "OpenClaw是一个开源、自托管的AI Agent框架，核心设计理念是：将大语言模型的\"大脑\"与用户真实数字工具链（文件系统、浏览器、Shell、消息平台）深度连接，让AI真正在操作系统层面执行多步骤复杂任务。OpenClaw以Node.js为核心运行引擎，构建了Gateway—Channel—LLM三层架构，通过MCP协议与外部生态无缝连接。截至2026年，OpenClaw已积累超过43万行代码，拥有25个内置工具和5000+社区Skills，支持所有主流商用大模型和本地模型。");
        PB(b);

        // ── 二、技术原理 ──
        H1(b, "二、技术原理与系统架构");
        H2(b, "2.1  三层架构设计");
        P(b, "OpenClaw采用清晰的三层分层架构，各层职责明确，协同完成从用户请求到任务完成的完整闭环：");
        Tbl(b, new[] { "层级", "核心职责", "关键技术" }, new[] {
            new[] { "Gateway层", "会话生命周期管理、WebSocket连接", "WebSocket、Session路由" },
            new[] { "Channel层", "多平台消息协议适配与转换", "消息协议解析、平台适配器" },
            new[] { "LLM层",     "推理决策与工具调用编排",      "Function Calling、流式响应" }
        });
        Caption(b, "表2-1  OpenClaw三层架构总览");
        AddImg(b, imgArch, ImgH(), "图2-1  OpenClaw三层架构与消息流向示意图");
        H2(b, "2.2  Gateway（网关层）");
        P(b, "Gateway是整个系统的中央控制平面，默认监听本地地址127.0.0.1:18789。它同时管理多个消息平台连接（飞书、Telegram、WhatsApp等），将收到的消息路由到相应的Agent会话，等待处理结果后通过正确渠道发回响应。Gateway本身不处理业务逻辑，仅负责连接与会话分发。");
        H2(b, "2.3  Channel（渠道层）");
        P(b, "Channel层负责适配不同消息平台的协议与消息格式。OpenClaw通过可插拔的Channel模块接入各类IM工具，每个Channel将平台特定的消息格式统一转换为内部标准格式，再交给Gateway路由。添加新平台支持只需实现对应的Channel适配器，极大降低了接入成本。");
        H2(b, "2.4  LLM层");
        P(b, "LLM层是实际执行推理与决策的核心。OpenClaw采用模型无关（Model-Agnostic）设计，支持主流商业模型、开源/国产模型以及本地模型，并支持多模型Failover自动切换：");
        Tbl(b, new[] { "模型类别", "支持模型" }, new[] {
            new[] { "商业旗舰模型", "Anthropic Claude Opus/Sonnet/Haiku, OpenAI GPT-4o/5, Google Gemini 2.0 Flash" },
            new[] { "开源/国产模型", "DeepSeek V3, Moonshot Kimi K2.5" },
            new[] { "本地模型",     "通过 Ollama / LM Studio / vLLM 接入任意兼容模型" },
            new[] { "容灾 Failover", "多模型自动切换，单一模型故障不影响服务连续性" }
        });
        Caption(b, "表2-2  OpenClaw支持的AI模型列表（截至2026年Q1）");
        H2(b, "2.5  MCP协议集成");
        P(b, "OpenClaw在2026年正式支持Model Context Protocol（MCP）标准。MCP是由Anthropic主导的开放标准，旨在为AI模型与外部工具/数据源之间提供统一、一致的连接协议，被喻为\"AI世界的USB接口\"。OpenClaw MCP支持两种工作模式：");
        B(b, "MCP Server模式（openclaw mcp serve）：将OpenClaw作为MCP服务器暴露，允许外部MCP客户端（如Codex、Claude Code）连接到OpenClaw的对话会话并进行工具调用");
        B(b, "MCP Client模式：OpenClaw通过MCP协议连接外部MCP服务器，实现对第三方工具和服务的集成");
        AddImg(b, imgMcp, ImgH(), "图2-2  Model Context Protocol（MCP）架构示意图");
        P(b, "MCP Server核心工具接口：conversations_list（列出对话）、messages_read（读取消息）、events_poll（事件轮询）、messages_send（发送消息）、permissions_respond（处理审批请求）。");
        PB(b);

        // ── 三、核心能力 ──
        H1(b, "三、核心能力解析");
        H2(b, "3.1  工具系统（Built-in Tools）");
        P(b, "OpenClaw内置25个核心工具，覆盖Agent在操作系统层面的所有关键能力：");
        Tbl(b, new[] { "工具类别", "具体功能", "安全级别" }, new[] {
            new[] { "Shell执行",    "执行任意Shell命令，支持sudo和交互式命令",  "⚠️ 高风险" },
            new[] { "文件系统",     "读写、创建、删除、搜索本地文件",            "⚠️ 高风险" },
            new[] { "浏览器控制",   "通过CDP协议控制浏览器，自动化Web操作",      "⚠️ 中风险" },
            new[] { "定时任务",     "基于Cron表达式的定时任务调度",               "✅ 低风险" },
            new[] { "Webhook",      "接收外部HTTP回调，触发Agent响应",            "✅ 低风险" },
            new[] { "多智能体",     "跨会话的任务分派与协调",                     "✅ 低风险" },
            new[] { "审批流程",     "敏感操作的确认审批工作流",                   "🔒 强制" }
        });
        Caption(b, "表3-1  OpenClaw核心内置工具分类与安全分级");
        H2(b, "3.2  Skills（技能系统）");
        P(b, "Skills是OpenClaw的可扩展能力单元，采用Markdown格式定义（.md文件），存放在~/.openclaw/workspace/skills/目录下。每个Skill文件包含能力描述和使用说明，Agent读取后即可理解并调用对应功能，无需重启服务。");
        AddImg(b, imgTools, ImgH(), "图3-1  OpenClaw工具与技能生态系统示意图");
        P(b, "Skills三大核心特点：");
        B(b, "零门槛创作：任何人都能编写Markdown文档为Agent添加新能力，无需编写代码");
        B(b, "5000+社区生态：ClawHub社区技能市场覆盖邮件管理、服务器监控、日程管理、企业微信、飞书等场景");
        B(b, "热加载安装：Skills安装时仅下载文件，不影响运行中的Agent进程，实现无缝扩展");
        Tbl(b, new[] { "Skills分类", "代表技能", "功能描述" }, new[] {
            new[] { "办公协作",   "飞书、企业微信、钉钉",         "消息推送、日程管理、文档操作" },
            new[] { "开发运维",   "Git、数据库、Web服务器",        "代码管理、数据库查询、进程监控" },
            new[] { "信息获取",   "网页搜索、RSS订阅、新闻聚合",   "实时信息抓取与摘要" },
            new[] { "文件处理",   "PDF解析、Office转换、图片处理", "文档格式转换与内容提取" },
            new[] { "定时自动化", "Cron调度、每日提醒、定期报告",  "周期性任务的自动执行" }
        });
        Caption(b, "表3-2  OpenClaw Skills分类体系（ClawHub 2026Q1）");
        H2(b, "3.3  记忆系统（Memory）");
        P(b, "OpenClaw的记忆系统采用多层次存储设计，保障会话连续性与个性化适应：");
        B(b, "文件系统记忆：明文Markdown文件存储于~/.openclaw/workspace/，包括AGENTS.md（工作区规范）、SOUL.md（人格定义）、TOOLS.md（工具笔记）、MEMORY.md（长期记忆）等");
        B(b, "结构化记忆：SQLite数据库存储会话日志，支持向量嵌入（Vector Embeddings）实现语义搜索，让Agent从历史会话中快速检索相关内容");
        B(b, "每日日志：memory/YYYY-MM-DD.md记录每日工作日志，形成可追溯的成长轨迹");
        P(b, "三层记忆协同工作，使OpenClaw能够感知上下文、记住用户偏好、在长周期任务中保持一致性。");
        H2(b, "3.4  多智能体与并发协作");
        P(b, "OpenClaw支持多智能体协作模式：");
        B(b, "隔离实例：不同消息渠道路由到彼此隔离的独立Agent实例，每个实例拥有独立workspace和记忆");
        B(b, "任务委托：主Agent将任务分解后委托给子Agent（subagent）并行执行，显著提升复杂任务处理效率");
        B(b, "编排协调：通过MCP协议连接多个专业化Agent，实现\"主脑调度+专家执行\"的协同工作流");
        PB(b);

        // ── 四、安全模型 ──
        H1(b, "四、安全模型");
        P(b, "OpenClaw赋予Agent极高的系统权限（Shell访问、文件读写、浏览器控制），这既是其强大能力的来源，也带来了潜在的安全风险。2026年曝光的安全事件包括CVE-2026-25253（WebSocket劫持漏洞）和\"ClawHavoc\"供应链攻击，引起了广泛重视。");
        AddImg(b, imgSec, ImgH(), "图4-1  OpenClaw安全防护体系：Docker沙箱 + WASM隔离");
        H2(b, "4.1  安全机制");
        Tbl(b, new[] { "安全机制", "描述", "实现方式" }, new[] {
            new[] { "操作审批（Approval）",       "敏感工具调用默认需要用户确认",       "Gateway审批工作流，防止未授权操作" },
            new[] { "范围权限（Scoped Perms）", "工具调用权限可精细化控制",            "基于角色的权限模型（RBAC）" },
            new[] { "Docker沙箱（NanoClaw）",    "Agent运行在独立容器中隔离",           "Docker容器技术，进程级隔离" },
            new[] { "WASM沙箱（未来）",          "每个Skill运行在独立WASM虚拟机",        "WebAssembly字节码级别隔离（路线图）" },
            new[] { "发送者白名单",              "只响应已配对/授权的用户",             "Channel层配对验证机制" }
        });
        Caption(b, "表4-1  OpenClaw安全机制全景图");
        H2(b, "4.2  安全最佳实践");
        B(b, "在专用设备/账户中运行，避免与生产环境混合");
        B(b, "仅在本地监听（127.0.0.1），不对公网暴露Gateway端口");
        B(b, "安装社区Skills前审查其内容，防止恶意代码注入");
        B(b, "定期更新OpenClaw版本，及时修补已知漏洞");
        B(b, "使用NanoClaw安全分支替代标准版，获得Docker容器级隔离");
        PB(b);

        // ── 五、技术趋势 ──
        H1(b, "五、2026技术趋势与未来展望");
        AddImg(b, imgTrends, ImgH(), "图5-1  2026年AI Agent技术趋势与OpenClaw生态演进路线图");
        H2(b, "5.1  从\"提示词工程\"到\"意图编排\"");
        P(b, "2026年，业界对AI Agent的使用方式正在从精心设计提示词（Prompt Engineering）向意图编排（Intent Orchestration）转变。开发者不再逐字编写Prompt，而是通过高层次的意图描述，让Agent自主规划执行路径，调用所需工具完成复杂任务。OpenClaw的Skills系统和多工具调用机制正是这一趋势的典型代表。");
        H2(b, "5.2  WebAssembly沙箱化");
        P(b, "WASM沙箱技术将成为AI Agent安全隔离的行业标准。预计2026年底，主流开源Agent框架都将提供WASM运行时选项，实现能力粒度的精确管控。OpenClaw已在路线图中规划Native WASM支持。");
        H2(b, "5.3  向量数据库与本地记忆增强");
        P(b, "OpenClaw正在推进Native Vector Embeddings支持，将向量相似度搜索深度集成到SQLite数据库中，Agent能在本地完成语义记忆检索，无需依赖云端向量服务，进一步强化隐私保护。");
        H2(b, "5.4  MCP协议成为行业标准");
        P(b, "Model Context Protocol（MCP）正快速获得广泛支持。继Anthropic、OpenClaw之后，预计Google、Microsoft等厂商也将全面支持MCP标准。跨平台的工具生态将因此打破壁垒，开发者可以一次编写工具，任意AI平台复用。");
        H2(b, "5.5  多智能体协作深化");
        P(b, "多个专业化Agent协同工作将成为主流范式：");
        Tbl(b, new[] { "Agent角色", "职责定位", "代表工具/技能" }, new[] {
            new[] { "主脑Agent", "任务分解与调度协调", "AGENTS.md、意图理解" },
            new[] { "代码Agent", "代码开发与调试",    "Shell、Git、文件操作" },
            new[] { "数据Agent", "数据收集与分析",     "搜索、API调用、数据库" },
            new[] { "外联Agent", "沟通与信息传递",     "飞书、企业微信、邮件" }
        });
        Caption(b, "表5-1  多智能体协作中的角色分工体系");
        PB(b);

        // ── 六、总结 ──
        H1(b, "六、总结");
        P(b, "OpenClaw代表了2026年开源AI Agent发展的最高水位。它以Node.js为核心运行引擎，构建了Gateway—Channel—LLM三层架构，通过MCP协议与外部生态无缝连接；内置25+工具和5000+社区Skills，赋予AI在操作系统层面执行真实任务的能力；多层记忆系统保障了会话连续性与个性化适应；积极拥抱WASM沙箱化以应对安全挑战。");
        P(b, "随着MCP协议成为行业通用标准、意图编排范式深入人心，OpenClaw正在从\"工具\"进化为\"平台\"——一个连接AI大脑与数字世界的开放基础设施。对于开发者而言，现在是深入参与这一生态的最佳时机。");

        H1(b, "附录：OpenClaw 2026关键数据一览");
        Tbl(b, new[] { "指标维度", "数据" }, new[] {
            new[] { "代码规模",    "430,000+ 行（Node.js/TypeScript）" },
            new[] { "内置工具",    "25个核心工具" },
            new[] { "社区Skills",  "5,000+（ClawHub）" },
            new[] { "支持模型",    "10+ 商业模型 + 任意Ollama兼容模型" },
            new[] { "支持平台",    "飞书、Telegram、WhatsApp、Discord等20+平台" },
            new[] { "已知CVE",    "CVE-2026-25253（已修复）" },
            new[] { "安全分支",   "NanoClaw（Docker沙箱版）" },
            new[] { "协议支持",   "MCP Server + MCP Client双模式" }
        });
        Caption(b, "附表  OpenClaw 2026关键指标汇总");

        P(b, "报告编制：OpenClaw研究组  |  2026年4月");
        P(b, "© 2026 OpenClaw Research Group. 本报告基于公开资料整理，仅供参考。");

        // Finalize
        b.AppendChild(new SectionProperties(new PageSize { Width = 11906, Height = 16838 },
            new PageMargin { Top = 1440, Right = 1440, Bottom = 1440, Left = 1440, Header = 720, Footer = 720, Gutter = 0 }));
        mainPart.Document.Save();
        Console.WriteLine($"✅ Saved: /workspace/OpenClaw技术研究报告_图文版.docx  ({new FileInfo("/workspace/OpenClaw技术研究报告_图文版.docx").Length / 1024.0:F1} KB)");
    }
}
