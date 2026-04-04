"""
Gemma 4 Demo — 全模态开放模型（图像 + 视频 + 文本 + 音频）
===========================================================
模型：google/gemma-4-31b（可替换为 E2B / E4B / 26B-A4B）
来源：https://huggingface.co/google/gemma-4-31b
许可证：Apache 2.0（完全开放，可商用）
最低显存：
  - E2B/E4B: ~6-8GB（INT4）
  - 31B: ~64GB（FP16）

安装依赖：
  pip install transformers accelerate torch keras

用法：
  python gemma-4-demo.py
"""

import torch
from transformers import AutoProcessor, AutoModelForCausalLM

# ============================================================
# 配置
# ============================================================
# 推荐从 E2B/E4B 开始（显存需求最低）
MODEL_SIZES = {
    "E2B": "google/gemma-4-E2B",
    "E4B": "google/gemma-4-E4B",
    "26B-A4B": "google/gemma-4-26b-a4b",
    "31B": "google/gemma-4-31b",
}

def load_model(size: str = "E4B"):
    """加载指定规格的 Gemma 4 模型"""
    model_name = MODEL_SIZES.get(size, "google/gemma-4-E4B")
    print(f"[INFO] Loading Gemma 4 ({size}): {model_name}")

    processor = AutoProcessor.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    model.eval()
    print(f"[INFO] Gemma 4 ({size}) loaded successfully")
    print(f"[INFO] Multimodal: text + image + video (E2B/E4B also supports audio)")
    return processor, model


def run_vqa(
    processor, model,
    image_path: str,
    question: str,
    max_new_tokens: int = 512,
):
    """执行视觉问答"""
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": image_path},
                {"type": "text", "text": question},
            ],
        }
    ]

    text = processor.tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = processor(text=[text], images=[image_path], return_tensors="pt")
    inputs = {k: v.to(model.device) for k, v in inputs.items() if v is not None}

    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False)

    input_len = inputs["input_ids"].shape[1]
    generated = outputs[0][input_len:]
    return processor.tokenizer.decode(generated, skip_special_tokens=True)


def run_text_only(
    model, processor,
    question: str,
    max_new_tokens: int = 512,
):
    """纯文本推理（无需图像）"""
    messages = [
        {"role": "user", "content": [{"type": "text", "text": question}]}
    ]
    text = processor.tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = processor(text=[text], return_tensors="pt")
    inputs = {k: v.to(model.device) for k, v in inputs.items() if v is not None}

    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False)

    input_len = inputs["input_ids"].shape[1]
    generated = outputs[0][input_len:]
    return processor.tokenizer.decode(generated, skip_special_tokens=True)


def main():
    """演示 Gemma 4 多模态 + 纯文本推理"""
    # 默认使用 E4B（平衡显存需求和能力）
    processor, model = load_model(size="E4B")

    test_image = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusion/anchoir.jpg"

    # ---- 示例 1：多模态理解 ----
    print("\n[示例1] 多模态图像理解")
    print("-" * 50)
    try:
        response = run_vqa(
            processor, model, test_image,
            "Describe this image in detail."
        )
        print(f"[OUTPUT] {response}")
    except Exception as e:
        print(f"[ERROR] {e}")

    # ---- 示例 2：纯文本数学推理 (AIME 2026 强项) ----
    print("\n[示例2] 纯文本数学推理 (Gemma 4 31B AIME 2026: 89.2%)")
    print("-" * 50)
    try:
        math_question = "Solve: If x^2 - 5x + 6 = 0, what are the values of x?"
        response = run_text_only(model, processor, math_question)
        print(f"[INPUT] {math_question}")
        print(f"[OUTPUT] {response}")
    except Exception as e:
        print(f"[ERROR] {e}")

    # ---- 模型规格对比说明 ----
    print("\n[规格说明]")
    print("-" * 50)
    print("""
    Gemma 4 提供 4 种规格，请根据硬件选择：
    
    | 规格     | 参数量  | 显存需求(FP16) | 适用场景             |
    |----------|---------|----------------|----------------------|
    | E2B      | ~2B     | ~6GB           | 边缘设备 / 手机端    |
    | E4B      | ~4B     | ~8GB           | 笔记本 / 消费级GPU   |
    | 26B-A4B  | MoE     | ~48GB          | 工作站 / 专业GPU     |
    | 31B      | 31B     | ~64GB          | 服务器 / 多卡部署    |
    
    所有规格均支持 Apache 2.0，完全可商用。
    """)


if __name__ == "__main__":
    main()
