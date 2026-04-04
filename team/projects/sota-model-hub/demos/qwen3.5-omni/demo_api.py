"""
Qwen3.5-Omni API 调用示例
=========================
模型：Qwen3.5-Omni（Proprietary，仅 API 访问）
官方文档：https://qwen.ai/blog?id=qwen3.5-omni
API 接入：Alibaba Cloud Model Studio / DashScope

⚠️ 注意：Qwen3.5-Omni 不开放权重，仅支持云端 API 调用。
   需要 Alibaba Cloud 账号 + DashScope API Key（开通 Qwen-Omni 服务）。
"""

import json
import base64
import httpx

# ============================================================
# 配置区 — 请替换为你的实际凭证
# ============================================================
API_KEY = "YOUR_DASHSCOPE_API_KEY"          # 替换为你的 DashScope API Key
MODEL_NAME = "qwen3.5-Omni-Plus"            # 可选: Omni-Plus / Omni-Flash / Omni-Light
API_ENDPOINT = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"

# ============================================================
# 示例 1：文本 + 图像输入
# ============================================================
def query_with_image(image_path: str, prompt: str) -> str:
    """
    上传图像并提问（多模态理解）。
    image_path: 本地图片路径
    prompt:    提问文本
    """
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}},
                    {"type": "text", "text": prompt}
                ]
            }
        ],
        "max_tokens": 512,
        "temperature": 0.7,
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    response = httpx.post(API_ENDPOINT, headers=headers, json=payload, timeout=60.0)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


# ============================================================
# 示例 2：视频理解
# ============================================================
def query_with_video(video_path: str, prompt: str) -> str:
    """
    上传视频并提问（视频理解）。
    video_path: 本地视频路径（建议 < 10MB）
    prompt:     提问文本
    """
    with open(video_path, "rb") as f:
        vid_b64 = base64.b64encode(f.read()).decode("utf-8")

    # 推断 MIME 类型（简化处理）
    import mimetypes
    mime = mimetypes.guess_type(video_path)[0] or "video/mp4"

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "video_url", "video_url": {"url": f"data:{mime};base64,{vid_b64}"}},
                    {"type": "text", "text": prompt}
                ]
            }
        ],
        "max_tokens": 512,
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    response = httpx.post(API_ENDPOINT, headers=headers, json=payload, timeout=120.0)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


# ============================================================
# 示例 3：流式语音对话（文本输入 + 语音输出请求）
# ============================================================
def stream_speech_response(text_prompt: str) -> str:
    """
    发送文本指令，请求模型以语音（streaming）回复。
    需要在 payload 中设置 response_format: "audio"（如 API 支持）。
    """
    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": text_prompt}],
        "max_tokens": 256,
        # audio 输出需要开通对应服务，具体参数参考 DashScope 官方文档
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    with httpx.stream("POST", API_ENDPOINT, headers=headers, json=payload, timeout=60.0) as resp:
        for line in resp.iter_lines():
            if line.startswith("data: "):
                data = line[6:]
                if data == "[DONE]":
                    break
                yield json.loads(data)


# ============================================================
# 入口
# ============================================================
if __name__ == "__main__":
    # 快速验证连通性（纯文本）
    test_payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": "你好，请用一句话介绍 Qwen3.5-Omni 的核心能力。"}],
        "max_tokens": 128,
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    r = httpx.post(API_ENDPOINT, headers=headers, json=test_payload, timeout=30.0)
    print("状态码:", r.status_code)
    print("回复:", r.json()["choices"][0]["message"]["content"])
