"""
Qwen3-VL Demo — 视觉语言模型推理示例
=====================================
模型：Qwen3-VL-8B-Instruct
来源：https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct
许可证：Apache 2.0（可商用）
最低显存：~18GB（FP16）；约10GB（INT4量化）

安装依赖：
  pip install transformers qwen-vl-utils accelerate torch

用法：
  python qwen3-vl-demo.py
"""

import torch
from transformers import AutoProcessor, AutoModelForCausalLM
from qwen_vl_utils import process_vision_info

# ============================================================
# 配置
# ============================================================
MODEL_NAME = "Qwen/Qwen3-VL-8B-Instruct"
PROMPT_TEMPLATE = """You are a helpful assistant. Describe the image in detail."""

def load_model():
    """加载 Qwen3-VL-8B-Instruct 模型和处理器"""
    print(f"[INFO] 正在加载模型: {MODEL_NAME}")
    processor = AutoProcessor.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True
    )
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    print("[INFO] 模型加载完成")
    return processor, model


def run_inference(
    processor,
    model,
    image_path: str,
    prompt: str = PROMPT_TEMPLATE,
    max_new_tokens: int = 256,
):
    """
    执行视觉问答推理

    Args:
        image_path: 本地图片路径或图片URL
        prompt: 用户提问
        max_new_tokens: 最大生成 token 数

    Returns:
        模型生成的文本回答
    """
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": image_path},
                {"type": "text", "text": prompt},
            ],
        }
    ]

    # 准备输入
    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    image_inputs, video_inputs = process_vision_info(messages)

    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    )
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    # 推理
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
        )

    # 解码
    generated_ids = outputs[:, inputs["input_ids"].shape[1]:]
    response = processor.batch_decode(
        generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )[0]

    return response


def main():
    """主函数：演示 Qwen3-VL 图像描述能力"""
    processor, model = load_model()

    # 示例 1：本地图片（请替换为实际存在的图片路径）
    print("\n[示例1] 图像描述")
    print("-" * 50)

    # 你可以替换为任意本地图片路径进行测试
    test_image = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusion/anchoir.jpg"
    print(f"[INPUT] 图片: {test_image}")
    print(f"[INPUT] 提示: 描述这张图片的详细内容")

    try:
        response = run_inference(processor, model, test_image, "描述这张图片的详细内容")
        print(f"[OUTPUT] {response}")
    except Exception as e:
        print(f"[ERROR] 推理失败: {e}")
        print("提示：如遇网络问题，请确保图片URL可访问，或使用本地图片路径。")

    # 示例 2：数学图表理解
    print("\n[示例2] 图表理解")
    print("-" * 50)
    chart_image = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/cats/photo-of-three-cats.jpg"
    try:
        response = run_inference(
            processor, model, chart_image,
            "这张图片里有几只动物？请描述它们。"
        )
        print(f"[OUTPUT] {response}")
    except Exception as e:
        print(f"[ERROR] {e}")


if __name__ == "__main__":
    main()
