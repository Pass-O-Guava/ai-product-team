#!/usr/bin/env python3
import os, re
D = "/workspace/slides"
os.makedirs(D, exist_ok=True)

def W(fname, html):
    open(os.path.join(D, fname), "w", encoding="utf-8").write(html)
    sz = len(html)
    print(f"OK {fname} ({sz}b)")

def tt(d): return d.replace("{","{{").replace("}","}}")

# Slide 06
W("slide06.html", """<!DOCTYPE html><html lang="zh"><head><meta charset="UTF-8"><title>slide06</title><style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:"PingFang SC","Microsoft YaHei",sans-serif;background:#0a0f2e;color:#fff}
.slide{width:100vw;height:100vh;display:flex;flex-direction:column;padding:60px 80px;position:relative}
.tag{font-size:13px;letter-spacing:3px;color:#10b981;text-transform:uppercase;font-weight:600;margin-bottom:20px}
.sn{font-size:13px;color:#334155;font-weight:700;margin-bottom:20px}
.scqa{position:absolute;top:60px;right:80px;background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.3);border-radius:8px;padding:10px 18px;font-size:13px;color:#10b981;font-weight:600;letter-spacing:1px}
h1{font-size:38px;font-weight:700;color:#fff;margin-bottom:8px}
.sub{font-size:17px;color:#64748b;margin-bottom:36px}
.lay{display:grid;grid-template-columns:1.1fr 1fr;gap:56px;align-items:center;flex:1}
.sr{grid-template-columns:repeat(2,1fr);display:grid;gap:16px}
.st2{background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);border-radius:14px;padding:20px 18px;text-align:center}
.v{font-size:36px;font-weight:800;color:#3b82f6;line-height:1}
.vg{color:#10b981}.vr{color:#ef4444}.vo{color:#f59e0b}
.lbl{font-size:13px;color:#94a3b8;margin-top:8px;line-height:1.4}
.biz{background:rgba(16,185,129,0.07);border:1px solid rgba(16,185,129,0.2);border-radius:16px;padding:28px}
.biz-t{font-size:15px;font-weight:700;color:#10b981;margin-bottom:18px;letter-spacing:1px}
.bi{display:flex;align-items:flex-start;gap:12px;font-size:14px;color:#cbd5e1;line-height:1.6;margin-bottom:12px}
.bi .a{color:#10b981;font-weight:700;flex-shrink:0}
.bi strong{color:#fff}
.hbar{display:flex;align-items:center;gap:16px;background:rgba(59,130,246,0.07);border-radius:12px;padding:16px 22px;margin-top:16px}
.ft{position:absolute;bottom:36px;left:80px;right:80px;display:flex;justify-content:space-between}
.ft span{font-size:12px;color:#475569}
</style></head><body>
<div class="slide">
<div class="tag">A &#8212; Answer 成果一</div><div class="sn">06 / 14</div>
<div class="scqa">SCQA &#xb7; A</div>
<h1>意图识别准确率稳定在 95%+</h1>
<div class="sub">技术指标 &#8594; 商业价值：误解率降低 = 人工介入减少 = 运营成本下降</div>
<div class="lay">
<div>
<div class="sr">
<div class="st2"><div class="v">95%+</div><div class="lbl">意图识别准确率<br>覆盖8个产线场景</div></div>
<div class="st2"><div class="v vg">+9.9pt</div><div class="lbl">L1准确率提升<br>86.5% &#8594; 96.4%</div></div>
<div class="st2"><div class="v vr">0条</div><div class="lbl">PARSE_ERROR<br>问题全部清零</div></div>
<div class="st2"><div class="v vo">693条</div><div class="lbl">测试用例<br>100%质检覆盖</div></div>
</div>
<div class="hbar"><div><strong style="color:#fff">沉淀：</strong>5轮提示词迭代、14个提示词文件、意图视图表7版、质检规范文档2版</div></div>
</div>
<div class="biz">
<div class="biz-t">业务价值翻译</div>
<div class="bi"><span class="a">&#8594;</span><div>覆盖<strong>8个业务场景</strong>，用户交互误解率显著降低</div></div>
<div class="bi"><span class="a">&#8594;</span><div>PARSE_ERROR清零 = <strong>系统具备稳定交付能力</strong></div></div>
<div class="bi"><span class="a">&#8594;</span><div>人工介入减少 = <strong>客服/运营效率提升</strong></div></div>
<div class="bi"><span class="a">&#8594;</span><div>为<strong>业务智能体大规模部署</strong>奠定基础</div></div>
<div class="bi"><span class="a">&#x2713;</span><div>用户满意度&#x2191; &nbsp; 人工成本&#x2193; &nbsp; 业务扩展能力&#x2191;</div></div>
</div>
</div>
<div class="ft"><span>SCQA模型 &#xb7; 2026年Q1 AI模型工程团队述职</span><span>06 / 14</span></div>
</div></body></html>""")

# Slide 07
W("slide07.html", """<!DOCTYPE html><html lang="zh"><head><meta charset="UTF-8"><title>slide07</title><style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:"PingFang SC","Microsoft YaHei",sans-serif;background:#0a0f2e;color:#fff}
.slide{width:100vw;height:100vh;display:flex;flex-direction:column;padding:60px 80px;position:relative}
.tag{font-size:13px;letter-spacing:3px;color:#8b5cf6;text-transform:uppercase;font-weight:600;margin-bottom:20px}
.sn{font-size:13px;color:#334155;font-weight:700;margin-bottom:20px}
.scqa{position:absolute;top:60px;right:80px;background:rgba(139,92,246,0.1);border:1px solid rgba(139,92,246,0.3);border-radius:8px;padding:10px 18px;font-size:13px;color:#8b5cf6;font-weight:600;letter-spacing:1px}
h1{font-size:38px;font-weight:700;color:#fff;margin-bottom:8px}
.sub{font-size:17px;color:#64748b;margin-bottom:36px}
.lay{display:grid;grid-template-columns:1fr 1fr;gap:52px;align-items:center;flex:1}
.jump{text-align:center;background:rgba(139,92,246,0.07);border:1px solid rgba(139,92,246,0.2);border-radius:20px;padding:32px;margin-bottom:18px}
.jump-lbl{font-size:14px;color:#94a3b8;margin-bottom:16px}
.jump-nums{display:flex;align-items:center;justify-content:center;gap:32px}
.n1{font-size:72px;font-weight:800;color:#475569}
.arr{font-size:40px;color:#8b5cf6}
.n2{font-size:80px;font-weight:800;color:#8b5cf6}
.jump-cap{margin-top:16px;font-size:14px;color:#94a3b8}
.biz{background:rgba(139,92,246,0.07);border:1px solid rgba(139,92,246,0.2);border-radius:16px;padding:24px}
.biz-t{font-size:14px;font-weight:700;color:#a78bfa;margin-bottom:14px}
.bi{display:flex;align-items:flex-start;gap:10px;font-size:13px;color:#cbd5e1;line-height:1.6;margin-bottom:10px}
.bi .a{color:#8b5cf6;font-weight:700;flex-shrink:0}
.bi strong{color:#fff}
.rc{display:flex;flex-direction:column;gap:14px}
.mc{background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:18px 20px}
.mc-t{font-size:12px;color:#94a3b8;margin-bottom:6px}
.mc-v{font-size:22px;font-weight:700;color:#8b5cf6;margin-bottom:3px}
.mc-d{font-size:12px;color:#64748b}
.ft{position:absolute;bottom:36px;left:80px;right:80px;display:flex;justify-content:space-between}
.ft span{font-size:12px;color:#475569}
</style></head><body>
<div class="slide">
<div class="tag">A &#8212; Answer 成果二</div><div class="sn">07 / 14</div>
<div class="scqa">SCQA &#xb7; A</div>
<h1>规划能力：26% &#8594; 52%，业务场景翻倍提升</h1>
<div class="sub">技术指标 &#8594; 商业价值：排障准确率翻倍 = 自动化程度提升 = 运维成本下降</div>
<div class="lay">
<div>
<div class="jump">
<div class="jump-lbl">Cloudnet排障场景 &#xb7; Qwen3-4B LoRA微调后</div>
<div class="jump-nums"><span class="n1">26%</span><span class="arr">&#8594;</span><span class="n2">52%</span></div>
<div class="jump-cap">业务数据驱动规划能力 &#xb7; 翻倍增长</div>
</div>
<div class="biz">
<div class="biz-t">业务价值翻译</div>
<div class="bi"><span class="a">&#8594;</span><div>排障准确率翻倍 = <strong>更多故障可自动修复</strong></div></div>
<div class="bi"><span class="a">&#8594;</span><div>自动化程度提升 = <strong>人工干预减少，MTTR下降</strong></div></div>
<div class="bi"><span class="a">&#8594;</span><div>验证了<strong>"业务数据驱动规划能力"</strong>技术路线</div></div>
<div class="bi"><span class="a">&#x2713;</span><div>故障自愈率&#x2191; &nbsp; MTTR&#x2193;</div></div>
</div>
</div>
<div class="rc">
<div class="mc"><div class="mc-t">测评体系</div><div class="mc-v">2套</div><div class="mc-d">PlanBench + DeepPlanning 通用测评集</div></div>
<div class="mc"><div class="mc-t">业务测评集</div><div class="mc-v">40个</div><div class="mc-d">Cloudnet智能体排障场景</div></div>
<div class="mc"><div class="mc-t">闭环验证</div><div class="mc-v">完整</div><div class="mc-d">测评 &#8594; 分析 &#8594; 训练 &#8594; 验证</div></div>
<div class="mc"><div class="mc-t">Q2目标（通用规划）</div><div class="mc-v">40%+</div><div class="mc-d">PlanBench准确率（当前9.6%，提升30%+）</div></div>
</div>
</div>
<div class="ft"><span>SCQA模型 &#xb7; 2026年Q1 AI模型工程团队述职</span><span>07 / 14</span></div>
</div></body></html>""")

print("Done slides 06-07")
