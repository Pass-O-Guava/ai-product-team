// SOTA Radar Prototype — 版本历史（完整版）
// 规范：前端版本 V+主版本.次版本，与前后端版本统一
// 版本命名：V5.x = 后端v0.1对接前端；V6.x = OpenClaw真实触发；V7.x = SSE实时推送；V8.x = Cron自动化

export interface VersionInfo {
  id: string
  label: string     // 显示标签，如 'V5.0'
  date: string
  color: string
  component: string
  isPage?: boolean
  pageId?: string
  desc?: string     // hover时显示
}

// ──────────────────────────────────────────────────────────────
// 版本历史
// ──────────────────────────────────────────────────────────────
export const VERSION_LIST: VersionInfo[] = [

  // ═══════════════════════════════════════════
  // 第一阶段：视觉方案探索（已完成）
  // ═══════════════════════════════════════════
  {
    id: 'v1.0', label: 'V1.0', date: '2026-04-05',
    color: '#64748b',
    desc: '初版原型，A/B/C/D四方案并行，WY选定C方案',
    component: 'AppV1',
  },
  {
    id: 'v2.0', label: 'V2.0', date: '2026-04-05',
    color: '#38bdf8',
    desc: '确立组织架构树（PM→Coordinator→5调研员），加入DAG工作流和手动触发按钮',
    component: 'AppV2',
  },
  {
    id: 'v2.1', label: 'V2.1', date: '2026-04-05',
    color: '#34d399',
    desc: '新增Auto Research流程图、迭代历史、监控目标',
    component: 'AppV2',
  },
  {
    id: 'v2.2', label: 'V2.2', date: '2026-04-05',
    color: '#a78bfa',
    desc: '今日打假加来源链接、原始引述、完整证据链，支持横向滚动',
    component: 'AppV2',
  },

  // ═══════════════════════════════════════════
  // 第二阶段：产品功能完善（已完成）
  // ═══════════════════════════════════════════
  {
    id: 'v3.0', label: 'V3.0', date: '2026-04-05',
    color: '#fbbf24',
    desc: '模型知识库页面，多维筛选+实时搜索+12个真实模型',
    component: 'AppV2',
    isPage: true, pageId: 'library',
  },
  {
    id: 'v3.1', label: 'V3.1', date: '2026-04-05',
    color: '#f472b6',
    desc: 'Skills文档库，文件目录式导航，5个真实Skill文档',
    component: 'AppV2',
    isPage: true, pageId: 'skills',
  },

  // ═══════════════════════════════════════════
  // 第三阶段：前后端集成（进行中）
  // ═══════════════════════════════════════════
  {
    id: 'v4.0', label: 'V4.0', date: '2026-04-05',
    color: '#38bdf8',
    desc: '首页完整+标签导航（首页/模型知识库/Skills文档库），OpenClaw品牌升级，PM+Coordinator合并，三团队并列架构',
    component: 'AppV2',
  },

  // ─── V5.x：后端v0.1 对接前端，API集成 ───
  {
    id: 'v5.0', label: 'V5.0', date: '2026-04-05',
    color: '#38bdf8',
    desc: '后端FastAPI接入前端，API客户端+静态fallback，模型知识库实时数据，飞轮触发按钮，状态面板轮询，Toast通知',
    component: 'AppV2',
  },

  // ─── V6.x：OpenClaw Agent 真实触发 ───
  {
    id: 'v6.0', label: 'V6.0', date: '2026-04-06',
    color: '#34d399',
    desc: 'OpenClaw Agent真实接入，飞轮真实触发，多智能体并行调研任务分发，结果自动归档知识库',
    component: 'AppV2',
  },

  // ─── V7.x：SSE 实时状态推送 ───
  {
    id: 'v7.0', label: 'V7.0', date: 'TBD',
    color: '#a78bfa',
    desc: '后端SSE实时推送运行状态到前端，前端Dashboard实时刷新无需轮询',
    component: 'AppV2',
  },

  // ─── V8.x：Cron 自动化 + GitHub同步 ───
  {
    id: 'v8.0', label: 'V8.0', date: 'TBD',
    color: '#fbbf24',
    desc: 'Cron定时任务（07:00/13:30自动运行），GitHub自动同步备份，版本标签自动打tag',
    component: 'AppV2',
  },

  // ════════════════════════════════════════════════════════════
  // ▼ 后续版本在此追加（勿删此标记）
  // 追加格式：
  // {
  //   id: 'vX.Y', label: 'VX.Y', date: 'YYYY-MM-DD',
  //   color: '#xxxxxx',
  //   desc: '本版本主要变更',
  //   component: 'AppV2',
  // },
  // ════════════════════════════════════════════════════════════
]

export const CURRENT_VERSION = 'v6.0'
export const CURRENT_LABEL = 'V5.0'
