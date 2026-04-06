/**
 * API client for SOTA Radar — tries live backend, falls back to static data.
 */
import { staticModels } from './dataLib'

const API_BASE = 'http://localhost:7861'

export interface ModelSummary {
  id: string; name: string; category: string; publisher: string
  params: string; license_tag: string; is_sota: boolean; updated_at: string
}

export interface ModelDetail extends ModelSummary {
  benchmarks: {name: string; score: string; source?: string}[]
  hf_url: string; modality: string; insight: string; knowledge?: string
}

export interface StatusInfo {
  state: string
  current_run: { run_id: string; status: string; started_at: string; finished_at: string | null; progress: number } | null
  today_runs: number
  today_models_updated: number
}

export async function fetchModels(params?: {
  category?: string; license?: string; search?: string
  sort?: string; page?: number; page_size?: number
}): Promise<{models: ModelSummary[]; total: number}> {
  try {
    const q = new URLSearchParams()
    if (params?.category && params.category !== '全部') q.set('category', params.category)
    if (params?.license && params.license !== '全部') q.set('license', params.license)
    if (params?.search) q.set('search', params.search)
    if (params?.sort) q.set('sort', params.sort)
    if (params?.page) q.set('page', String(params.page))
    if (params?.page_size) q.set('page_size', String(params.page_size ?? 12))
    const r = await fetch(`${API_BASE}/api/v1/models?${q}`)
    if (!r.ok) throw new Error('API error')
    const data = await r.json()
    return data
  } catch {
    // Fallback to static data
    let models = [...staticModels]
    if (params?.category && params.category !== '全部') {
      models = models.filter(m => m.category === params.category)
    }
    if (params?.license && params.license !== '全部') {
      models = models.filter(m => m.license_tag === params.license)
    }
    if (params?.search) {
      const q = params.search.toLowerCase()
      models = models.filter(m =>
        m.name.toLowerCase().includes(q) ||
        m.publisher.toLowerCase().includes(q)
      )
    }
    if (params?.sort === '名称 A-Z') {
      models = [...models].sort((a, b) => a.name.localeCompare(b.name))
    } else if (params?.sort === 'Benchmark评分') {
      // Keep original order (Benchmark sort needs benchmark data only available in detail)
      models = [...models]
    }
    return { models, total: models.length }
  }
}

export async function fetchModelDetail(id: string): Promise<ModelDetail | null> {
  try {
    const r = await fetch(`${API_BASE}/api/v1/models/${id}`)
    if (!r.ok) throw new Error()
    return await r.json()
  } catch {
    return null
  }
}

export async function triggerFlywheel(modelIds?: string[]): Promise<{run_id: string; status: string}> {
  const r = await fetch(`${API_BASE}/api/v1/flywheel/trigger`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ model_ids: modelIds ?? [] }),
  })
  if (!r.ok) throw new Error('Trigger failed')
  return await r.json()
}

export async function fetchStatus(): Promise<StatusInfo | null> {
  try {
    const r = await fetch(`${API_BASE}/api/v1/status/current`)
    if (!r.ok) throw new Error()
    return await r.json()
  } catch {
    return null
  }
}
