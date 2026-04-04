#!/usr/bin/env python3
"""
Qwen3.5-397B-A17B 推理 Demo
模型：Qwen3.5-397B-A17B（MoE，397B 总参数 / 17B 激活参数）
来源：https://huggingface.co/Qwen/Qwen3.5-397B-A17B
License：Qwen3.5 License（基于 LlamaRC，商用友好）

使用方法：
  # vLLM 部署
  pip install vllm
  python inference_qwen35_397b.py

  # 或通过 transformers（需要大显存）
  pip install transformers accelerate
  python inference_qwen35_397b.py --backend transformers
"""

import argparse
import os

DEFAULT_MODEL = "Qwen/Qwen3.5-397B-A17B"
DEFAULT_PROMPT = "用 Python 写一个快速排序算法，并解释时间复杂度。"


def run_vllm(prompt: str, model: str, temperature: float = 0.7, max_tokens: int = 1024):
    """通过 vLLM 推理（推荐，生产级效率）"""
    try:
        from vllm import LLM, SamplingParams
    except ImportError:
        print("❌ 请先安装 vLLM: pip install vllm")
        return

    print(f"🚀 加载模型: {model} ...")
    # 注意：397B MoE 模型需要多卡部署，单卡无法运行
    # 推荐：至少 8x A100 80G 或等效配置
    llm = LLM(
        model=model,
        tensor_parallel_size=8,  # 根据实际硬件调整
        trust_remote_code=True,
    )

    sampling_params = SamplingParams(
        temperature=temperature,
        max_tokens=max_tokens,
        stop=["<|im_end|>", "```"]
    )

    print(f"📤 输入: {prompt}")
    outputs = llm.generate([prompt], sampling_params)
    print(f"📥 输出:\n{outputs[0].outputs[0].text}")


def run_transformers(prompt: str, model: str, temperature: float = 0.7, max_tokens: int = 512):
    """通过 HuggingFace Transformers 推理（研究用途）"""
    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
    except ImportError:
        print("❌ 请先安装: pip install transformers torch accelerate")
        return

    print(f"🚀 加载模型: {model} ...")
    tokenizer = AutoTokenizer.from_pretrained(model, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )

    messages = [{"role": "user", "content": prompt}]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer([text], return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        temperature=temperature,
        do_sample=temperature > 0,
    )
    response = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
    print(f"📥 输出:\n{response}")


def main():
    parser = argparse.ArgumentParser(description="Qwen3.5-397B-A17B 推理 Demo")
    parser.add_argument("--model", default=os.environ.get("MODEL_NAME", DEFAULT_MODEL),
                        help="HuggingFace 模型 ID")
    parser.add_argument("--prompt", default=DEFAULT_PROMPT,
                        help="输入提示词")
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--max_tokens", type=int, default=1024)
    parser.add_argument("--backend", choices=["vllm", "transformers"], default="vllm",
                        help="推理后端（vLLM 推荐生产用）")
    args = parser.parse_args()

    if args.backend == "vllm":
        run_vllm(args.prompt, args.model, args.temperature, args.max_tokens)
    else:
        run_transformers(args.prompt, args.model, args.temperature, args.max_tokens)


if __name__ == "__main__":
    main()
