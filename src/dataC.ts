// Version C — Data Layer
// 真实组织架构 + DAG工作流 + 手动触发模拟

export const orgChart = {
  pm: { id: 'pm', name: 'PM + Coordinator', role: '总指挥 & 调研协调（合并）', icon: '🎯', color: '#38bdf8', desc: '任务拆分 / 委派 / 验收结果，同时负责调研协调' },
  teams: [
    {
      team: '调研团队', icon: '🔍', color: '#34d399',
      members: [
        { id: 'vlm-r',    name: 'VLM-Researcher',     role: '视觉语言模型调研',    status: 'idle' },
        { id: 'alm-r',    name: 'ALM-Researcher',     role: '音频语言模型调研',    status: 'idle' },
        { id: 'video-r',  name: 'Video-Researcher',   role: '视频理解模型调研',    status: 'idle' },
        { id: 'unified-r',name: 'Unified-Researcher', role: '多模态统一模型调研',  status: 'idle' },
        { id: 'text-r',   name: 'Text-Researcher',    role: '纯语言模型调研',      status: 'idle' },
        { id: 'emb-r',    name: 'Embedding-Researcher', role: 'Embedding模型调研',  status: 'idle' },
      ],
    },
    {
      team: '质检团队', icon: '🔎', color: '#fbbf24',
      members: [
        { id: 'qc1', name: 'QC-A', role: '质检员（数据准确性）', status: 'idle' },
        { id: 'qc2', name: 'QC-B', role: '质检员（Benchmark验证）', status: 'idle' },
        { id: 'qc3', name: 'QC-C', role: '质检员（许可证核查）', status: 'idle' },
      ],
    },
    {
      team: '文档管理团队', icon: '📦', color: '#a78bfa',
      members: [
        { id: 'doc-mgr', name: 'Doc-Manager', role: '文档同步 & GitHub管理', status: 'idle' },
        { id: 'tester',  name: 'Tester',      role: '测试 & 质量验收',      status: 'idle' },
      ],
    },
  ],
}

// Cron schedule
export const cronSchedule = {
  morning: { time: '07:00 UTC+8', label: '早7点', action: '全量调研扫描 + 质检 + 归档', nextRun: '明天 07:00' },
  afternoon: { time: '13:30 UTC+8', label: '下午1点半', action: '增量扫描 + 质检反馈循环', nextRun: '今天 13:30' },
}

// DAG workflow steps
export type NodeStatus = 'idle' | 'running' | 'done' | 'rejected' | 'pending'

export interface DagNode {
  id: string
  label: string
  sub: string
  status: NodeStatus
  agent?: string
  duration?: string
  note?: string
  x?: number  // for manual layout
  y?: number
}

export interface DagEdge {
  from: string
  to: string
  label?: string
  dashed?: boolean
  color?: string
}

// Full DAG (including reverse edge for rejection)
export const dagNodes: DagNode[] = [
  { id: 'trigger',   label: '触发工作流',    sub: '定时 / 手动',        status: 'idle',    duration: '--' },
  { id: '分配',      label: 'Coordinator',   sub: '任务分发',            status: 'idle',    agent: 'coordinator', duration: '--' },
  { id: 'scout',     label: 'Scout 调研',   sub: '5类模型并行扫描',     status: 'idle',    agent: 'teams',       duration: '--' },
  { id: 'qc',        label: 'QC 质检',      sub: 'P0门禁核查',          status: 'idle',    agent: 'reviewer',    duration: '--' },
  { id: '反馈',      label: '质检反馈',     sub: '拒绝附原因 → 改进',   status: 'idle',    note: '循环回调研',   duration: '--' },
  { id: '归档',      label: 'Archiver 归档', sub: '文档同步 + GitHub',   status: 'idle',    agent: 'coordinator', duration: '--' },
  { id: '自审',      label: 'Skill 自审',   sub: '对照SKILL.md进化',    status: 'idle',    note: '每日一次',     duration: '--' },
  { id: '完成',      label: '完成汇报',      sub: '飞书推送 + 状态更新', status: 'idle',    agent: 'pm',          duration: '--' },
]

export const dagEdges: DagEdge[] = [
  { from: 'trigger',  to: '分配',   label: '开始' },
  { from: '分配',     to: 'scout',  label: '分发' },
  { from: 'scout',    to: 'qc',    label: '提交' },
  { from: 'qc',       to: '归档',   label: '通过' },
  { from: 'qc',       to: '反馈',   label: '拒绝',  color: '#f87171', dashed: true },
  { from: '反馈',     to: 'scout',  label: '打回重做', color: '#f87171', dashed: true },
  { from: '归档',     to: '自审',   label: '同步' },
  { from: '自审',     to: '完成',   label: '进化' },
  { from: '完成',     to: 'trigger', label: '等待下次', dashed: true, color: '#6b7280' },
]

// When triggered, nodes light up in sequence
export function buildDagSnapshot(progress: number): DagNode[] {
  // progress: 0-100
  const steps: Array<{ nodeId: string; status: NodeStatus; startPct: number; endPct: number }> = [
    { nodeId: 'trigger',  status: 'done',    startPct: 0,  endPct: 5  },
    { nodeId: '分配',     status: 'done',    startPct: 5,  endPct: 15 },
    { nodeId: 'scout',    status: 'done',    startPct: 15, endPct: 45 },
    { nodeId: 'qc',       status: 'done',    startPct: 45, endPct: 65 },
    { nodeId: '归档',     status: 'done',    startPct: 65, endPct: 80 },
    { nodeId: '自审',     status: 'done',    startPct: 80, endPct: 92 },
    { nodeId: '完成',     status: 'done',    startPct: 92, endPct: 100 },
  ]

  return dagNodes.map(node => {
    const step = steps.find(s => s.nodeId === node.id)
    if (!step) return { ...node, status: 'idle' as NodeStatus }
    if (progress >= step.endPct) return { ...node, status: 'done' as NodeStatus }
    if (progress >= step.startPct) return { ...node, status: 'running' as NodeStatus }
    return { ...node, status: 'pending' as NodeStatus }
  })
}

// Truth cases (today)
export const truthCases = [
  {
    id: 'tc1',
    time: '13:18',
    model: 'Mistral Small 4',
    source: 'Mistral 官方博客',
    claim: '"全球最强开源模型"',
    verdict: '夸大其词',
    ourAction: 'QC 实测 SWE-bench 73.1%，落后 GLM-5 的 77.8%',
    ourAction2: '→ 降级为"特色模型待补"，去除 SOTA 标签',
    evidence: [
      { label: '宣传 SWE-bench', val: '~78%',  type: 'claimed' },
      { label: '实测 SWE-bench', val: '73.1%', type: 'measured' },
      { label: 'vs GLM-5',       val: '77.8%', type: 'comparison' },
    ],
    lesson: '教训：许可证正确 ≠ SOTA。Benchmark缺失 = 不能声称SOTA。',
  },
  {
    id: 'tc2',
    time: '13:12',
    model: 'Qwen3.6-Plus',
    source: '阿里云博客',
    claim: '"多模态能力全面升级"',
    verdict: '待核实',
    ourAction: '发现 BuildFastWithAI 称 text-only，阿里博客提及视觉感知',
    ourAction2: '→ 有条件入库，标注 ⚠️ 模态待核实，向调研员发出核实请求',
    evidence: [
      { label: 'BuildFastWithAI', val: 'text-only', type: 'conflict' },
      { label: '阿里博客',         val: '视觉感知',   type: 'conflict' },
      { label: '官方确认',         val: '暂无',       type: 'missing' },
    ],
    lesson: '分类争议影响使用场景判断。入库前必须等官方确认。',
  },
  {
    id: 'tc3',
    time: '13:05',
    model: 'Step-3.5-Flash',
    source: 'HuggingFace',
    claim: '"国产最强 Embedding"',
    verdict: '证据不足',
    ourAction: 'HF 页面无 Benchmark 数据，许可证显示 unknown',
    ourAction2: '→ P0-3 门禁触发：license=unknown 不得入库，已拦截',
    evidence: [
      { label: 'Benchmark数据', val: '无',      type: 'missing' },
      { label: '许可证',         val: 'unknown', type: 'missing' },
      { label: 'P0门禁',         val: '拒绝入库', type: 'action' },
    ],
    lesson: 'HF 页面上有 ≠ 可商用。未核实前不得声明。',
  },
]

export const todayLog = [
  { time: '13:20', agent: 'Text-Researcher', action: '完成 GLM-5 调研入库，Benchmark 证据完整，Apache 2.0 可商用确认', status: 'done' },
  { time: '13:18', agent: 'Reviewer',         action: '拦截 Mistral Small 4 SOTA 声明，SWE-bench 实测 73.1% < 77.8%',   status: 'done' },
  { time: '13:15', agent: 'Reviewer',         action: '向调研员发出 Qwen3.6-Plus 模态核实请求，等待官方确认',           status: 'pending' },
  { time: '13:12', agent: 'Coordinator',      action: '将 Step-3.5-Flash 标为拒绝，附 P0-3 拒绝原因反馈调研员',         status: 'done' },
  { time: '13:08', agent: 'Coordinator',      action: '同步 models.json → README / OVERVIEW / BENCHMARKS / 模型卡',    status: 'done' },
  { time: '13:05', agent: 'Reviewer',         action: '启动 Skill 自审，对照 SKILL.md，发现 Benchmark 数据系统性缺失',   status: 'done' },
]

export const closedLoop = {
  title: '闭环逻辑',
  desc: '每轮执行完毕后 Skill 自审启动 → 读取 commit 历史 → 对照 SKILL.md → 发现漏洞 → 更新规则 → 下一轮用更强的规则跑',
  metrics: {
    'P0拦截率':       '4%（2/50）',
    'Benchmark合规率': '68% → 目标 >90%',
    'SKILL自审':       '已触发1次，发现系统性漏洞',
  },
}
