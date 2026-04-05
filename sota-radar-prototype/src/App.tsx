/**
 * SOTA Radar — 版本切换器
 * 规则：只追加，不覆盖历史版本
 */
import { useState } from 'react'
import AppV1 from './AppV1'
import AppC from './AppC'
import { VERSION_LIST, CURRENT_VERSION } from './versions'

function VersionSwitcher({ current, onSwitch }: { current: string; onSwitch: (v: string) => void }) {
  const [expanded, setExpanded] = useState(false)

  return (
    <div style={{
      position: 'fixed', bottom: 20, left: '50%', transform: 'translateX(-50%)',
      zIndex: 9999, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 8,
    }}>
      <button
        onClick={() => setExpanded(e => !e)}
        style={{
          padding: '7px 18px', borderRadius: 100,
          border: `1.5px solid ${VERSION_LIST.find(v => v.id === current)?.color ?? '#38bdf8'}60`,
          background: 'rgba(0,0,0,0.88)', backdropFilter: 'blur(24px)',
          color: VERSION_LIST.find(v => v.id === current)?.color ?? '#38bdf8',
          fontSize: 12, fontWeight: 700, cursor: 'pointer',
          boxShadow: '0 8px 32px rgba(0,0,0,0.6)',
          letterSpacing: '0.05em',
        }}
      >
        {expanded ? '收起版本 ▲' : `${VERSION_LIST.find(v => v.id === current)?.label ?? current}  (点击切换)`}
      </button>

      {expanded && (
        <div style={{
          background: 'rgba(0,0,0,0.92)', backdropFilter: 'blur(24px)',
          border: '1px solid rgba(255,255,255,0.08)',
          borderRadius: 16, padding: '14px 14px',
          boxShadow: '0 16px 48px rgba(0,0,0,0.7)',
          display: 'flex', flexDirection: 'column', gap: 6,
          minWidth: 340,
        }}>
          <div style={{
            fontSize: 9, color: '#4b5563', fontWeight: 700,
            letterSpacing: '0.12em', textTransform: 'uppercase',
            padding: '0 6px 8px',
            borderBottom: '1px solid rgba(255,255,255,0.05)',
            marginBottom: 2,
          }}>
            版本历史 · {VERSION_LIST.length} 个版本
          </div>

          {VERSION_LIST.map((v) => {
            const isActive = v.id === current
            return (
              <button
                key={v.id}
                onClick={() => { onSwitch(v.id); setExpanded(false) }}
                title={v.desc}
                style={{
                  display: 'flex', alignItems: 'center', gap: 10,
                  padding: '9px 12px', borderRadius: 10, border: 'none',
                  background: isActive ? v.color + '18' : 'transparent',
                  cursor: 'pointer', textAlign: 'left', width: '100%',
                  transition: 'background 0.15s',
                }}
                onMouseEnter={e => { if (!isActive) (e.currentTarget as HTMLButtonElement).style.background = 'rgba(255,255,255,0.05)' }}
                onMouseLeave={e => { if (!isActive) (e.currentTarget as HTMLButtonElement).style.background = 'transparent' }}
              >
                <div style={{
                  fontSize: 9, fontWeight: 900,
                  padding: '3px 8px', borderRadius: 6,
                  background: v.color + (isActive ? '25' : '15'),
                  color: v.color,
                  border: `1px solid ${v.color}${isActive ? '60' : '30'}`,
                  minWidth: 40, textAlign: 'center',
                  letterSpacing: '0.05em',
                }}>
                  {v.label}
                </div>
                <div style={{ flex: 1, minWidth: 0 }}>
                  <div style={{
                    fontSize: 12, fontWeight: isActive ? 700 : 400,
                    color: isActive ? v.color : '#94a3b8',
                    marginBottom: 2,
                  }}>
                    {v.desc}
                  </div>
                  <div style={{ fontSize: 10, color: '#4b5563' }}>{v.date}</div>
                </div>
                {isActive && (
                  <div style={{
                    width: 6, height: 6, borderRadius: '50%',
                    background: v.color,
                    boxShadow: `0 0 6px ${v.color}`,
                    flexShrink: 0,
                  }} />
                )}
              </button>
            )
          })}
        </div>
      )}
    </div>
  )
}

export default function App() {
  const [currentVersion, setCurrentVersion] = useState(CURRENT_VERSION)

  // Determine which page to show based on version
  function getActivePage(version: string): string {
    if (version === 'v3.0') return 'library'
    if (version === 'v3.1') return 'skills'
    return 'home'
  }

  return (
    <div style={{ position: 'relative', minHeight: '100vh' }}>
      <VersionSwitcher current={currentVersion} onSwitch={setCurrentVersion} />
      {currentVersion === 'v1.0' && <AppV1 />}
      {(currentVersion.startsWith('v2.') || currentVersion === 'v4.0' || currentVersion.startsWith('v4.')) && (
        <AppC activePage={getActivePage(currentVersion)} />
      )}
      {currentVersion === 'v3.0' && <AppC activePage="library" />}
      {currentVersion === 'v3.1' && <AppC activePage="skills" />}
    </div>
  )
}
