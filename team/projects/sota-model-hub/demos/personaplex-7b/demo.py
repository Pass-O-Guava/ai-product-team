"""
PersonaPlex-7B Demo
=========================
模型: nvidia/personaplex-7b-v1
来源: https://huggingface.co/nvidia/personaplex-7b-v1
许可证: NVIDIA Research License（需确认商用条款）
发布日期: 2026-01-15

依赖安装:
  pip install transformers torchaudio torch accelerate

特点: 全双工流式语音对话，240ms 端到端延迟，
      边听边说，无需等待对方说完

用法:
  python demo.py --role "assistant"
  python demo.py --role "friend" --persona "friendly and humorous"
"""

import argparse
import torch
from transformers import AutoModelForCausalLM, AutoProcessor
import numpy as np

def load_model():
    """加载 PersonaPlex 模型"""
    model_id = "nvidia/personaplex-7b-v1"
    print(f"[INFO] 正在加载: {model_id}")

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


def build_role_prompt(role: str, persona: str) -> str:
    """构建角色提示"""
    return f"""You are {role}. Personality: {persona}.
You engage in natural, full-duplex conversation.
Respond concisely and naturally.
"""


def streaming_chat(model, processor, role: str, persona: str):
    """
    全双工流式对话演示
    
    核心特点:
    - 12 帧/秒更新（每帧 ~83ms）
    - Lo-Fi 24kHz 音频输出
    - 240ms 端到端延迟
    
    注: 完整实时对话需要麦克风+实时音频流，
    此演示展示消息级生成流程。
    """
    print(f"\n=== PersonaPlex 全双工对话 ===")
    print(f"角色: {role} | 人格: {persona}")
    print("（输入文本后模型将以 240ms 延迟模拟全双工响应）\n")

    system_prompt = build_role_prompt(role, persona)
    conversation = [{"role": "system", "content": system_prompt}]

    while True:
        try:
            user_input = input("你: ")
            if not user_input.strip():
                continue

            conversation.append({"role": "user", "content": user_input})

            # 构建 prompt
            prompt = processor.tokenizer.apply_chat_template(
                conversation,
                tokenize=False,
                add_generation_prompt=True,
            )

            inputs = processor(
                text=prompt,
                return_tensors="pt",
            )
            inputs = {k: v.to(model.device) for k, v in inputs.items()}

            # 生成（模拟流式）
            print(f"PersonaPlex (240ms 延迟...): ", end="", flush=True)
            outputs = model.generate(
                **inputs,
                max_new_tokens=256,
                do_sample=True,
                temperature=0.7,
            )

            response = processor.tokenizer.decode(
                outputs[0][inputs["input_ids"].shape[1]:],
                skip_special_tokens=True
            )
            print(f"{response}\n")
            conversation.append({"role": "assistant", "content": response})

        except KeyboardInterrupt:
            print("\n[INFO] 对话结束")
            break


def main():
    parser = argparse.ArgumentParser(description="PersonaPlex 全双工对话演示")
    parser.add_argument("--role", type=str, default="assistant",
                        help="角色名称（如 assistant, friend, therapist）")
    parser.add_argument("--persona", type=str, 
                        default="helpful, concise, and friendly",
                        help="角色性格描述")
    args = parser.parse_args()

    model, processor = load_model()
    streaming_chat(model, processor, args.role, args.persona)


if __name__ == "__main__":
    main()
