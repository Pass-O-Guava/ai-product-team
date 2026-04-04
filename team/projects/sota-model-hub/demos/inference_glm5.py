#!/usr/bin/env python3
"""
GLM-5 推理 Demo
模型：GLM-5（Zhipu AI，745B MoE）
来源：https://huggingface.co/zhipuai/GLM-5（需确认官方路径）
Benchmark：AIME 2026 92.7%，MATH-500 97.4%，史上最低幻觉率

使用方法：
  pip install vllm transformers torch
  # 至少 8x A100 80G
  python inference_glm5.py --prompt "求 x^2 - 5x + 6 = 0 的根"
"""

import argparse, os

DEFAULT_MODEL = "zhipuai/glm-5"
DEFAULT_PROMPT = "求一元二次方程 x^2 - 5x + 6 = 0 的根，并说明过程。"

def run(prompt, model, backend="vllm", temperature=0.7, max_tokens=1024):
    if backend == "vllm":
        try:
            from vllm import LLM, SamplingParams
        except ImportError:
            print("❌ pip install vllm"); return
        print(f"🚀 加载: {model}")
        llm = LLM(model=model, tensor_parallel_size=8, trust_remote_code=True)
        outputs = llm.generate([prompt], SamplingParams(temperature=temperature, max_tokens=max_tokens))
        print(f"📥 输出:\n{outputs[0].outputs[0].text}")
    else:
        try:
            import torch; from transformers import AutoModelForCausalLM, AutoTokenizer
        except ImportError:
            print("❌ pip install transformers torch"); return
        print(f"🚀 加载: {model}")
        tok = AutoTokenizer.from_pretrained(model, trust_remote_code=True)
        m = AutoModelForCausalLM.from_pretrained(model, torch_dtype=torch.bfloat16, device_map="auto", trust_remote_code=True)
        inp = tok([prompt], return_tensors="pt").to(m.device)
        out = m.generate(**inp, max_new_tokens=max_tokens, temperature=temperature)
        print(f"📥 输出:\n{tok.decode(out[0][inp.input_ids.shape[1]:], skip_special_tokens=True)}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--model", default=os.environ.get("MODEL_NAME", DEFAULT_MODEL))
    p.add_argument("--prompt", default=DEFAULT_PROMPT)
    p.add_argument("--temperature", type=float, default=0.7)
    p.add_argument("--max_tokens", type=int, default=1024)
    p.add_argument("--backend", choices=["vllm","transformers"], default="vllm")
    args = p.parse_args()
    run(args.prompt, args.model, args.backend, args.temperature, args.max_tokens)
