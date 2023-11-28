import os
import requests
from src.image_processing.image_utils import encode_image_to_base64

api_key = os.getenv('OPENAI_API_KEY')

def send_image_to_gpt4v(image_path, prompt):
    """Sends the image to GPT-4V and retrieves the response."""
    base64_image = encode_image_to_base64(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 4000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()