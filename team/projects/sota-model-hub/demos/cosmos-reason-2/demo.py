#!/usr/bin/env python3
"""
NVIDIA Cosmos Reason 2 物理AI视频理解 Demo
模型: nvidia/cosmos-reason2-8B  (可选: 2B)
来源: GitHub https://github.com/nvidia-cosmos/cosmos-reason2
      HuggingFace NIM https://build.nvidia.com/nvidia/cosmos-reason2-8b/modelcard
Benchmark: Physical AI Leaderboard #1（NVIDIA官方公告 CES 2026）

依赖:
  pip install transformers torch accelerate huggingface_hub

用途:
  机器人视频感知、具身AI、实时物理推理、长视频事件时序分析
"""

import argparse
import torch
from transformers import AutoProcessor, AutoModelForVision2Seq
from PIL import Image

# 8B for best quality, use 2B for edge deployment
MODEL_NAME = "nvidia/cosmos-reason2-8B"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


def load_model(name: str = MODEL_NAME):
    print(f"[INFO] Loading {name} — Physical AI reasoning model ...")
    processor = AutoProcessor.from_pretrained(name, trust_remote_code=True)
    model = AutoModelForVision2Seq.from_pretrained(
        name,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    print("[INFO] Model loaded. Apache 2.0 style license.")
    return processor, model


def extract_frames(video_path: str, num_frames: int = 8):
    from decord import VideoReader, cpu
    vr = VideoReader(video_path, ctx=cpu(0))
    indices = list(range(0, len(vr), len(vr) // num_frames))[:num_frames]
    return [Image.fromarray(f) for f in vr.get_batch(indices).asnumpy()]


def reason_about_video(processor, model, frames, question: str):
    """
    使用 Cosmos Reason 2 对视频进行物理推理
    核心：模型自带 chain-of-thought 推理 token，逐 token 思考物理交互
    """
    prompt = (
        "You are a physical AI reasoning assistant. Analyze the video frames "
        "with physical common sense understanding (object properties, collisions, "
        f"trajectories, weight, material interactions).\n\nQuestion: {question}"
    )

    messages = [{"role": "user", "content": [
        *[{ "type": "image", "image": f } for f in frames],
        { "type": "text", "text": prompt },
    ]}]

    try:
        text = processor.apply_chat_template(messages, add_generation_prompt=True)
        inputs = processor(text=text, images=frames, return_tensors="pt").to(DEVICE)
    except Exception:
        inputs = processor(text=prompt, images=frames, return_tensors="pt").to(DEVICE)

    with torch.no_grad():
        out = model.generate(
            **inputs,
            max_new_tokens=768,  # 允许长链推理输出
            do_sample=False,      # Cosmos 推荐 deterministic 输出
        )

    input_len = inputs["input_ids"].shape[1]
    response = processor.batch_decode(out[:, input_len:], skip_special_tokens=True)[0]

    print(f"\n[Q] {question}\n[A] {response}")
    return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cosmos Reason 2 物理AI视频推理 Demo")
    parser.add_argument("--video_path", type=str, default="")
    parser.add_argument("--question", type=str,
        default="分析视频中物体的物理属性和运动轨迹，判断它们之间可能发生的物理交互。")
    args = parser.parse_args()

    processor, model = load_model()

    if args.video_path:
        print(f"[INFO] Processing video: {args.video_path}")
        frames = extract_frames(args.video_path)
    else:
        print("[INFO] No video — using dummy frames for quick test.")
        frames = [Image.new("RGB", (224, 224), color="red")]

    reason_about_video(processor, model, frames, args.question)

    print("\n✅ Demo complete!")
    print("提示: Cosmos Reason 2 专为物理世界AI设计，适合机器人视频感知、具身智能场景。")
