// AppV1 — 早期演示版本（已归档）
// 当前版本请使用 AppC（V2.0~V8.0）
export default function AppV1() {
  return (
    <div style={{
      minHeight: '100vh', background: '#030712', color: '#f1f5f9',
      fontFamily: "'Inter',system-ui,sans-serif",
      display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'column', gap: 16,
    }}>
      <div style={{ fontSize: 48 }}>📦</div>
      <div style={{ fontSize: 24, fontWeight: 800, color: '#38bdf8' }}>V1.0 已归档</div>
      <div style={{ fontSize: 14, color: '#64748b', textAlign: 'center', maxWidth: 400 }}>
        此为早期演示版本，功能已整合到后续版本中。
        <br />请点击下方版本切换器，查看 V2.0 及以上版本。
      </div>
      <div style={{ fontSize: 11, color: '#374151', marginTop: 8 }}>
        推荐使用最新版本，体验完整功能
      </div>
    </div>
  )
}
