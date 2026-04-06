/**
 * SOTA Radar — 主仪表盘 (AppC)
 * V4.0~V8.0 均使用此组件，版本切换控制功能可用性
 */
import { useState, useEffect, useRef } from 'react'
import { truthCases } from './dataA'
import { orgChart, cronSchedule, dagNodes, buildDagSnapshot, todayLog, type DagNode, type NodeStatus } from './dataC'
import ModelLibrary from './ModelLibrary'
import SkillsViewer from './SkillsViewer'

// 外部传入的版本号，用于条件渲染
interface AppCProps {
  version?: string  // e.g. 'v4.0', 'v5.0', 'v6.0'
  activePage?: 'home' | 'library' | 'skills'
}

const c = {
  bg: '#030712', surface: '#0f172a', card: '#111827',
  border: '#1e293b', text: '#f1f5f9', muted: '#64748b',
  accent: '#38bdf8', accent2: '#818cf8', green: '#34d399',
  red: '#f87171', amber: '#fbbf24', pink: '#f472b6', purple: '#a78bfa',
}

// ─── 工具函数 ───────────────────────────────────────────────
function versionGte(a: string, b: string): boolean {
  const parse = (v: string) => {
    const m = v.replace('v','').split('.')
    return parseInt(m[0]) * 100 + parseInt(m[1] || '0')
  }
  return parse(a) >= parse(b)
}

// ─── Status badge ───────────────────────────────────────────────
function StatusBadge({ status }: { status: NodeStatus }) {
  const cfg: Record<NodeStatus, { color: string; bg: string; label: string }> = {
    idle: { color: c.muted, bg: '#1e293b', label: '待机' },
    pending: { color: c.muted, bg: '#1e293b', label: '等待' },
    running: { color: c.accent, bg: '#0c2645', label: '进行中' },
    done: { color: c.green, bg: '#052e16', label: '完成' },
    rejected: { color: c.red, bg: '#2d0a0a', label: '拒绝' },
  }
  const x = cfg[status]
  return (
    <span style={{ fontSize: 9, fontWeight: 700, padding: '2px 7px', borderRadius: 100, background: x.bg, color: x.color, border: `1px solid ${x.color}40` }}>
      {status === 'running' ? `⚡ ${x.label}` : x.label}
    </span>
  )
}

// ─── DAG Visualizer ────────────────────────────────────────────
function DAGView({ nodes }: { nodes: DagNode[] }) {
  const nodeW = 78; const nodeH = 48
  const p = (id: string) => {
    const m: Record<string, { x: number; y: number }> = {
      trigger: { x: 30, y: 90 }, '分配': { x: 130, y: 30 },
      scout: { x: 230, y: 30 }, qc: { x: 330, y: 30 },
      '反馈': { x: 430, y: 130 }, '归档': { x: 430, y: 30 },
      '自审': { x: 530, y: 30 }, '完成': { x: 620, y: 30 },
    }
    return m[id]
  }
  const cx = (id: string) => p(id).x + nodeW / 2
  const cy = (id: string) => p(id).y + nodeH / 2

  const edges = [
    { from: 'trigger', to: '分配', label: '开始' },
    { from: '分配', to: 'scout', label: '分发' },
    { from: 'scout', to: 'qc', label: '提交' },
    { from: 'qc', to: '归档', label: '通过' },
    { from: 'qc', to: '反馈', label: '拒绝', color: c.red, dashed: true },
    { from: '反馈', to: 'scout', label: '打回', color: c.red, dashed: true },
    { from: '归档', to: '自审', label: '同步' },
    { from: '自审', to: '完成', label: '进化' },
    { from: '完成', to: 'trigger', label: '等待下次', color: c.muted, dashed: true },
  ]

  return (
    <svg width={680} height={220} style={{ overflow: 'visible' }}>
      <defs>
        <marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
          <polygon points="0 0, 10 3.5, 0 7" fill={c.accent} opacity="0.7" />
        </marker>
        <marker id="arrowRed" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
          <polygon points="0 0, 10 3.5, 0 7" fill={c.red} opacity="0.7" />
        </marker>
        <marker id="arrowGray" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
          <polygon points="0 0, 10 3.5, 0 7" fill={c.muted} opacity="0.5" />
        </marker>
      </defs>
      {edges.map((e, i) => {
        const sx = cx(e.from), sy = cy(e.from), ex = cx(e.to), ey = cy(e.to)
        const mx = (sx + ex) / 2, my = (sy + ey) / 2
        const c1x = mx, c1y = sy, c2x = mx, c2y = ey
        const color = e.color || c.accent
        const marker = e.dashed ? (e.color === c.red ? 'url(#arrowRed)' : 'url(#arrowGray)') : 'url(#arrow)'
        return (
          <g key={i}>
            <path d={`M ${sx} ${sy} C ${c1x} ${c1y} ${c2x} ${c2y} ${ex} ${ey}`}
              stroke={color} strokeWidth={e.dashed ? 1.5 : 2}
              strokeDasharray={e.dashed ? '5,4' : undefined}
              fill="none" markerEnd={marker} opacity={e.dashed ? 0.6 : 0.8} />
            <text x={mx} y={my - 6} textAnchor="middle" fill={color} fontSize={9} opacity={0.9}>{e.label}</text>
          </g>
        )
      })}
      {nodes.map(n => {
        const pos = p(n.id); if (!pos) return null
        const isRejected = n.status === 'rejected'
        return (
          <g key={n.id} style={{ cursor: 'default' }}>
            <rect x={pos.x} y={pos.y} width={nodeW} height={nodeH} rx={10}
              fill={isRejected ? c.red + '22' : c.card}
              stroke={isRejected ? c.red + '60' : c.border}
              strokeWidth={1.5} />
            <text x={pos.x + nodeW / 2} y={pos.y + nodeH / 2 - 4} textAnchor="middle"
              fill={isRejected ? c.red : c.accent} fontSize={11} fontWeight={700}>{n.label}</text>
            <text x={pos.x + nodeW / 2} y={pos.y + nodeH / 2 + 12} textAnchor="middle"
              fill={c.muted} fontSize={9}>{n.sub}</text>
          </g>
        )
      })}
    </svg>
  )
}

// ─── Org Chart ─────────────────────────────────────────────────
function OrgChart({ expanded, onToggle }: { expanded: boolean; onToggle: () => void }) {
  const { pm, teams } = orgChart
  return (
    <div style={{ marginBottom: 8 }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 6 }}>
        <div style={{ width: 36, height: 36, borderRadius: 10, background: c.pink + '25', border: `1.5px solid ${c.pink}60`, display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 18 }}>
          {pm.icon}
        </div>
        <div>
          <div style={{ fontSize: 13, fontWeight: 800, color: c.text }}>
            {pm.name} <span style={{ fontSize: 10, color: c.pink, fontWeight: 600 }}>{pm.role}</span>
          </div>
          <div style={{ fontSize: 10, color: c.muted }}>{pm.desc}</div>
        </div>
        <button onClick={onToggle} style={{
          marginLeft: 'auto', background: c.surface, border: `1px solid ${c.border}`,
          borderRadius: 8, padding: '4px 10px', color: c.accent, fontSize: 11, cursor: 'pointer',
        }}>
          {expanded ? '收起 ▲' : '展开 ▼'}
        </button>
      </div>
      {expanded && <div style={{ width: 18, height: 1, background: c.border, marginBottom: 10 }} />}
      {expanded && (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 10 }}>
          {teams.map(t => (
            <div key={t.team} style={{
              background: c.card, border: `1px solid ${c.border}`, borderRadius: 12, padding: '12px',
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 8 }}>
                <span style={{ fontSize: 14 }}>{t.icon}</span>
                <span style={{ fontSize: 12, fontWeight: 700, color: t.color }}>{t.team}</span>
                <span style={{ fontSize: 9, color: c.muted }}>({t.members.length})</span>
              </div>
              {t.members.map(m => (
                <div key={m.id} style={{
                  display: 'flex', alignItems: 'center', gap: 6, padding: '4px 0',
                  borderBottom: `1px solid ${c.border}30`,
                }}>
                  <StatusBadge status={m.status as NodeStatus} />
                  <div>
                    <div style={{ fontSize: 11, fontWeight: 600, color: c.text }}>{m.name}</div>
                    <div style={{ fontSize: 9, color: c.muted }}>{m.role}</div>
                  </div>
                </div>
              ))}
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

// ─── Cron Cards ────────────────────────────────────────────────
function CronCards({ version }: { version: string }) {
  const [statusData, setStatusData] = useState<any>(null)
  const [triggerResult, setTriggerResult] = useState<{type: 'success'|'error'; msg: string} | null>(null)
  const [loading, setLoading] = useState(false)
  const hasBackend = versionGte(version, 'v5.0')

  useEffect(() => {
    if (!hasBackend) return
    const poll = async () => {
      try {
        const r = await fetch('http://localhost:7860/api/v1/status/current')
        if (r.ok) setStatusData(await r.json())
      } catch {}
    }
    poll()
    const id = setInterval(poll, 15000)
    return () => clearInterval(id)
  }, [hasBackend])

  function handleTrigger() {
    if (!hasBackend) return
    setLoading(true)
    fetch('http://localhost:7860/api/v1/flywheel/trigger', { method: 'POST', headers: {'Content-Type':'application/json'}, body: '{}' })
      .then(r => r.json())
      .then(d => setTriggerResult({ type: 'success', msg: `🚀 飞轮已触发！run_id: ${d.run_id}` }))
      .catch(() => setTriggerResult({ type: 'error', msg: '❌ 触发失败，请稍后重试' }))
      .finally(() => setLoading(false))
      setTimeout(() => setTriggerResult(null), 5000)
  }

  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr auto', gap: 12, alignItems: 'start' }}>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10 }}>
        {Object.values(cronSchedule).map((s: any, i: number) => (
          <div key={i} style={{
            background: c.card, border: `1px solid ${c.border}`, borderRadius: 12,
            padding: '12px 16px', display: 'flex', alignItems: 'center', gap: 12,
          }}>
            <div style={{ flex: 1 }}>
              <div style={{ fontSize: 12, fontWeight: 700, color: c.text }}>{s.time}</div>
              <div style={{ fontSize: 11, color: c.muted }}>{s.task}</div>
            </div>
            <span style={{ fontSize: 9, fontWeight: 600, padding: '3px 8px', borderRadius: 100, background: c.green + '20', color: c.green, border: `1px solid ${c.green}40` }}>{s.type}</span>
          </div>
        ))}
      </div>

      {/* 右侧：状态 + 触发按钮（V5.0+才显示） */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 10, minWidth: 200 }}>
        {hasBackend && statusData && (
          <div style={{
            background: c.card, border: `1px solid ${c.border}`, borderRadius: 12, padding: '12px',
          }}>
            <div style={{ fontSize: 10, color: c.muted, marginBottom: 6 }}>实时状态</div>
            <div style={{ fontSize: 11, fontWeight: 700, color: statusData.state === 'RUNNING' ? c.accent : c.muted }}>
              {statusData.state === 'RUNNING' ? '⚡ 进行中' : '○ 待机'}
            </div>
            <div style={{ fontSize: 10, color: c.muted, marginTop: 4 }}>
              今日运行：{statusData.today_runs} 次
            </div>
          </div>
        )}
        {hasBackend && (
          <button
            onClick={handleTrigger}
            disabled={loading}
            style={{
              padding: '10px 16px', borderRadius: 10, border: 'none', cursor: loading ? 'not-allowed' : 'pointer',
              background: loading ? c.surface : 'linear-gradient(135deg, #0052d4, #0d47a1)',
              color: loading ? c.muted : '#fff', fontWeight: 700, fontSize: 13, textAlign: 'center',
              boxShadow: '0 4px 16px #0052d440',
            }}
          >
            {loading ? '触发中…' : '🚀 立即触发'}
          </button>
        )}
        {!hasBackend && (
          <div style={{
            background: c.card, border: `1px solid ${c.border}`, borderRadius: 12, padding: '12px',
            textAlign: 'center', fontSize: 11, color: c.muted,
          }}>
            后端功能待接入<br /><span style={{ fontSize: 10, color: c.accent }}>切换至 V5.0+ 体验</span>
          </div>
        )}
      </div>

      {/* Toast */}
      {triggerResult && (
        <div style={{
          position: 'fixed', top: 80, right: 24, zIndex: 9999,
          padding: '10px 18px', borderRadius: 10,
          background: triggerResult.type === 'success' ? '#052e16' : '#2d0a0a',
          color: triggerResult.type === 'success' ? c.green : c.red,
          border: `1px solid ${triggerResult.type === 'success' ? c.green : c.red}40`,
          fontSize: 12, fontWeight: 600,
          boxShadow: '0 8px 24px rgba(0,0,0,0.5)',
          maxWidth: 320,
        }}>
          {triggerResult.msg}
        </div>
      )}
    </div>
  )
}

// ─── Verdict Badge ─────────────────────────────────────────────
function VerdictBadge({ verdict }: { verdict: string }) {
  const map: Record<string, { color: string; bg: string }> = {
    '✅ 已修复': { color: c.green, bg: '#052e16' },
    '⚠️ 待核实': { color: c.amber, bg: '#3b1d00' },
    '❌ 误报': { color: c.red, bg: '#2d0a0a' },
    '✅ 合规': { color: c.green, bg: '#052e16' },
    '⚠️ 合规存疑': { color: c.amber, bg: '#3b1d00' },
    '❌ 不合规': { color: c.red, bg: '#2d0a0a' },
  }
  const x = map[verdict] || { color: c.muted, bg: c.card }
  return (
    <span style={{ fontSize: 10, fontWeight: 700, padding: '3px 8px', borderRadius: 100, background: x.bg, color: x.color, border: `1px solid ${x.color}50` }}>
      {verdict}
    </span>
  )
}

// ─── Truth Card ────────────────────────────────────────────────
function TruthCard({ item, index }: { item: any; index: number }) {
  const [expanded, setExpanded] = useState(false)
  return (
    <div style={{
      minWidth: 340, maxWidth: 380, background: c.card, border: `1px solid ${c.border}`,
      borderRadius: 14, overflow: 'hidden', flexShrink: 0,
    }}>
      <div style={{ padding: '14px 16px', borderBottom: `1px solid ${c.border}` }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 6 }}>
          <span style={{ fontSize: 9, fontWeight: 700, padding: '2px 7px', borderRadius: 100, background: '#1e293b', color: c.muted }}>
            Case {index + 1}
          </span>
          <span style={{ fontSize: 9, padding: '2px 7px', borderRadius: 100, background: c.red + '20', color: c.red, border: `1px solid ${c.red}40` }}>
            {item.category}
          </span>
        </div>
        <div style={{ fontSize: 13, fontWeight: 800, color: c.text, marginBottom: 4 }}>{item.title}</div>
        <div style={{ fontSize: 11, color: c.muted }}>{item.source}</div>
      </div>
      <div style={{ padding: '12px 16px' }}>
        <div style={{ fontSize: 11, color: c.muted, marginBottom: 6 }}>核查结论</div>
        <VerdictBadge verdict={item.ourVerdict} />
        <div style={{ fontSize: 10, color: c.text, marginTop: 10, lineHeight: 1.6 }}>{item.summary}</div>
      </div>
      {item.evidence && item.evidence.length > 0 && (
        <div style={{ padding: '0 16px 12px' }}>
          <div style={{ fontSize: 11, color: c.muted, marginBottom: 6 }}>证据链</div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
            {item.evidence.map((e: any, i: number) => (
              <div key={i} style={{ display: 'flex', gap: 6, fontSize: 10, color: c.text }}>
                <span style={{ color: c.accent, fontWeight: 700 }}>→</span>
                <span>{e}</span>
              </div>
            ))}
          </div>
        </div>
      )}
      {item.exactQuote && (
        <div style={{ padding: '0 16px 12px' }}>
          <div style={{ fontSize: 11, color: c.muted, marginBottom: 4 }}>原始引述</div>
          <blockquote style={{
            margin: 0, padding: '8px 12px', borderLeft: `3px solid ${c.accent}50`,
            background: c.surface, borderRadius: '0 6px 6px 0', fontSize: 10,
            color: c.muted, fontStyle: 'italic', lineHeight: 1.6,
          }}>
            "{item.exactQuote}"
          </blockquote>
        </div>
      )}
      {item.sourceUrl && (
        <div style={{ padding: '0 16px 12px' }}>
          <a href={item.sourceUrl} target="_blank" rel="noopener noreferrer" style={{
            fontSize: 10, color: c.accent, textDecoration: 'none',
          }}>
            ↗ 查看来源
          </a>
        </div>
      )}
      <div style={{ padding: '8px 16px', borderTop: `1px solid ${c.border}`, background: c.surface }}>
        <button onClick={() => setExpanded(!expanded)} style={{
          fontSize: 10, color: c.muted, background: 'none', border: 'none', cursor: 'pointer', padding: 0,
        }}>
          {expanded ? '收起 ▲' : '展开 lesson ▼'}
        </button>
        {expanded && (
          <p style={{ fontSize: 10, color: c.muted, margin: '8px 0 0', fontStyle: 'italic', lineHeight: 1.5 }}>
            → {item.lesson}
          </p>
        )}
      </div>
    </div>
  )
}

// ─── Work Log ──────────────────────────────────────────────────
function WorkLog() {
  return (
    <div style={{ background: c.surface, border: `1px solid ${c.border}`, borderRadius: 14, overflow: 'hidden' }}>
      <div style={{ padding: '12px 16px', borderBottom: `1px solid ${c.border}`, fontSize: 12, fontWeight: 700, color: c.text }}>
        今日工作记录
      </div>
      <div style={{ padding: '12px 16px', display: 'flex', flexDirection: 'column', gap: 10 }}>
        {todayLog.map((l, i) => (
          <div key={i} style={{ display: 'flex', gap: 10, fontSize: 11 }}>
            <span style={{ color: c.accent, fontWeight: 700, minWidth: 80 }}>{l.agent}</span>
            <span style={{ color: c.muted }}>{l.action}</span>
          </div>
        ))}
      </div>
    </div>
  )
}

// ─── Closed Loop Flow ───────────────────────────────────────────
function ClosedLoopFlow() {
  const steps = [
    { icon: '📝', label: 'Commit History', sub: '变更记录' },
    { icon: '🔍', label: 'Skill Self-Review', sub: '规则自审' },
    { icon: '📊', label: 'Pattern Analysis', sub: '模式分析' },
    { icon: '🔄', label: 'Update Skills', sub: '更新规则' },
    { icon: '⏰', label: 'Next Run', sub: '等待下次' },
  ]
  return (
    <div style={{ display: 'flex', gap: 0, alignItems: 'center', overflowX: 'auto', padding: '4px 0' }}>
      {steps.map((s, i) => (
        <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 0, flexShrink: 0 }}>
          <div style={{
            background: c.card, border: `1px solid ${c.border}`, borderRadius: 12,
            padding: '12px 16px', textAlign: 'center', minWidth: 120,
          }}>
            <div style={{ fontSize: 20, marginBottom: 4 }}>{s.icon}</div>
            <div style={{ fontSize: 11, fontWeight: 700, color: c.text }}>{s.label}</div>
            <div style={{ fontSize: 9, color: c.muted }}>{s.sub}</div>
          </div>
          {i < steps.length - 1 && (
            <div style={{ display: 'flex', alignItems: 'center', padding: '0 4px' }}>
              <span style={{ color: c.accent, fontSize: 14 }}>→</span>
            </div>
          )}
        </div>
      ))}
    </div>
  )
}

// ─── Goals Panel ───────────────────────────────────────────────
function GoalsPanel({ version }: { version: string }) {
  const goals = [
    { label: 'P0拦截率', value: '4%', target: '>10%', ok: false },
    { label: 'Benchmark合规', value: '68%', target: '>90%', ok: false },
    { label: 'Skill更新', value: '3项', target: '持续', ok: true },
    { label: '质检覆盖率', value: '100%', target: '100%', ok: true },
  ]
  return (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 10 }}>
      {goals.map((g, i) => (
        <div key={i} style={{
          background: c.card, border: `1px solid ${g.ok ? c.green + '40' : c.amber + '40'}`,
          borderRadius: 12, padding: '14px', textAlign: 'center',
        }}>
          <div style={{ fontSize: 20, fontWeight: 900, color: g.ok ? c.green : c.amber, marginBottom: 4 }}>
            {g.value}
          </div>
          <div style={{ fontSize: 11, color: c.muted }}>{g.label}</div>
          <div style={{ fontSize: 9, color: c.muted, marginTop: 2 }}>目标 {g.target}</div>
        </div>
      ))}
    </div>
  )
}

// ─── MAIN APP ──────────────────────────────────────────────────

// ─── Task Board ────────────────────────────────────────────────
function TaskBoard({ version }: { version: string }) {
  const tasks = [
    { id: 'v5.1', title: 'V5.0: FastAPI核心+知识存储', owner: '子智能体-A', status: '已完成', started: '10:05', finished: '10:15', duration: '10分钟', version: 'V5.0', notes: '后端v0.1完成，7860端口运行', color: '#34d399' },
    { id: 'v5.2', title: 'V5.0: 前端API接入+版本切换', owner: 'AI PM', status: '已完成', started: '10:16', finished: '11:30', duration: '74分钟', version: 'V5.0', notes: '版本切换器重构，AppC重写', color: '#34d399' },
    { id: 'v6.1', title: 'V6.0: OpenClaw Agent真实触发', owner: '子智能体-3', status: '进行中', started: '01:36', finished: '—', duration: '进行中', version: 'V6.0', notes: 'OpenClaw CLI接入，线程化触发', color: '#38bdf8' },
    { id: 'v7.1', title: 'V7.0: SSE实时状态推送', owner: '待分配', status: '待开始', started: '—', finished: '—', duration: '—', version: 'V7.0', notes: '', color: '#64748b' },
    { id: 'v8.1', title: 'V8.0: Cron定时+GitHub同步', owner: '待分配', status: '待开始', started: '—', finished: '—', duration: '—', version: 'V8.0', notes: '', color: '#64748b' },
  ]

  return (
    <div style={{ maxWidth: 1100, margin: '0 auto', padding: '0 48px 48px' }}>
      <div style={{ marginBottom: 28 }}>
        <div style={{ fontSize: 10, color: '#38bdf8', fontWeight: 700, letterSpacing: '0.1em', textTransform: 'uppercase', marginBottom: 8 }}>
          团队协作 · 任务追踪
        </div>
        <h1 style={{ fontSize: 26, fontWeight: 900, color: '#f1f5f9', margin: 0 }}>
          任务看板 · Task Board
        </h1>
        <p style={{ fontSize: 13, color: '#64748b', margin: '8px 0 0' }}>
          每个任务有明确owner、时间记录、状态追踪 · 当前时间 {new Date().toLocaleTimeString('zh-CN', {hour:'2-digit',minute:'2-digit',second:'2-digit'})}
        </p>
      </div>

      {/* Stats row */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: 12, marginBottom: 28 }}>
        {[
          { label: '总任务', value: tasks.length, color: '#38bdf8' },
          { label: '已完成', value: tasks.filter(t => t.status === '已完成').length, color: '#34d399' },
          { label: '进行中', value: tasks.filter(t => t.status === '进行中').length, color: '#38bdf8' },
          { label: '待开始', value: tasks.filter(t => t.status === '待开始').length, color: '#64748b' },
          { label: '本周完成', value: tasks.filter(t => t.status === '已完成').length, color: '#a78bfa' },
        ].map((s, i) => (
          <div key={i} style={{ background: '#111827', border: `1px solid #1e293b`, borderRadius: 12, padding: '16px', textAlign: 'center' }}>
            <div style={{ fontSize: 28, fontWeight: 900, color: s.color }}>{s.value}</div>
            <div style={{ fontSize: 11, color: '#64748b', marginTop: 4 }}>{s.label}</div>
          </div>
        ))}
      </div>

      {/* Task list */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
        {tasks.map((t, i) => (
          <div key={t.id} style={{
            background: '#111827', border: `1px solid ${t.color}40`, borderRadius: 14,
            padding: '16px 20px',
            borderLeft: `4px solid ${t.color}`,
          }}>
            <div style={{ display: 'flex', alignItems: 'flex-start', gap: 12 }}>
              {/* Version tag */}
              <div style={{
                fontSize: 9, fontWeight: 900, padding: '4px 10px', borderRadius: 100,
                background: t.color + '20', color: t.color, border: `1px solid ${t.color}60`,
                minWidth: 48, textAlign: 'center', letterSpacing: '0.05em', flexShrink: 0, marginTop: 2,
              }}>
                {t.version}
              </div>

              {/* Content */}
              <div style={{ flex: 1 }}>
                <div style={{ fontSize: 14, fontWeight: 700, color: '#f1f5f9', marginBottom: 4 }}>{t.title}</div>
                <div style={{ fontSize: 11, color: '#64748b', marginBottom: t.notes ? 6 : 0 }}>
                  👤 {t.owner} {t.notes ? `· ${t.notes}` : ''}
                </div>
                {t.notes && <div style={{ fontSize: 11, color: '#475569', fontStyle: 'italic' }}>→ {t.notes}</div>}
              </div>

              {/* Time tracking */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: 4, alignItems: 'flex-end', flexShrink: 0 }}>
                <span style={{
                  fontSize: 10, fontWeight: 700, padding: '3px 10px', borderRadius: 100,
                  background: t.color + '20', color: t.color, border: `1px solid ${t.color}40`,
                }}>
                  {t.status}
                </span>
                <div style={{ fontSize: 10, color: '#475569', textAlign: 'right' }}>
                  {t.started !== '—' && <>开始 {t.started}<br /></>}
                  {t.finished !== '—' && <>结束 {t.finished}<br /></>}
                  <strong style={{ color: '#94a3b8' }}>{t.duration}</strong>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default function AppC({ version = 'v5.0', activePage = 'home' }: AppCProps) {
  const [mounted, setMounted] = useState(false)
  const [orgExpanded, setOrgExpanded] = useState(true)
  const [activeTab, setActiveTab] = useState<string>(activePage)
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null)

  useEffect(() => { setTimeout(() => setMounted(true), 100) }, [])
  useEffect(() => { setActiveTab(activePage as any) }, [activePage])

  return (
    <div style={{ minHeight: '100vh', background: c.bg, color: c.text, fontFamily: "'Inter',system-ui,sans-serif", position: 'relative' }}>
      {/* Background glow */}
      <div style={{ position: 'fixed', inset: 0, pointerEvents: 'none', zIndex: 0, overflow: 'hidden' }}>
        <div style={{ position: 'absolute', width: 600, height: 600, top: -200, left: -100, borderRadius: '50%', background: 'radial-gradient(circle,#1d4ed820 0%,transparent 70%)' }} />
        <div style={{ position: 'absolute', width: 500, height: 500, top: 200, right: -150, borderRadius: '50%', background: 'radial-gradient(circle,#818cf810 0%,transparent 70%)' }} />
      </div>

      {/* Nav */}
      <div style={{
        borderBottom: `1px solid ${c.border}`, padding: '0 48px', height: 60,
        display: 'flex', alignItems: 'center', gap: 0, position: 'sticky', top: 0, zIndex: 100,
        background: 'rgba(3,7,18,0.9)', backdropFilter: 'blur(20px)',
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginRight: 24 }}>
          <div style={{
            width: 32, height: 32, borderRadius: 8,
            background: `linear-gradient(135deg, ${c.accent}40, ${c.accent2}40)`,
            border: `1.5px solid ${c.accent}60`,
            display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 16,
          }}>
            ⚡
          </div>
          <div>
            <div style={{ fontSize: 14, fontWeight: 800, color: c.text, lineHeight: 1.2 }}>SOTA Radar</div>
            <div style={{ fontSize: 9, color: c.accent, fontWeight: 600 }}>模型知识飞轮</div>
          </div>
        </div>

        {/* Version badge */}
        <div style={{
          fontSize: 9, fontWeight: 700, padding: '3px 8px', borderRadius: 100,
          background: '#38bdf820', color: c.accent, border: `1px solid #38bdf840`,
          marginRight: 8, letterSpacing: '0.05em',
        }}>
          {version.toUpperCase()}
        </div>

        {/* Tab nav */}
        <div style={{ display: 'flex', gap: 4, marginLeft: 8 }}>
          {[
            { id: 'home', label: '🏠 首页' },
            { id: 'tasks', label: '📋 任务看板' },
            { id: 'library', label: '📚 模型知识库' },
            { id: 'skills', label: '📄 Skills文档库' },
          ].map(tab => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id as any)}
              style={{
                padding: '5px 14px', borderRadius: 8, border: 'none', fontSize: 12, fontWeight: 600,
                cursor: 'pointer', transition: 'all 0.15s',
                background: activeTab === tab.id ? c.accent + '22' : 'transparent',
                color: activeTab === tab.id ? c.accent : c.muted,
                borderBottom: activeTab === tab.id ? `2px solid ${c.accent}` : '2px solid transparent',
              }}
            >
              {tab.label}
            </button>
          ))}
        </div>

        <div style={{ marginLeft: 'auto', display: 'flex', alignItems: 'center', gap: 8 }}>
          <span style={{ fontSize: 11, color: c.green, fontWeight: 600 }}>●</span>
          <span style={{ fontSize: 11, color: c.muted }}>Powered by OpenClaw</span>
        </div>
      </div>

      {/* Page content */}
      {activeTab === 'tasks' && (
        <div style={{ paddingTop: 80 }}>
          <TaskBoard version={version} />
        </div>
      )}
      {(activeTab === 'library' || activeTab === 'skills') && (
        <div style={{ paddingTop: 80 }}>
          {activeTab === 'library' && <ModelLibrary />}
          {activeTab === 'skills' && <SkillsViewer />}
        </div>
      )}

      {activeTab === 'home' && (
        <div style={{ maxWidth: 1200, margin: '0 auto', padding: '40px 48px', position: 'relative', zIndex: 1 }}>

          {/* Hero */}
          <div style={{ textAlign: 'center', marginBottom: 40, opacity: mounted ? 1 : 0, transition: 'opacity 0.5s' }}>
            <div style={{ fontSize: 10, fontWeight: 700, letterSpacing: '0.15em', color: c.accent, marginBottom: 12, textTransform: 'uppercase' }}>
              OpenClaw Multi-Agent Architecture
            </div>
            <h1 style={{ fontSize: 32, fontWeight: 900, color: c.text, margin: '0 0 12px', lineHeight: 1.2 }}>
              基于 <span style={{ color: c.accent }}>OpenClaw</span> 多智能体架构<br />构建模型知识飞轮
            </h1>
            <p style={{ fontSize: 14, color: c.muted, margin: 0 }}>
              全自动 SOTA 模型发现 · 实时质检 · 持续进化
            </p>
          </div>

          {/* Section 1: Org Chart */}
          <section style={{ marginBottom: 32 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 16 }}>
              <h2 style={{ fontSize: 18, fontWeight: 900, color: c.text, margin: 0 }}>OpenClaw 模型知识飞轮多智能体团队</h2>
            </div>
            <div style={{ background: c.surface, border: `1px solid ${c.border}`, borderRadius: 16, padding: 20 }}>
              <OrgChart expanded={orgExpanded} onToggle={() => setOrgExpanded(e => !e)} />
            </div>
          </section>

          {/* Section 2: DAG */}
          <section style={{ marginBottom: 32 }}>
            <h2 style={{ fontSize: 18, fontWeight: 900, color: c.text, margin: '0 0 16px' }}>🔄 模型知识飞轮工作流 · Workflow Engine</h2>
            <div style={{ background: c.surface, border: `1px solid ${c.border}`, borderRadius: 16, padding: 20, overflowX: 'auto' }}>
              <DAGView nodes={dagNodes} />
            </div>
          </section>

          {/* Section 3: Cron + Trigger */}
          <section style={{ marginBottom: 32 }}>
            <h2 style={{ fontSize: 18, fontWeight: 900, color: c.text, margin: '0 0 16px' }}>⏰ 定时调度 · Cron Schedule</h2>
            <div style={{ background: c.surface, border: `1px solid ${c.border}`, borderRadius: 16, padding: 20 }}>
              <CronCards version={version} />
            </div>

          </section>

          {/* Section 4: Truth Filter */}
          <section style={{ marginBottom: 32 }}>
            <h2 style={{ fontSize: 18, fontWeight: 900, color: c.text, margin: '0 0 16px' }}>🔍 今日打假 · Truth Filter</h2>
            <div style={{ display: 'flex', gap: 16, overflowX: 'auto', paddingBottom: 8 }}>
              {truthCases.map((item, i) => <TruthCard key={item.id} item={item} index={i} />)}
            </div>
          </section>

          {/* Section 5: Closed Loop */}
          <section style={{ marginBottom: 32 }}>
            <h2 style={{ fontSize: 18, fontWeight: 900, color: c.text, margin: '0 0 16px' }}>🔄 模型知识飞轮 · 闭环机制</h2>
            <div style={{ background: c.surface, border: `1px solid ${c.border}`, borderRadius: 16, padding: 20 }}>
              <ClosedLoopFlow />
              <div style={{ marginTop: 16 }}>
                <div style={{ fontSize: 12, fontWeight: 700, color: c.text, marginBottom: 12 }}>迭代历史</div>
                {[
                  { round: 'Round 1', trigger: 'Benchmark数据字段系统性缺失', found: '发现sync_docs.py条件逻辑错误', action: '修复3处脚本bug，更新SKILL.md自审清单' },
                  { round: 'Round 2', trigger: 'P0拦截率仅4%', found: '质检规则缺少许可证必填检查', action: '新增许可证字段核查规则' },
                ].map((r, i) => (
                  <div key={i} style={{
                    padding: '10px 14px', borderRadius: 10, marginBottom: 8,
                    background: c.card, border: `1px solid ${c.border}`,
                  }}>
                    <div style={{ display: 'flex', gap: 8, alignItems: 'center', marginBottom: 4 }}>
                      <span style={{ fontSize: 10, fontWeight: 700, padding: '2px 7px', borderRadius: 100, background: c.accent + '20', color: c.accent }}>{r.round}</span>
                      <span style={{ fontSize: 10, color: c.muted }}>触发：{r.trigger}</span>
                    </div>
                    <div style={{ fontSize: 10, color: c.text, marginBottom: 2 }}>→ 发现：{r.found}</div>
                    <div style={{ fontSize: 10, color: c.green }}>✓ 行动：{r.action}</div>
                  </div>
                ))}
              </div>
            </div>
          </section>

          {/* Section 6: Work Log + Goals */}
          <section style={{ marginBottom: 32 }}>
            <h2 style={{ fontSize: 18, fontWeight: 900, color: c.text, margin: '0 0 16px' }}>📊 监控目标 · Goals</h2>
            <GoalsPanel version={version} />
          </section>

          {/* Footer */}
          <footer style={{ textAlign: 'center', padding: '24px 0', borderTop: `1px solid ${c.border}`, marginTop: 32 }}>
            <div style={{ fontSize: 11, color: c.muted }}>
              © 2026 SOTA Radar · 小龙虾 OpenClaw 多智能体团队 · <span style={{ color: c.accent }}>{version.toUpperCase()}</span>
            </div>
          </footer>
        </div>
      )}
    </div>
  )
}
