/**
 * SkillsViewer — Document library viewer (stub, shows static content).
 */
import { useState } from 'react'

const c = {
  bg: '#030712', surface: '#0f172a', card: '#111827',
  border: '#1e293b', text: '#f1f5f9', muted: '#64748b',
  accent: '#38bdf8', accent2: '#818cf8', green: '#34d399',
  red: '#f87171', amber: '#fbbf24', purple: '#a78bfa',
}

const skills = [
  {
    id: 'researcher', name: 'researcher', label: '调研员', color: c.green,
    desc: '负责扫描多类模型数据源，抓取最新模型发布信息',
    tools: ['WebSearch', 'WebFetch', 'HFScraper'],
    status: 'active', version: 'v2.1', updated: '2026-04-05',
  },
  {
    id: 'reviewer', name: 'reviewer', label: '质检员', color: c.amber,
    desc: '多维度门禁核查：许可证合规、Benchmark数据完整性、SOTA声明证据链',
    tools: ['LicenseCheck', 'BenchmarkVerify', 'TruthFilter'],
    status: 'active', version: 'v1.8', updated: '2026-04-04',
  },
  {
    id: 'archiver', name: 'archiver', label: '归档员', color: c.purple,
    desc: '将审核通过的模型同步至文档体系（README / OVERVIEW / BENCHMARKS / 模型卡）',
    tools: ['GitSync', 'DocWriter', 'HFUploader'],
    status: 'active', version: 'v1.5', updated: '2026-04-03',
  },
  {
    id: 'self-review', name: 'self-review', label: '自审员', color: c.accent,
    desc: '对照 SKILL.md 和 Git commit 历史，识别系统性失误并驱动规则进化',
    tools: ['CommitReader', 'PatternAnalyzer', 'SkillUpdater'],
    status: 'beta', version: 'v0.9', updated: '2026-04-05',
  },
  {
    id: 'coordinator', name: 'coordinator', label: '协调员', color: c.red,
    desc: '总指挥 · 任务委派 · 进度追踪 · 飞书结果推送',
    tools: ['TaskRouter', 'ProgressTracker', 'FeishuNotifier'],
    status: 'active', version: 'v2.0', updated: '2026-04-05',
  },
]

export default function SkillsViewer() {
  const [selected, setSelected] = useState<string | null>(null)
  const skill = skills.find(s => s.id === selected)

  return (
    <div style={{ minHeight: '100vh', background: c.bg, color: c.text, fontFamily: "'Inter',system-ui,sans-serif" }}>
      {/* Header */}
      <div style={{
        borderBottom: `1px solid ${c.border}`, padding: '0 48px', height: 60,
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        background: c.bg + 'dd', backdropFilter: 'blur(20px)',
        position: 'fixed', top: 0, left: 0, right: 0, zIndex: 20,
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <div style={{
            width: 34, height: 34, borderRadius: 10,
            background: `linear-gradient(135deg,${c.accent},${c.accent2})`,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            color: '#fff', fontSize: 16, fontWeight: 900,
          }}>
            S
          </div>
          <span style={{ fontSize: 17, fontWeight: 900, letterSpacing: '-0.02em' }}>
            <span style={{
              background: `linear-gradient(135deg,${c.accent},${c.accent2})`,
              WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent',
              backgroundClip: 'text',
            }}>
              Skills 文档库
            </span>
          </span>
        </div>
        <span style={{ fontSize: 12, color: c.muted }}>{skills.length} 个智能体 · 实时运转</span>
      </div>

      {/* Content */}
      <div style={{ maxWidth: 1200, margin: '0 auto', padding: '100px 48px 60px', position: 'relative', zIndex: 1 }}>
        <div style={{ display: 'flex', gap: 24 }}>
          {/* Sidebar */}
          <div style={{ width: 280, flexShrink: 0 }}>
            <div style={{ fontSize: 11, fontWeight: 700, color: c.muted, marginBottom: 10, letterSpacing: '0.1em', textTransform: 'uppercase' }}>
              智能体列表
            </div>
            {skills.map(s => (
              <div
                key={s.id}
                onClick={() => setSelected(s.id === selected ? null : s.id)}
                style={{
                  padding: '12px 14px', borderRadius: 10, marginBottom: 8, cursor: 'pointer',
                  background: selected === s.id ? s.color + '15' : c.surface,
                  border: `1px solid ${selected === s.id ? s.color + '50' : c.border}`,
                  transition: 'all 0.15s',
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
                  <div style={{
                    width: 8, height: 8, borderRadius: '50%', background: s.color,
                    boxShadow: `0 0 6px ${s.color}`,
                  }} />
                  <span style={{ fontSize: 13, fontWeight: 700, color: c.text }}>{s.label}</span>
                  <span style={{
                    marginLeft: 'auto', fontSize: 9, fontWeight: 700, padding: '2px 7px',
                    borderRadius: 100, background: s.status === 'active' ? c.green + '20' : c.amber + '20',
                    color: s.status === 'active' ? c.green : c.amber,
                  }}>
                    {s.status}
                  </span>
                </div>
                <div style={{ fontSize: 11, color: c.muted }}>{s.name} · v{s.version}</div>
              </div>
            ))}
          </div>

          {/* Main */}
          <div style={{ flex: 1 }}>
            {!skill ? (
              <div style={{ textAlign: 'center', padding: '80px 0', color: c.muted }}>
                <div style={{ fontSize: 48, marginBottom: 16 }}>👆</div>
                <div style={{ fontSize: 15, fontWeight: 700 }}>选择左侧智能体查看详情</div>
              </div>
            ) : (
              <div style={{
                background: c.surface, border: `1px solid ${c.border}`,
                borderRadius: 14, padding: '24px 28px',
              }}>
                {/* Header */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 20 }}>
                  <div style={{
                    width: 44, height: 44, borderRadius: 12,
                    background: skill.color + '20', border: `1.5px solid ${skill.color}50`,
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    fontSize: 20,
                  }}>
                    {skill.name[0].toUpperCase()}
                  </div>
                  <div>
                    <div style={{ fontSize: 20, fontWeight: 900, color: c.text }}>
                      {skill.label}
                      <span style={{ fontSize: 12, color: c.muted, marginLeft: 8, fontWeight: 400 }}>
                        @{skill.name}
                      </span>
                    </div>
                    <div style={{ fontSize: 12, color: c.muted }}>
                      v{skill.version} · 更新于 {skill.updated}
                    </div>
                  </div>
                  <span style={{
                    marginLeft: 'auto', fontSize: 10, fontWeight: 700, padding: '4px 10px',
                    borderRadius: 100, background: skill.color + '20',
                    color: skill.color, border: `1px solid ${skill.color}40`,
                  }}>
                    {skill.status === 'active' ? '✅ 激活' : '🧪 Beta'}
                  </span>
                </div>

                {/* Description */}
                <div style={{
                  padding: '14px 16px', background: c.bg, borderRadius: 10, marginBottom: 20,
                  border: `1px solid ${c.border}`,
                }}>
                  <div style={{ fontSize: 11, color: c.muted, marginBottom: 6 }}>职能描述</div>
                  <div style={{ fontSize: 14, color: c.text, lineHeight: 1.7 }}>{skill.desc}</div>
                </div>

                {/* Tools */}
                <div>
                  <div style={{ fontSize: 11, color: c.muted, marginBottom: 10, fontWeight: 700 }}>工具集</div>
                  <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
                    {skill.tools.map(tool => (
                      <span key={tool} style={{
                        fontSize: 12, fontWeight: 600, padding: '5px 12px', borderRadius: 8,
                        background: skill.color + '15', color: skill.color,
                        border: `1px solid ${skill.color}40`,
                      }}>
                        ⚙️ {tool}
                      </span>
                    ))}
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}
