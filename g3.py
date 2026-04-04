import os
D = "/workspace/slides"
os.makedirs(D, exist_ok=True)
def W(f,c): open(os.path.join(D,f),"w",encoding="utf-8").write(c); print(f"OK {f}")

BASE = """<!DOCTYPE html><html lang="zh"><head><meta charset="UTF-8"><title>s{id}</title><style>
*.{m:0;p:0;bx:border-box}
body{font-family:PingFang SC,Microsoft YaHei,sans-serif;background:#0a0f2e;color:#fff}
.slide{width:100vw;height:100vh;display:flex;flex-direction:column;padding:60px 80px;position:relative}
.tag{font-size:13px;letter-spacing:3px;color:{tc};text-transform:uppercase;font-weight:600;margin-bottom:20px}
.sn{font-size:13px;color:#334155;font-weight:700;margin-bottom:20px}
.scqa{position:absolute;top:60px;right:80px;background:{sb};border:1px solid {sc};border-radius:8px;padding:10px 18px;font-size:13px;color:{tc};font-weight:600;letter-spacing:1px}
h1{font-size:38px;font-weight:700;color:#fff;margin-bottom:8px}
.sub{font-size:17px;color:#64748b;margin-bottom:{sm}}
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
.ba{font-weight:700;flex-shrink:0}
.ft{position:absolute;bottom:36px;left:80px;right:80px;display:flex;justify-content:space-between}
.ft span{font-size:12px;color:#475569}
</style></head><body>
<div class="slide">
<div class="tag">{tag}</div><div class="sn">{sn}</div>
<div class="scqa">{sctag}</div>
<h1>{h1}</h1>
<div class="sub">{sub}</div>
{body}
<div class="ft"><span>SCQA模型 · 2026年Q1 AI模型工程团队述职</span><span>{sn}</span></div>
</div></body></html>"""

def p(num, tc, sb, sc, sctag, h1, sub, body, sn):
    return BASE.format(id=num, tc=tc, sb=sb, sc=sc, sctag=sctag, h1=h1, sub=sub, body=body, sn=sn, sm="36px")

# slide 08
b08 = '''<div class="lay" style="grid-template-columns:1fr 1fr">
<div>
<div class="st" style="border-bottom:1px solid rgba(59,130,246,0.15)">TTFT（首字响应）&amp; 吞吐优化数据</div>
<div class="pi"><div class="ph"><span class="pn">NV 4P4D 多轮对话</span><div style="display:flex;gap:6px"><span class="bdg bb">吞吐+10%</span><span class="bdg bg2">TTFT -17.5%</span></div></div><div class="pm"><div class="m"><div class="mv">-17.5%</div><div class="ml">TTFT降低</div></div><div class="m"><div class="mv mvg">+10%</div><div class="ml">吞吐提升</div></div><div class="m"><div class="mv">8轮</div><div class="ml">多轮对话</div></div></div><div class="bar"><div style="height:5px;width:82%;background:linear-gradient(90deg,#3b82f6,#60a5fa);border-radius:3px"></div></div></div>
<div class="pi"><div class="ph"><span class="pn">1P1D 多DP精细化调度</span><div style="display:flex;gap:6px"><span class="bdg bb">吞吐+3.5%</span><span class="bdg bg2">TTFT -9%</span></div></div><div class="pm"><div class="m"><div class="mv">-9%</div><div class="ml">TTFT降低</div></div><div class="m"><div class="mv mvg">+3.5%</div><div class="ml">吞吐提升</div></div><div class="m"><div class="mv">精细化</div><div class="ml">DP配置</div></div></div><div class="bar"><div style="height:5px;width:60%;background:linear-gradient(90deg,#10b981,#34d399);border-radius:3px"></div></div></div>
<div class="pi"><div class="ph"><span class="pn">超节点 DeepSeek-R1</span><div style="display:flex;gap:6px"><span class="bdg bb">吞吐+1%</span><span class="bdg bg2">TTFT -7%</span></div></div><div class="pm"><div class="m"><div class="mv">-7%</div><div class="ml">TTFT均值</div></div><div class="m"><div class="mv mvg">-5%</div><div class="ml">P90时延</div></div><div class="m"><div class="mv">国产</div><div class="ml">超节点</div></div></div><div class="bar"><div style="height:5px;width:45%;background:linear-gradient(90deg,#8b5cf6,#a78bfa);border-radius:3px"></div></div></div>
</div>
<div>
<div class="st" style="border-bottom:1px solid rgba(59,130,246,0.15)">核心突破：纯算法优化，零硬件投入</div>
<div class="pi" style="margin-bottom:16px"><div style="font-size:13px;color:#fff;font-weight:600;margin-bottom:6px">缓存感知调度原理</div><div style="font-size:12px;color:#94a3b8;line-height:1.7">通过分析KV Cache命中情况优化请求调度，<strong style="color:#fff">ROI极高</strong>，不依赖硬件升级。</div></div>
<div class="biz" style="background:rgba(16,185,129,0.07);border:1px solid rgba(16,185,129,0.2)">
<div class="biz_t" style="color:#10b981">商业价值翻译</div>
<div class="bi"><span class="ba" style="color:#10b981">→</span><div>TTFT -17.5% = 用户感知<strong>响应速度明显加快</strong></div></div>
<div class="bi"><span class="ba" style="color:#10b981">→</span><div>吞吐+10% = <strong>相同硬件承载更多并发用户</strong></div></div>
<div class="bi"><span class="ba" style="color:#10b981">→</span><div>精细化DP = 支持<strong>差异化SLA保障</strong></div></div>
<div class="bi"><span class="ba" style="color:#10b981">→</span><div><strong>零额外硬件投入</strong>，纯算法优化</div></div>
</div>
</div>
</div>'''

W("slide08.html", p(8,"#3b82f6","rgba(59,130,246,0.1)","rgba(59,130,246,0.3)","SCQA · A",
    "推理性能优化：缓存感知调度全面落地",
    "技术指标 → 商业价值：TTFT降低 = 用户等待减少 = 产品体验提升", b08, "08 / 14"))

# slide 09
b09 = '''<div class="lay" style="grid-template-columns:1fr 1fr">
<div>
<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px">
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(245,158,11,0.15);border-radius:12px;padding:16px"><div style="font-size:14px;font-weight:700;color:#fbbf24;margin-bottom:5px">Qwen3-235B-AWQ</div><div style="display:flex;align-items:center;gap:6px;margin-bottom:6px"><div style="width:7px;height:7px;background:#10b981;border-radius:50%"></div><span style="font-size:11px;color:#10b981;font-weight:600">已上线</span></div><div style="font-size:11px;color:#64748b;line-height:1.5">海光镜像更新至vLLM0.11.0</div></div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(245,158,11,0.15);border-radius:12px;padding:16px"><div style="font-size:14px;font-weight:700;color:#fbbf24;margin-bottom:5px">Qwen3-Next-80B</div><div style="display:flex;align-items:center;gap:6px;margin-bottom:6px"><div style="width:7px;height:7px;background:#10b981;border-radius:50%"></div><span style="font-size:11px;color:#10b981;font-weight:600">已上线</span></div><div style="font-size:11px;color:#64748b;line-height:1.5">解决回答重复问题</div></div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(245,158,11,0.15);border-radius:12px;padding:16px"><div style="font-size:14px;font-weight:700;color:#fbbf24;margin-bottom:5px">Qwen3-VL-8B-Instruct</div><div style="display:flex;align-items:center;gap:6px;margin-bottom:6px"><div style="width:7px;height:7px;background:#10b981;border-radius:50%"></div><span style="font-size:11px;color:#10b981;font-weight:600">已上线</span></div><div style="font-size:11px;color:#64748b;line-height:1.5">图片问答功能正常</div></div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(245,158,11,0.15);border-radius:12px;padding:16px"><div style="font-size:14px;font-weight:700;color:#fbbf24;margin-bottom:5px">DeepSeek-OCR</div><div style="display:flex;align-items:center;gap:6px;margin-bottom:6px"><div style="width:7px;height:7px;background:#10b981;border-radius:50%"></div><span style="font-size:11px;color:#10b981;font-weight:600">已上线</span></div><div style="font-size:11px;color:#64748b;line-height:1.5">百度飞桨方案</div></div>
<div style="grid-column:span 2;background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.25);border-radius:12px;padding:16px;text-align:center;font-size:14px;color:#34d399;font-weight:600">4个模型全部上线 → 支撑招标文件生成业务正式发布</div>
</div>
</div>
<div style="display:flex;flex-direction:column;gap:14px">
<div style="background:rgba(16,185,129,0.07);border:1px solid rgba(16,185,129,0.2);border-radius:12px;padding:20px;text-align:center"><div style="font-size:40px;font-weight:800;color:#10b981;margin-bottom:4px">业务交付</div><div style="font-size:13px;color:#94a3b8">海光K100 → 招标文件生成</div><div style="font-size:11px;color:#64748b;margin-top:4px">从"技术验证"到"商业落地"里程碑</div></div>
<div class="biz" style="background:rgba(245,158,11,0.07);border:1px solid rgba(245,158,11,0.2)">
<div class="biz_t" style="color:#f59e0b">商业价值翻译</div>
<div class="bi"><span class="ba" style="color:#f59e0b">→</span><div>国产算力正式支撑<strong>核心业务上线</strong></div></div>
<div class="bi"><span class="ba" style="color:#f59e0b">→</span><div>验证团队<strong>国产化适配能力</strong>，可复制推广</div></div>
<div class="bi"><span class="ba" style="color:#f59e0b">→</span><div>为<strong>信创合规</strong>提供技术保障</div></div>
<div class="bi"><span class="ba" style="color:#f59e0b">→</span><div>形成方法论和工具链，<strong>后续适配周期大幅缩短</strong></div></div>
</div>
</div>
</div>'''

W("slide09.html", p(9,"#f59e0b","rgba(245,158,11,0.1)","rgba(245,158,11,0.3)","SCQA · A",
    "国产算力适配：海光K100四大模型全量上线",
    "技术指标 → 商业价值：从"技术验证"到"业务交付"的关键跨越", b09, "09 / 14"))

# slide 10
b10 = '''<div style="display:flex;flex-direction:column;gap:16px;flex:1">
<div style="display:grid;grid-template-columns:52px 1fr 40px 1fr;gap:20px;align-items:center;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);border-radius:14px;padding:20px 24px">
<div style="font-size:38px;font-weight:800;color:#ef4444;opacity:0.4;text-align:center;line-height:1">01</div>
<div><div style="font-size:12px;font-weight:700;color:#ef4444;margin-bottom:8px;letter-spacing:1px">教训：训练环境成项目瓶颈</div><div style="display:flex;flex-direction:column;gap:5px"><div style="font-size:12px;color:#94a3b8;padding-left:10px;border-left:2px solid rgba(255,255,255,0.1);line-height:1.5">NCCL通信异常、多节点训练频繁中断</div><div style="font-size:12px;color:#94a3b8;padding-left:10px;border-left:2px solid rgba(255,255,255,0.1);line-height:1.5">未将环境就绪作为独立里程碑</div></div></div>
<div style="text-align:center;font-size:24px;opacity:0.25">→</div>
<div><div style="font-size:12px;font-weight:700;color:#10b981;margin-bottom:8px;letter-spacing:1px">Q2行动承诺</div><div style="display:flex;flex-direction:column;gap:5px"><div style="font-size:12px;color:#cbd5e1;padding-left:10px;border-left:2px solid rgba(16,185,129,0.3);line-height:1.5"><strong style="color:#10b981">前置验证：</strong>NCCL/RDMA/多节点同步在项目启动前完成</div><div style="font-size:12px;color:#cbd5e1;padding-left:10px;border-left:2px solid rgba(16,185,129,0.3);line-height:1.5"><strong style="color:#10b981">独立里程碑：</strong>环境就绪检查纳入项目基线，不与开发并行</div></div></div>
</div>
<div style="display:grid;grid-template-columns:52px 1fr 40px 1fr;gap:20px;align-items:center;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);border-radius:14px;padding:20px 24px">
<div style="font-size:38px;font-weight:800;color:#f59e0b;opacity:0.4;text-align:center;line-height:1">02</div>
<div><div style="font-size:12px;font-weight:700;color:#f59e0b;margin-bottom:8px;letter-spacing:1px">教训：数据质量拖慢多个项目</div><div style="display:flex;flex-direction:column;gap:5px"><div style="font-size:12px;color:#94a3b8;padding-left:10px;border-left:2px solid rgba(255,255,255,0.1);line-height:1.5">标签错误、分类不清晰、多次返工</div><div style="font-size:12px;color:#94a3b8;padding-left:10px;border-left:2px solid rgba(255,255,255,0.1);line-height:1.5">数据交接环节缺乏质量把控</div></div></div>
<div style="text-align:center;font-size:24px;opacity:0.25">→</div>
<div><div style="font-size:12px;font-weight:700;color:#10b981;margin-bottom:8px;letter-spacing:1px">Q2行动承诺</div><div style="display:flex;flex-direction:column;gap:5px"><div style="font-size:12px;color:#cbd5e1;padding-left:10px;border-left:2px solid rgba(16,185,129,0.3);line-height:1.5"><strong style="color:#10b981">Checklist：</strong>建立从采集到验收的完整质量管控链条</div><div style="font-size:12px;color:#cbd5e1;padding-left:10px;border-left:2px solid rgba(16,185,129,0.3);line-height:1.5"><strong style="color:#10b981">技术审核：</strong>数据交接增设技术审核节点，不合格不接收</div></div></div>
</div>
<div style="display:grid;grid-template-columns:52px 1fr 40px 1fr;gap:20px;align-items:center;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);border-radius:14px;padding:20px 24px">
<div style="font-size:38px;font-weight:800;color:#3b82f6;opacity:0.4;text-align:center;line-height:1">03</div>
<div><div style="font-size:12px;font-weight:700;color:#3b82f6;margin-bottom:8px;letter-spacing:1px">教训：国产化适配超预期耗时</div><div style="display:flex;flex-direction:column;gap:5px"><div style="font-size:12px;color:#94a3b8;padding-left:10px;border-left:2px solid rgba(255,255,255,0.1);line-height:1.5">底层算子差异未提前识别，多轮调试</div><div style="font-size:12px;color:#94a3b8;padding-left:10px;border-left:2px solid rgba(255,255,255,0.1);line-height:1.5">缺乏渐进式验证流程</div></div></div>
<div style="text-align:center;font-size:24px;opacity:0.25">→</div>
<div><div style="font-size:12px;font-weight:700;color:#10b981;margin-bottom:8px;letter-spacing:1px">Q2行动承诺</div><div style="display:flex;flex-direction:column;gap:5px"><div style="font-size:12px;color:#cbd5e1;padding-left:10px;border-left:2px solid rgba(16,185,129,0.3);line-height:1.5"><strong style="color:#10b981">前置调研：</strong>国产化任务预留预研窗口，单机→小集群→生产</div><div style="font-size:12px;color:#cbd5e1;padding-left:10px;border-left:2px solid rgba(16,185,129,0.3);line-height:1.5"><strong style="color:#10b981">渐进验证：</strong>建立标准化技术验证到规模部署流程</div></div></div>
</div>
</div>'''

W("slide10.html", p(10,"#ef4444","rgba(239,68,68,0.1)","rgba(239,68,68,0.3)","SCQA · C→A",
    "Q1三个教训，每个都转化为Q2行动承诺",
    "C → A 模型：问题是诊断软件，行动才是确诊确药", b10, "10 / 14"))

# slide 11
b11 = '''<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;flex:1">
<div style="border-radius:16px;padding:28px;border:1px solid rgba(255,255,255,0.06);background:rgba(255,255,255,0.02);display:flex;flex-direction:column;gap:16px">
<div style="height:3px;border-radius:16px 16px 0 0;margin:-28px -28px 0 -28px;background:linear-gradient(90deg,#3b82f6,#60a5fa)"></div>
<div style="font-size:13px;font-weight:700;color:#3b82f6;letter-spacing:1px">战略一</div>
<div style="font-size:18px;font-weight:700;color:#fff;line-height:1.4">通用规划能力<br>拓展<strong style="color:#3b82f6">+30%</strong></div>
<div style="font-size:13px;color:#94a3b8;line-height:1.6">PlanBench决战标：9.6% → 40%+</div>
<div style="background:rgba(59,130,246,0.08);border-radius:8px;padding:12px 14px"><div style="font-size:12px;color:#93c5fd;line-height:1.6">→ PDDL训练集制作</div><div style="font-size:12px;color:#64748b;line-height:1.5;margin-top:4px">目标：5k+条规划轨迹</div></div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(59,130,246,0.15);border-radius:8px;padding:10px 12px;text-align:center"><div style="font-size:22px;font-weight:700;color:#3b82f6">+30%</div><div style="font-size:11px;color:#64748b;margin-top:2px">规划能力提升</div></div>
</div>
<div style="border-radius:16px;padding:28px;border:1px solid rgba(255,255,255,0.06);background:rgba(255,255,255,0.02);display:flex;flex-direction:column;gap:16px">
<div style="height:3px;border-radius:16px 16px 0 0;margin:-28px -28px 0 -28px;background:linear-gradient(90deg,#10b981,#34d399)"></div>
<div style="font-size:13px;font-weight:700;color:#10b981;letter-spacing:1px">战略二</div>
<div style="font-size:18px;font-weight:700;color:#fff;line-height:1.4">分布式集群推理<br>项目立项</div>
<div style="font-size:13px;color:#94a3b8;line-height:1.6">完成"分布式集群推理"TMT项目立项</div>
<div style="background:rgba(16,185,129,0.08);border-radius:8px;padding:12px 14px"><div style="font-size:12px;color:#93c5fd;line-height:1.6">→ KV Cache卸载功能验证</div><div style="font-size:12px;color:#64748b;line-height:1.5;margin-top:4px">→ 缓存感知调度再提升10%</div></div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(16,185,129,0.15);border-radius:8px;padding:10px 12px;text-align:center"><div style="font-size:22px;font-weight:700;color:#10b981">立项</div><div style="font-size:11px;color:#64748b;margin-top:2px">分布式集群推理</div></div>
</div>
<div style="border-radius:16px;padding:28px;border:1px solid rgba(255,255,255,0.06);background:rgba(255,255,255,0.02);display:flex;flex-direction:column;gap:16px">
<div style="height:3px;border-radius:16px 16px 0 0;margin:-28px -28px 0 -28px;background:linear-gradient(90deg,#8b5cf6,#a78bfa)"></div>
<div style="font-size:13px;font-weight:700;color:#a78bfa;letter-spacing:1px">战略三</div>
<div style="font-size:18px;font-weight:700;color:#fff;line-height:1.4">论文业务投稿<br><strong style="color:#a78bfa">"破冰"</strong></div>
<div style="font-size:13px;color:#94a3b8;line-height:1.6">目标：1-2篇学术论文投稿</div>
<div style="background:rgba(139,92,246,0.08);border-radius:8px;padding:12px 14px"><div style="font-size:12px;color:#93c5fd;line-height:1.6">→ 建立激励机制</div><div style="font-size:12px;color:#64748b;line-height:1.5;margin-top:4px">→ 团队经验总结拓展</div></div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(139,92,246,0.15);border-radius:8px;padding:10px 12px;text-align:center"><div style="font-size:22px;font-weight:700;color:#a78bfa">1-2篇</div><div style="font-size:11px;color:#64748b;margin-top:2px">论文投稿目标</div></div>
</div>
</div>'''

W("slide11.html", p(11,"#3b82f6","rgba(59,130,246,0.1)","rgba(59,130,246,0.3)","SCQA · Q&A",
    "Q2三大硬仗：第一把刘也，第二把论文投稿",
    "Q → A 模型：问题导向行动，行动导向结果", b11, "11 / 14"))

# slide 12
b12 = '''<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;flex:1;align-content:center">
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(59,130,246,0.15);border-radius:16px;padding:28px;text-align:center"><div style="font-size:48px;font-weight:800;color:#3b82f6;margin-bottom:8px">12</div><div style="font-size:14px;font-weight:700;color:#fff;margin-bottom:6px">专利推进</div><div style="font-size:12px;color:#94a3b8;line-height:1.6">已确认 7项<br>评审中 5项</div><div style="margin-top:12px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.06);font-size:11px;color:#64748b">采办方向：模型推理 | 训练优化 | 网络预测</div></div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(16,185,129,0.15);border-radius:16px;padding:28px;text-align:center"><div style="font-size:48px;font-weight:800;color:#10b981;margin-bottom:8px">18</div><div style="font-size:14px;font-weight:700;color:#fff;margin-bottom:6px">问题单解决</div><div style="font-size:12px;color:#94a3b8;line-height:1.6">网络产品12个<br>无线产品4个<br>其他产品2个</div><div style="margin-top:12px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.06);font-size:11px;color:#64748b">3个项目验收完成</div></div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(139,92,246,0.15);border-radius:16px;padding:28px;text-align:center"><div style="font-size:48px;font-weight:800;color:#a78bfa;margin-bottom:8px">5种</div><div style="font-size:14px;font-weight:700;color:#fff;margin-bottom:6px">RL算法适配</div><div style="font-size:12px;color:#94a3b8;line-height:1.6">DPO | GRPO | DAPO<br>GSPO | GDPO</div><div style="margin-top:12px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.06);font-size:11px;color:#64748b">支持框架：llamafactory | swift | Verl</div></div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(245,158,11,0.15);border-radius:16px;padding:28px;text-align:center"><div style="font-size:48px;font-weight:800;color:#fbbf24;margin-bottom:8px">完成</div><div style="font-size:14px;font-weight:700;color:#fff;margin-bottom:6px">白皮书发布</div><div style="font-size:12px;color:#94a3b8;line-height:1.6">《H3C百业灵犀AI<br>模型工程技术白皮书》</div><div style="margin-top:12px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.06);font-size:11px;color:#64748b">26年规划已入档</div></div>
</div>
<div style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:20px 24px;text-align:center"><div style="font-size:14px;color:#94a3b8;line-height:1.8"><strong style="color:#fff">技术壁垒 即 护城河</strong><br>专利、方法论、标准化流程 — 这些都是团队的核心竞争力</div></div>'''

W("slide12.html", p(12,"#3b82f6","rgba(59,130,246,0.1)","rgba(59,130,246,0.3)","SCQA · 数据",
    "关键数字一览通：Q1成果梳理毛飘香",
    "技术指标全部确认，商业价值每一项都有明确的加分项", b12, "12 / 14"))

# slide 13
b13 = '''<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;flex:1;text-align:center;gap:40px">
<div>
<div style="font-size:56px;margin-bottom:16px">🦞</div>
<div style="font-size:28px;font-weight:700;color:#fff;line-height:1.5;max-width:800px">Q1成为事实证明：<br><span style="color:#3b82f6">技术验证 → 业务交付</span><br><span style="color:#10b981">成本控制 → 效率提升</span><br><span style="color:#a78bfa">单点突破 → 系统性输出</span></div>
</div>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:16px;padding:32px 40px;max-width:700px"><div style="font-size:15px;color:#94a3b8;line-height:2">Q2我们将重点打击<strong style="color:#fff"> 通用规划能力 +30%+</strong>、<br>完成<strong style="color:#fff"> 分布式集群推理</strong>项目立项、<br>实现<strong style="color:#fff"> 论文投稿"破冰"</strong>——<br><strong style="color:#fff">持续为业务创造价值。</strong></div></div>
<div style="font-size:14px;color:#475569;letter-spacing:2px">团队态度：勇于承认不足，突破时不踩坑。</div>
</div>'''

W("slide13.html", p(13,"#10b981","rgba(