#!/usr/bin/env python3
"""Generate slides 08-14"""
import os
D = "/workspace/slides"
os.makedirs(D, exist_ok=True)
def W(f, c): open(os.path.join(D, f), "w", encoding="utf-8").write(c); print(f"OK {f}")

CSS = """*{margin:0;padding:0;box-sizing:border-box}
body{font-family:"PingFang SC","Microsoft YaHei",sans-serif;background:#0a0f2e;color:#fff}
.slide{width:100vw;height:100vh;display:flex;flex-direction:column;padding:60px 80px;position:relative}
.tag{font-size:13px;letter-spacing:3px;text-transform:uppercase;font-weight:600;margin-bottom:20px}
.sn{font-size:13px;color:#334155;font-weight:700;margin-bottom:20px}
.scqa{position:absolute;top:60px;right:80px;border-radius:8px;padding:10px 18px;font-size:13px;font-weight:600;letter-spacing:1px}
h1{font-size:38px;font-weight:700;color:#fff;margin-bottom:8px}
.sub{font-size:17px;color:#64748b;margin-bottom:32px}
.lay{display:grid;gap:48px;align-items:center;flex:1}
.st{font-size:14px;font-weight:700;color:#93c5fd;margin-bottom:14px;padding-bottom:8px}
.pi{background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:14px 18px;margin-bottom:10px}
.ph{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.pn{font-size:12px;color:#94a3b8}
.bdg{padding:2px 8px;border-radius:5px;font-size:11px;font-weight:700}
.bb{background:rgba(59,130,246,0.2);color:#3b82f6}
.bg2{background:rgba(16,185,129,0.2);color:#10b981}
.pm{display:flex;gap:20px}
.m{text-align:center}
.mv{font-size:22px;font-weight:800;color:#3b82f6}
.mvg{color:#10b981}
.ml{font-size:11px;color:#64748b;margin-top:3px}
.bar{height:5px;background:rgba(255,255,255,0.05);border-radius:3px;margin-top:8px}
.biz{border-radius:16px;padding:22px}
.biz_t{font-size:13px;font-weight:700;margin-bottom:12px}
.bi{display:flex;align-items:flex-start;gap:10px;font-size:12px;color:#cbd5e1;line-height:1.6;margin-bottom:8px}
.bi_a{font-weight:700;flex-shrink:0}
.ft{position:absolute;bottom:36px;left:80px;right:80px;display:flex;justify-content:space-between}
.ft span{font-size:12px;color:#475569}"""

def page(num, tag_color, scqa_bg, scqa_border, scqa_color, h1, sub, body_content, footer=None):
    footer = footer or f"{num} / 14"
    return f'''<!DOCTYPE html><html lang="zh"><head><meta charset="UTF-8"><title>slide{num}</title><style>{CSS}</style></head><body>
<div class="slide">
<div class="tag" style="color:{tag_color}">{"A \u2014 Answer" if num>=6 else ""} {num if num<=5 else ""}</div>
<div class="sn">{footer}</div>
<div class="scqa" style="background:{scqa_bg};border:1px solid {scqa_border};color:{scqa_color}">SCQA</div>
<h1>{h1}</h1>
<div class="sub">{sub}</div>
{body_content}
<div class="ft"><span>SCQA\u6a21\u578b \u00b7 2026\u5e74Q1 AI\u6a21\u578b\u5de5\u7a0b\u56e2\u961f\u8f9e\u804c</span><span>{footer}</span></div>
</div></body></html>'''

# SLIDE 08: 推理优化
body08 = '''<div class="lay" style="grid-template-columns:1fr 1fr">
<div>
<div class="st" style="border-bottom:1px solid rgba(59,130,246,0.15)">TTFT\uff08\u9996\u5b57\u54cd\u5e94\uff09&amp;\u541e\u541e\u4f18\u5316\u6570\u636e</div>
<div class="pi"><div class="ph"><span class="pn">NV 4P4D \u591a\u8f6e\u5bf9\u8bdd</span><div style="display:flex;gap:6px"><span class="bdg bb">\u541e\u541e+10%</span><span class="bdg bg2">TTFT -17.5%</span></div></div><div class="pm"><div class="m"><div class="mv">-17.5%</div><div class="ml">TTFT\u964d\u4f4e</div></div><div class="m"><div class="mv mvg">+10%</div><div class="ml">\u541e\u541e\u63d0\u5347</div></div><div class="m"><div class="mv">8\u8f6e</div><div class="ml">\u591a\u8f6e\u5bf9\u8bdd</div></div></div><div class="bar"><div style="height:5px;width:82%;background:linear-gradient(90deg,#3b82f6,#60a5fa);border-radius:3px"></div></div></div>
<div class="pi"><div class="ph"><span class="pn">1P1D \u591aDP\u7cbe\u7ec6\u5316\u8c03\u5ea6</span><div style="display:flex;gap:6px"><span class="bdg bb">\u541e\u541e+3.5%</span><span class="bdg bg2">TTFT -9%</span></div></div><div class="pm"><div class="m"><div class="mv">-9%</div><div class="ml">TTFT\u964d\u4f4e</div></div><div class="m"><div class="mv mvg">+3.5%</div><div class="ml">\u541e\u541e\u63d0\u5347</div></div><div class="m"><div class="mv">\u7cbe\u7ec6\u5316</div><div class="ml">DP\u914d\u7f6e</div></div></div><div class="bar"><div style="height:5px;width:60%;background:linear-gradient(90deg,#10b981,#34d399);border-radius:3px"></div></div></div>
<div class="pi"><div class="ph"><span class="pn">\u8d85\u8282\u70b9 DeepSeek-R1</span><div style="display:flex;gap:6px"><span class="bdg bb">\u541e\u541e+1%</span><span class="bdg bg2">TTFT -7%</span></div></div><div class="pm"><div class="m"><div class="mv">-7%</div><div class="ml">TTFT\u5747\u503c</div></div><div class="m"><div class="mv mvg">-5%</div><div class="ml">P90\u65f6\u5ef6</div></div><div class="m"><div class="mv">\u56fd\u4ea7</div><div class="ml">\u8d85\u8282\u70b9</div></div></div><div class="bar"><div style="height:5px;width:45%;background:linear-gradient(90deg,#8b5cf6,#a78bfa);border-radius:3px"></div></div></div>
</div>
<div>
<div class="st" style="border-bottom:1px solid rgba(59,130,246,0.15)">\u6838\u5fc3\u7a81\u7834\uff1a\u7eaf\u7b97\u6cd5\u4f18\u5316\uff0c\u96f6\u786c\u4ef6\u6295\u5165</div>
<div class="pi" style="margin-bottom:16px"><div style="font-size:13px;color:#fff;font-weight:600;margin-bottom:6px">\u7f13\u5b58\u611f\u77e5\u8c03\u5ea6\u539f\u7406</div><div style="font-size:12px;color:#94a3b8;line-height:1.7">\u901a\u8fc7\u5206\u6790KV Cache\u547d\u4e2d\u60c5\u51b5\u4f18\u5316\u8bf7\u6c42\u8c03\u5ea6\uff0c<strong style="color:#fff">ROI\u6781\u9ad8</strong>\uff0c\u4e0d\u4f9d\u8d56\u786c\u4ef6\u5347\u7ea7\u3002</div></div>
<div class="biz" style="background:rgba(16,185,129,0.07);border:1px solid rgba(16,185,129,0.2)">
<div class="biz_t" style="color:#10b981">\u5546\u4e1a\u4ef7\u503c\u7ffb\u8bd1</div>
<div class="bi"><span class="bi_a" style="color:#10b981">\u2192</span><div>\u901a\u8fc7KV Cache\u4f18\u5316\u8bf7\u6c42\u8c03\u5ea6\uff0c<strong style="color:#fff">ROI\u6781\u9ad8</strong></div></div>
<div class="bi"><span class="bi_a" style="color:#10b981">\u2192</span><div>TTFT -17.5% = \u7528\u6237\u611f\u77e5<strong style="color:#fff">\u54cd\u5e94\u901f\u5ea6\u660e\u663e\u52a0\u5feb</strong></div></div>
<div class="bi"><span class="bi_a" style="color:#10b981">\u2192</span><div>\u541e\u541e+10% = <strong style="color:#fff">\u76f8\u540c\u786c\u4ef6\u627f\u8f7d\u66f4\u591a\u5e76\u53d1\u7528\u6237</strong></div></div>
<div class="bi"><span class="bi_a" style="color:#10b981">\u2192</span><div><strong style="color:#fff">\u96f6\u989d\u5916\u786c\u4ef6\u6295\u5165</strong>\uff0c\u7eaf\u7b97\u6cd5\u4f18\u5316</div></div>
</div>
</div>
</div>'''

W("slide08.html", page(8, "#3b82f6", "rgba(59,130,246,0.1)", "rgba(59,130,246,0.3)", "#3b82f6",
    "\u63a8\u7406\u6027\u80fd\u4f18\u5316\uff1a\u7f13\u5b58\u611f\u77e5\u8c03\u5ea6\u5168\u9762\u843d\u5730",
    "\u6280\u672f\u6307\u6807 \u2192 \u5546\u4e1a\u4ef7\u503c\uff1aTTFT\u964d\u4f4e = \u7528\u6237\u7b49\u5f85\u51cf\u5c11 = \u4ea7\u54c1\u4f53\u9a8c\u63d0\u5347",
    body08))

# SLIDE 09: 国产算力
body09 = '''<div class="lay" style="grid-template-columns:1fr 1fr">
<div>
<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px">
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(245,158,11,0.15);border-radius:12px;padding:16px">
<div style="font-size:14px;font-weight:700;color:#fbbf24;margin-bottom:5px">Qwen3-235B-AWQ</div>
<div style="display:flex;align-items:center;gap:6px;margin-bottom:6px"><div style="width:7px;height:7px;background:#10b981;border-radius:50%"></div><span style="font-size:11px;color:#10b981;font-weight:600">\u5df2\u4e0a\u7ebf</span></div>
<div style="font-size:11px;color:#64748b;line-height:1.5">\u6d77\u5149\u955c\u50cf\u66f4\u65b0\u81f3vLLM0.11.0</div></div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(245,158,11,0.15);border-radius:12px;padding:16px">
<div style="font-size:14px;font-weight:700;color:#fbbf24;margin-bottom:5px">Qwen3-Next-80B</div>
<div style="display:flex;align-items:center;gap:6px;margin-bottom:6px"><div style="width:7px;height:7px;background:#10b981;border-radius:50%"></div><span style="font-size:11px;color:#10b981;font-weight:600">\u5df2\u4e0a\u7ebf</span></div>
<div style="font-size:11px;color:#64748b;line-height:1.5">\u89e3\u51b3\u56de\u7b54\u91cd\u590d\u95ee\u9898</div></div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(245,158,11,0.15);border-radius:12px;padding:16px">
<div style="font-size:14px;font-weight:700;color:#fbbf24;margin-bottom:5px">Qwen3-VL-8B-Instruct</div>
<div style="display:flex;align-items:center;gap:6px;margin-bottom:6px"><div style="width:7px;height:7px;background:#10b981;border-radius:50%"></div><span style="font-size:11px;color:#10b981;font-weight:600">\u5df2\u4e0a\u7ebf</span></div>
<div style="font-size:11px;color:#64748b;line-height:1.5">\u56fe\u7247\u95ee\u7b54\u529f\u80fd\u6b63\u5e38</div></div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(245,158,11,0.15);border-radius:12px;padding:16px">
<div style="font-size:14px;font-weight:700;color:#fbbf24;margin-bottom:5px">DeepSeek-OCR</div>
<div style="display:flex;align-items:center;gap:6px;margin-bottom:6px"><div style="width:7px;height:7px;background:#10b981;border-radius:50%"></div><span style="font-size:11px;color:#10b981;font-weight:600">\u5df2\u4e0a\u7ebf</span></div>
<div style="font-size:11px;color:#64748b;line-height:1.5">\u767e\u5ea6\u98de\u6851\u65b9\u6848</div></div>
<div style="grid-column:span 2;background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.25);border-radius:12px;padding:16px;text-align:center;font-size:14px;color:#34d399;font-weight:600">4\u4e2a\u6a21\u578b\u5168\u90e8\u4e0a\u7ebf \u2192 \u652f\u6491\u6321\u6807\u6587\u4ef6\u751f\u6210\u4e1a\u52a1\u6b63\u5f0f\u53d1\u5e03</div>
</div>
</div>
<div style="display:flex;flex-direction:column;gap:14px">
<div style="background:rgba(16,185,129,0.07);border:1px solid rgba(16,185,129,0.2);border-radius:12px;padding:20px;text-align:center">
<div style="font-size:40px;font-weight:800;color:#10b981;margin-bottom:4px">\u4e1a\u52a1\u4ea4\u4ed8</div>
<div style="font-size:13px;color:#94a3b8">\u6d77\u5149K100 \u2192 \u6321\u6807\u6587\u4ef6\u751f\u6210</div>
<div style="font-size:11px;color:#64748b;margin-top:4px">\u4ece"\u6280\u672f\u9a8c\u8bc1"\u5230"\u5546\u4e1a\u843d\u5730"\u91cc\u7a0b\u7891</div>
</div>
<div class="biz" style="background:rgba(245,158,11,0.07);border:1px solid rgba(245,158,11,0.2)">
<div class="biz_t" style="color:#f59e0b">\u5546\u4e1a\u4ef7\u503c\u7ffb\u8bd1</div>
<div class="bi"><span class="bi_a" style="color:#f59e0b">\u2192</span><div>\u56fd\u4ea7\u7b97\u529b\u6b63\u5f0f\u652f\u6491<strong style="color:#fff">\u6838\u5fc3\u4e1a\u52a1\u4e0a\u7ebf</strong></div></div>
<div class="bi"><span class="bi_a" style="color:#f59e0b">\u2192</span><div>\u9a8c\u8bc1\u56e2\u961f<strong style="color:#fff">\u56fd\u4ea7\u5316\u9002\u914d\u80fd\u529b</strong>\uff0c\u53ef\u590d\u5236\u63a8\u5e7f</div></div>
<div class="bi"><span class="bi_a" style="color:#f59e0b">\u2192</span><div>\u4e3a<strong style="color:#fff">\u4fe1\u521b\u5408\u89c4</strong>\u63d0\u4f9b\u6280\u672f\u4fdd\u969c</div></div>
<div class="bi"><span class="bi_a" style="color:#f59e0b">\u2192</span><div>\u5f62\u6210\u65b9\u6cd5\u8bba\u548c\u5de5\u5177\u94fe\uff0c<strong style="color:#fff">\u540e\u7eed\u9002\u914d\u5468\u671f\u5927\u5e45\u7f29\u77ed</strong></div></div>
</div>
</div>
</div>'''

W("slide09.html", page(9, "#f59e0b", "rgba(245,158,11,0.1)", "rgba(245,158,11,0.3)", "#f59e0b",
    "\u56fd\u4ea7\u7b97\u529b\u9002\u914d\uff1a\u6d77\u5149K100\u56db\u5927\u6a21\u578b\u5168\u91cf\u4e0a\u7ebf",
    "\u6280\u672f\u6307\u6807 \u2192 \u5546\u4e1a\u4ef7\u503c\uff1a\u4ece\"\u6280\u672f\u9a8c\u8bc1\"\u5230\"\u4e1a\u52a1\u4ea4\u4ed8\"\u7684\u5173\u952e\u8de8\u8d8a",
    body09))

# SLIDE 10: 问题复盘
body10 = '''<div style="display:flex;flex-direction:column;gap:16px;flex:1">
<div style="display:grid;grid-template-columns:52px 1fr 40px 1fr;gap:20px;align-items:center;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);border-radius:14px;padding:20px 24px">
<div style="font-size:38px;font-weight:800;color:#ef4444;opacity:0.4;text-align:center;line-height:1">01</div>
<div><div style="font-size:12px;font-weight:700;color:#ef4444;margin-bottom:8px;letter-spacing:1px">\u6559\u8bad\uff1a\u8bad\u7ec3\u73af\u5883\u6210\u9879\u76ee\u74f6\u957f</div><div style="display:flex;flex-direction:column;gap:5px"><div style="font-size:12px;color:#94a3b8;padding-left:10px;border-left:2px solid rgba(255,255,255,0.1);line-height:1.5">NCCL\u901a\u4fe1\u5f02\u5e38\u3001\u591a\u8282\u70b9\u8bad\u7ec3\u9891\u7e41\u4e2d\u65ad</div><div style="font-size:12px;color:#94a3b8;padding-left:10px;border-left:2px solid rgba(255,255,255,0.1);line-height:1.5">\u672a\u5c06\u73af\u5883\u5c31\u7eea\u4f5c\u4e3a\u72ec\u7acb\u91cc\u7a0b\u7891</div></div></div>
<div style="text-align:center;font-size:24px;opacity:0.25">\u2192</div>
<div><div style="font-size:12px;font-weight:700;color:#10b981;margin-bottom:8px;letter-spacing:1px">Q2\u884c\u52a8\u627f\u8bfa</div><div style="display:flex;flex-direction:column;gap:5px"><div style="font-size:12px;color:#cbd5e1;padding-left:10px;border-left:2px solid rgba(16,185,129,0.3);line-height:1.5"><strong style="color:#10b981">\u524d\u7f6e\u9a8c\u8bc1\uff1a</strong>NCCL/RDMA/\u591a\u8282\u70b9\u540c\u6b65\u5728\u9879\u76ee\u542f\u52a8\u524d\u5b8c\u6210</div><div style="font-size:12px;color:#cbd5e1;padding-left:10px;border-left:2px solid rgba(16,185,129,0.3);line-height:1.5"><strong style="color:#10b981">\u72ec\u7acb\u91cc\u7a0b\u7891\uff1a</strong>\u73af\u5883\u5c31\u7eea\u68c0\u67e5\u7eb3\u5165\u9879\u76ee\u57fa\u7ebf\uff0c\u4e0d\u4e0e\u5f00\u53d1\u5e76\u884c</div></div></div>
</div>
<div style="display:grid;grid-template-columns:52px 1fr 40px 1fr;gap:20px;align-items:center;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);border-radius:14px;padding:20px 24px">
<div style="font-size:38px;font-weight:800;color:#f59e0b;opacity:0.4;text-align:center;line-height:1">02</div>
<div><div style="font-size:12px;font-weight:700;color:#f59e0b;margin-bottom:8px;letter-spacing:1px">\u6559\u8bad\uff1a\u6570\u636e\u8d28\u91cf\u62d6\u6162\u591a\u4e2a\u9879\u76ee</div><div style="display:flex;flex-direction:column;gap:5px"><div style="font-size:12px;color:#94a3b8;padding-left:10px;border-left:2px solid rgba(255,255,255,0.1);line-height:1.5">\u6807\u7b7e\u9519\u8bef\u3001\u5206\u7c7b\u4e0d\u6e05\u6670\u3001\u591a\u6b21\u8fd4\u5de5</div><div style="font-size:12px;color:#94a3b8;padding-left:10px;border-left:2px solid rgba(255,255,255,0.1);line-height:1.5">\u6570\u636e\u4ea4\u63a5\u73af\u8282\u7f3a\u4e4f\u8d28\u91cf\u628a\u63a7</div></div></div>
<div style="text-align:center;font-size:24px;opacity:0.25">\u2192</div>
<div><div style="font-size:12px;font-weight:700;color:#10b981;margin-bottom:8px;letter-spacing:1px">Q2\u884c\u52a8\u627f\u8bfa</div><div style="display:flex;flex-direction:column;gap:5px"><div style="font-size:12px;color:#cbd5e1;padding-left:10px;border-left:2px solid rgba(16,185,129,0.3);line-height:1.5"><strong style="color:#10b981">Checklist\uff1a</strong>\u5efa\u7acb\u4ece\u91c7\u96c6\u5230\u9a8c\u6536\u7684\u5b8c\u6574\u8d28\u91cf\u7ba1\u63a7\u94fe\u6761</div><div style="font-size:12px;color:#cbd5e1;padding-left:10px;border-left:2px solid rgba(16,185,129,0.3);line-height:1.5"><strong style="color:#10b981">\u6280\u672f\u5ba1\u6838\uff1a</strong>\u6570\u636e\u4ea4\u63a5\u589e\u8bbe\u6280\u672f\u5ba1\u6838\u8282\u70b9\uff0c\u4e0d\u5408\u683c\u4e0d\u63a5\u6536</div></div></div>
</div>
<div style="display:grid;grid-template-columns:52px 1fr 40px 1fr;gap:20px;align-items:center;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);border-radius:14px;padding:20px 24px">
<div style="font-size:38px;font-weight:800;color:#3b82f6;opacity:0.4;text-align:center;line-height:1">03</div>
<div><div style="font-size:12px;font-weight:700;color:#3b82f6;margin-bottom:8px;letter-spacing:1px">\u6559\u8bad\uff1a\u56fd\u4ea7\u5316\u9002\u914d\u8d85\u9884\u671f\u8017\u65f6</div><div style="display:flex;flex-direction:column;gap:5px"><div style="font-size:12px;color:#94a3b8;padding-left:10px;border-left:2px solid rgba(255,255,255,0.1);line-height:1.5">\u5e95\u5c42\u7b97\u5b50\u5dee\u5f02\u672a\u63d0\u524d\u8bc6\u522b\uff0c\u591a\u8f6e\u8c03\u8bd5</div><div style="font-size:12px;color:#94a3b8;padding-left:10px;border-left:2px solid rgba(255,255,255,0.1);line-height:1.5">\u7f3a\u4e4f\u6e10\u8fdb\u5f0f\u9a8c\u8bc1\u6d41\u7a0b</div></div></div>
<div style="text-align:center;font-size:24px;opacity:0.25">\u2192</div>
<div><div style="font-size:12px;font-weight:700;color:#10b981;margin-bottom:8px;letter-spacing:1px">Q2\u884c\u52a8\u627f\u8bfa</div><div style="display:flex;flex-direction:column;gap:5px"><div style="font-size:12px;color:#cbd5e1;padding-left:10px;border-left:2px solid rgba(16,185,129,0.3);line-height:1.5"><strong style="color:#10b981">\u524d\u7f6e\u8c03\u7814\uff1a</strong>\u56fd\u4ea7\u5316\u4efb\u52a1\u9884\u7559\u987预\u7814\u7a97\u53e3\uff0c\u5355\u673a\u2192\u5c0f\u96c6\u7fa4\u2192\u751f\u4ea7</div><div style="font-size:12px;color:#cbd5e1;padding-left:10px;border-left:2px solid rgba(16,185,129,0.3);line-height:1.5"><strong style="color:#10b981">\u6e10\u8fdb\u5f0f\u9a8c\u8bc1\uff1a</strong>\u5efa\u7acb\u6807\u51c6\u5316\u6280\u672f\u9a8c\u8bc1\u5230\u89c4\u6a21\u90e8\u7f72\u6d41\u7a0b</div></div></div>
</div>
</div>'''

W("slide10.html", page(10, "#ef4444", "rgba(239,68,68,0.1)", "rgba(239,68,68,0.3)", "#ef4444",
    "Q1\u4e09\u4e2a\u6559\u8bad\uff0c\u6bcf\u4e2a\u90fd\u8f6c\u5316\u4e3aQ2\u884c\u52a8\u627f\u8bfa",
    "C \u2192 A \u6a21\u578b\uff1a\u95ee\u9898\u662f\u8bca\u65ad\u8f6f\u4ef6\uff0c\u884c\u52a8\u624d\u662f\u91ca\u8bc1\u786e\u8bca",
    body10))

# SLIDE 11: Q2目标
body11 = '''<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;flex:1">
<div style="border-radius:16px;padding:28px;border:1px solid rgba(255,255,255,0.06);background:rgba(255,255,255,0.02);display:flex;flex-direction:column;gap:16px">
<div style="height:3px;border-radius:16px 16px 0 0;margin:-28px -28px 0 -28px;background:linear-gradient(90deg,#3b82f6,#60a5fa)"></div>
<div style="font-size:13px;font-weight:700;color:#3b82f6;letter-spacing:1px">\u6218\u7565\u4e00</div>
<div style="font-size:18px;font-weight:700;color:#fff;line-height:1.4">\u901a\u7528\u89c4\u5212\u80fd\u529b<br>\u62d3\u5c55<strong style="color:#3b82f6">30%+</strong></div>
<div style="font-size:13px;color:#94a3b8;line-height:1.6">PlanBench\u51b3\u6218\u6807\uff1a9.6% \u2192 40%+</div>
<div style="background:rgba(59,130,246,0.08);border-radius:8px;padding:12px 14px">
<div style="font-size:12px;color:#93c5fd;line-height:1.6">\u2192 PDDL
\u4e1a\u52a1\u6570\u636e\u5efa\u8bbe
<div style="font-size:12px;color:#64748b;line-height:1.5">\u76ee\u6807\uff1a5k+\u6761PDDL\u89c4\u5212\u8f68\u8ff9</div>
</div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(59,130,246,0.15);border-radius:8px;padding:10px 12px;text-align:center">
<div style="font-size:22px;font-weight:700;color:#3b82f6">+30%</div>
<div style="font-size:11px;color:#64748b;margin-top:2px">\u89c4\u5212\u80fd\u529b\u63d0\u5347</div>
</div>
</div>
<div style="border-radius:16px;padding:28px;border:1px solid rgba(255,255,255,0.06);background:rgba(255,255,255,0.02);display:flex;flex-direction:column;gap:16px">
<div style="height:3px;border-radius:16px 16px 0 0;margin:-28px -28px 0 -28px;background:linear-gradient(90deg,#10b981,#34d399)"></div>
<div style="font-size:13px;font-weight:700;color:#10b981;letter-spacing:1px">\u6218\u7565\u4e8c</div>
<div style="font-size:18px;font-weight:700;color:#fff;line-height:1.4">\u5206\u5e03\u5f0f\u96c6\u7fa4\u63a8\u7406<br>\u9879\u76ee\u7acb\u9879</div>
<div style="font-size:13px;color:#94a3b8;line-height:1.6">\u5b8c\u6210\u201c\u5206\u5e03\u5f0f\u96c6\u7fa4\u63a8\u7406\u201dTMT\u9879\u76ee\u7acb\u9879</div>
<div style="background:rgba(16,185,129,0.08);border-radius:8px;padding:12px 14px">
<div style="font-size:12px;color:#93c5fd;line-height:1.6">\u2192 KV Cache\u5378\u8f7d\u529f\u80fd\u9a8c\u8bc1</div>
<div style="font-size:12px;color:#64748b;line-height:1.5;margin-top:4px">\u2192 \u7f13\u5b58\u611f\u77e5\u8c03\u5ea6\u518d\u63d0\u534710%</div>
</div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(16,185,129,0.15);border-radius:8px;padding:10px 12px;text-align:center">
<div style="font-size:22px;font-weight:700;color:#10b981">\u7acb\u9879</div>
<div style="font-size:11px;color:#64748b;margin-top:2px">\u5206\u5e03\u5f0f\u96c6\u7fa4\u63a8\u7406</div>
</div>
</div>
<div style="border-radius:16px;padding:28px;border:1px solid rgba(255,255,255,0.06);background:rgba(255,255,255,0.02);display:flex;flex-direction:column;gap:16px">
<div style="height:3px;border-radius:16px 16px 0 0;margin:-28px -28px 0 -28px;background:linear-gradient(90deg,#8b5cf6,#a78bfa)"></div>
<div style="font-size:13px;font-weight:700;color:#a78bfa;letter-spacing:1px">\u6218\u7565\u4e09</div>
<div style="font-size:18px;font-weight:700;color:#fff;line-height:1.4">\u8bba\u6587\u4e1a\u52a1\u6295\u7a3f<br><strong style="color:#a78bfa">\u201c\u7834\u51b0\u201d</strong></div>
<div style="font-size:13px;color:#94a3b8;line-height:1.6">\u76ee\u6807\uff1a1-2\u7bc7\u5b66\u672f\u8bba\u6587\u6295\u7a3f</div>
<div style="background:rgba(139,92,246,0.08);border-radius:8px;padding:12px 14px">
<div style="font-size:12px;color:#93c5fd;line-height:1.6">\u2192 \u5efa\u7acb\u6fc0\u52b1\u673a\u5236</div>
<div style="font-size:12px;color:#64748b;line-height:1.5;margin-top:4px">\u2192 \u56e2\u961f\u5b9e\u9a8c\u603b\u7ed3\u62d3\u5c55</div>
</div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(139,92,246,0.15);border-radius:8px;padding:10px 12px;text-align:center">
<div style="font-size:22px;font-weight:700;color:#a78bfa">1-2\u7bc7</div>
<div style="font-size:11px;color:#64748b;margin-top:2px">\u8bba\u6587\u6295\u7a3f\u76ee\u6807</div>
</div>
</div>
</div>'''

W("slide11.html", page(11, "#3b82f6", "rgba(59,130,246,0.1)", "rgba(59,130,246,0.3)", "#3b82f6",
    "Q2\u4e09\u5927\u786c\u4efb\uff1a\u7b2c\u4e00\u628a\u5289\u5179\u7b2c\u4e8c\u628a\u8bba\u6587\u6295\u7a3f",
    "Q \u2192 A \u6a21\u578b\uff1a\u95ee\u9898\u5bfc\u5411\u884c\u52a8\uff0c\u884c\u52a8\u5bfc\u5411\u7ed3\u679c",
    body11))

# SLIDE 12: 关键数字
body12 = '''<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;flex:1;align-content:center">
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(59,130,246,0.15);border-radius:16px;padding:28px;text-align:center">
<div style="font-size:48px;font-weight:800;color:#3b82f6;margin-bottom:8px">12</div>
<div style="font-size:14px;font-weight:700;color:#fff;margin-bottom:6px">\u4e13\u5229\u63d0\u4ea4</div>
<div style="font-size:12px;color:#94a3b8;line-height:1.6">\u5df2\u786e\u8ba4 7\u9879<br>\u5ba1\u6279\u4e2d 5\u9879</div>
<div style="margin-top:12px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.06)">
<div style="font-size:11px;color:#64748b">\u91c7\u7528\u65b9\u5411</div>
<div style="font-size:12px;color:#3b82f6;font-weight:600">\u6a21\u578b\u63a8\u7406 | \u8bad\u7ec3\u4f18\u5316 | \u7f51\u7edc\u9884\u6d4b</div>
</div>
</div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(16,185,129,0.15);border-radius:16px;padding:28px;text-align:center">
<div style="font-size:48px;font-weight:800;color:#10b981;margin-bottom:8px">18</div>
<div style="font-size:14px;font-weight:700;color:#fff;margin-bottom:6px">\u95ee\u9898\u5355\u89e3\u51b3</div>
<div style="font-size:12px;color:#94a3b8;line-height:1.6">\u7f51\u7edc\u4ea7\u54c112\u4e2a<br>\u65e0\u7ebf\u4ea7\u54c14\u4e2a<br>\u5176\u4ed6\u4ea7\u54c12\u4e2a</div>
<div style="margin-top:12px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.06)">
<div style="font-size:11px;color:#64748b">\u4ea7\u54c1\u7ebf\u5168\u8986\u76d6</div>
<div style="font-size:12px;color:#10b981;font-weight:600">3\u4e2a\u9879\u76ee\u9a8c\u6536\u5b8c\u6210</div>
</div>
</div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(139,92,246,0.15);border-radius:16px;padding:28px;text-align:center">
<div style="font-size:48px;font-weight:800;color:#a78bfa;margin-bottom:8px">5\u79cd</div>
<div style="font-size:14px;font-weight:700;color:#fff;margin-bottom:6px">RL\u7b97\u6cd5\u9002\u914d</div>
<div style="font-size:12px;color:#94a3b8;line-height:1.6">DPO | GRPO | DAPO<br>GSPO | GDPO</div>
<div style="margin-top:12px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.06)">
<div style="font-size:11px;color:#64748b">\u652f\u6301\u6846\u67b6</div>
<div style="font-size:12px;color:#a78bfa;font-weight:600">llamafactory | swift | Verl</div>
</div>
</div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(245,158,11,0.15);border-radius:16px;padding:28px;text-align:center">
<div style="font-size:48px;font-weight:800;color:#fbbf24;margin-bottom:8px">\u5b8c\u6210</div>
<div style="font-size:14px;font-weight:700;color:#fff;margin-bottom:6px">\u767d\u76d8\u4e66\u53d1\u5e03</div>
<div style="font-size:12px;color:#94a3b8;line-height:1.6">《H3C\u767e\u4e1a\u7075\u8e1fAI<br>\u6a21\u578b\u5de5\u7a0b\u6280\u672f<br>\u767d\u76d8\u4e66》</div>
<div style="margin-top:12px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.06)">
<div style="font-size:11px;color:#64748b">\u6280\u672f\u6587\u6863</div>
<div style="font-size:12px;color:#fbbf24;font-weight:600">26\u5e74\u89c4\u5212\u5165\u6863</div>
</div>
</div>
</div>
<div style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:20px 24px;text-align:center">
<div style="font-size:14px;color:#94a3b8;line-height:1.8"><strong style="color:#fff">\u6280\u672f\u5821\u5792 \u5373 \u62d3\u62d4\u62a4\u57ce</strong><br>\u4e13\u5229\u3001\u65b9\u6cd5\u8bba\u3001\u6807\u51c6\u5316\u6d41\u7a0b \u2014 \u8fd9\u4e9b\u90fd\u662f\u56e2\u961f\u7684\u6838\u5fc3\u7ade\u4e89\u529b</div>
</div>'''

W("slide12.html", page(12, "#3b82f6", "rgba(59,130,246,0.1)", "rgba(59,130,246,0.3)", "#3b82f6",
    "\u5173\u952e\u6570\u5b57\u4e00\u949f\u770b\u61c2\uff1aQ1\u6210\u679c\u7626\u6bdb\u98d8\u9999",
    "\u6280\u672f\u6307\u6807\u5168\u90e8\u786e\u8ba4\uff0c\u5546\u4e1a\u4ef7\u503c\u6bcf\u4e00\u9879\u90fd\u6709\u660e\u786e\u7684\u52a0\u5206\u9879",
    body12))

# SLIDE 13: 结语
body13 = '''<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;flex:1;text-align:center;gap:40px">
<div>
<div style="font-size:56px;margin-bottom:16px">\ud83e\udd1e</div>
<div style="font-size:28px;font-weight:700;color:#fff;line-height:1.5;max-width:800px">
Q1\u6210\u4e3a\u4e8b\u5b9e\u8bc1\u660e\u4e86\uff1a<br>
<span style="color:#3b82f6">\u6280\u672f\u9a8c\u8bc1 \u2192 \u4e1a\u52a1\u4ea4\u4ed8</span><br>
<span style="color:#10b981">\u6210\u672c\u63a7\u5236 \u2192 \u7ee9\u6548\u63d0\u5347</span><br>
<span style="color:#a78bfa">\u5355\u70b9\u7a81\u7834 \u2192 \u7cfb\u7edf\u6027\u8f93\u51fa</span>
</div>
</div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:16px;padding:32px 40px;max-width:700px">
<div style="font-size:15px;color:#94a3b8;line-height:2">
Q2\u6211\u4eec\u5c06\u91cd\u70b9\u6253\u7834<strong style="color:#fff"> \u901a\u7528\u89c4\u5212\u80fd\u529b +30%+</strong>\u3001<br>
\u5b8c\u6210<strong style="color:#fff"> \u5206\u5e03\u5f0f\u96c6\u7fa4\u63a8\u7406</strong>\u9879\u76ee\u7acb\u9879\u3001<br>
\u5b9e\u73b0<strong style="color:#fff"> \u8bba\u6587\u6295\u7a3f\u201c\u7834\u51b0\u201d</strong>\u2014\u2014<br>
<strong style="color:#fff">\u6301\u7eed\u4e3a\u4e1a\u52a1\u521b\u9020\u4ef7\u503c\u3002</strong>
</div>
</div>
<div style="font-size:14px;color:#475569;letter-spacing:2px">\u56e2\u961f\u6001\u5ea6\uff1a\u52c7\u4e8e\u627f\u8ba4\u4e0d\u8db3\uff0c\u7a81\u7834\u65f6\u4e0d\u60e8\u8e0f\u3002</div>
</div>'''

W("slide13.html", page(13, "#10b981", "rgba(16,185,129,0.1)", "rgba(16,185,129,0.3)", "#10b981",
    "\u7ed3\u8bed\uff1aQ1\u6253\u57fa\u7840\uff0cQ2\u518d\u8fdb\u4e00\u6b65",
    "A \u2014 Answer \uff1a\u884c\u52a8\u5c06\u4e16\u754c\u5e94\u9a8c\u6211\u4eec\u7684\u6539\u53d8",
    body13))

# SLIDE 14: 附录
body14 = '''<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;flex:1;align-content:start}
<div>
<div style="font-size:14px;font-weight:700;color:#93c5fd;margin-bottom:14px;padding-bottom:8px;border-bottom:1px solid rgba(59,130,246,0.15)">\u6280\u672f\u6307\u6807\u539f\u59cb\u6570\u636e</div>
<div style="display:flex;flex-direction:column;gap:10px}
<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px">
<div style="font-size:13px;color:#94a3b8">\u610f\u56fe\u8bc6\u522b\u51c6\u786e\u7387</div><div style="font-size:13px;font-weight:700;color:#3b82f6">95%+</div></div>
<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px">
<div style="font-size:13px;color:#94a3b8">L1\u51c6\u786e\u7387</div><div style="font-size:13px;font-weight:700;color:#3b82f6">96.4%</div></div>
<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px">
<div style="font-size:13px;color:#94a3b8">TTFT\u964d\u4f4e</div><div style="font-size:13px;font-weight:700;color:#10b981">17.5%</div></div>
<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px">
<div style="font-size:13px;color:#94a3b8">\u89c4\u5212\u80fd\u529b\u63d0\u5347</div><div style="font-size:13px;font-weight:700;color:#8b5cf6">26%\u219252%</div></div>
<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px">
<div style="font-size:13px;color:#94a3b8">\u4e13\u5229\u63d0\u4ea4</div><div style="font-size:13px;font-weight:700;color:#f59e0b">12\u9879</div></div>
<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px">
<div style="font-size:13px;color:#94a3b8">\u4ea7\u54c1\u7ebf\u95ee\u9898\u5355</div><div style="font-size:13px;font-weight:700;color:#ef4444">18\u4e2a</div></div>
</div>
<div>
<div style="font-size:14px;font-weight:700;color:#93c5fd;margin-bottom:14px;padding-bottom:8px;border-bottom:1px solid rgba(59,130,246,0.15)">\u9884\u671fQ2\u6210\u679c</div>
<div style="display:flex;flex-direction:column;gap:10px}
<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(59,130,246,0.05);border:1px solid rgba(59,130,246,0.15);border-radius:8px">
<div style="font-size:13px;color:#94a3b8">PlanBench</div><div style="font-size:13px;font-weight:700;color:#3b82f6">40%+</div></div>
<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(16,185,129,0.05);border:1px solid rgba(16,185,129,0.15);border-radius:8px">
<div style="font-size:13px;color:#94a3b8">\u5206\u5e03\u5f0f\u96c6\u7fa4</div><div style="font-size:13px;font-weight:700;color:#10b981">\u7acb\u9879</div></div>
<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(139,92,246,0.05);border:1px solid rgba(139,92,246,0.15);border-radius:8px">
<div style="font-size:13px;color:#94a3b8">\u8bba\u6587\u6295\u7a3f</div><div style="font-size:13px;font-weight:700;color:#a78bfa">1-2\u7bc7</div></div>
<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px">
<div style="font-size:13px;color:#94a3b8">\u7f13\u5b58\u8c03\u5ea6\u63d0\u5347</div><div style="font-size:13px;font-weight:700;color:#3b82f6">+10%</div></div>
<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px">
<div style="font-size:13px;color:#94a3b8">PDDL\u89c4\u5212\u8f68\u8ff9</div><div style="font-size:13px;font-weight:700;color:#10b981">5k+</div></div>
<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px">
<div style="font-size:13px;color:#94a3b8">\u4ea7\u54c1\u7ebf\u9a8c\u6536</div><div style="font-size:13px;font-weight:700;color:#ef4444">2\u9879</div></div>
</div>
</div>'''

W("slide14.html", page(14, "#64748b", "rgba(100,116,139,0.1)", "rgba(100,116,139,0.3)", "#64748b",
    "\u9644\u5f55\uff1a\u6280\u672f\u6307\u6807\u539f\u59cb\u6570\u636e\u4e0eQ2\u5c55\u671b",
    "\u4ec5\u4f9b\u6280\u672f\u76f8\u5173\u8005\u53c2\u9605\uff0c\u4e3b\u4f1a\u5185\u5bb9\u4ee5\u524d\u9875\u4e3a\u51c6",
    body12))

print("All done!")
