/**
 * API client for SOTA Radar
 * 
 * 架构说明：
 * - 本项目前端为静态 SPA，部署在 MiniMax Space 等公网环境
 * - 后端（7860/7861 端口）运行于服务器内部，属于服务端组件，浏览器无法直接访问
 * - 部署后（生产环境）：API 调用被禁用，始终使用静态数据（dataLib.ts）
 * - 本地开发时：如有本地后端可尝试连接，但始终有 fallback 保护
 * 
 * V6.0 事故修复：
 *   根因：API_BASE = 'http://localhost:7861' 被硬编码到前端 Bundle
 *   后果：部署后浏览器无法访问服务器内部地址 → 页面完全空白
 *   修复：移除所有硬编码后端地址，生产环境永远使用静态数据
 * 
 * 注意：triggerFlywheel 和 fetchStatus 在生产环境为无操作
 *       真实触发由服务端 cron/scheduler 完成，前端仅为视觉反馈
 */

import { staticModels } from './dataLib'

// ─────────────────────────────────────────────────────────────────────────────
// 移除硬编码：不再引用任何 localhost:N 端口
// 生产环境（前端独立部署时）：永远不调用任何 API
// ─────────────────────────────────────────────────────────────────────────────

const IS_PRODUCTION = typeof window !== 'undefined' &&
  !window.location.hostname.includes('localhost') &&
  !window.location.hostname.includes('127.0.0.1')

// API_BASE 仅保留给本地开发时使用（开发者本地启动后端时）
// 生产部署时此值不会被使用（见下方函数内的 IS_PRODUCTION 守卫）
const LOCAL_DEV_API_BASE = 'http://localhost:7860'

export interface ModelSummary {
  id: string
  name: string
  category: string
  publisher: string
  params: string
  license_tag: string
  is_sota: boolean
  updated_at: string
}

export interface ModelDetail extends ModelSummary {
  benchmarks: { name: string; score: string; source?: string }[]
  hf_url: string
  modality: string
  insight: string
  knowledge?: string
}

export interface StatusInfo {
  state: string
  current_run: {
    run_id: string
    status: string
    started_at: string
    finished_at: string | null
    progress: number
  } | null
  today_runs: number
  today_models_updated: number
}

// ─────────────────────────────────────────────────────────────────────────────
// 公共 API 函数
// ─────────────────────────────────────────────────────────────────────────────

export async function fetchModels(params?: {
  category?: string
  license?: string
  search?: string
  sort?: string
  page?: number
  page_size?: number
}): Promise<{ models: ModelSummary[]; total: number }> {
  // ── 生产环境：直接使用静态数据，不发送任何网络请求 ──
  if (IS_PRODUCTION) {
    return filterStaticModels(params)
  }

  // ── 本地开发：优先尝试真实 API，失败则 fallback ──
  try {
    const q = new URLSearchParams()
    if (params?.category && params.category !== '全部') q.set('category', params.category)
    if (params?.license && params.license !== '全部') q.set('license', params.license)
    if (params?.search) q.set('search', params.search)
    if (params?.sort) q.set('sort', params.sort)
    if (params?.page) q.set('page', String(params.page))
    if (params?.page_size) q.set('page_size', String(params.page_size ?? 12))

    const r = await fetch(`${LOCAL_DEV_API_BASE}/api/v1/models?${q}`)
    if (!r.ok) throw new Error('API error')
    return await r.json()
  } catch {
    // 网络不可用时 fallback 到静态数据
    return filterStaticModels(params)
  }
}

export async function fetchModelDetail(id: string): Promise<ModelDetail | null> {
  // ── 生产环境：静态数据中无 detail，使用简略 summary ──
  if (IS_PRODUCTION) {
    const all = staticModels as unknown as ModelDetail[]
    return all.find((m: any) => m.id === id) || null
  }

  try {
    const r = await fetch(`${LOCAL_DEV_API_BASE}/api/v1/models/${id}`)
    if (!r.ok) throw new Error()
    return await r.json()
  } catch {
    return null
  }
}

export async function triggerFlywheel(modelIds?: string[]): Promise<{ run_id: string; status: string }> {
  // ── 生产环境：禁用（触发由服务端 cron 完成）──
  if (IS_PRODUCTION) {
    return {
      run_id: `prod-${Date.now()}`,
      status: 'scheduled-by-cron',
    }
  }

  try {
    const r = await fetch(`${LOCAL_DEV_API_BASE}/api/v1/flywheel/trigger`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ model_ids: modelIds ?? [] }),
    })
    if (!r.ok) throw new Error('Trigger failed')
    return await r.json()
  } catch {
    return { run_id: 'local-unavailable', status: 'error' }
  }
}

export async function fetchStatus(): Promise<StatusInfo> {
  // ── 生产环境：返回 idle 状态（真实状态由 cron 驱动）──
  if (IS_PRODUCTION) {
    return {
      state: 'IDLE',
      current_run: null,
      today_runs: 0,
      today_models_updated: 0,
    }
  }

  try {
    const r = await fetch(`${LOCAL_DEV_API_BASE}/api/v1/status/current`)
    if (!r.ok) throw new Error()
    return await r.json()
  } catch {
    return {
      state: 'IDLE',
      current_run: null,
      today_runs: 0,
      today_models_updated: 0,
    }
  }
}

// ─────────────────────────────────────────────────────────────────────────────
// 内部工具函数
// ─────────────────────────────────────────────────────────────────────────────

function filterStaticModels(params?: {
  category?: string
  license?: string
  search?: string
  sort?: string
  page?: number
  page_size?: number
}): { models: ModelSummary[]; total: number } {
  let models = [...(staticModels ?? [])] as ModelSummary[]

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
  }

  const pageSize = params?.page_size ?? 12
  const page = params?.page ?? 1
  const start = (page - 1) * pageSize
  const paginated = models.slice(start, start + pageSize)

  return { models: paginated, total: models.length }
}
