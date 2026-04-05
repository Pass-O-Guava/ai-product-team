// SOTA Radar Prototype — 版本历史
// 命名规范：V主版本.次版本
// 追加规则：新版本追加到列表末尾，不要删除历史记录
// 格式：{ id, label, date, color, component, isPage?, pageId?, desc? }

export interface VersionInfo {
  id: string
  label: string
  date: string
  color: string
  component: string
  isPage?: boolean
  pageId?: string
  desc?: string
}

// ──────────────────────────────────────────────────────────────
// 版本历史（按时间顺序追加，不要删除已有条目）
// ──────────────────────────────────────────────────────────────
export const VERSION_LIST: VersionInfo[] = [

  // V1.x — 早期探索版本
  {
    id: 'v1.0', label: 'V1.0', date: '2026-04-05',
    color: '#64748b',
    desc: '初版原型，A/B/C/D四方案并行，WY选定C方案',
    component: 'AppV1',
  },

  // V2.x — C方案迭代版本
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

  // V3.x — 新增页面（独立页面版本）
  {
    id: 'v3.0', label: 'V3.0', date: '2026-04-05',
    color: '#fbbf24',
    desc: '模型知识库页面，多维筛选+实时搜索+12个真实模型（独立页面）',
    component: 'AppV2',
    isPage: true,
    pageId: 'library',
  },
  {
    id: 'v3.1', label: 'V3.1', date: '2026-04-05',
    color: '#f472b6',
    desc: 'Skills文档库，文件目录式导航，5个真实Skill文档（独立页面）',
    component: 'AppV2',
    isPage: true,
    pageId: 'skills',
  },

  // V4.x — 完整产品版本
  {
    id: 'v4.0', label: 'V4.0', date: '2026-04-05',
    color: '#38bdf8',
    desc: '首页完整+标签导航（首页/模型知识库/Skills文档库），OpenClaw品牌升级，PM+Coordinator合并，三团队并列架构',
    component: 'AppV2',
  },

  // ════════════════════════════════════════════════════════════
  // ▼ 后续バージョン，在此追加（勿删此标记）
  // 追加格式：
  // {
  //   id: 'vX.Y', label: 'VX.Y', date: 'YYYY-MM-DD',
  //   color: '#xxxxxx',
  //   desc: '本版本主要变更',
  //   component: 'AppV2',
  // },
  // ════════════════════════════════════════════════════════════
]

export const CURRENT_VERSION = 'v4.0'
export const CURRENT_LABEL = 'V4.0'
