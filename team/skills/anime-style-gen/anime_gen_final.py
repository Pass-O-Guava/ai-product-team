import os
import sys
import base64
import re
from openai import OpenAI
from pathlib import Path

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 anime_gen_final.py <image_path> <style_prompt> <output_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    style_prompt = sys.argv[2]
    output_path = sys.argv[3]

    api_key = "sk-u1LzG0e2eHyx2BYiXbtgpNShbJAIRnzItZhwcD8LZmCH9X8o"
    base_url = "https://www.dmxapi.cn/v1"
    model = "gemini-3-pro-image-preview"
    client = OpenAI(api_key=api_key, base_url=base_url)

    with open(image_path, "rb") as f:
        base64_data = base64.b64encode(f.read()).decode("utf-8")

    # The REFINED "High Fidelity Full Frame" Rules (No Default Card)
    rules = (
        "TASK: Transform the original photo into the specified artistic style. "
        "1. FULL FRAME: Generate a full-frame image. DO NOT add any borders, frames, or trading card elements unless explicitly requested in the prompt. "
        "2. STYLE: Apply the specified style (e.g., Studio Ghibli) to the entire scene. "
        "3. STRUCTURAL FIDELITY: Keep the exact layout, composition, and spatial positions of the original photo. No angle changes. "
        "4. FACIAL OPTIMIZATION: If original expression is neutral/flat, adjust to a warm, gentle smile. If already happy, keep original. "
        "5. NO DISTORTION: Ensure characters remain highly recognizable. "
        "6. Return ONLY the base64 image data."
    )

    prompt_body = f"Transform into {style_prompt}. {rules}"
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt_body},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_data}"}}
                    ]
                }
            ]
        )
        
        content = response.choices[0].message.content
        match = re.search(r'base64,([a-zA-Z0-9+/=]+)', content)
        if match:
            img_data = base64.b64decode(match.group(1))
            with open(output_path, "wb") as f:
                f.write(img_data)
            print(f"✅ Full-Frame Image saved: {output_path}")
            print(f"MEDIA: {Path(output_path).resolve()}")
        else:
            print(f"❌ Error: {content[:100]}...")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
