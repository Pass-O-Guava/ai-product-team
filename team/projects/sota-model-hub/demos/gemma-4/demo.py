#!/usr/bin/env python3
"""
Gemma 4 视频理解 Demo
模型: google/gemma-4-9b-it  (可选: 2b-it / 4b-it / 27b-it / 31b-it)
来源: HuggingFace https://huggingface.co/blog/gemma4
      vLLM: https://docs.vllm.ai/projects/recipes/en/latest/Google/Gemma4.html

依赖:
  pip install transformers torch accelerate huggingface_hub decord

用法:
  python demo.py --video_path your_video.mp4 --question "描述视频内容"
"""

import argparse
import torch
from transformers import AutoProcessor, AutoModelForVision2Seq
from PIL import Image

MODEL_NAME = "google/gemma-4-9b-it"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


def load_model(name: str = MODEL_NAME):
    print(f"[INFO] Loading {name} ...")
    processor = AutoProcessor.from_pretrained(name)
    model = AutoModelForVision2Seq.from_pretrained(
        name,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )
    print("[INFO] Model loaded.")
    return processor, model


def extract_frames(video_path: str, num_frames: int = 8):
    """均匀采样视频帧"""
    from decord import VideoReader, cpu
    vr = VideoReader(video_path, ctx=cpu(0))
    indices = list(range(0, len(vr), len(vr) // num_frames))[:num_frames]
    return [Image.fromarray(f) for f in vr.get_batch(indices).asnumpy()]


def ask_video(processor, model, frames, question: str):
    """多帧视频问答"""
    messages = [{
        "role": "user",
        "content": [
            *[{ "type": "image", "image": f } for f in frames],
            { "type": "text", "text": question },
        ]
    }]
    text = processor.apply_chat_template(messages, add_generation_prompt=True)
    inputs = processor(text=text, images=frames, return_tensors="pt").to(DEVICE)

    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=512, do_sample=True, temperature=0.7)

    response = processor.batch_decode(out[:, inputs["input_ids"].shape[1]:], skip_special_tokens=True)[0]
    print(f"\n[Q] {question}\n[A] {response}")
    return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_path", type=str, default="")
    parser.add_argument("--question", type=str, default="简要描述这个视频的内容和主要事件。")
    args = parser.parse_args()

    processor, model = load_model()

    if args.video_path:
        frames = extract_frames(args.video_path)
    else:
        print("[INFO] No video provided — using dummy image for quick test.")
        frames = [Image.new("RGB", (224, 224), color="skyblue")]

    ask_video(processor, model, frames, args.question)
