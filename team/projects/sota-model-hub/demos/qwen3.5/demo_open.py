"""
Qwen3.5 开源版（Apache 2.0）本地推理示例
=========================================
模型：Qwen3.5-35B-A3B / Qwen3.5-27B（开源）
GitHub：https://github.com/QwenLM/Qwen3.5
HuggingFace：https://huggingface.co/collections/Qwen/qwen35
许可证：Apache 2.0（中小规格开源，397B MoE 闭源）

安装：
  pip install transformers torch accelerate bitsandbytes  # bitsandbytes 用于 4-bit 量化

推荐配置：Qwen3.5-35B-A3B 至少 24GB VRAM（4-bit 量化可降至 ~16GB）
"""

import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

# ============================================================
# 配置
# ============================================================
MODEL_NAME = "Qwen/Qwen3.5-35B-A3B"     # 开源规格之一（35B 总参 / 3B 激活）
HF_TOKEN = os.environ.get("HF_TOKEN", "YOUR_HF_TOKEN")
DEVICE = "cuda"

# 4-bit 量化配置（节省显存）
BNB_CONFIG = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)


def load_model():
    print(f"Loading {MODEL_NAME} with 4-bit quantization...")
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        token=HF_TOKEN,
        trust_remote_code=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        quantization_config=BNB_CONFIG,
        device_map="auto",
        token=HF_TOKEN,
        trust_remote_code=True,
    )
    print("Done.")
    return model, tokenizer


def chat(model, tokenizer, messages: list) -> str:
    """多轮对话接口"""
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt").to(DEVICE)
    outputs = model.generate(**inputs, max_new_tokens=512, temperature=0.7)
    response = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
    return response


if __name__ == "__main__":
    model, tokenizer = load_model()

    messages = [
        {"role": "user", "content": "解释 Qwen3.5 的 Native Multimodal Agent 架构与 Qwen3 的主要区别。"}
    ]
    result = chat(model, tokenizer, messages)
    print("Response:", result)
