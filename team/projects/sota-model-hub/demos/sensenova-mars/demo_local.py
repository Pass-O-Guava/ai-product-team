"""
SenseNova-MARS 本地推理示例
============================
模型：SenseNova-MARS-8B / SenseNova-MARS-32B（开源）
GitHub：https://github.com/OpenSenseNova/SenseNova-MARS
arXiv：https://arxiv.org/abs/2512.24330

✅ 开源可本地部署，支持 8B（端侧）和 32B（服务器）两个规格。

安装依赖：
  pip install transformers torch huggingface_hub accelerate

首次运行自动下载模型权重（需 HuggingFace 账号 + Token）：
  huggingface-cli login
  # 或设置 HF_TOKEN 环境变量
"""

import os
import torch
from transformers import AutoModelForCausalLM, AutoProcessor
from transformers import AutoTokenizer

# ============================================================
# 配置区
# ============================================================
MODEL_NAME = "OpenSenseNova/SenseNova-MARS-8B"   # 可选: "OpenSenseNova/SenseNova-MARS-32B"
HF_TOKEN = os.environ.get("HF_TOKEN", "YOUR_HF_TOKEN_HERE")
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# ============================================================
# 加载模型
# ============================================================
def load_model():
    print(f"正在加载模型 {MODEL_NAME} 到 {DEVICE} ...")
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
    print("模型加载完成。")
    return model, processor


# ============================================================
# 示例 1：图像理解
# ============================================================
def query_image(model, processor, image_path: str, question: str) -> str:
    """
    上传图像 + 问题，返回文本回答（多模态理解）。
    """
    from PIL import Image

    image = Image.open(image_path).convert("RGB")
    messages = [
        {"role": "user", "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": question}
        ]}
    ]

    inputs = processor(text=messages, images=image, return_tensors="pt").to(DEVICE)
    outputs = model.generate(**inputs, max_new_tokens=512)
    return processor.batch_decode(outputs, skip_special_tokens=True)[0]


# ============================================================
# 示例 2：视频理解（多帧）
# ============================================================
def query_video_frames(model, processor, frame_paths: list, question: str) -> str:
    """
    上传多帧图像模拟视频理解（按时间顺序排列帧路径）。
    """
    from PIL import Image

    images = [Image.open(p).convert("RGB") for p in frame_paths]
    messages = [
        {"role": "user", "content": [
            *[{"type": "image", "image": img} for img in images],
            {"type": "text", "text": question}
        ]}
    ]

    inputs = processor(text=messages, images=images, return_tensors="pt").to(DEVICE)
    outputs = model.generate(**inputs, max_new_tokens=512)
    return processor.batch_decode(outputs, skip_special_tokens=True)[0]


# ============================================================
# 示例 3：Agentic 规划任务（文本多轮）
# ============================================================
def agentic_task(model, processor, task: str) -> str:
    """
    发送复杂任务描述，模型自主规划步骤并执行。
    SenseNova-MARS 支持多工具调用和规划链。
    """
    messages = [
        {"role": "system", "content": "你是一个多模态智能体，可以规划步骤、搜索信息并回答问题。"},
        {"role": "user", "content": task}
    ]

    inputs = processor(text=messages, return_tensors="pt").to(DEVICE)
    outputs = model.generate(**inputs, max_new_tokens=1024)
    return processor.batch_decode(outputs, skip_special_tokens=True)[0]


# ============================================================
# 入口
# ============================================================
if __name__ == "__main__":
    model, processor = load_model()

    # 快速文本测试
    test_output = agentic_task(
        model, processor,
        "请简要说明 SenseNova-MARS 的核心创新点和它与普通 VLM 的区别。"
    )
    print("文本任务结果:", test_output)
