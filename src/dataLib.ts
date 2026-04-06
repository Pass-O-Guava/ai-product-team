import type { ModelSummary } from './api'

export const staticModels: ModelSummary[] = [
  {id:'cogvideox-5b',name:'CogVideoX-5B',category:'Video',publisher:'智谱AI',params:'5B',license_tag:'✅可商用',is_sota:false,updated_at:'2026-04-05T18:11:47.887213'},
  {id:'glm-4-9b-chat',name:'GLM-4-9B-Chat',category:'Text',publisher:'智谱AI',params:'9B',license_tag:'✅可商用',is_sota:false,updated_at:'2026-04-05T18:11:47.886753'},
  {id:'glm-5-9b-0414',name:'GLM-5-9B-0414',category:'Text',publisher:'智谱AI',params:'9B',license_tag:'✅可商用',is_sota:true,updated_at:'2026-04-05T18:11:47.886996'},
  {id:'glm-5v-turbo',name:'GLM-5V-Turbo',category:'Multimodal',publisher:'智谱AI',params:'~130B',license_tag:'✅可商用',is_sota:true,updated_at:'2026-04-05T18:11:47.886111'},
  {id:'hunievideo',name:'HunieVideo',category:'Video',publisher:'字节跳动',params:'13B',license_tag:'⚠️需申请',is_sota:false,updated_at:'2026-04-05T18:11:47.887111'},
  {id:'janus-pro-7b',name:'Janus-Pro-7B',category:'Multimodal',publisher:'字节跳动',params:'7B',license_tag:'✅可商用',is_sota:false,updated_at:'2026-04-05T18:11:47.886542'},
  {id:'kimi-k2-5',name:'Kimi K2.5',category:'Multimodal',publisher:'月之暗面',params:'200B+',license_tag:'⚠️需申请',is_sota:true,updated_at:'2026-04-05T18:11:47.886248'},
  {id:'qwen2-5-omni-7b',name:'Qwen2.5-Omni-7B',category:'Audio',publisher:'阿里巴巴',params:'7B',license_tag:'✅可商用',is_sota:false,updated_at:'2026-04-05T18:11:47.886653'},
  {id:'qwen3-6-plus',name:'Qwen3.6-Plus',category:'Multimodal',publisher:'阿里巴巴',params:'~140B',license_tag:'⚠️需申请',is_sota:false,updated_at:'2026-04-05T18:11:47.886414'},
  {id:'qwen3-vl-235b-a22b',name:'Qwen3-VL-235B-A22B',category:'Multimodal',publisher:'阿里巴巴通义实验室',params:'235B MoE / 22B激活',license_tag:'✅可商用',is_sota:true,updated_at:'2026-04-05T18:11:47.885898'},
  {id:'qwq-32b',name:'QWQ-32B',category:'Text',publisher:'阿里巴巴',params:'32B',license_tag:'✅可商用',is_sota:true,updated_at:'2026-04-05T18:11:47.886873'},
  {id:'step-3-5-flash',name:'Step-3.5-Flash',category:'Embedding',publisher:'阶跃星辰',params:'-',license_tag:'❌不可商用',is_sota:false,updated_at:'2026-04-05T18:11:47.887325'},
]


export const staticModelInsights: Record<string, string> = {
  'cogvideox-5b': "# CogVideoX-5B  ## 基本信息 - 发布方：智谱AI - 参数量：5B - 模态：video generation - 发布日期：2026-03  ## 许可证 Apache 2.0 ✅可商用  ## 入选理由 智谱开源视频",
  'glm-4-9b-chat': "# GLM-4-9B-Chat  ## 基本信息 - 发布方：智谱AI - 参数量：9B - 模态：text-only - 发布日期：2024-01  ## 许可证 Apache 2.0 ✅可商用  ## Benchmark 数据 | Be",
  'glm-5-9b-0414': "# GLM-5-9B-0414  ## 基本信息 - 发布方：智谱AI - 参数量：9B - 模态：text-only - 发布日期：2026-04  ## 许可证 Apache 2.0 ✅可商用  ## Benchmark 数据 | Be",
  'glm-5v-turbo': "# GLM-5V-Turbo  ## 基本信息 - 发布方：智谱AI - 参数量：~130B - 模态：text+image - 发布日期：2026-04-01  ## 许可证 Apache 2.0 ✅可商用  ## Benchmark 数",
  'hunievideo': "# HunieVideo  ## 基本信息 - 发布方：字节跳动 - 参数量：13B - 模态：video+image - 发布日期：2026-03  ## 许可证 专有协议 ⚠️需申请  ## 入选理由 字节跳动最强开源视频理解模型",
  'janus-pro-7b': "# Janus-Pro-7B  ## 基本信息 - 发布方：字节跳动 - 参数量：7B - 模态：text+image - 发布日期：2026-01  ## 许可证 Apache 2.0 ✅可商用  ## Benchmark 数据 | Be",
  'kimi-k2-5': "# Kimi K2.5  ## 基本信息 - 发布方：月之暗面 - 参数量：200B+ - 模态：text+image+video - 发布日期：2026-02  ## 许可证 专有协议 ⚠️需申请  ## Benchmark 数据 | B",
  'qwen2-5-omni-7b': "# Qwen2.5-Omni-7B  ## 基本信息 - 发布方：阿里巴巴 - 参数量：7B - 模态：text+audio+image - 发布日期：2026-03  ## 许可证 Apache 2.0 ✅可商用  ## 入选理由 端到端",
  'qwen3-6-plus': "# Qwen3.6-Plus  ## 基本信息 - 发布方：阿里巴巴 - 参数量：~140B - 模态：text+image（待核实） - 发布日期：2026-03  ## 许可证 Tongyi Qianwen License ⚠️需申请 ",
  'qwen3-vl-235b-a22b': "# Qwen3-VL-235B-A22B  ## 基本信息 - 发布方：阿里巴巴通义实验室 - 参数量：235B MoE / 22B激活 - 模态：text+image+video - 发布日期：2025-09-23  ## 许可证 Ton",
  'qwq-32b': "# QWQ-32B  ## 基本信息 - 发布方：阿里巴巴 - 参数量：32B - 模态：text-only - 发布日期：2026-03  ## 许可证 Apache 2.0 ✅可商用  ## Benchmark 数据 | Benchma",
  'step-3-5-flash': "# Step-3.5-Flash  ## 基本信息 - 发布方：阶跃星辰 - 参数量：- - 模态：text-only - 发布日期：2026-03  ## 许可证 unknown ❌不可商用  ## 入选理由 阶跃星辰Embedding，",
}
