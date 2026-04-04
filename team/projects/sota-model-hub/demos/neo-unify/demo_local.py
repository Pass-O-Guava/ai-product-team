"""
NEO-unify 本地推理示例
=======================
模型：NEO-unify（SenseNova，2B 参数，开源 Apache 2.0）
官方博客：https://huggingface.co/blog/sensenova/neo-unify
架构：Encoder-Free 原生多模态融合 + Mixture-of-Transformer (MoT)

✅ 完全开源，可本地部署，无需 API Key。

安装依赖：
  pip install transformers torch huggingface_hub accelerate

首次运行：
  export HF_TOKEN=your_token
"""

import os
import torch
from transformers import AutoModelForCausalLM, AutoProcessor

MODEL_NAME = "sensenova/neo-unify-2B"   # 确认 HuggingFace 官方模型名后替换
HF_TOKEN = os.environ.get("HF_TOKEN", "YOUR_HF_TOKEN")
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


def load_model():
    print(f"Loading NEO-unify 2B on {DEVICE} ...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.bfloat16 if DEVICE == "cuda" else torch.float32,
        device_map="auto",
        token=HF_TOKEN,
        trust_remote_code=True,
    )
    processor = AutoProcessor.from_pretrained(
        MODEL_NAME,
        token=HF_TOKEN,
        trust_remote_code=True,
    )
    print("Model loaded.")
    return model, processor


def understand_and_generate_image(model, processor, image_path: str, prompt: str) -> str:
    """
    输入图像 + 文本指令 → 文本回答 + 图像生成（原生统一）
    NEO-unify 支持理解与生成一体化，无需调用外部模型。
    """
    from PIL import Image
    image = Image.open(image_path).convert("RGB")

    messages = [
        {"role": "user", "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": prompt}
        ]}
    ]

    inputs = processor(text=messages, images=image, return_tensors="pt").to(DEVICE)
    outputs = model.generate(**inputs, max_new_tokens=512)
    return processor.batch_decode(outputs, skip_special_tokens=True)[0]


def text_only_task(model, processor, prompt: str) -> str:
    """纯文本理解任务（快速验证）"""
    messages = [{"role": "user", "content": prompt}]
    inputs = processor(text=messages, return_tensors="pt").to(DEVICE)
    outputs = model.generate(**inputs, max_new_tokens=256)
    return processor.batch_decode(outputs, skip_special_tokens=True)[0]


if __name__ == "__main__":
    model, processor = load_model()
    # 纯文本快速测试
    result = text_only_task(
        model, processor,
        "Explain the key innovation of the NEO architecture in one paragraph."
    )
    print("Result:", result)
