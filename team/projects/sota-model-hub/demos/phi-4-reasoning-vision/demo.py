#!/usr/bin/env python3
"""
Phi-4-reasoning-vision-15B 自适应推理视频 Demo
模型: microsoft/Phi-4-reasoning-vision-15B
来源: Microsoft Research Blog https://www.microsoft.com/en-us/research/blog/phi-4-reasoning-vision
      arXiv: https://arxiv.org/abs/2603.03975

核心创新:
  自适应思维机制（Adaptive Thinking）— 模型自己判断何时需要深度思考，
  何时直接输出，是"何时思考"的选择模型，而非全链思维链。
  15B 参数实现与更大模型竞争的质量，同时推理速度更快。

依赖:
  pip install transformers torch accelerate huggingface_hub

用法:
  python demo.py --video_path video.mp4 --question "描述视频"
"""

import argparse
import torch
from transformers import AutoProcessor, AutoModelForVision2Seq
from PIL import Image

MODEL_NAME = "microsoft/Phi-4-reasoning-vision-15B"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


def load_model(name: str = MODEL_NAME):
    print(f"[INFO] Loading {name} — Adaptive Reasoning Multimodal Model ...")
    processor = AutoProcessor.from_pretrained(name, trust_remote_code=True)
    model = AutoModelForVision2Seq.from_pretrained(
        name,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    print("[INFO] Model loaded. Open-weight (check license for commercial use).")
    return processor, model


def extract_frames(video_path: str, num_frames: int = 8):
    """均匀采样视频帧"""
    from decord import VideoReader, cpu
    vr = VideoReader(video_path, ctx=cpu(0))
    indices = list(range(0, len(vr), len(vr) // num_frames))[:num_frames]
    return [Image.fromarray(f) for f in vr.get_batch(indices).asnumpy()]


def adaptive_analyze(processor, model, frames, question: str):
    """
    自适应推理分析 — 模型自动判断推理深度
    简单问题 → 快速输出
    复杂问题 → 触发 chain-of-thought 推理
    """
    messages = [{"role": "user", "content": [
        *[{ "type": "image", "image": f } for f in frames],
        { "type": "text", "text": question },
    ]}]

    try:
        text = processor.apply_chat_template(messages, add_generation_prompt=True)
        inputs = processor(text=text, images=frames, return_tensors="pt").to(DEVICE)
    except Exception:
        inputs = processor(text=question, images=frames, return_tensors="pt").to(DEVICE)

    with torch.no_grad():
        out = model.generate(
            **inputs,
            max_new_tokens=512,
            do_sample=True,
            temperature=0.7,
        )

    input_len = inputs["input_ids"].shape[1]
    response = processor.batch_decode(out[:, input_len:], skip_special_tokens=True)[0]

    print(f"\n[Q] {question}")
    print(f"[A] {response}")
    return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phi-4-reasoning-vision 自适应推理视频Demo")
    parser.add_argument("--video_path", type=str, default="")
    parser.add_argument("--question", type=str,
        default="分析这个视频，按时间顺序描述主要事件，并推测下一步可能发生什么。")
    args = parser.parse_args()

    processor, model = load_model()

    if args.video_path:
        print(f"[INFO] Processing: {args.video_path}")
        frames = extract_frames(args.video_path)
    else:
        print("[INFO] No video — using dummy image for quick test.")
        frames = [Image.new("RGB", (224, 224), color="yellow")]

    adaptive_analyze(processor, model, frames, args.question)

    print("\n✅ Demo complete!")
    print("提示: 简单问题（如颜色识别）模型将快速输出；")
    print("      复杂问题（如事件预测）模型将触发自适应深度推理。")
