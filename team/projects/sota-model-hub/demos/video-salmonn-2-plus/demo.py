"""
video-SALMONN 2+ Demo
=========================
模型: tsinghua-ee/video-SALMONN-2_plus_72B
       tsinghua-ee/video_SALMONN2plus_72B_audioAlign (2026-01-28 audio-aligned)
来源: https://huggingface.co/tsinghua-ee/video_SALMONN2plus_72B_audioAlign
论文: https://arxiv.org/abs/2506.15220
GitHub: https://github.com/bytedance/video-SALMONN-2
发布日期: 2026-01-28（72B audio-aligned 版本）

依赖安装:
  pip install transformers torch accelerate av decord librosa

用法:
  python demo.py --video_path ./test.mp4 --model_size 3B
  python demo.py --video_path ./test.mp4 --model_size 72B --use_audio_aligned
  python demo.py --video_path ./test.mp4 --question "What is happening in this video?"
"""

import argparse
import torch
import numpy as np

def load_model(model_size: str = "3B", use_audio_aligned: bool = False):
    if use_audio_aligned:
        id_map = {
            "72B": "tsinghua-ee/video_SALMONN2plus_72B_audioAlign",
            "7B":  "tsinghua-ee/video_SALMONN2plus_7B_audioAlign",
            "3B":  "tsinghua-ee/video_SALMONN2plus_3B_audioAlign",
        }
        model_id = id_map.get(model_size, "tsinghua-ee/video_SALMONN2plus_3B_audioAlign")
    else:
        model_id = f"tsinghua-ee/video-SALMONN-2_plus_{model_size}"

    print(f"[INFO] Loading: {model_id}")
    from transformers import AutoModelForCausalLM, AutoProcessor
    processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_id, torch_dtype=torch.float16, device_map="auto", trust_remote_code=True)
    model.eval()
    print("[OK] Model loaded")
    return model, processor

def extract_frames(video_path, max_frames=16):
    try:
        from decord import VideoReader, cpu
        vr = VideoReader(video_path, ctx=cpu(0))
        idx = np.linspace(0, len(vr)-1, max_frames, dtype=int)
        return vr.get_batch(idx).asnumpy()
    except Exception:
        import cv2
        cap = cv2.VideoCapture(video_path)
        frames = []
        for _ in range(max_frames):
            ret, frame = cap.read()
            if not ret: break
            frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        cap.release()
        return np.array(frames[:max_frames])

def extract_audio(video_path, sr=16000):
    import librosa
    audio, _ = librosa.load(video_path, sr=sr, mono=True)
    return audio

def understand(model, processor, video_path, question):
    frames = extract_frames(video_path)
    audio  = extract_audio(video_path)
    inputs = processor(
        videos=frames, audios=audio, sampling_rate=16000,
        text=question, return_tensors="pt")
    inputs = {k: (v.to(model.device) if isinstance(v, torch.Tensor) else v)
              for k, v in inputs.items()}
    outputs = model.generate(**inputs, max_new_tokens=512, do_sample=False)
    return processor.batch_decode(outputs, skip_special_tokens=True)[0]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--video_path", required=True)
    ap.add_argument("--model_size", default="3B", choices=["3B","7B","72B"])
    ap.add_argument("--use_audio_aligned", action="store_true",
                    help="使用 2026-01/02 audio-aligned 版本")
    ap.add_argument("--question", type=str, default=None)
    args = ap.parse_args()

    model, processor = load_model(args.model_size, args.use_audio_aligned)

    q = args.question or "Please describe this video in detail, including visual content and audio."
    print(f"\n[Q] {q}")
    print(f"[A] {understand(model, processor, args.video_path, q)}")

if __name__ == "__main__":
    main()
