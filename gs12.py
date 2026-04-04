#!/usr/bin/env python3
"""Generate slides 12-14"""
import os
D = "/workspace/slides"
os.makedirs(D, exist_ok=True)
def W(f,c): open(os.path.join(D,f),"w",encoding="utf-8").write(c); print(f"OK {f} ({len(c)}b)")

B='<!DOCTYPE html><html lang="zh"><head><meta charset="UTF-8"><title>s{id}</title><style>*.{m:0;p:0;bx:border-box}body{font-family:PingFang SC,Microsoft YaHei,sans-serif;background:#0a0f2e;color:#fff}.slide{width:100vw;height:100vh;display:flex;flex-direction:column;padding:60px 80px;position:relative}.tag{font-size:13px;letter-spacing:3px;color:{tc};text-transform:uppercase;font-weight:600;margin-bottom:20px}.sn{font-size:13px;color:#334155;font-weight:700;margin-bottom:20px}.scqa{position:absolute;top:60px;right:80px;background:{sb};border:1px solid {sc};border-radius:8px;padding:10px 18px;font-size:13px;color:{tc};font-weight:600;letter-spacing:1px}h1{font-size:38px;font-weight:700;color:#fff;margin-bottom:8px}.sub{font-size:17px;color:#64748b;margin-bottom:36px}.ft{position:absolute;bottom:36px;left:80px;right:80px;display:flex;justify-content:space-between}.ft span{font-size:12px;color:#475569}</style></head><body><div class="slide"><div class="tag">{tag}</div><div class="sn">{sn}</div><div class="scqa">{sctag}</div><h1>{h1}</h1><div class="sub">{sub}</div>{body}<div class="ft"><span>SCQA模型 · 2026年Q1 AI模型工程团队述职</span><span>{sn}</span></div></div></body></html>'

def P(n,tc,sb,sc,sctag,h1,sub,body):
    W(f"slide{n}.html",B.format(id=n,tc=tc,sb=sb,sc=sc,sctag=sctag,h1=h1,sub=sub,body=body,sn=f"{n:02d} / 14",tag=sctag.split(" ")[0] if sctag else "SCQA"))

# slide12
P(12,"#3b82f6","rgba(59,130,246,0.1)","rgba(59,130,246,0.3)","SCQA · 数据",
  "关键数字一览通：Q1成果梳理毛飘香",
  "技术指标全部确认，商业价值每一项都有明确的加分项",
  '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;flex:1;align-content:center">'
  '<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(59,130,246,0.15);border-radius:16px;padding:28px;text-align:center"><div style="font-size:48px;font-weight:800;color:#3b82f6;margin-bottom:8px">12</div><div style="font-size:14px;font-weight:700;color:#fff;margin-bottom:6px">专利推进</div><div style="font-size:12px;color:#94a3b8;line-height:1.6">已确认 7项<br>评审中 5项</div><div style="margin-top:12px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.06);font-size:11px;color:#64748b">模型推理 | 训练优化 | 网络预测</div></div>'
  '<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(16,185,129,0.15);border-radius:16px;padding:28px;text-align:center"><div style="font-size:48px;font-weight:800;color:#10b981;margin-bottom:8px">18</div><div style="font-size:14px;font-weight:700;color:#fff;margin-bottom:6px">问题单解决</div><div style="font-size:12px;color:#94a3b8;line-height:1.6">网络产品12个<br>无线产品4个<br>其他产品2个</div><div style="margin-top:12px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.06);font-size:11px;color:#64748b">3个项目验收完成</div></div>'
  '<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(139,92,246,0.15);border-radius:16px;padding:28px;text-align:center"><div style="font-size:48px;font-weight:800;color:#a78bfa;margin-bottom:8px">5种</div><div style="font-size:14px;font-weight:700;color:#fff;margin-bottom:6px">RL算法适配</div><div style="font-size:12px;color:#94a3b8;line-height:1.6">DPO | GRPO | DAPO<br>GSPO | GDPO</div><div style="margin-top:12px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.06);font-size:11px;color:#64748b">llamafactory | swift | Verl</div></div>'
  '<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(245,158,11,0.15);border-radius:16px;padding:28px;text-align:center"><div style="font-size:48px;font-weight:800;color:#fbbf24;margin-bottom:8px">完成</div><div style="font-size:14px;font-weight:700;color:#fff;margin-bottom:6px">白皮书发布</div><div style="font-size:12px;color:#94a3b8;line-height:1.6">《H3C百业灵犀AI<br>模型工程技术白皮书》</div><div style="margin-top:12px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.06);font-size:11px;color:#64748b">26年规划已入档</div></div></div>'
  '<div style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:20px 24px;text-align:center;margin-top:24px"><div style="font-size:14px;color:#94a3b8;line-height:1.8"><strong style="color:#fff">技术壁垒 即 护城河</strong><br>专利、方法论、标准化流程 — 这些都是团队的核心竞争力</div></div>')

# slide13
P(13,"#10b981","rgba(16,185,129,0.1)","rgba(16,185,129,0.3)","SCQA · A",
  "结语：Q1打基础，Q2再进一步",
  "A — Answer ：行动将世界应答我们的改变",
  '<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;flex:1;text-align:center;gap:40px">'
  '<div><div style="font-size:56px;margin-bottom:16px">🦞</div><div style="font-size:28px;font-weight:700;color:#fff;line-height:1.5;max-width:800px">Q1成为事实证明：<br><span style="color:#3b82f6">技术验证 → 业务交付</span><br><span style="color:#10b981">成本控制 → 效率提升</span><br><span style="color:#a78bfa">单点突破 → 系统性输出</span></div></div>'
  '<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:16px;padding:32px 40px;max-width:700px"><div style="font-size:15px;color:#94a3b8;line-height:2">Q2我们将重点打击<strong style="color:#fff"> 通用规划能力 +30%+</strong>、<br>完成<strong style="color:#fff"> 分布式集群推理</strong>项目立项、<br>实现<strong style="color:#fff"> 论文投稿"破冰"</strong>——<br><strong style="color:#fff">持续为业务创造价值。</strong></div></div>'
  '<div style="font-size:14px;color:#475569;letter-spacing:2px">团队态度：勇于承认不足，突破时不踩坑。</div></div>')

# slide14
P(14,"#64748b","rgba(100,116,139,0.1)","rgba(100,116,139,0.3)","附录",
  "附录：技术指标原始数据与Q2展望",
  "仅供技术相关者参考，主会内容以前页为准",
  '<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;flex:1;align-content:start">'
  '<div><div style="font-size:14px;font-weight:700;color:#93c5fd;margin-bottom:14px;padding-bottom:8px;border-bottom:1px solid rgba(59,130,246,0.15)">技术指标原始数据</div>'
  '<div style="display:flex;flex-direction:column;gap:8px">'
  '<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px"><div style="font-size:13px;color:#94a3b8">意图识别准确率</div><div style="font-size:13px;font-weight:700;color:#3b82f6">95%+</div></div>'
  '<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px"><div style="font-size:13px;color:#94a3b8">L1准确率</div><div style="font-size:13px;font-weight:700;color:#3b82f6">96.4%</div></div>'
  '<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px"><div style="font-size:13px;color:#94a3b8">TTFT降低（4P4D）</div><div style="font-size:13px;font-weight:700;color:#10b981">17.5%</div></div>'
  '<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px"><div style="font-size:13px;color:#94a3b8">规划能力提升</div><div style="font-size:13px;font-weight:700;color:#8b5cf6">26%→52%</div></div>'
  '<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px"><div style="font-size:13px;color:#94a3b8">专利推进</div><div style="font-size:13px;font-weight:700;color:#f59e0b">12项</div></div>'
  '<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px"><div style="font-size:13px;color:#94a3b8">产品线问题单</div><div style="font-size:13px;font-weight:700;color:#ef4444">18个</div></div></div></div>'
  '<div><div style="font-size:14px;font-weight:700;color:#93c5fd;margin-bottom:14px;padding-bottom:8px;border-bottom:1px solid rgba(59,130,246,0.15)">预期Q2成果</div>'
  '<div style="display:flex;flex-direction:column;gap:8px">'
  '<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(59,130,246,0.05);border:1px solid rgba(59,130,246,0.15);border-radius:8px"><div style="font-size:13px;color:#94a3b8">PlanBench</div><div style="font-size:13px;font-weight:700;color:#3b82f6">40%+</div></div>'
  '<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(16,185,129,0.05);border:1px solid rgba(16,185,129,0.15);border-radius:8px"><div style="font-size:13px;color:#94a3b8">分布式集群</div><div style="font-size:13px;font-weight:700;color:#10b981">立项</div></div>'
  '<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(139,92,246,0.05);border:1px solid rgba(139,92,246,0.15);border-radius:8px"><div style="font-size:13px;color:#94a3b8">论文投稿</div><div style="font-size:13px;font-weight:700;color:#a78bfa">1-2篇</div></div>'
  '<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px"><div style="font-size:13px;color:#94a3b8">缓存调度提升</div><div style="font-size:13px;font-weight:700;color:#3b82f6">+10%</div></div>'
  '<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px"><div style="font-size:13px;color:#94a3b8">PDDL规划轨迹</div><div style="font-size:13px;font-weight:700;color:#10b981">5k+</div></div>'
  '<div style="display:flex;justify-content:space-between;padding:10px 14px;background:rgba(255,255,255,0.02);border-radius:8px"><div style="font-size:13px;color:#94a3b8">产品线验收</div><div style="font-size:13px;font-weight:700;color:#ef4444">2项</div></div></div></div></div>')

print("All slides generated!")
