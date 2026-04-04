"""
Phi-4-reasoning-vision-15B Demo — 多模态推理示例
=================================================
模型：microsoft/Phi-4-reasoning-vision-15B
来源：https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B
许可证：MIT（可商用）
最低显存：~32GB（FP16）；约16GB（INT4量化）

安装依赖：
  pip install transformers accelerate torch

用法：
  python phi-4-vision-demo.py
"""

import torch
from transformers import AutoProcessor, AutoModelForCausalLM

# ============================================================
# 配置
# ============================================================
MODEL_NAME = "microsoft/Phi-4-reasoning-vision-15B"
MAX_NEW_TOKENS = 512

def load_model():
    """加载 Phi-4-reasoning-vision-15B"""
    print(f"[INFO] Loading model: {MODEL_NAME}")
    processor = AutoProcessor.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    model.eval()
    print("[INFO] Model loaded successfully")
    return processor, model


def run_inference(
    processor,
    model,
    image_path: str,
    question: str,
    max_new_tokens: int = MAX_NEW_TOKENS,
):
    """
    执行视觉问答推理

    Args:
        image_path: 本地图片路径或URL
        question: 问题文本
        max_new_tokens: 最大生成 token 数

    Returns:
        模型生成的文本回答
    """
    # Phi-4-reasoning-vision 使用标准的 messages 格式
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

    inputs = processor(
        text=[text],
        images=[image_path],
        return_tensors="pt",
        padding=True,
    )
    inputs = {k: v.to(model.device) for k, v in inputs.items() if v is not None}

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
        )

    # 解码（跳过输入部分）
    input_len = inputs["input_ids"].shape[1]
    generated = outputs[0][input_len:]
    response = processor.tokenizer.decode(generated, skip_special_tokens=True)
    return response


def main():
    """演示 Phi-4-reasoning-vision 的数学推理和 UI 理解能力"""
    processor, model = load_model()

    # ---- 示例 1：数学图表理解 ----
    print("\n[示例1] 数学图表理解 (MathVista)")
    print("-" * 50)

    # 使用 HuggingFace 内置测试图片
    math_image = "https://huggingface.co/datasets/raushan-test/transformers_dummy/resolve/main/image.png"
    question = "Solve this math problem shown in the image. Show your reasoning step by step."

    print(f"[INPUT] Question: {question}")
    try:
        response = run_inference(processor, model, math_image, question)
        print(f"[OUTPUT] {response}")
    except Exception as e:
        print(f"[ERROR] {e}")

    # ---- 示例 2：UI/屏幕理解 (ScreenSpot) ----
    print("\n[示例2] UI 屏幕理解 (ScreenSpot benchmark 强项)")
    print("-" * 50)

    ui_image = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline_example.jpg"
    question = "Describe all the UI elements you can see in this screenshot. List each interactive element."

    print(f"[INPUT] Question: {question}")
    try:
        response = run_inference(processor, model, ui_image, question)
        print(f"[OUTPUT] {response}")
    except Exception as e:
        print(f"[ERROR] {e}")


if __name__ == "__main__":
    main()
