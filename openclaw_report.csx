// Build: /root/.dotnet/dotnet build MiniMaxAIDocx.Cli/MiniMaxAIDocx.Cli.csproj -c Release
// Run:   /root/.dotnet/dotnet run --project MiniMaxAIDocx.Cli/MiniMaxAIDocx.Cli.csproj -c Release -- <args>
// This file: MiniMaxAIDocx.Cli/openclaw_report.csx (run via dotnet-script or compiled)
#r "nuget: DocumentFormat.OpenXml, 3.2.0"

using DocumentFormat.OpenXml;
using DocumentFormat.OpenXml.Packaging;
using DocumentFormat.OpenXml.Wordprocessing;
using System;
using System.Collections.Generic;

// ─────────────────────────────────────────────────────────────
// Report Content
// ─────────────────────────────────────────────────────────────
var title = "OpenClaw AI Agent 技术研究报告";
var subtitle = "2026年最新版";
var date = "2026年4月";

// Sections: (heading, level, body_text[])
var sections = new List<(string heading, int level, string[] body)>
{
    ("一、研究背景", 1, new[] {
        "1.1 AI Agent 发展趋势",
        "2026年被称为\"通用AI智能体元年\"。以OpenClaw为代表的开源自主Agent框架正在重塑人机协作方式。与传统聊天机器人不同，OpenClaw被设计为\"永远在线\"的数字工作者——它持续运行在用户本地硬件上，通过消息应用（飞书、WhatsApp、Telegram等）随时待命，主动执行任务而非被动应答。",
        "",
        "1.2 OpenClaw 的诞生",
        "OpenClaw是一个开源、自托管的AI Agent框架，最早于2024年公开亮相，2025—2026年快速迭代成熟。它核心理念是：将大语言模型的\"大脑\"与用户真实数字工具链（文件系统、浏览器、Shell、消息平台）深度连接，让AI真正在操作系统层面执行多步骤复杂任务。"
    }),

    ("二、技术原理与系统架构", 1, new[] {
        "2.1 三层架构设计",
        "OpenClaw采用清晰的三层分层架构，各层职责明确，协同完成从用户请求到任务完成的完整闭环：",
        "",
        "【表1：OpenClaw三层架构】",
        "层级|主要职责|关键技术",
        "Gateway层|会话生命周期管理|WebSocket、长连接",
        "Channel层|多平台消息适配|消息协议转换、路由",
        "LLM层|推理决策与工具调用|Function Calling、流式响应",
        "",
        "2.2 Gateway（网关层）",
        "Gateway是整个系统的中央控制平面，默认监听本地地址127.0.0.1:18789。它同时管理多个消息平台连接（飞书、Telegram、WhatsApp等），将收到的消息路由到相应的Agent会话，等待处理结果后通过正确渠道发回响应。Gateway本身不处理业务逻辑，仅负责连接与会话分发。",
        "",
        "2.3 Channel（渠道层）",
        "Channel层负责适配不同消息平台的协议与消息格式。OpenClaw通过可插拔的Channel模块接入各类IM工具，每个Channel将平台特定的消息格式统一转换为内部标准格式，再交给Gateway路由。这使得添加新平台支持只需实现对应的Channel适配器。",
        "",
        "2.4 LLM层",
        "LLM层是实际执行推理与决策的核心。OpenClaw采用模型无关（Model-Agnostic）设计，支持包括Anthropic Claude系列、OpenAI GPT-4o/5、DeepSeek V3、Google Gemini 2.0 Flash、Moonshot Kimi K2.5在内的主流商业模型，以及通过Ollama/LM Studio/vLLM接入的本地模型。该层还负责工具调用（Function Calling）和流式输出（Streaming Response）。",
        "",
        "2.5 MCP协议集成",
        "OpenClaw在2026年正式支持Model Context Protocol（MCP）标准。MCP是由Anthropic主导的开放标准，旨在为AI模型与外部工具/数据源之间提供统一、一致的连接协议。",
        "",
        "OpenClaw MCP支持两种工作模式：",
        "• MCP Server模式（openclaw mcp serve）：将OpenClaw作为MCP服务器暴露，允许外部MCP客户端（如Codex、Claude Code）连接到OpenClaw的对话会话并进行工具调用",
        "• MCP Client模式：OpenClaw通过MCP协议连接外部MCP服务器，实现对第三方工具和服务的集成",
        "",
        "MCP Server的核心机制：外部MCP客户端通过标准stdio协议连接OpenClaw Gateway（WebSocket），OpenClaw将已有路由会话暴露为MCP对话，并提供conversations_list、messages_read、events_poll、messages_send等标准化工具接口。"
    }),

    ("三、核心能力解析", 1, new[] {
        "3.1 工具系统（Built-in Tools）",
        "OpenClaw内置25个核心工具，覆盖Agent在操作系统层面的所有关键能力：",
        "",
        "【表2：核心内置工具】",
        "工具类别|具体功能",
        "Shell执行|执行任意Shell命令，支持sudo和交互式命令",
        "文件系统|读写、创建、删除、搜索本地文件",
        "浏览器控制|通过CDP协议控制浏览器，自动化Web操作",
        "定时任务|基于Cron表达式的定时任务调度",
        "Webhook|接收外部HTTP回调，触发Agent响应",
        "多智能体|跨会话的任务分派与协调",
        "审批流程|敏感操作的确认审批工作流",
        "",
        "3.2 Skills（技能系统）",
        "Skills是OpenClaw的可扩展能力单元，采用Markdown格式定义（.md文件），存放在~/.openclaw/workspace/skills/目录下。每个Skill文件包含能力描述和使用说明，Agent读取后即可理解并调用对应功能，无需重启服务。",
        "",
        "Skills特点：",
        "• 无需编码即可创作：任何人都能编写Markdown文档为Agent添加新能力",
        "• 社区生态丰富：ClawHub社区技能市场提供5000+社区技能，覆盖邮件管理、服务器监控、日程管理等场景",
        "• 增量安装：Skills安装时仅下载对应文件，不影响运行中的Agent进程",
        "",
        "3.3 记忆系统（Memory）",
        "OpenClaw的记忆系统是其保持会话连续性的关键，采用多层次存储设计：",
        "",
        "• 文件系统记忆：以明文Markdown文件存储在~/.openclaw/workspace/，包括AGENTS.md（工作区规范）、SOUL.md（人格定义）、TOOLS.md（工具笔记）、MEMORY.md（长期记忆）等",
        "• 结构化记忆：通过SQLite数据库存储会话日志，并支持向量嵌入（Vector Embeddings）实现语义搜索，让Agent能快速从历史会话中检索相关内容",
        "• 每日日志：memory/YYYY-MM-DD.md记录每日工作日志，形成可追溯的成长轨迹",
        "",
        "3.4 多智能体与并发",
        "OpenClaw支持多智能体协作：可将不同消息渠道路由到彼此隔离的独立Agent实例，每个实例拥有独立的workspace和记忆。也可由一个主Agent将任务委托给子Agent（subagent）并行执行，实现复杂的任务分解与协同。"
    }),

    ("四、安全模型", 1, new[] {
        "OpenClaw赋予Agent极高的系统权限（Shell访问、文件读写、浏览器控制），这既是其强大能力的来源，也带来了潜在的安全风险。2026年曝光的安全事件包括CVE-2026-25253（WebSocket劫持漏洞）和\"ClawHavoc\"供应链攻击，引起了广泛重视。",
        "",
        "4.1 安全机制",
        "• 操作审批（Approval）：敏感工具调用（如删除文件、发送外部请求）默认需要用户确认，通过审批工作流防止未经授权的操作",
        "• 范围权限（Scoped Permissions）：工具调用权限可精细化控制，避免\"一键越权\"",
        "• 沙箱隔离：NanoClaw安全分支采用Docker容器技术将Agent运行在隔离环境中，即使被攻陷也难以影响宿主机",
        "• 发送者白名单：基于消息平台的信任模型，只响应已配对/授权的用户",
        "",
        "4.2 安全最佳实践",
        "• 在专用设备/账户中运行，避免与生产环境混合",
        "• 仅在本地监听（127.0.0.1），不对公网暴露Gateway端口",
        "• 安装社区Skills前审查其内容，防止恶意代码注入",
        "• 定期更新OpenClaw版本，及时修补已知漏洞",
        "",
        "4.3 未来安全方向：WASM沙箱",
        "根据OpenClaw 2026路线图，下一代安全模型将基于WebAssembly（WASM）沙箱实现严格的能力隔离——每个Skill运行在独立的WASM虚拟机中，从根本上限制其对系统资源的访问。",
        ""
    }),

    ("五、2026技术趋势与未来展望", 1, new[] {
        "5.1 从\"提示词工程\"到\"意图编排\"",
        "2026年，业界对AI Agent的使用方式正在从精心设计提示词（Prompt Engineering）向意图编排（Intent Orchestration）转变。开发者不再逐字编写Prompt，而是通过高层次的意图描述，让Agent自主规划执行路径，调用所需工具完成复杂任务。OpenClaw的Skills系统和多工具调用机制正是这一趋势的典型代表。",
        "",
        "5.2 WebAssembly沙箱化",
        "WASM沙箱技术将成为AI Agent安全隔离的行业标准。预计2026年底，主流开源Agent框架都将提供WASM运行时选项，实现能力粒度的精确管控。",
        "",
        "5.3 向量数据库与本地记忆增强",
        "OpenClaw正在推进Native Vector Embeddings支持，将向量相似度搜索深度集成到SQLite数据库中。这意味着Agent能在本地完成语义记忆检索，无需依赖云端向量服务，进一步强化隐私保护。",
        "",
        "5.4 MCP协议成为行业标准",
        "Model Context Protocol（MCP）正快速获得广泛支持。继Anthropic、OpenClaw之后，预计Google、Microsoft等厂商也将全面支持MCP标准。跨平台的工具生态将因此打破壁垒，开发者可以一次编写工具，任意AI平台复用。",
        "",
        "5.5 多智能体协作深化",
        "多个专业化Agent协同工作将成为主流范式。一个\"主脑\"Agent负责任务分解与调度，多个\"专家\"Agent各自处理特定领域任务（如代码开发、数据分析、外联沟通），这将显著提升复杂任务的处理效率与质量。",
        ""
    }),

    ("六、总结", 1, new[] {
        "OpenClaw代表了2026年开源AI Agent发展的最高水位。它以Node.js为核心运行引擎，构建了Gateway—Channel—LLM三层架构，通过MCP协议与外部生态无缝连接；内置25+工具和5000+社区Skills，赋予AI在操作系统层面执行真实任务的能力；多层记忆系统保障了会话连续性与个性化适应；积极拥抱WASM沙箱化以应对安全挑战。",
        "",
        "随着MCP协议成为行业通用标准、意图编排范式深入人心，OpenClaw正在从\"工具\"进化为\"平台\"——一个连接AI大脑与数字世界的开放基础设施。对于开发者而言，现在是深入参与这一生态的最佳时机。",
        "",
        "报告编制：OpenClaw研究组 | 2026年4月"
    }),
};

// ─────────────────────────────────────────────────────────────
// C# Code to generate the DOCX
// ─────────────────────────────────────────────────────────────

string outputPath = "/workspace/OpenClaw技术研究报告.docx";

var corpBlue = "2F5496";
var darkGray = "404040";
var lightBlue = "D6E4F0";

using var doc = WordprocessingDocument.Create(outputPath, WordprocessingDocumentType.Document);
var mainPart = doc.AddMainDocumentPart();
mainPart.Document = new Document(new Body());

var body = mainPart.Document.Body!;

// Page setup: A4
var sectPr = new SectionProperties(
    new PageSize { Width = 11906, Height = 16838 },
    new PageMargin { Top = 1440, Right = 1440, Bottom = 1440, Left = 1440, Header = 720, Footer = 720, Gutter = 0 }
);

// Styles helper
void AddHeading(Body b, string text, int level)
{
    var p = new Paragraph();
    var pPr = new ParagraphProperties(
        new SpacingBetweenLines { Before = level == 1 ? "400" : "240", After = "120" }
    );
    string styleId = level == 1 ? "Heading1" : "Heading2";
    pPr.AppendChild(new ParagraphStyleId { Val = styleId });
    p.AppendChild(pPr);

    var r = new Run();
    var rPr = new RunProperties(
        new Bold(),
        new FontSize { Val = level == 1 ? "36" : "28" },
        new Color { Val = corpBlue }
    );
    r.AppendChild(rPr);
    r.AppendChild(new Text(text));
    p.AppendChild(r);
    b.AppendChild(p);
}

void AddBody(Body b, string text)
{
    if (string.IsNullOrWhiteSpace(text)) { return; }
    var p = new Paragraph();
    var pPr = new ParagraphProperties(
        new SpacingBetweenLines { After = "160", Line = "276", LineRule = LineSpacingRuleValues.Auto }
    );
    p.AppendChild(pPr);
    var r = new Run();
    var rPr = new RunProperties(
        new FontSize { Val = "21" },
        new Color { Val = darkGray }
    );
    r.AppendChild(rPr);
    r.AppendChild(new Text(text) { Space = SpaceProcessingModeValues.Preserve });
    p.AppendChild(r);
    b.AppendChild(p);
}

void AddTable(Body b, string[] headers, string[][] rows)
{
    var tbl = new Table();
    // Table properties
    var tblPr = new TableProperties(
        new TableWidth { Width = "5000", Type = TableWidthUnitValues.Pct },
        new TableBorders(
            new TopBorder { Val = BorderValues.Single, Size = 8, Color = corpBlue },
            new BottomBorder { Val = BorderValues.Single, Size = 8, Color = corpBlue },
            new LeftBorder { Val = BorderValues.Single, Size = 4, Color = "AAAAAA" },
            new RightBorder { Val = BorderValues.Single, Size = 4, Color = "AAAAAA" },
            new InsideHorizontalBorder { Val = BorderValues.Single, Size = 4, Color = "CCCCCC" },
            new InsideVerticalBorder { Val = BorderValues.Single, Size = 4, Color = "CCCCCC" }
        )
    );
    tbl.AppendChild(tblPr);

    // Grid
    var tblGrid = new TableGrid();
    for (int i = 0; i < headers.Length; i++) tblGrid.AppendChild(new GridColumn { Width = "2000" });
    tbl.AppendChild(tblGrid);

    // Header row
    var hrow = new TableRow();
    for (int i = 0; i < headers.Length; i++)
    {
        var tc = new TableCell();
        tc.AppendChild(new TableCellProperties(new Shading { Fill = corpBlue }));
        var cp = new Paragraph();
        var cr = new Run();
        cr.AppendChild(new RunProperties(new Bold(), new FontSize { Val = "20" }, new Color { Val = "FFFFFF" }));
        cr.AppendChild(new Text(headers[i]));
        cp.AppendChild(cr);
        tc.AppendChild(cp);
        hrow.AppendChild(tc);
    }
    tbl.AppendChild(hrow);

    // Data rows
    foreach (var row in rows)
    {
        var tr = new TableRow();
        for (int i = 0; i < row.Length; i++)
        {
            var tc = new TableCell();
            var cp = new Paragraph();
            var cr = new Run();
            cr.AppendChild(new RunProperties(new FontSize { Val = "20" }, new Color { Val = darkGray }));
            cr.AppendChild(new Text(row[i]) { Space = SpaceProcessingModeValues.Preserve });
            cp.AppendChild(cr);
            tc.AppendChild(cp);
            tr.AppendChild(tc);
        }
        tbl.AppendChild(tr);
    }

    b.AppendChild(tbl);
    b.AppendChild(new Paragraph(new Run(new Text("")))); // spacing
}

// ── COVER PAGE ──
var coverTitle = new Paragraph();
coverTitle.AppendChild(new ParagraphProperties(
    new Justification { Val = JustificationValues.Center },
    new SpacingBetweenLines { Before = "2400", After = "400" }
));
var ctr = new Run();
ctr.AppendChild(new RunProperties(new Bold(), new FontSize { Val = "56" }, new Color { Val = corpBlue }));
ctr.AppendChild(new Text("OpenClaw AI Agent"));
coverTitle.AppendChild(ctr);
body.AppendChild(coverTitle);

var coverSub = new Paragraph();
coverSub.AppendChild(new ParagraphProperties(
    new Justification { Val = JustificationValues.Center },
    new SpacingBetweenLines { After = "200" }
));
var csr = new Run();
csr.AppendChild(new RunProperties(new Bold(), new FontSize { Val = "44" }, new Color { Val = corpBlue }));
csr.AppendChild(new Text("技术研究报告"));
coverSub.AppendChild(csr);
body.AppendChild(coverSub);

var coverYear = new Paragraph();
coverYear.AppendChild(new ParagraphProperties(
    new Justification { Val = JustificationValues.Center },
    new SpacingBetweenLines { After = "800" }
));
var cyr = new Run();
cyr.AppendChild(new RunProperties(new FontSize { Val = "28" }, new Color { Val = "888888" }));
cyr.AppendChild(new Text("2026年最新版"));
coverYear.AppendChild(cyr);
body.AppendChild(coverYear);

var coverMeta = new Paragraph();
coverMeta.AppendChild(new ParagraphProperties(
    new Justification { Val = JustificationValues.Center },
    new SpacingBetweenLines { After = "200" }
));
var cmr = new Run();
cmr.AppendChild(new RunProperties(new FontSize { Val = "22" }, new Color { Val = "666666" }));
cmr.AppendChild(new Text($"编制日期：{date}"));
coverMeta.AppendChild(cmr);
body.AppendChild(coverMeta);

var coverAuthor = new Paragraph();
coverAuthor.AppendChild(new ParagraphProperties(
    new Justification { Val = JustificationValues.Center },
    new SpacingBetweenLines { After = "200" }
));
var car = new Run();
car.AppendChild(new RunProperties(new FontSize { Val = "22" }, new Color { Val = "666666" }));
car.AppendChild(new Text("研究编制：OpenClaw研究组"));
coverAuthor.AppendChild(car);
body.AppendChild(coverAuthor);

body.AppendChild(new Paragraph(new Run(new Break { Type = BreakValues.Page })));

// ── SECTIONS ──
foreach (var (heading, level, bodyTexts) in sections)
{
    // Check if this section contains a table marker
    bool hasTable = false;
    List<string> tableHeaders = new();
    List<string[]> tableRows = new();

    foreach (var bt in bodyTexts)
    {
        if (bt.StartsWith("【表"))
        {
            hasTable = true;
            tableHeaders.Clear();
            tableRows.Clear();
            continue;
        }
        if (hasTable && bt.Contains("|"))
        {
            var cols = bt.Split('|', StringSplitOptions.RemoveEmptyEntries);
            if (tableHeaders.Count == 0)
            {
                foreach (var c in cols) tableHeaders.Add(c.Trim());
            }
            else
            {
                var row = new List<string>();
                foreach (var c in cols) row.Add(c.Trim());
                tableRows.Add(row.ToArray());
            }
        }
        else if (hasTable && !bt.Contains("|") && !string.IsNullOrWhiteSpace(bt))
        {
            hasTable = false;
        }
    }

    // We handle table separately - just add heading + body without table lines
    AddHeading(body, heading, level);

    foreach (var bt in bodyTexts)
    {
        if (bt.StartsWith("【表")) continue; // skip table title line
        if (string.IsNullOrWhiteSpace(bt) || bt == bodyTexts[0]) { AddBody(body, bt); continue; }
        if (bt.Contains("|")) continue; // table content lines handled above
        AddBody(body, bt);
    }

    if (hasTable && tableHeaders.Count > 0 && tableRows.Count > 0)
    {
        AddTable(body, tableHeaders.ToArray(), tableRows.ToArray());
    }
}

// Add sectPr
body.AppendChild(sectPr);

// Save styles part
var stylesPart = mainPart.AddNewPart<StyleDefinitionsPart>();
var styles = new Styles();
styles.Save();

// Document properties
var docProps = doc.AddCoreFilePropertiesPart();
var nsMgr = new System.Xml.XmlNamespaceManager(new System.Xml.NameTable());
nsMgr.AddNamespace("d", "http://purl.org/dc/elements/1.1/");
docProps.StreamValue = @"<?xml version=""1.0"" encoding=""UTF-8""?>
<Properties xmlns=""http://schemas.openxmlformats.org/package/2006/metadata/core-properties"">
  <title>OpenClaw AI Agent 技术研究报告</title>
  <creator>OpenClaw研究组</creator>
  <date>2026-04-04</date>
</Properties>";

mainPart.Document.Save();
Console.WriteLine($"Report saved to: {outputPath}");
