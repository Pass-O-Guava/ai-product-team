/**
 * API client for SOTA Radar — 真实后端 + 静态 fallback。
 * 生产: VITE_API_BASE 配置（默认 :7860 同源代理）
 * 开发: http://localhost:7860
 */
import { staticModels } from './dataLib'

const API_BASE = (typeof import.meta !== 'undefined' && (import.meta as any).env?.VITE_API_BASE)
  || `${window.location.protocol}//${window.location.hostname}:7860`

export interface ModelSummary {
  id: string; name: string; category: string; publisher: string
  params: string; license_tag: string; is_sota: boolean; updated_at: string
}

export interface ModelDetail extends ModelSummary {
  benchmarks: { name: string; score: string; source?: string }[]
  hf_url: string; modality: string; insight: string; knowledge?: string
}

// ─── Flywheel Run & DAG State ────────────────────────────────────────────────

export interface FlywheelStep {
  step: string
  started_at: string | null
  finished_at: string | null
  status: 'pending' | 'running' | 'done' | 'failed'
  message: string
}

export interface FlywheelRun {
  run_id: string
  status: 'IDLE' | 'RUNNING' | 'COMPLETING' | 'COMPLETED' | 'FAILED'
  started_at: string | null
  finished_at: string | null
  progress: number
  steps: FlywheelStep[]
  results: {
    models_researched?: number
    models_passed?: number
    models_rejected?: number
    p0_count?: number
    skills_updated?: string[]
    evolution_triggered?: boolean
    evolution_reason?: string
    iteration?: number
  }
  errors: string[]
}

export interface CurrentStatus {
  state: string
  current_run: {
    run_id: string; status: string; started_at: string
    finished_at: string | null; progress: number
  } | null
  today_runs: number
  today_models_updated: number
}

// 向后兼容别名
export type StatusInfo = CurrentStatus

// ─── Skills Evolution ─────────────────────────────────────────────────────────

export interface EvolutionStatus {
  skills_index: Record<string, {
    version: string; updated_at: string; trigger: string; file: string
    changelog: { version: string; updated_at: string; trigger: string }[]
  }>
  recent_evolutions: {
    id: string; run_id: string; iteration: number
    trigger_reason: string
    patterns_found: { type: string; description: string; count: number }[]
    skills_updated: string[]
    logged_at: string
  }[]
  next_iteration: number
}

// ─── Helper ───────────────────────────────────────────────────────────────────

async function apiFetch(path: string, opts?: RequestInit): Promise<any> {
  const r = await fetch(`${API_BASE}${path}`, {
    ...opts,
    headers: { 'Content-Type': 'application/json', ...(opts?.headers ?? {}) },
  })
  if (!r.ok) throw new Error(`API ${r.status}: ${r.statusText}`)
  return r.json()
}

// ─── Models ──────────────────────────────────────────────────────────────────

export async function fetchModels(params?: {
  category?: string; license?: string; search?: string
  sort?: string; page?: number; page_size?: number
}): Promise<{ models: ModelSummary[]; total: number }> {
  try {
    const q = new URLSearchParams()
    if (params?.category && params.category !== '全部') q.set('category', params.category)
    if (params?.license && params.license !== '全部') q.set('license', params.license)
    if (params?.search) q.set('search', params.search)
    if (params?.sort) q.set('sort', params.sort)
    if (params?.page) q.set('page', String(params.page))
    if (params?.page_size) q.set('page_size', String(params.page_size ?? 12))
    return await apiFetch(`/api/v1/models?${q}`)
  } catch {
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
        m.name.toLowerCase().includes(q) || m.publisher.toLowerCase().includes(q)
      )
    }
    if (params?.sort === '名称 A-Z') {
      models = [...models].sort((a, b) => a.name.localeCompare(b.name))
    }
    return { models, total: models.length }
  }
}

export async function fetchModelDetail(id: string): Promise<ModelDetail | null> {
  try {
    return await apiFetch(`/api/v1/models/${id}`)
  } catch {
    return null
  }
}

// ─── Flywheel ─────────────────────────────────────────────────────────────────

export async function triggerFlywheel(modelIds?: string[]): Promise<{ run_id: string; status: string }> {
  return apiFetch(`/api/v1/flywheel/trigger`, {
    method: 'POST',
    body: JSON.stringify({ model_ids: modelIds ?? [] }),
  })
}

export async function fetchStatus(): Promise<CurrentStatus | null> {
  try {
    return await apiFetch(`/api/v1/status/current`)
  } catch {
    return null
  }
}

export async function fetchRunStatus(runId: string): Promise<FlywheelRun | null> {
  try {
    return await apiFetch(`/api/v1/flywheel/status/${runId}`)
  } catch {
    return null
  }
}

export async function fetchEvolutionStatus(): Promise<EvolutionStatus | null> {
  try {
    return await apiFetch(`/api/v1/flywheel/evolution/status`)
  } catch {
    return null
  }
}


// ─── Skills 自进化历史 ─────────────────────────────────────────────────────────

export async function fetchEvolutionHistory(limit = 20): Promise<{
  iterations: {
    id: string; run_id: string; iteration: number
    trigger_reason: string
    patterns_found: { type: string; description: string; count: number }[]
    skills_updated: string[]
    logged_at: string
  }[]
  total: number
}> {
  try {
    const evo = await apiFetch(`/api/v1/flywheel/evolution/status`)
    return { iterations: (evo?.recent_evolutions ?? []), total: evo?.recent_evolutions?.length ?? 0 }
  } catch {
    return { iterations: [], total: 0 }
  }
}
