#!/usr/bin/env python3
"""
Qwen3-Coder-Next 推理 Demo（代码专用）
模型：Qwen3-Coder-Next（80B 总 / 3B 激活，MoE）
来源：https://huggingface.co/Qwen/Qwen3-Coder-Next
Benchmark：Aider's 74%，SWE-rebench 54.4%（Feb 2026）
特点：3B 激活参数 → 消费级 GPU 可运行（MacBook + 64GB RAM 或等效）

使用方法：
  pip install transformers torch accelerate
  python inference_qwen3_coder_next.py

  # 生产部署（推荐 vLLM，2卡）
  pip install vllm
  python inference_qwen3_coder_next.py --backend vllm --tensor_parallel_size 2
"""

import argparse, os

DEFAULT_MODEL = "Qwen/Qwen3-Coder-Next"
DEFAULT_CODE_PROMPT = """修复以下 Python 代码的 bug：
```python
def fibonacci(n):
    if n <= 0: return []
    elif n == 1: return [0]
    elif n == 2: return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i] + fib[i-2])  # BUG: 当 n=2 时 index error
        return fib
```
请说明 bug 并给出修复代码。
"""

def run_transformers(prompt, model, temperature=0.7, max_tokens=2048):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    print(f"🚀 加载 {model}（消费级 GPU 可运行，3B 激活）")
    tok = AutoTokenizer.from_pretrained(model, trust_remote_code=True)
    m = AutoModelForCausalLM.from_pretrained(model, torch_dtype=torch.bfloat16, device_map="auto", trust_remote_code=True)
    inp = tok([prompt], return_tensors="pt").to(m.device)
    out = m.generate(**inp, max_new_tokens=max_tokens, temperature=temperature, do_sample=temperature>0)
    print(f"📥 输出:\n{tok.decode(out[0][inp.input_ids.shape[1]:], skip_special_tokens=True)}")

def run_vllm(prompt, model, temperature=0.7, max_tokens=2048):
    from vllm import LLM, SamplingParams
    print(f"🚀 加载 {model}")
    llm = LLM(model=model, tensor_parallel_size=2, trust_remote_code=True)
    outputs = llm.generate([prompt], SamplingParams(temperature=temperature, max_tokens=max_tokens))
    print(f"📥 输出:\n{outputs[0].outputs[0].text}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Qwen3-Coder-Next 代码推理 Demo")
    p.add_argument("--model", default=os.environ.get("MODEL_NAME", DEFAULT_MODEL))
    p.add_argument("--prompt", default=DEFAULT_CODE_PROMPT)
    p.add_argument("--temperature", type=float, default=0.7)
    p.add_argument("--max_tokens", type=int, default=2048)
    p.add_argument("--backend", choices=["transformers","vllm"], default="transformers")
    args = p.parse_args()
    if args.backend == "vllm":
        run_vllm(args.prompt, args.model, args.temperature, args.max_tokens)
    else:
        run_transformers(args.prompt, args.model, args.temperature, args.max_tokens)
