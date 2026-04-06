// SOTA Radar — 任务时间追踪系统
// 规范：每个任务有明确owner、时间记录、状态追踪

export type TaskStatus = '待开始' | '进行中' | '已完成' | '已阻塞'

export interface Task {
  id: string           // e.g. 'v6.1'
  title: string        // e.g. 'V6.0: OpenClaw Agent接入'
  owner: string        // e.g. '子智能体-3' or 'AI PM'
  version: string      // e.g. 'V6.0'
  status: TaskStatus
  created_at: string   // ISO datetime
  started_at?: string  // ISO datetime
  finished_at?: string // ISO datetime
  duration_min?: number // minutes
  notes?: string
  blockers?: string[]   // 阻塞原因
}

export interface TaskLog {
  updated_at: string
  tasks: Task[]
}

// ─── 初始化任务板（每次启动时读取）───
export const initialTasks: Task[] = [
  // V5.x 已完成
  {
    id: 'v5.1',
    title: 'V5.0: FastAPI核心+知识存储',
    owner: '子智能体-A',
    version: 'V5.0',
    status: '已完成',
    created_at: '2026-04-05T10:00:00Z',
    started_at: '2026-04-05T10:05:00Z',
    finished_at: '2026-04-05T10:15:00Z',
    duration_min: 10,
    notes: '后端v0.1完成，FastAPI+12模型数据+REST API上线',
  },
  {
    id: 'v5.2',
    title: 'V5.0: 前端API接入+版本切换',
    owner: 'AI PM',
    version: 'V5.0',
    status: '已完成',
    created_at: '2026-04-05T10:15:00Z',
    started_at: '2026-04-05T10:16:00Z',
    finished_at: '2026-04-05T11:30:00Z',
    duration_min: 74,
    notes: '版本切换器重构，AppC重写，版本号V1.0~V8.0整理完毕',
  },
  // V6.x 进行中
  {
    id: 'v6.1',
    title: 'V6.0: OpenClaw Agent真实触发',
    owner: '子智能体-3',
    version: 'V6.0',
    status: '进行中',
    created_at: '2026-04-06T01:36:00Z',
    started_at: '2026-04-06T01:36:00Z',
    notes: '接入OpenClaw CLI，flywheel真实触发，后端线程化',
  },
  // V7.x 待开始
  {
    id: 'v7.1',
    title: 'V7.0: SSE实时状态推送',
    owner: '待分配',
    version: 'V7.0',
    status: '待开始',
    created_at: '2026-04-06T01:36:00Z',
  },
  // V8.x 待开始
  {
    id: 'v8.1',
    title: 'V8.0: Cron定时+Cron任务+GitHub同步',
    owner: '待分配',
    version: 'V8.0',
    status: '待开始',
    created_at: '2026-04-06T01:36:00Z',
  },
]
