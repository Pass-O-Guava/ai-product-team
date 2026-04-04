#!/usr/bin/env python3
"""
Kimi K2.5 视频理解 Demo
模型: moonshotai/Kimi-K2.5
来源: HuggingFace https://huggingface.co/moonshotai/Kimi-K2.5
      NVIDIA NIM: https://build.nvidia.com/moonshotai/kimi-k2.5/modelcard
Benchmark: Video-MMMU 86.6%（开源顶尖）

依赖:
  pip install transformers torch accelerate huggingface_hub

用法:
  python demo.py --video_path video.mp4
"""

import argparse
import torch
from transformers import AutoProcessor, AutoModelForVision2Seq
from PIL import Image

MODEL_NAME = "moonshotai/Kimi-K2.5"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


def load_model(name: str = MODEL_NAME):
    print(f"[INFO] Loading {name} ...")
    processor = AutoProcessor.from_pretrained(name, trust_remote_code=True)
    model = AutoModelForVision2Seq.from_pretrained(
        name,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    print("[INFO] Model loaded. MIT Licensed — commercial use allowed.")
    return processor, model


def extract_frames(video_path: str, num_frames: int = 8):
    """从视频均匀采样帧"""
    from decord import VideoReader, cpu
    vr = VideoReader(video_path, ctx=cpu(0))
    indices = list(range(0, len(vr), len(vr) // num_frames))[:num_frames]
    return [Image.fromarray(f) for f in vr.get_batch(indices).asnumpy()]


def analyze_video(processor, model, frames, question: str):
    """对视频帧进行问答"""
    prompt = f"你是一个专业的视频理解助手。请仔细观看以下 {len(frames)} 帧画面，然后回答问题。\n\n问题: {question}"

    messages = [{"role": "user", "content": [
        *[{ "type": "image" } for _ in frames],
        { "type": "text", "text": prompt },
    ]}]

    # 注意：Kimi K2.5 可能使用不同的 chat template，
    # 实际使用时请参考 HuggingFace 模型卡最新说明
    try:
        text = processor.tokenizer.apply_chat_template(messages, add_generation_prompt=True)
        inputs = processor(text=text, images=frames, return_tensors="pt").to(DEVICE)

        with torch.no_grad():
            out = model.generate(**inputs, max_new_tokens=512)

        response = processor.batch_decode(out[:, inputs["input_ids"].shape[1]:], skip_special_tokens=True)[0]
    except Exception as e:
        # Fallback: 直接用 processor 处理
        inputs = processor(text=question, images=frames, return_tensors="pt").to(DEVICE)
        with torch.no_grad():
            out = model.generate(**inputs, max_new_tokens=512)
        response = processor.decode(out[0], skip_special_tokens=True)

    print(f"\n[Q] {question}\n[A] {response}")
    return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kimi K2.5 视频理解 Demo")
    parser.add_argument("--video_path", type=str, default="")
    parser.add_argument("--question", type=str,
        default="请详细描述视频中发生的事件，注意时间顺序和关键细节。")
    args = parser.parse_args()

    processor, model = load_model()

    if args.video_path:
        print(f"[INFO] Extracting frames from: {args.video_path}")
        frames = extract_frames(args.video_path)
    else:
        print("[INFO] No video — using dummy frames for quick test.")
        frames = [Image.new("RGB", (224, 224), color="green")]

    analyze_video(processor, model, frames, args.question)
