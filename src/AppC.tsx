/**
 * Version C v4 — 前沿科技 · 多智能体架构 + 完整证据链
 * Main dashboard: Hero + Org chart + DAG workflow + Truth Filter + Closed Loop
 */
import { useState, useEffect, useRef } from 'react'
import ModelLibrary from './ModelLibrary'
import SkillsViewer from './SkillsViewer'
import { truthCases } from './dataA'
import {
  orgChart,
  dagNodes,
  buildDagSnapshot,
  todayLog,
  type DagNode,
  type NodeStatus,
} from './dataC'
import {
  triggerFlywheel,
  fetchStatus,
  fetchRunStatus,
  fetchEvolutionHistory,
  fetchRunLogs,
  type StatusInfo,
  type FlywheelRun,
} from './api'

// 本地生成 run_id（不依赖后端）
function genRunId(): string {
  const ts = new Date().toISOString().replace(/[-:T]/g, '').slice(0, 14)
  const rand = Math.random().toString(36).slice(2, 9)
  return `fw_${ts}_${rand}`
}

// ─── Design tokens ────────────────────────────────────────────────────────────
const c = {
  bg: '#030712',
  surface: '#0f172a',
  card: '#111827',
  border: '#1e293b',
  text: '#f1f5f9',
  muted: '#64748b',
  accent: '#38bdf8',
  accent2: '#818cf8',
  green: '#34d399',
  red: '#f87171',
  amber: '#fbbf24',
  pink: '#f472b6',
  purple: '#a78bfa',
}

// ─── Status badge ─────────────────────────────────────────────────────────────
function StatusBadge({ status }: { status: NodeStatus }) {
  const cfg: Record<NodeStatus, { color: string; bg: string; label: string }> = {
    idle:    { color: c.muted,  bg: '#1e293b',  label: '待机' },
    pending: { color: c.muted,  bg: '#1e293b',  label: '等待' },
    running: { color: c.accent, bg: '#0c2645', label: '进行中' },
    done:    { color: c.green,  bg: '#052e16', label: '完成' },
    rejected:{ color: c.red,    bg: '#2d0a0a', label: '拒绝' },
  }
  const x = cfg[status]
  return (
    <span style={{
      fontSize: 9, fontWeight: 700, padding: '2px 7px', borderRadius: 100,
      background: x.bg, color: x.color, border: `1px solid ${x.color}40`,
    }}>
      {status === 'running' ? `⚡ ${x.label}` : x.label}
    </span>
  )
}

// ─── DAG Visualizer ───────────────────────────────────────────────────────────
function DAGView({ nodes }: { nodes: DagNode[] }) {
  const nodeW = 78
  const nodeH = 48

  // Manual layout: {nodeId: {x, y}}
  const layout: Record<string, { x: number; y: number }> = {
    trigger: { x: 30,  y: 90  },
    '分配':  { x: 130, y: 30  },
    scout:   { x: 230, y: 30  },
    qc:      { x: 330, y: 30  },
    '反馈':  { x: 430, y: 130 },
    '归档':  { x: 430, y: 30  },
    '自审':  { x: 530, y: 30  },
    '完成':  { x: 620, y: 30  },
  }

  const cx = (id: string) => layout[id].x + nodeW / 2
  const cy = (id: string) => layout[id].y + nodeH / 2

  const edges = [
    { from: 'trigger', to: '分配',  label: '开始',  color: c.border, dashed: false },
    { from: '分配',     to: 'scout', label: '分发',  color: c.border, dashed: false },
    { from: 'scout',   to: 'qc',    label: '提交',  color: c.border, dashed: false },
    { from: 'qc',      to: '归档',  label: '通过',  color: c.border, dashed: false },
    { from: 'qc',      to: '反馈',  label: '拒绝',  color: c.red,    dashed: true  },
    { from: '反馈',    to: 'scout', label: '打回',  color: c.red,    dashed: true  },
    { from: '归档',    to: '自审',  label: '同步',  color: c.border, dashed: false },
    { from: '自审',    to: '完成',  label: '进化',  color: c.border, dashed: false },
    { from: '完成',    to: 'trigger', label: '等待下次', color: c.muted, dashed: true },
  ]

  return (
    <svg width={680} height={220} style={{ overflow: 'visible' }}>
      <defs>
        <marker id="arr-norm" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
          <polygon points="0 0,8 3,0 6" fill={c.border} />
        </marker>
        <marker id="arr-red" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
          <polygon points="0 0,8 3,0 6" fill={c.red} />
        </marker>
        <marker id="arr-gray" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
          <polygon points="0 0,8 3,0 6" fill={c.muted} />
        </marker>
        <filter id="glow">
          <feGaussianBlur stdDeviation="3" result="b" />
          <feMerge>
            <feMergeNode in="b" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>

      {edges.map((e, i) => {
        let d: string
        if (e.from === '反馈' && e.to === 'scout') {
          // Curve from feedback back up to scout
          d = `M${cx(e.from)},${cy(e.from)} C${cx(e.from)},${cy(e.from) - 80} ${cx(e.to)},${cy(e.to) - 80} ${cx(e.to) + nodeW / 2},${cy(e.to) + nodeH / 2}`
        } else if (e.from === '完成' && e.to === 'trigger') {
          // Curve from 完成 back to trigger
          const tp = layout['trigger']
          d = `M${cx(e.from)},${cy(e.from)} C${cx(e.from)},${cy(e.from) + 80} ${tp.x + nodeW / 2},${tp.y + nodeH + 80} ${tp.x + nodeW / 2},${tp.y + nodeH}`
        } else {
          d = `M${cx(e.from)},${cy(e.from) - nodeH / 2} L${cx(e.to)},${cy(e.to) + nodeH / 2}`
        }
        const mk = e.color === c.red ? 'url(#arr-red)' : e.color === c.muted ? 'url(#arr-gray)' : 'url(#arr-norm)'
        const midX = (cx(e.from) + cx(e.to)) / 2
        const midY = (cy(e.from) + cy(e.to)) / 2
        return (
          <g key={i}>
            <path d={d} stroke={e.color} strokeWidth={1.5} fill="none"
              strokeDasharray={e.dashed ? '4 3' : undefined}
              markerEnd={mk} />
            {e.label && (
              <text x={midX} y={midY - 4} textAnchor="middle" fill={e.color}
                fontSize="9" fontWeight={600}>
                {e.label}
              </text>
            )}
          </g>
        )
      })}

      {nodes.map(n => {
        const pos = layout[n.id]
        if (!pos) return null
        const isR = n.status === 'running'
        const isD = n.status === 'done'
        const isJ = n.status === 'rejected'
        const bc  = isR ? c.accent : isD ? c.green : isJ ? c.red : c.border

        return (
          <g key={n.id} filter={isR ? 'url(#glow)' : undefined}>
            {isR && (
              <rect x={pos.x - 2} y={pos.y - 2} width={nodeW + 4} height={nodeH + 4}
                rx={10} fill="none" stroke={c.accent} strokeWidth={1.5}
                strokeDasharray="4 2" />
            )}
            <rect x={pos.x} y={pos.y} width={nodeW} height={nodeH} rx={8}
              fill={c.card} stroke={bc} strokeWidth={isR ? 2 : 1} />
            {isR && (
              <rect x={pos.x} y={pos.y} width={nodeW} height={3} rx={2}
                fill={c.accent} />
            )}
            <text x={pos.x + nodeW / 2} y={pos.y + 18} textAnchor="middle"
              fill={c.text} fontSize={10} fontWeight={700}>
              {n.label}
            </text>
            <text x={pos.x + nodeW / 2} y={pos.y + 30} textAnchor="middle"
              fill={c.muted} fontSize={8}>
              {n.sub}
            </text>
            <text x={pos.x + nodeW / 2} y={pos.y + 43} textAnchor="middle">
              <StatusBadge status={n.status} />
            </text>
          </g>
        )
      })}
    </svg>
  )
}

// ─── Org Chart ────────────────────────────────────────────────────────────────
function OrgChart({ expanded, onToggle }: { expanded: boolean; onToggle: () => void }) {
  const { pm, teams } = orgChart
  return (
    <div style={{ marginBottom: 8 }}>
      {/* PM + Coordinator node */}
      <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 6 }}>
        <div style={{
          width: 36, height: 36, borderRadius: 10,
          background: c.accent + '25', border: `1.5px solid ${c.accent}60`,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          fontSize: 18,
        }}>
          {pm.icon}
        </div>
        <div>
          <div style={{ fontSize: 13, fontWeight: 800, color: c.text }}>
            {pm.name}{' '}
            <span style={{ fontSize: 10, color: c.accent, fontWeight: 600 }}>{pm.role}</span>
          </div>
          <div style={{ fontSize: 10, color: c.muted }}>{pm.desc}</div>
        </div>
        <button
          onClick={onToggle}
          style={{
            marginLeft: 'auto', background: c.surface, border: `1px solid ${c.border}`,
            borderRadius: 8, padding: '4px 10px', color: c.accent, fontSize: 11,
            cursor: 'pointer',
          }}
        >
          {expanded ? '收起 ▲' : '展开 ▼'}
        </button>
      </div>

      {/* Three team columns */}
      {expanded && (
        <div style={{ paddingLeft: 12, borderLeft: `2px solid ${c.accent}30` }}>
          {teams.map(t => (
            <div key={t.team} style={{
              background: c.surface, border: `1px solid ${c.border}`,
              borderRadius: 10, padding: '10px 12px', marginBottom: 8,
            }}>
              <div style={{ fontSize: 11, fontWeight: 800, color: t.color, marginBottom: 6 }}>
                {t.icon} {t.team}
              </div>
              {t.members.map(m => (
                <div key={m.id} style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 3 }}>
                  <div style={{
                    width: 6, height: 6, borderRadius: '50%',
                    background: m.status === 'running' ? c.green : c.muted,
                    boxShadow: m.status === 'running' ? `0 0 6px ${c.green}` : 'none',
                  }} />
                  <div>
                    <span style={{ fontSize: 11, color: c.text, fontWeight: 600 }}>{m.name}</span>
                    <span style={{ fontSize: 9, color: c.muted }}> · {m.role}</span>
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

// ─── Cron schedule cards (live data) ────────────────────────────────────────
function CronCards({ status }: { status: StatusInfo | null }) {
  const isRunning = status?.state === 'RUNNING' && status?.current_run?.status === 'RUNNING'
  const runCount = status?.today_runs ?? 0
  const updated = status?.current_run?.started_at
    ? new Date(status.current_run.started_at).toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' })
    : '--:--'

  const cards = [
    {
      icon: '🕐', label: '早7点', time: '07:00 UTC+8',
      action: '全量调研扫描 + 质检 + 归档',
      nextRun: isRunning ? '⏳ 运行中...' : '明天 07:00',
      live: { runs: runCount, label: '今日触发', color: isRunning ? c.accent : c.muted },
    },
    {
      icon: '🕐', label: '下午1点半', time: '13:30 UTC+8',
      action: '增量扫描 + 质检反馈循环',
      nextRun: isRunning ? '⏳ 运行中...' : '今天 13:30',
      live: { runs: status?.today_models_updated ?? 0, label: '模型更新', color: c.green },
    },
  ]

  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>
      {cards.map(cron => (
        <div key={cron.label} style={{
          background: c.surface, border: `1px solid ${c.border}`,
          borderRadius: 10, padding: '10px 12px',
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 4 }}>
            <span style={{ fontSize: 12 }}>{cron.icon}</span>
            <span style={{ fontSize: 12, fontWeight: 800, color: c.text }}>{cron.label}</span>
            <span style={{ marginLeft: 'auto', fontSize: 10, color: c.muted }}>{cron.time}</span>
          </div>
          <div style={{ fontSize: 10, color: c.muted, lineHeight: 1.5 }}>{cron.action}</div>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: 6 }}>
            <div style={{ fontSize: 9, color: cron.live.color }}>{cron.live.label}: {cron.live.runs}</div>
            <div style={{ fontSize: 9, color: c.accent }}>上次: {updated}</div>
          </div>
          <div style={{ fontSize: 9, color: c.accent, marginTop: 2 }}>下次: {cron.nextRun}</div>
        </div>
      ))}
    </div>
  )
}

// ─── Workflow panel (DAG + trigger button) ──────────────────────────────────
function WorkflowPanel({ progress, onTrigger, toast }: {
  progress: number
  onTrigger: () => void
  toast: { msg: string; type: 'success' | 'error' } | null
}) {
  const [nodes, setNodes] = useState<DagNode[]>(dagNodes)

  useEffect(() => {
    setNodes(buildDagSnapshot(progress))
  }, [progress])

  const isRunning = progress > 0 && progress < 100

  return (
    <div style={{
      background: c.surface, border: `1px solid ${c.border}`,
      borderRadius: 14, padding: 16,
    }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 14 }}>
        <div>
          <div style={{ fontSize: 13, fontWeight: 800, color: c.text }}>
            模型知识飞轮工作流 · Workflow Engine
          </div>
          <div style={{ fontSize: 11, color: c.muted }}>支持循环的 DAG（有向有环图）</div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          {/* Progress bar */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <div style={{ width: 80, height: 4, background: c.border, borderRadius: 2, overflow: 'hidden' }}>
              <div style={{
                width: `${progress}%`, height: '100%',
                background: progress < 100 ? c.accent : c.green,
                transition: 'width 0.5s',
              }} />
            </div>
            <span style={{ fontSize: 10, color: c.muted, minWidth: 28 }}>{progress}%</span>
          </div>
          {/* Trigger button */}
          <button
            onClick={onTrigger}
            disabled={isRunning}
            style={{
              padding: '6px 14px', borderRadius: 8, border: 'none',
              background: isRunning
                ? c.surface
                : `linear-gradient(135deg,${c.accent},${c.accent2})`,
              color: isRunning ? c.muted : '#fff',
              fontSize: 11, fontWeight: 700,
              cursor: isRunning ? 'not-allowed' : 'pointer',
              display: 'flex', alignItems: 'center', gap: 5,
            }}
          >
            <span>🚀</span>
            {progress === 0
              ? '立即触发'
              : progress >= 100
                ? '再次触发'
                : '运行中...'}
          </button>
        </div>
      </div>

      <div style={{ overflowX: 'auto' }}><DAGView nodes={nodes} /></div>

      <div style={{ display: 'flex', gap: 12, marginTop: 8, flexWrap: 'wrap' }}>
        {[
          { color: c.muted, l: '待机' },
          { color: c.accent, l: '进行中' },
          { color: c.green, l: '完成' },
          { color: c.red, l: '拒绝/打回' },
        ].map(x => (
          <div key={x.l} style={{ display: 'flex', alignItems: 'center', gap: 5 }}>
            <div style={{ width: 8, height: 8, borderRadius: 2, background: x.color }} />
            <span style={{ fontSize: 10, color: c.muted }}>{x.l}</span>
          </div>
        ))}
        <div style={{ display: 'flex', alignItems: 'center', gap: 5, marginLeft: 'auto' }}>
          <div style={{ width: 20, height: 1, borderTop: `1.5px dashed ${c.red}` }} />
          <span style={{ fontSize: 10, color: c.muted }}>质检打回归</span>
        </div>
      </div>
    </div>
  )
}

// ─── Verdict badge ────────────────────────────────────────────────────────────
function VerdictBadge({ v }: { v: string }) {
  const mc: Record<string, string> = {
    '夸大其词': c.red,
    '待核实':   c.amber,
    '证据不足': '#fb923c',
  }
  const color = mc[v] || c.muted
  const suffix: Record<string, string> = {
    '夸大其词': '— 证据不实',
    '待核实':   '— 信息矛盾',
    '证据不足': '— 缺少关键数据',
  }
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 5 }}>
      <span style={{
        fontSize: 9, fontWeight: 700, padding: '2px 8px', borderRadius: 100,
        background: color + '20', color: color, border: `1px solid ${color}40`,
      }}>
        {v}
      </span>
      <span style={{ fontSize: 9, color }}>{suffix[v] || ''}</span>
    </div>
  )
}

// ─── Truth card ───────────────────────────────────────────────────────────────
function TruthCard({ item, idx }: { item: typeof truthCases[0]; idx: number }) {
  const letters = ['A', 'B', 'C']
  const vc: Record<string, string> = {
    '夸大其词': c.red,
    '待核实':   c.amber,
    '证据不足': '#fb923c',
  }
  const verdictColor = vc[item.verdict] || c.muted

  return (
    <div style={{
      background: c.surface, border: `1px solid ${c.border}`,
      borderRadius: 14, overflow: 'hidden',
      minWidth: 340, maxWidth: 360, flexShrink: 0,
    }}>
      {/* Top accent line */}
      <div style={{
        height: 3,
        background: `linear-gradient(90deg, ${verdictColor}60, transparent)`,
      }} />

      <div style={{ padding: '14px 16px' }}>
        {/* Header: model + source link */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 10 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <div style={{
              width: 24, height: 24, borderRadius: 6,
              background: verdictColor + '20', border: `1px solid ${verdictColor}40`,
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              color: verdictColor, fontSize: 10, fontWeight: 900,
            }}>
              {letters[idx]}
            </div>
            <span style={{ fontSize: 11, color: c.muted }}>{item.time}</span>
          </div>
          <VerdictBadge v={item.verdict} />
        </div>

        {/* Model name + source */}
        <div style={{ marginBottom: 10 }}>
          <div style={{ fontSize: 15, fontWeight: 800, color: c.text, marginBottom: 4 }}>
            {item.model}
          </div>
          {item.sourceUrl ? (
            <a href={item.sourceUrl} target="_blank" rel="noopener noreferrer"
              style={{ fontSize: 11, color: c.accent, textDecoration: 'none', display: 'inline-flex', alignItems: 'center', gap: 4 }}>
              {item.source} ↗
            </a>
          ) : (
            <span style={{ fontSize: 11, color: c.muted }}>{item.source}</span>
          )}
        </div>

        {/* Our verdict conclusion */}
        <div style={{ marginBottom: 10 }}>
          <div style={{ fontSize: 10, fontWeight: 700, color: c.accent, marginBottom: 4 }}>
            我们核查结论
          </div>
          <p style={{ fontSize: 12, color: c.text, margin: 0, lineHeight: 1.6 }}>
            {item.ourVerdict}
          </p>
        </div>

        {/* Evidence chain table */}
        <div style={{ background: '#030712', borderRadius: 8, overflow: 'hidden', marginBottom: 10 }}>
          <div style={{ padding: '8px 12px 6px', borderBottom: `1px solid ${c.border}` }}>
            <span style={{ fontSize: 10, fontWeight: 700, color: c.text }}>证据链</span>
          </div>
          {item.evidence.map((ev, i) => {
            const isBad = ev.val.includes('无') || ev.val === '暂无'
              || ev.val === 'unknown' || ev.val === '拒绝入库'
            return (
              <div key={i} style={{
                padding: '7px 12px',
                borderBottom: i < item.evidence.length - 1 ? `1px solid ${c.border}` : 'none',
              }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: 8 }}>
                  <span style={{ fontSize: 11, color: c.muted, flex: 1 }}>{ev.label}</span>
                  <span style={{ fontSize: 11, fontWeight: 700, color: isBad ? c.red : c.text, flexShrink: 0 }}>
                    {ev.val}
                  </span>
                </div>
                {ev.sourceUrl ? (
                  <a href={ev.sourceUrl} target="_blank" rel="noopener noreferrer"
                    style={{ fontSize: 10, color: c.accent, textDecoration: 'none', opacity: 0.8, display: 'inline-flex', alignItems: 'center', gap: 3, marginTop: 2 }}>
                    来源: {ev.source} ↗
                  </a>
                ) : (
                  <span style={{ fontSize: 10, color: c.muted, opacity: 0.6, marginTop: 2, display: 'block' }}>
                    来源: {ev.source}
                  </span>
                )}
              </div>
            )
          })}
        </div>

        {/* Lesson */}
        <p style={{
          fontSize: 10, color: c.muted, margin: 0, fontStyle: 'italic',
          lineHeight: 1.5, borderTop: `1px solid ${c.border}`, paddingTop: 8,
        }}>
          → {item.lesson}
        </p>

        {/* Original quote */}
        <div style={{
          background: '#060d1a', border: `1px solid ${verdictColor}30`,
          borderRadius: 8, padding: '10px 12px', marginTop: 10,
        }}>
          <div style={{ fontSize: 9, fontWeight: 700, color: verdictColor, marginBottom: 5, letterSpacing: '0.05em' }}>
            原始引述
          </div>
          <p style={{ fontSize: 11, color: c.text, margin: 0, lineHeight: 1.6, fontStyle: 'italic' }}>
            "{item.exactQuote}"
          </p>
        </div>
      </div>
    </div>
  )
}

// ─── Work log ─────────────────────────────────────────────────────────────────
function WorkLog() {
  return (
    <div style={{ background: c.surface, border: `1px solid ${c.border}`, borderRadius: 14, overflow: 'hidden' }}>
      <div style={{
        padding: '12px 16px', borderBottom: `1px solid ${c.border}`,
        display: 'flex', alignItems: 'center', gap: 8,
      }}>
        <span style={{ fontSize: 11, fontWeight: 700, color: c.text }}>Work Log · 今日</span>
        <span style={{ marginLeft: 'auto', fontSize: 10, color: c.muted }}>
          {new Date().toISOString().slice(0, 10)}
        </span>
      </div>
      {todayLog.map((log, i) => (
        <div key={i} style={{
          display: 'flex', alignItems: 'center', gap: 10, padding: '9px 14px',
          borderBottom: i < todayLog.length - 1 ? `1px solid ${c.border}` : 'none',
        }}>
          <span style={{ fontSize: 10, color: c.muted, width: 36, flexShrink: 0 }}>{log.time}</span>
          <span style={{ fontSize: 11, color: c.text, flex: 1, lineHeight: 1.4 }}>{log.action}</span>
          <span style={{
            fontSize: 10, fontWeight: 700,
            color: log.status === 'done' ? c.green : c.amber, flexShrink: 0,
          }}>
            {log.status === 'done' ? '✓' : '◷'}
          </span>
        </div>
      ))}
    </div>
  )
}

// ─── Closed loop flow (5 steps) ──────────────────────────────────────────────
function ClosedLoopFlow() {
  const steps = [
    { id: 'commit',  label: '① Commit History',    sub: '每次执行记录',        icon: '📝', color: c.accent  },
    { id: 'review',  label: '② Skill Self-Review', sub: '对照 SKILL.md',       icon: '🔍', color: c.amber  },
    { id: 'pattern', label: '③ Pattern Analysis',  sub: '找重复失误',          icon: '🔎', color: c.purple },
    { id: 'update', label: '④ Update Skills',     sub: '更新规则',            icon: '✏️', color: c.green  },
    { id: 'next',   label: '⑤ Next Run',          sub: '用更强规则跑',        icon: '🚀', color: c.accent  },
  ]
  return (
    <div style={{
      background: '#060d1a', border: `1px solid ${c.border}`,
      borderRadius: 12, padding: '16px 20px', marginBottom: 14,
    }}>
      <div style={{
        fontSize: 11, fontWeight: 700, color: c.accent,
        marginBottom: 12, letterSpacing: '0.05em',
      }}>
        AUTO RESEARCH · SKILL 闭环流程
      </div>
      <div style={{ display: 'flex', alignItems: 'center' }}>
        {steps.map((s, i) => (
          <div key={s.id} style={{ display: 'flex', alignItems: 'center', flex: 1 }}>
            <div style={{ textAlign: 'center', flex: 1 }}>
              <div style={{
                width: 40, height: 40, borderRadius: 10, margin: '0 auto 6px',
                background: s.color + '20', border: `1.5px solid ${s.color}50`,
                display: 'flex', alignItems: 'center', justifyContent: 'center',
                fontSize: 18,
              }}>
                {s.icon}
              </div>
              <div style={{ fontSize: 10, fontWeight: 700, color: c.text, marginBottom: 2 }}>{s.label}</div>
              <div style={{ fontSize: 9, color: c.muted }}>{s.sub}</div>
            </div>
            {i < steps.length - 1 && (
              <div style={{ display: 'flex', alignItems: 'center', paddingBottom: 20 }}>
                <div style={{ width: 20, height: 1, background: c.border }} />
                <div style={{
                  width: 0, height: 0,
                  borderTop: '4px solid transparent',
                  borderBottom: '4px solid transparent',
                  borderLeft: `6px solid ${c.border}`,
                }} />
              </div>
            )}
          </div>
        ))}
      </div>
      <div style={{
        marginTop: 12, padding: '8px 12px', background: c.surface,
        borderRadius: 8, fontSize: 11, color: c.muted, lineHeight: 1.6,
      }}>
        <span style={{ color: c.accent, fontWeight: 700 }}>反馈信号：</span>
        拦截率变化 + Benchmark合规率变化 + 重复失误次数。当 ≥2 次出现同类失误，触发 Skill 更新。
      </div>
    </div>
  )
}

// ─── Iteration history ────────────────────────────────────────────────────────
function IterationHistory({ latestRun }: { latestRun: number }) {
  const [flash, setFlash] = useState(false)

  useEffect(() => {
    if (latestRun > 0) {
      setFlash(true)
      const t = setTimeout(() => setFlash(false), 2000)
      return () => clearTimeout(t)
    }
  }, [latestRun])

  const rounds = [
    {
      round: '第1轮 · 初版自审', date: '2026-04-05', isLatest: true,
      trigger: 'SKILL.md v1 部署后，触发首次自动化自审，对照 GitHub commit 历史逐条核对',
      findings: [
        'Benchmark 数据字段系统性缺失（16处）',
        'P0 许可证门禁漏拦（2处，Mistral Small 4 / Step-3.5-Flash）',
        '信息源优先级未标注（8处）',
      ],
      updates: [
        'Benchmark 数据字段改为必填，空值拒绝入库',
        'P0-3 门禁新增许可证二次确认步骤',
        '所有信息源强制标注优先级',
      ],
      metrics: { p0Rate: '4%（2/50）', bm: '68%', skillUpdates: '3项', score: '52/100' },
    },
    {
      round: '第2轮（积累中）', date: '下次触发后', isLatest: false,
      trigger: '积累 ≥50 条入库记录后自动触发，或 P0 拦截率 >5% 时立即触发',
      findings: ['待积累更多数据——当前入库记录不足50条'],
      updates: ['待触发后确定'],
      metrics: null,
    },
  ]

  return (
    <div style={{
      background: c.surface, border: `1px solid ${c.border}`,
      borderRadius: 12, overflow: 'hidden', marginBottom: 14,
    }}>
      <div style={{
        padding: '12px 16px', borderBottom: `1px solid ${c.border}`,
        display: 'flex', alignItems: 'center', gap: 8,
      }}>
        <span style={{ fontSize: 11, fontWeight: 700, color: c.text }}>迭代历史 · Iteration History</span>
        <span style={{ marginLeft: 'auto', fontSize: 10, color: c.muted }}>共1轮</span>
      </div>

      {rounds.map((r, i) => (
        <div key={r.round} style={{
          padding: '14px 16px',
          borderBottom: i < rounds.length - 1 ? `1px solid ${c.border}` : 'none',
          background: r.isLatest && flash ? `${c.accent}10` : 'transparent',
          transition: 'background 0.5s',
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 8 }}>
            <span style={{
              fontSize: 10, fontWeight: 800, padding: '2px 8px', borderRadius: 100,
              background: r.isLatest ? `${c.green}20` : c.surface,
              color: r.isLatest ? c.green : c.muted,
              border: `1px solid ${r.isLatest ? `${c.green}40` : c.border}`,
            }}>
              {r.round}
            </span>
            <span style={{ fontSize: 11, color: c.muted }}>{r.date}</span>
            {r.isLatest && (
              <span style={{
                marginLeft: 'auto', fontSize: 9, fontWeight: 700, color: c.accent,
                background: `${c.accent}15`, padding: '2px 8px', borderRadius: 100,
              }}>
                最新
              </span>
            )}
          </div>

          <div style={{ fontSize: 11, color: c.text, marginBottom: 6, fontStyle: 'italic' }}>
            触发：{r.trigger}
          </div>

          <div style={{ marginBottom: 8 }}>
            <div style={{ fontSize: 10, color: c.red, fontWeight: 700, marginBottom: 4 }}>发现（Findings）</div>
            {r.findings.map((f, fi) => (
              <div key={fi} style={{ fontSize: 11, color: c.muted, paddingLeft: 10, marginBottom: 2 }}>
                • {f}
              </div>
            ))}
          </div>

          <div style={{ marginBottom: 8 }}>
            <div style={{ fontSize: 10, color: c.green, fontWeight: 700, marginBottom: 4 }}>更新（Updates）</div>
            {r.updates.map((u, ui) => (
              <div key={ui} style={{ fontSize: 11, color: c.muted, paddingLeft: 10, marginBottom: 2 }}>
                • {u}
              </div>
            ))}
          </div>
          {r.metrics && (
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 6 }}>
              {[
                { label: 'P0拦截率',     val: r.metrics.p0Rate,      color: c.amber  },
                { label: 'Benchmark合规', val: r.metrics.bm,          color: c.accent },
                { label: 'Skill更新',    val: r.metrics.skillUpdates, color: c.green  },
                { label: 'Score',         val: r.metrics.score,        color: c.purple },
              ].map(m => (
                <div key={m.label} style={{
                  background: '#060d1a', borderRadius: 6, padding: '6px 8px', textAlign: 'center',
                }}>
                  <div style={{ fontSize: 9, color: c.muted, marginBottom: 2 }}>{m.label}</div>
                  <div style={{ fontSize: 12, fontWeight: 800, color: m.color }}>{m.val}</div>
                </div>
              ))}
            </div>
          )}
        </div>
      ))}
    </div>
  )
}

// ─── Goals panel ──────────────────────────────────────────────────────────────
function GoalsPanel() {
  const goals = [
    { label: 'P0拦截率',      current: '4%',   target: '< 2%',  desc: 'license错误 + SOTA无证据',       color: c.amber  },
    { label: 'Benchmark合规率', current: '68%', target: '> 90%', desc: '入库模型必须有Benchmark数据',   color: c.accent },
    { label: '自审触发',       current: '每日', target: '≥2次同类失误立即触发', desc: '自审循环加速',       color: c.green  },
    { label: '平均修复周期',   current: '24h',  target: '< 4h',  desc: '从发现到Skill更新生效',         color: c.purple },
  ]
  return (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 10, marginBottom: 14 }}>
      {goals.map(g => (
        <div key={g.label} style={{
          background: c.surface, border: `1px solid ${c.border}`,
          borderRadius: 10, padding: '12px 12px',
        }}>
          <div style={{ fontSize: 10, color: c.muted, marginBottom: 6 }}>{g.label}</div>
          <div style={{ display: 'flex', alignItems: 'baseline', gap: 6, marginBottom: 4 }}>
            <span style={{ fontSize: 20, fontWeight: 900, color: g.color }}>{g.current}</span>
            <span style={{ fontSize: 11, color: c.muted }}>→</span>
            <span style={{ fontSize: 13, fontWeight: 700, color: c.green }}>{g.target}</span>
          </div>
          <div style={{ fontSize: 10, color: c.muted, lineHeight: 1.4 }}>{g.desc}</div>
        </div>
      ))}
    </div>
  )
}

// ─── Main App ─────────────────────────────────────────────────────────────────
export default function AppC({ activePage = 'home' }: { activePage?: string }) {
  const [mounted, setMounted] = useState(false)
  const [orgExpanded, setOrgExpanded] = useState(true)
  const [progress, setProgress] = useState(100)
  const [animating, setAnimating] = useState(false)
  const [triggerCount, setTriggerCount] = useState(0)
  const [activeTab, setActiveTab] = useState<'home' | 'library' | 'skills'>(activePage as 'home' | 'library' | 'skills')
  const [status, setStatus] = useState<StatusInfo | null>(null)
  const [toast, setToast] = useState<{ msg: string; type: 'success' | 'error' } | null>(null)
  const runIdRef = useRef<string | null>(null)  // 当前飞轮 run_id，供轮询使用
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null)

  useEffect(() => { setTimeout(() => setMounted(true), 100) }, [])

  // Fix: 同步父组件版本切换导致的 activePage 变化到内部 activeTab
  useEffect(() => {
    setActiveTab(activePage as 'home' | 'library' | 'skills')
  }, [activePage])

  // Load live status on mount
  useEffect(() => {
    fetchStatus().then(s => { if (s) setStatus(s) }).catch(() => {})
    // Refresh status every 30s
    const interval = setInterval(() => {
      fetchStatus().then(s => { if (s) setStatus(s) }).catch(() => {})
    }, 30000)
    return () => clearInterval(interval)
  }, [])

  function showToast(msg: string, type: 'success' | 'error') {
    setToast({ msg, type })
    setTimeout(() => setToast(null), 4000)
  }

  async function handleTrigger() {
    if (animating) return
    setAnimating(true)
    setProgress(0)
    setTriggerCount(c => c + 1)

    let runId = 'mock_' + Date.now()

    // 先乐观更新 UI（RUNNING 状态）
    setStatus(prev => ({
      ...(prev ?? { state: 'IDLE', current_run: null, today_runs: 0, today_models_updated: 0 }),
      state: 'RUNNING',
      current_run: {
        run_id: runId,
        status: 'RUNNING',
        started_at: new Date().toISOString(),
        finished_at: null,
        progress: 0,
      },
      today_runs: (prev?.today_runs ?? 0) + 1,
    }))
    showToast('🚀 飞轮已触发！（本地模拟模式）', 'success')

    // 启动本地模拟进度动画（同时尝试调后端，不阻塞）
    timerRef.current = setInterval(async () => {
      pollFailCount

      // 尝试调后端（有后端时用真实状态，无后端时用模拟）
      try {
        const run = await fetchRunStatus(runId)
        if (run) {
          setProgress(Math.round(run.progress * 100))
          setStatus(prev => prev ? {
            ...prev,
            state: run.status,
            current_run: prev.current_run ? {
              ...prev.current_run,
              status: run.status,
              progress: run.progress,
              finished_at: run.finished_at,
            } : null,
          } : prev)
          if (run.status === 'COMPLETED' || run.status === 'FAILED') {
            clearInterval(timerRef.current!)
            setAnimating(false)
            setProgress(run.status === 'COMPLETED' ? 100 : 0)
            if (run.status === 'COMPLETED') {
              showToast('✅ 第' + (run.results?.iteration ?? '?') + '轮飞轮运转完成！', 'success')
            } else {
              showToast('❌ 飞轮失败：' + (run.errors?.[0] ?? '未知错误'), 'error')
            }
            return
          }
        }
      } catch { /* 后端不在线，继续模拟 */ }

      // 本地模拟进度（后端不可用时降级为纯前端动画）
      setProgress(prev => {
        const next = Math.min(prev + 3, 97)
        if (next >= 97) {
          clearInterval(timerRef.current!)
          setAnimating(false)
          setProgress(100)
          setStatus(st => st ? {
            ...st,
            state: 'COMPLETED',
            current_run: st.current_run ? {
              ...st.current_run,
              status: 'DONE',
              finished_at: new Date().toISOString(),
              progress: 100,
            } : null,
          } : st)
          showToast('✅ 第' + (triggerCount) + '轮飞轮运转完成！（本地模拟）', 'success')
        }
        return next
      })
    }, 400)
    return

    // 立即将 runId 存入 ref，供轮询使用
    runIdRef.current = runId

    setAnimating(true)
    setProgress(0)
    setTriggerCount(c => c + 1)

    // 立即更新状态为 RUNNING（乐观更新）
    setStatus(prev => ({
      ...(prev ?? { state: 'IDLE', current_run: null, today_runs: 0, today_models_updated: 0 }),
      state: 'RUNNING',
      current_run: {
        run_id: runId,
        status: 'RUNNING',
        started_at: new Date().toISOString(),
        finished_at: null,
        progress: 0,
      },
      today_runs: (prev?.today_runs ?? 0) + 1,
    }))

    // 轮询 run 状态（每 3 秒），实时更新 DAG 和进度条
    let pollFailCount = 0
    timerRef.current = setInterval(async () => {
      try {
        const run = await fetchRunStatus(runId)
        if (!run) return

        // 进度条
        setProgress(Math.round(run.progress * 100))

        // 更新完整状态
        setStatus(prev => prev ? {
          ...prev,
          state: run.status,
          current_run: prev.current_run ? {
            ...prev.current_run,
            status: run.status,
            progress: run.progress,
            finished_at: run.finished_at,
          } : null,
        } : null)

        // 飞轮完成
        if (run.status === 'COMPLETED' || run.status === 'FAILED') {
          clearInterval(timerRef.current!)
          setAnimating(false)
          setProgress(run.status === 'COMPLETED' ? 100 : 0)

          if (run.status === 'COMPLETED') {
            // 更新 Skills 自进化展示
            try {
              const evo = await fetchEvolutionHistory()
              if (evo) {
                const latestEvo = evo.iterations?.[0]
                if (run.results?.evolution_triggered !== false) {
                  showToast(
                    `✅ 第${run.results?.iteration ?? '?'}轮完成！`
                    + (latestEvo ? ` 自进化触发：${latestEvo.trigger_reason}` : ''),
                    'success'
                  )
                }
              }
            } catch { /* ignore */ }
          } else {
            showToast(`❌ 飞轮失败：${run.errors?.[0] ?? '未知错误'}`, 'error')
          }
        }
      } catch {
        // 轮询错误不弹 toast，避免刷屏
        pollFailCount++
        if (pollFailCount >= 10) {
          clearInterval(timerRef.current!)
          setAnimating(false)
          showToast('⚠️ 后端连接超时（5分钟），请检查 FastAPI 是否在 7860 端口运行', 'error')
        }
      }
    }, 3000)
  }

  return (
    <div style={{
      minHeight: '100vh', background: c.bg, color: c.text,
      fontFamily: "'Inter',system-ui,sans-serif", position: 'relative',
    }}>
      {/* Ambient glows */}
      <div style={{ position: 'fixed', inset: 0, pointerEvents: 'none', zIndex: 0, overflow: 'hidden' }}>
        <div style={{
          position: 'absolute', width: 600, height: 600, top: -200, left: -100,
          borderRadius: '50%',
          background: 'radial-gradient(circle,#1d4ed820 0%,transparent 70%)',
        }} />
        <div style={{
          position: 'absolute', width: 500, height: 500, top: 200, right: -150,
          borderRadius: '50%',
          background: 'radial-gradient(circle,#818cf810 0%,transparent 70%)',
        }} />
      </div>

      {/* Toast notification */}
      {toast && (
        <div style={{
          position: 'fixed', top: 80, right: 24, zIndex: 9999,
          padding: '10px 18px', borderRadius: 10,
          background: toast.type === 'success' ? '#052e16' : '#2d0a0a',
          color: toast.type === 'success' ? '#34d399' : '#f87171',
          border: `1px solid ${toast.type === 'success' ? '#34d399' : '#f87171'}40`,
          fontSize: 13, fontWeight: 600, boxShadow: '0 8px 32px rgba(0,0,0,0.5)',
          minWidth: 200,
        }}>
          {toast.msg}
        </div>
      )}

      {/* ── Navigation ── */}
      <div style={{
        borderBottom: `1px solid ${c.border}`, padding: '0 48px', height: 60,
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        background: c.bg + 'dd', backdropFilter: 'blur(20px)',
        position: 'fixed', top: 0, left: 0, right: 0, zIndex: 20,
      }}>
        {/* Logo */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <div style={{
            width: 34, height: 34, borderRadius: 10,
            background: `linear-gradient(135deg,${c.accent},${c.accent2})`,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            color: '#fff', fontSize: 16, fontWeight: 900,
            boxShadow: `0 0 20px ${c.accent}50`,
          }}>
            S
          </div>
          <span style={{ fontSize: 17, fontWeight: 900, letterSpacing: '-0.02em' }}>
            <span style={{
              background: `linear-gradient(135deg,${c.accent},${c.accent2})`,
              WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent',
              backgroundClip: 'text',
            }}>
              SOTARadar
            </span>
            <span style={{ fontSize: 11, color: c.accent, fontWeight: 700, borderLeft: `1px solid ${c.border}`, paddingLeft: 10, marginLeft: 10 }}>
              SOTA Radar · 模型知识飞轮
            </span>
          </span>
        </div>

        {/* Tabs */}
        <div style={{ display: 'flex', gap: 4 }}>
          {([
            { id: 'home' as const,    label: '🏠 首页' },
            { id: 'library' as const, label: '📚 模型知识库' },
            { id: 'skills' as const,  label: '📄 Skills文档库' },
          ]).map(tab => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              style={{
                padding: '5px 14px', borderRadius: 8, border: 'none',
                fontSize: 12, fontWeight: 600, cursor: 'pointer',
                background: activeTab === tab.id ? c.accent + '22' : 'transparent',
                color: activeTab === tab.id ? c.accent : c.muted,
                borderBottom: activeTab === tab.id ? `2px solid ${c.accent}` : '2px solid transparent',
                transition: 'all 0.15s',
              }}
            >
              {tab.label}
            </button>
          ))}
        </div>

        {/* Right side */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 20, fontSize: 12 }}>
          <span style={{ color: c.muted }}>多智能体协作 · 每日运转</span>
          <span style={{ display: 'flex', alignItems: 'center', gap: 6, color: c.green }}>
            <div style={{
              width: 7, height: 7, borderRadius: '50%',
              background: c.green, boxShadow: `0 0 8px ${c.green}`,
            }} />
            LIVE
          </span>
          <span style={{ color: c.accent, fontWeight: 700, fontSize: 11 }}>
            ⚡ Powered by OpenClaw
          </span>
        </div>
      </div>

      {/* ── Non-home pages ── */}
      {activeTab !== 'home' && (
        <>
          {activeTab === 'library' && <ModelLibrary onNavigate={setActiveTab} />}
          {activeTab === 'skills' && <SkillsViewer onNavigate={setActiveTab} />}
        </>
      )}

      {/* ── Home page ── */}
      {activeTab === 'home' && (
        <div style={{ maxWidth: 1200, margin: '0 auto', padding: '100px 48px 48px', position: 'relative', zIndex: 1 }}>

          {/* ── Hero ── */}
          <div style={{
            textAlign: 'center', marginBottom: 48,
            opacity: mounted ? 1 : 0,
            transform: mounted ? 'translateY(0)' : 'translateY(16px)',
            transition: 'all 0.5s ease',
          }}>
            <h1 style={{ fontSize: 42, fontWeight: 900, lineHeight: 1.1, marginBottom: 16, letterSpacing: '-0.02em' }}>
              <span style={{
                background: `linear-gradient(135deg,${c.accent},${c.accent2})`,
                WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent',
                backgroundClip: 'text',
              }}>
                基于 OpenClaw 多智能体架构
              </span>
              <br />
              <span style={{ color: c.text }}>构建模型知识飞轮</span>
            </h1>
            <p style={{ fontSize: 15, color: c.muted, maxWidth: 560, margin: '0 auto', lineHeight: 1.7 }}>
              调研 → 质检 → 归档 → 自审 → 进化，Skills 自我闭环迭代机制。
              <strong style={{ color: c.accent }}> 每一条拦截都有原因，每一个原因都有证据。</strong>
            </p>
            <div style={{ display: 'flex', justifyContent: 'center', gap: 24, marginTop: 20 }}>
              {[
                { icon: '🔍', val: '5',  unit: '类模型并行扫描' },
                { icon: '🔎', val: '3',  unit: '维度质检门禁' },
                { icon: '📦', val: '2',  unit: '文档自动同步' },
                { icon: '🔄', val: '1',  unit: '日均自审闭环' },
              ].map(s => (
                <div key={s.unit} style={{ textAlign: 'center' }}>
                  <div style={{ fontSize: 28, fontWeight: 900, color: c.accent }}>{s.icon} {s.val}</div>
                  <div style={{ fontSize: 10, color: c.muted }}>{s.unit}</div>
                </div>
              ))}
            </div>
          </div>

          {/* ── Section 1: Org chart + Workflow ── */}
          <div style={{ marginBottom: 40 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 14 }}>
              <div style={{ width: 4, height: 24, borderRadius: 2, background: `linear-gradient(180deg,${c.accent},${c.purple})` }} />
              <h2 style={{ fontSize: 18, fontWeight: 900, color: c.text, margin: 0 }}>
                OpenClaw 模型知识飞轮多智能体团队
              </h2>
            </div>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16 }}>
              {/* Left: Org chart + Cron */}
              <div style={{
                background: c.surface, border: `1px solid ${c.border}`,
                borderRadius: 14, padding: 16,
              }}>
                <div style={{ fontSize: 12, fontWeight: 700, color: c.text, marginBottom: 12 }}>
                  组织架构 · Organization
                </div>
                <OrgChart expanded={orgExpanded} onToggle={() => setOrgExpanded(v => !v)} />
                <CronCards status={status} />
              </div>
              {/* Right: DAG Workflow */}
              <WorkflowPanel progress={progress} onTrigger={handleTrigger} toast={toast} />
            </div>
          </div>

          {/* ── Section 2: Closed Loop ── */}
          <div style={{ marginBottom: 40 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 14 }}>
              <div style={{ width: 4, height: 24, borderRadius: 2, background: `linear-gradient(180deg,${c.green},${c.accent})` }} />
              <h2 style={{ fontSize: 18, fontWeight: 900, color: c.text, margin: 0 }}>
                🔄 模型知识飞轮 · 闭环机制
              </h2>
              <span style={{ fontSize: 12, color: c.muted, marginLeft: 8, fontWeight: 400 }}>
                基于 Karpathy Auto Research + WY改进
              </span>
            </div>
            <ClosedLoopFlow />
            <div style={{ marginBottom: 14 }}>
              <div style={{ fontSize: 11, fontWeight: 700, color: c.text, marginBottom: 10 }}>
                监控目标 · Goals
              </div>

              {/* 执行日志面板：实时展示 Agent 调用过程 */}
              {runIdRef.current && (
                <ExecutionLogPanel runId={runIdRef.current} />
              )}
              <GoalsPanel />
            </div>
            <IterationHistory latestRun={triggerCount} />
          </div>

          {/* ── Section 3: Truth Filter ── */}
          <div style={{ marginBottom: 40 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 14 }}>
              <div style={{ width: 4, height: 24, borderRadius: 2, background: `linear-gradient(180deg,${c.red},${c.amber})` }} />
              <h2 style={{ fontSize: 18, fontWeight: 900, color: c.text, margin: 0 }}>
                Truth Filter · 今日打假
              </h2>
              <span style={{ fontSize: 12, color: c.muted, marginLeft: 8 }}>
                每一个拦截都有原因，每一个原因都有证据
              </span>
            </div>
            <div style={{
              display: 'flex', gap: 14, overflowX: 'auto', paddingBottom: 8,
              WebkitOverflowScrolling: 'touch',
            }}>
              {truthCases.map((item, i) => (
                <TruthCard key={item.id} item={item} idx={i} />
              ))}
            </div>
          </div>

          {/* ── Section 4: Work Log + Closed Loop summary ── */}
          <div style={{ marginBottom: 40 }}>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16 }}>
              <WorkLog />
              {/* Closed loop summary card */}
              <div style={{
                background: c.surface, border: `1px solid ${c.border}`,
                borderRadius: 14, padding: 16,
              }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 12 }}>
                  <span style={{ fontSize: 13, fontWeight: 800, color: c.text }}>🔄 闭环逻辑</span>
                </div>
                <p style={{ fontSize: 12, color: c.muted, lineHeight: 1.7, margin: '0 0 12px' }}>
                  每轮执行完毕后 Skill 自审启动 → 读取 commit 历史 → 对照 SKILL.md →
                  发现漏洞 → 更新规则 → 下一轮用更强的规则跑。
                </p>
                <div style={{ background: '#060d1a', borderRadius: 8, padding: 12 }}>
                  {[
                    ['P0拦截率',       '4%（2/50）',       c.amber  ],
                    ['Benchmark合规率', '68% → >90%',     c.accent ],
                    ['SKILL自审',      '已触发1次',        c.green  ],
                  ].map(([k, v, col]) => (
                    <div key={k} style={{
                      display: 'flex', justifyContent: 'space-between',
                      padding: '5px 0', borderBottom: `1px solid ${c.border}`,
                    }}>
                      <span style={{ fontSize: 11, color: c.muted }}>{k}</span>
                      <span style={{ fontSize: 11, fontWeight: 700, color: col as string }}>{v}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>

          {/* ── Footer ── */}
          <div style={{
            borderTop: `1px solid ${c.border}`, paddingTop: 28,
            display: 'flex', justifyContent: 'space-between', fontSize: 11, color: c.muted,
          }}>
            <span>© 2026 SOTA Radar · 小龙虾 OpenClaw 多智能体团队</span>
            <a
              href="https://github.com/Pass-O-Guava/sota-radar"
              target="_blank"
              rel="noopener noreferrer"
              style={{ color: c.accent, textDecoration: 'none' }}
            >
              github.com/Pass-O-Guava/sota-radar
            </a>
          </div>

        </div>
      )}
    </div>
  )
}

// ─── 执行日志面板（实时动态展示）────────────────────────────────────────────
function ExecutionLogPanel({ runId, onDone }: { runId: string; onDone?: () => void }) {
  const [logs, setLogs] = useState<any[]>([])
  const [collapsed, setCollapsed] = useState(false)
  const bottomRef = useRef<HTMLDivElement>(null)
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null)
  const pollCount = useRef(0)

  // 启动轮询
  useEffect(() => {
    if (!runId) return
    pollCount.current = 0
    const poll = async () => {
      pollCount.current++
      const data = await fetchRunLogs(runId)
      setLogs(data.logs || [])
      if (pollCount.current > 60 || data.logs?.some((l: any) => l.status === 'done')) {
        clearInterval(intervalRef.current!)
        onDone?.()
      }
    }
    poll()
    intervalRef.current = setInterval(poll, 3000)
    return () => clearInterval(intervalRef.current!)
  }, [runId])

  // 自动滚动到底部
  useEffect(() => {
    if (!collapsed && bottomRef.current) {
      bottomRef.current.scrollIntoView({ behavior: 'smooth' })
    }
  }, [logs, collapsed])

  const STATUS_COLORS: Record<string, string> = {
    running: c.amber, success: c.green, error: c.red, timeout: c.red,
  }
  const STEP_ICONS: Record<string, string> = {
    trigger: '🚀', dispatch: '📋', research: '🔍',
    qc_review: '🔬', archive: '📦', knowledge_write: '📝',
    self_review: '🔄', complete: '✅',
  }

  if (collapsed) {
    return (
      <div style={{
        background: c.surface, border: `1px solid ${c.border}`,
        borderRadius: 12, padding: '12px 16px', marginBottom: 14,
      }}>
        <button
          onClick={() => setCollapsed(false)}
          style={{
            background: 'none', border: 'none', cursor: 'pointer',
            color: c.muted, fontSize: 12, display: 'flex', alignItems: 'center', gap: 8,
          }}
        >
          <span>▶</span>
          <span>展开执行日志 ({logs.length} 条)</span>
        </button>
      </div>
    )
  }

  return (
    <div style={{
      background: c.surface, border: `1px solid ${c.border}`,
      borderRadius: 12, marginBottom: 14, overflow: 'hidden',
    }}>
      {/* Header */}
      <div style={{
        padding: '10px 16px',
        borderBottom: `1px solid ${c.border}`,
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        background: c.bg,
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <span style={{ fontSize: 13, fontWeight: 800, color: c.accent }}>📋 执行日志</span>
          <span style={{ fontSize: 11, color: c.muted }}>run_id: {runId.slice(0, 12)}…</span>
          {logs.length > 0 && (
            <span style={{
              fontSize: 10, padding: '2px 8px', borderRadius: 100,
              background: c.accent + '20', color: c.accent,
            }}>
              {logs.length} 条
            </span>
          )}
        </div>
        <div style={{ display: 'flex', gap: 8 }}>
          {logs.some((l: any) => l.status === 'running') && (
            <span style={{ fontSize: 11, color: c.amber, display: 'flex', alignItems: 'center', gap: 4 }}>
              <div style={{ width: 6, height: 6, borderRadius: '50%', background: c.amber, animation: 'pulse 1s infinite' }} />
              运行中…
            </span>
          )}
          <button
            onClick={() => setCollapsed(true)}
            style={{
              background: 'none', border: 'none', cursor: 'pointer',
              color: c.muted, fontSize: 12,
            }}
          >
            收起 △
          </button>
        </div>
      </div>

      {/* Log entries */}
      <div style={{
        maxHeight: 320, overflowY: 'auto',
        padding: '8px 0',
        fontFamily: "'Fira Code', 'Courier New', monospace",
        fontSize: 11,
      }}>
        {logs.length === 0 && (
          <div style={{ padding: '16px 16px', color: c.muted, textAlign: 'center' }}>
            等待日志写入…
          </div>
        )}
        {logs.map((log: any, i: number) => {
          const icon = STEP_ICONS[log.step_name] || '⚙️'
          const color = STATUS_COLORS[log.status] || c.muted
          const isRunning = log.status === 'running'
          return (
            <div key={log.id || i} style={{
              padding: '6px 16px',
              borderLeft: `2px solid ${isRunning ? c.amber : color}`,
              marginLeft: 8,
              opacity: isRunning ? 0.85 : (log.status === 'error' ? 0.7 : 1),
              background: isRunning ? c.amber + '08' : (log.status === 'error' ? c.red + '08' : 'transparent'),
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 2 }}>
                <span style={{ fontSize: 12 }}>{icon}</span>
                <span style={{ fontWeight: 700, color: c.text, fontSize: 11 }}>
                  [{log.step_name || log.agent_id}]
                </span>
                <span style={{ fontSize: 10, color: color, fontWeight: 600 }}>
                  {log.status.toUpperCase()}
                </span>
                {log.duration_ms != null && (
                  <span style={{ fontSize: 10, color: c.muted }}>
                    {log.duration_ms}ms
                  </span>
                )}
                <span style={{ fontSize: 10, color: c.muted, marginLeft: 'auto' }}>
                  {new Date(log.started_at).toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit', second: '2-digit' })}
                </span>
              </div>

              {/* 实际输出预览 */}
              {log.output && (
                <div style={{
                  color: c.text + 'bb', fontSize: 10, lineHeight: 1.5,
                  padding: '4px 8px', background: c.bg,
                  borderRadius: 4, marginTop: 3,
                  whiteSpace: 'pre-wrap', wordBreak: 'break-all',
                  maxHeight: 60, overflow: 'hidden',
                }}>
                  {String(log.output).slice(0, 200)}
                  {String(log.output).length > 200 && ' …'}
                </div>
              )}

              {/* 错误信息 */}
              {log.error && (
                <div style={{
                  color: c.red, fontSize: 10, padding: '3px 8px',
                  background: c.red + '15', borderRadius: 4, marginTop: 3,
                }}>
                  ⚠ {String(log.error).slice(0, 150)}
                </div>
              )}

              {/* 运行中动画 */}
              {isRunning && (
                <div style={{ display: 'flex', gap: 4, marginTop: 4 }}>
                  {[0, 1, 2].map(d => (
                    <div key={d} style={{
                      width: 5, height: 5, borderRadius: '50%', background: c.amber,
                      animation: `pulse 1s ${d * 0.3}s infinite`,
                    }} />
                  ))}
                </div>
              )}
            </div>
          )
        })}
        <div ref={bottomRef} />
      </div>

      <style>{`
        @keyframes pulse {
          0%, 100% { opacity: 1; transform: scale(1); }
          50% { opacity: 0.4; transform: scale(0.8); }
        }
      `}</style>
    </div>
  )
}
