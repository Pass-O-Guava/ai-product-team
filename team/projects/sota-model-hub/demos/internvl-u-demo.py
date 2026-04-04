"""
InternVL-U Demo — 统一多模态模型（理解 + 推理 + 生成 + 编辑）
================================================================
模型：InternVL-U/InternVL-U
来源：https://huggingface.co/InternVL-U/InternVL-U
许可证：MIT（可商用）
最低显存：约12GB（INT4量化后）

安装依赖：
  pip install transformers accelerate torch torchvision

用法：
  python internvl-u-demo.py

说明：
  InternVL-U 是全球首个将多模态理解、推理、生成、编辑
  整合在单一 4B 模型中的统一多模态模型（UMM）。
"""

import torch
from transformers import AutoProcessor, AutoModel

# ============================================================
# 配置
# ============================================================
MODEL_NAME = "InternVL-U/InternVL-U"

def load_model():
    """加载 InternVL-U 统一多模态模型"""
    print(f"[INFO] Loading InternVL-U: {MODEL_NAME}")
    processor = AutoProcessor.from_pretrained(MODEL_NAME, trust_remote_code=True)
    model = AutoModel.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    model.eval()
    print("[INFO] InternVL-U loaded successfully (4B params)")
    print("[INFO] Supported capabilities: Understanding + Reasoning + Generation + Editing")
    return processor, model


def multimodal_understanding(
    processor, model,
    image_path: str,
    question: str = "Describe this image in detail.",
    max_new_tokens: int = 256,
):
    """多模态理解 + 推理（VLM 能力）"""
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": image_path},
                {"type": "text", "text": question},
            ],
        }
    ]

    # 通用处理（InternVL-U 使用类似 Phi-4 的处理方式）
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


def main():
    """演示 InternVL-U 的四大能力"""
    processor, model = load_model()

    test_image = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusion/anchoir.jpg"

    # ---- 1. 多模态理解 ----
    print("\n[能力1] 多模态理解")
    print("-" * 50)
    try:
        response = multimodal_understanding(
            processor, model, test_image,
            "请详细描述这张图片的内容。"
        )
        print(f"[理解] {response}")
    except Exception as e:
        print(f"[ERROR] 理解失败: {e}")

    # ---- 2. 文本渲染 & 科学推理 ----
    print("\n[能力2] 文本渲染 & 科学推理")
    print("-" * 50)
    try:
        response = multimodal_understanding(
            processor, model, test_image,
            "Can you read all text in this image and answer any questions about it?"
        )
        print(f"[文本渲染] {response}")
    except Exception as e:
        print(f"[ERROR] {e}")

    # ---- 3 & 4. 图像生成 & 编辑 ----
    print("\n[能力3+4] 图像生成 & 编辑（请参考 GitHub 获取完整 API）")
    print("-" * 50)
    print("""
  InternVL-U 的图像生成和编辑能力需要调用特定的接口。
  详情请参考：
  - GitHub: https://github.com/OpenGVLab/InternVL-U
  - 论文: https://arxiv.org/abs/2603.09877
  
  基础理解能力已可通过上述 API 调用。
    """)


if __name__ == "__main__":
    main()
