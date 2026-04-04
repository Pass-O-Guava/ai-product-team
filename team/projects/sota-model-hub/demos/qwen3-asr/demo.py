"""
Qwen3-ASR Demo
=========================
模型: Qwen/Qwen3-ASR-1.7B / Qwen/Qwen3-ASR-0.6B
来源: https://huggingface.co/Qwen/Qwen3-ASR-1.7B
许可证: Apache 2.0（推断）
发布日期: 2026-01-29

依赖安装:
  pip install transformers torchaudio torch accelerate

用法:
  python demo.py --audio_path ./test.wav --model_size 1.7B
"""

import argparse
import torch
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
from optimum.quanto import qint8, quantize

def load_model(model_size: str = "1.7B"):
    """加载 Qwen3-ASR 模型"""
    model_id = f"Qwen/Qwen3-ASR-{model_size}"
    print(f"[INFO] 正在加载模型: {model_id}")

    processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
    
    # 加载模型（半精度节省显存）
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
    )

    # 量化加速（可选，INT8）
    # quantize(model, weights=qint8)

    print(f"[OK] 模型加载完成: {model_id}")
    return model, processor


def transcribe(model, processor, audio_path: str, language: str = None):
    """
    语音识别主函数
    
    参数:
        model: 已加载的模型
        processor: 处理器
        audio_path: 音频文件路径（.wav / .mp3 / .flac）
        language: 语言代码（如 "en", "zh", "ja"，None=自动检测）
    """
    import librosa

    # 加载音频（支持重采样到 16kHz）
    audio, sampling_rate = librosa.load(audio_path, sr=16000, mono=True)

    # 构建输入
    inputs = processor(
        audio,
        sampling_rate=sampling_rate,
        return_tensors="pt",
        language=language,  # None = 自动语言检测
    )
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    # 推理
    print("[INFO] 正在识别...")
    generated_ids = model.generate(
        inputs["input_features"],
        max_new_tokens=512,
        do_sample=False,
    )
    
    # 解码
    transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return transcription


def main():
    parser = argparse.ArgumentParser(description="Qwen3-ASR 语音识别演示")
    parser.add_argument("--audio_path", type=str, required=True, help="音频文件路径")
    parser.add_argument("--model_size", type=str, default="1.7B", choices=["1.7B", "0.6B"],
                        help="模型规格: 1.7B(SOTA) 或 0.6B(轻量)")
    parser.add_argument("--language", type=str, default=None,
                        help="语言代码（如 en/zh/ja），None=自动检测，支持52种语言")
    args = parser.parse_args()

    model, processor = load_model(args.model_size)
    result = transcribe(model, processor, args.audio_path, args.language)
    
    print(f"\n[RESULT] 识别结果:\n{result}")


if __name__ == "__main__":
    main()
