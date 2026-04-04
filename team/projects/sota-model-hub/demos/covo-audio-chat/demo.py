"""
Covo-Audio-Chat Demo
=========================
模型: tencent/Covo-Audio-Chat
来源: https://huggingface.co/tencent/Covo-Audio-Chat
许可证: CC BY 4.0（可商用）
发布日期: 2026-02-10

依赖安装:
  pip install transformers torchaudio torch accelerate

特点: 端到端语音对话，全双工，支持连续音频输入+音频输出

用法:
  python demo.py --mode chat
  python demo.py --mode transcribe --audio_path ./test.wav
"""

import argparse
import torch
from transformers import AutoModelForCausalLM, AutoProcessor
import numpy as np

def load_model():
    """加载 Covo-Audio 模型"""
    model_id = "tencent/Covo-Audio-Chat"
    print(f"[INFO] 正在加载模型: {model_id}")

    processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
    )
    model.eval()

    print("[OK] 模型加载完成")
    return model, processor


def chat_mode(model, processor):
    """
    全双工对话模式
    注意: 需要麦克风输入。演示为单轮文本输入->语音理解->文本回复。
    """
    print("\n=== Covo-Audio 文本对话模式 ===")
    print("提示: 输入你的问题，按回车发送（Ctrl+C 退出）\n")

    conversation_history = []

    while True:
        try:
            text_input = input("你: ")
            if not text_input.strip():
                continue

            conversation_history.append({"role": "user", "content": text_input})

            # 构建对话 prompt
            prompt = processor.tokenizer.apply_chat_template(
                conversation_history,
                tokenize=False,
                add_generation_prompt=True,
            )

            # 编码
            inputs = processor(
                text=prompt,
                return_tensors="pt",
            )
            inputs = {k: v.to(model.device) for k, v in inputs.items()}

            # 生成回复
            outputs = model.generate(
                **inputs,
                max_new_tokens=512,
                do_sample=True,
                temperature=0.7,
            )

            response = processor.decode(outputs[0][inputs["input_ids"].shape[1]:], 
                                       skip_special_tokens=True)
            print(f"Covo-Audio: {response}\n")
            conversation_history.append({"role": "assistant", "content": response})

        except KeyboardInterrupt:
            print("\n[INFO] 对话结束")
            break


def transcribe_mode(model, processor, audio_path: str):
    """音频理解模式（语音转文本）"""
    import librosa

    print(f"[INFO] 加载音频: {audio_path}")
    audio, sr = librosa.load(audio_path, sr=16000, mono=True)

    # 构建输入
    inputs = processor(
        audios=audio,
        sampling_rate=sr,
        return_tensors="pt",
    )
    inputs = {k: v.to(model.device) if isinstance(v, torch.Tensor) else v 
              for k, v in inputs.items()}

    print("[INFO] 正在分析音频...")
    outputs = model.generate(**inputs, max_new_tokens=512)
    result = processor.decode(outputs[0], skip_special_tokens=True)

    print(f"\n[RESULT] 音频理解结果:\n{result}")
    return result


def main():
    parser = argparse.ArgumentParser(description="Covo-Audio-Chat 演示")
    parser.add_argument("--mode", type=str, default="chat",
                        choices=["chat", "transcribe"],
                        help="chat=对话模式, transcribe=音频理解模式")
    parser.add_argument("--audio_path", type=str, default=None,
                        help="音频文件路径（transcribe 模式必填）")
    args = parser.parse_args()

    model, processor = load_model()

    if args.mode == "chat":
        chat_mode(model, processor)
    elif args.mode == "transcribe":
        if not args.audio_path:
            raise ValueError("--audio_path 在 transcribe 模式下必填")
        transcribe_mode(model, processor, args.audio_path)


if __name__ == "__main__":
    main()
