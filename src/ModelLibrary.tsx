/**
 * ModelLibrary — 全模型知识库页面（带导航Tab）
 */
import { useState, useEffect, useCallback } from 'react'
import { fetchModels, type ModelSummary } from './api'
import { staticModelInsights } from './dataLib'
import { NavTabs } from './SkillsViewer'

// ─── Design tokens ─────────────────────────────────────────────────────────────
const c = {
  bg: '#030712', surface: '#0f172a', card: '#111827',
  border: '#1e293b', text: '#f1f5f9', muted: '#64748b',
  accent: '#38bdf8', accent2: '#818cf8', green: '#34d399',
  red: '#f87171', amber: '#fbbf24', purple: '#a78bfa', pink: '#f472b6',
}

// ─── Category config ───────────────────────────────────────────────────────────
const CATEGORIES = ['全部', 'Text', 'Video', 'Embedding', 'Multimodal', 'Audio', 'Image']
const LICENSES = ['全部', 'Apache-2.0', 'MIT', 'GPL-3.0', 'Custom', 'unknown']
const SORTS = ['最近更新', '名称 A-Z', 'Benchmark评分', '参数量']

const CATEGORY_COLORS: Record<string, string> = {
  Text: c.accent, Video: c.purple, Embedding: c.green,
  Multimodal: c.amber, Audio: c.pink, Image: '#fb923c',
}
const CATEGORY_ICONS: Record<string, string> = {
  Text: '📝', Video: '🎬', Embedding: '🔢', Multimodal: '🧠', Audio: '🔊', Image: '🖼️',
}

// ─── Skeleton card ─────────────────────────────────────────────────────────────
function SkeletonCard() {
  return (
    <div style={{
      background: c.surface, border: `1px solid ${c.border}`,
      borderRadius: 14, padding: '16px',
      animation: 'pulse 1.5s ease-in-out infinite',
    }}>
      <style>{`@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}`}</style>
      <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 12 }}>
        <div style={{ width: 60, height: 18, background: c.border, borderRadius: 6 }} />
        <div style={{ width: 50, height: 18, background: c.border, borderRadius: 6 }} />
      </div>
      <div style={{ width: '80%', height: 22, background: c.border, borderRadius: 6, marginBottom: 8 }} />
      <div style={{ width: '50%', height: 14, background: c.border, borderRadius: 4, marginBottom: 12 }} />
      <div style={{ display: 'flex', gap: 6, marginBottom: 12 }}>
        <div style={{ width: 60, height: 22, background: c.border, borderRadius: 100 }} />
        <div style={{ width: 60, height: 22, background: c.border, borderRadius: 100 }} />
      </div>
      <div style={{ width: '100%', height: 36, background: c.border, borderRadius: 8 }} />
    </div>
  )
}

// ─── Model card ────────────────────────────────────────────────────────────────
function ModelCard({ model }: { model: ModelSummary }) {
  const insight = staticModelInsights[model.id] || `由 ${model.publisher} 发布 · ${model.params} · ${model.license_tag}`
  const catColor = CATEGORY_COLORS[model.category] || c.muted
  const catIcon = CATEGORY_ICONS[model.category] || '🤖'

  return (
    <div style={{
      background: c.surface, border: `1px solid ${c.border}`,
      borderRadius: 14, padding: '16px', cursor: 'pointer',
      transition: 'all 0.2s',
    }}
    onMouseEnter={e => {
      (e.currentTarget as HTMLDivElement).style.borderColor = catColor + '60'
      ;(e.currentTarget as HTMLDivElement).style.boxShadow = `0 0 20px ${catColor}15`
    }}
    onMouseLeave={e => {
      (e.currentTarget as HTMLDivElement).style.borderColor = c.border
      ;(e.currentTarget as HTMLDivElement).style.boxShadow = 'none'
    }}
    >
      {/* Header row */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 10 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
          <span style={{ fontSize: 12 }}>{catIcon}</span>
          <span style={{
            fontSize: 10, fontWeight: 700, padding: '2px 8px', borderRadius: 100,
            background: catColor + '20', color: catColor, border: `1px solid ${catColor}40`,
          }}>
            {model.category}
          </span>
        </div>
        {model.is_sota && (
          <span style={{
            fontSize: 9, fontWeight: 800, padding: '2px 8px', borderRadius: 100,
            background: c.amber + '20', color: c.amber, border: `1px solid ${c.amber}40`,
          }}>
            ⚡ SOTA
          </span>
        )}
      </div>

      {/* Model name */}
      <div style={{ fontSize: 17, fontWeight: 900, color: c.text, marginBottom: 4, letterSpacing: '-0.01em' }}>
        {model.name}
      </div>

      {/* Publisher */}
      <div style={{ fontSize: 12, color: c.muted, marginBottom: 10 }}>
        {model.publisher}
      </div>

      {/* Tags row */}
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 5, marginBottom: 12 }}>
        <span style={{
          fontSize: 10, fontWeight: 600, padding: '3px 8px', borderRadius: 6,
          background: c.card, color: c.muted, border: `1px solid ${c.border}`,
        }}>
          {model.params}
        </span>
        <span style={{
          fontSize: 10, fontWeight: 600, padding: '3px 8px', borderRadius: 6,
          background: c.card, color: c.muted, border: `1px solid ${c.border}`,
        }}>
          {model.license_tag}
        </span>
        <span style={{
          fontSize: 10, fontWeight: 600, padding: '3px 8px', borderRadius: 6,
          background: c.card, color: c.muted, border: `1px solid ${c.border}`,
        }}>
          {new Date(model.updated_at).toLocaleDateString('zh-CN')}
        </span>
      </div>

      {/* Insight */}
      <div style={{
        fontSize: 11, color: c.muted, lineHeight: 1.6,
        padding: '8px 10px', background: c.bg, borderRadius: 8,
        border: `1px solid ${c.border}`,
      }}>
        {insight}
      </div>
    </div>
  )
}

// ─── Empty state ───────────────────────────────────────────────────────────────
function EmptyState({ search }: { search: string }) {
  return (
    <div style={{ textAlign: 'center', padding: '60px 0' }}>
      <div style={{ fontSize: 48, marginBottom: 16 }}>🔍</div>
      <div style={{ fontSize: 16, fontWeight: 700, color: c.text, marginBottom: 8 }}>
        {search ? '未找到匹配的模型' : '暂无模型数据'}
      </div>
      <div style={{ fontSize: 13, color: c.muted }}>
        {search
          ? `没有找到包含"${search}"的模型，请尝试其他关键词`
          : '后台正在初始化数据，请稍后再试'}
      </div>
    </div>
  )
}

// ─── 主组件 ────────────────────────────────────────────────────────────────────
export default function ModelLibrary({ onNavigate }: { onNavigate?: (tab: 'home' | 'library' | 'skills') => void }) {
  const [models, setModels] = useState<ModelSummary[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [total, setTotal] = useState(0)

  const [search, setSearch] = useState('')
  const [category, setCategory] = useState('全部')
  const [license, setLicense] = useState('全部')
  const [sort, setSort] = useState('最近更新')
  const [page, setPage] = useState(1)
  const PAGE_SIZE = 12

  const load = useCallback(async (overridePage?: number) => {
    setLoading(true)
    setError(null)
    const pg = overridePage ?? page
    try {
      const result = await fetchModels({ category, license, search, sort, page: pg, page_size: PAGE_SIZE })
      setModels(result.models)
      setTotal(result.total)
      setPage(pg)
    } catch {
      setError('加载失败，请稍后重试')
    } finally {
      setLoading(false)
    }
  }, [category, license, search, sort, page])

  useEffect(() => { load(1) }, [category, license, sort])

  const handleSearch = (val: string) => {
    setSearch(val)
    setTimeout(() => load(1), 300)
  }

  const totalPages = Math.ceil(total / PAGE_SIZE)

  return (
    <div style={{
      minHeight: '100vh', background: c.bg, color: c.text,
      fontFamily: "'Inter',system-ui,sans-serif",
    }}>
      {/* Ambient glow */}
      <div style={{ position: 'fixed', inset: 0, pointerEvents: 'none', zIndex: 0, overflow: 'hidden' }}>
        <div style={{
          position: 'absolute', width: 700, height: 700, top: -200, right: -200,
          borderRadius: '50%',
          background: 'radial-gradient(circle,#818cf810 0%,transparent 70%)',
        }} />
      </div>

      {/* 顶部导航 Tab（复用 SkillsViewer 中的 NavTabs） */}
      <NavTabs active="library" onNavigate={onNavigate ?? (() => {})} />

      {/* Content */}
      <div style={{ maxWidth: 1200, margin: '0 auto', padding: '100px 48px 60px', position: 'relative', zIndex: 1 }}>

        {/* 搜索 + 筛选 */}
        <div style={{ marginBottom: 24 }}>
          {/* 搜索框 */}
          <div style={{ position: 'relative', marginBottom: 16 }}>
            <span style={{
              position: 'absolute', left: 14, top: '50%', transform: 'translateY(-50%)',
              fontSize: 16, zIndex: 1,
            }}>🔍</span>
            <input
              value={search}
              onChange={e => handleSearch(e.target.value)}
              placeholder="搜索模型名称、发布方、特性..."
              style={{
                width: '100%', padding: '11px 14px 11px 40px',
                background: c.surface, border: `1px solid ${c.border}`,
                borderRadius: 10, color: c.text, fontSize: 14,
                outline: 'none', boxSizing: 'border-box',
                transition: 'border-color 0.2s',
              }}
              onFocus={e => (e.target.style.borderColor = c.accent + '80')}
              onBlur={e => (e.target.style.borderColor = c.border)}
            />
          </div>

          {/* 筛选行 */}
          <div style={{ display: 'flex', gap: 12, flexWrap: 'wrap', alignItems: 'center' }}>
            {/* Category pills */}
            <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
              {CATEGORIES.map(cat => (
                <button
                  key={cat}
                  onClick={() => { setCategory(cat); setPage(1) }}
                  style={{
                    padding: '5px 14px', borderRadius: 100, border: 'none', fontSize: 12, fontWeight: 600,
                    cursor: 'pointer',
                    background: category === cat ? (CATEGORY_COLORS[cat] || c.accent) + '25' : c.surface,
                    color: category === cat ? (CATEGORY_COLORS[cat] || c.accent) : c.muted,
                    borderBottom: `2px solid ${category === cat ? (CATEGORY_COLORS[cat] || c.accent) : 'transparent'}`,
                    transition: 'all 0.15s',
                  }}
                >
                  {cat === '全部' ? '📂 全部' : (CATEGORY_ICONS[cat] || '') + ' ' + cat}
                </button>
              ))}
            </div>

            <div style={{ marginLeft: 'auto', display: 'flex', gap: 8, alignItems: 'center' }}>
              {/* License filter */}
              <select
                value={license}
                onChange={e => { setLicense(e.target.value); setPage(1) }}
                style={{
                  padding: '5px 10px', borderRadius: 8, background: c.surface,
                  color: c.text, border: `1px solid ${c.border}`, fontSize: 12, cursor: 'pointer',
                }}
              >
                {LICENSES.map(l => <option key={l} value={l}>{l === '全部' ? '📄 许可证' : l}</option>)}
              </select>

              {/* Sort */}
              <select
                value={sort}
                onChange={e => setSort(e.target.value)}
                style={{
                  padding: '5px 10px', borderRadius: 8, background: c.surface,
                  color: c.text, border: `1px solid ${c.border}`, fontSize: 12, cursor: 'pointer',
                }}
              >
                {SORTS.map(s => <option key={s} value={s}>{s}</option>)}
              </select>
            </div>
          </div>
        </div>

        {/* Error banner */}
        {error && (
          <div style={{
            padding: '10px 16px', borderRadius: 10, marginBottom: 16,
            background: c.red + '15', border: `1px solid ${c.red}40`,
            color: c.red, fontSize: 13, display: 'flex', justifyContent: 'space-between', alignItems: 'center',
          }}>
            <span>⚠️ {error}</span>
            <button
              onClick={() => load(1)}
              style={{
                padding: '4px 12px', borderRadius: 6, background: c.red + '20',
                color: c.red, border: `1px solid ${c.red}40`, cursor: 'pointer', fontSize: 12,
              }}
            >
              重试
            </button>
          </div>
        )}

        {/* Cards grid */}
        {loading ? (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: 16 }}>
            {Array.from({ length: 6 }).map((_, i) => <SkeletonCard key={i} />)}
          </div>
        ) : models.length === 0 ? (
          <EmptyState search={search} />
        ) : (
          <>
            <div style={{
              display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))',
              gap: 16, marginBottom: 24,
            }}>
              {models.map(m => <ModelCard key={m.id} model={m} />)}
            </div>

            {/* Pagination */}
            {totalPages > 1 && (
              <div style={{ display: 'flex', justifyContent: 'center', gap: 8 }}>
                <button
                  onClick={() => load(page - 1)}
                  disabled={page <= 1}
                  style={{
                    padding: '6px 14px', borderRadius: 8, background: c.surface,
                    color: page <= 1 ? c.muted : c.text, border: `1px solid ${c.border}`,
                    cursor: page <= 1 ? 'not-allowed' : 'pointer', fontSize: 13,
                  }}
                >
                  ← 上一页
                </button>
                <span style={{
                  padding: '6px 16px', borderRadius: 8, background: c.surface,
                  border: `1px solid ${c.border}`, fontSize: 13, color: c.accent, fontWeight: 700,
                }}>
                  {page} / {totalPages}
                </span>
                <button
                  onClick={() => load(page + 1)}
                  disabled={page >= totalPages}
                  style={{
                    padding: '6px 14px', borderRadius: 8, background: c.surface,
                    color: page >= totalPages ? c.muted : c.text, border: `1px solid ${c.border}`,
                    cursor: page >= totalPages ? 'not-allowed' : 'pointer', fontSize: 13,
                  }}
                >
                  下一页 →
                </button>
              </div>
            )}
          </>
        )}
      </div>
    </div>
  )
}
