import os
import requests
import time
from src.image_processing.image_utils import encode_image_to_base64
from src.text_processing.text_utils import get_previous_description
from src.utils.prompts import create_prompt_with_previous_description

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


def process_png_images(folder_path, output_folder):
    """Processes all PNG images in the specified folder and saves the extracted text."""
    files = os.listdir(folder_path)
    png_files = [file for file in files if file.endswith('.png')]
    png_files_sorted = sorted(png_files, key=lambda x: int(x.split('.')[0]))

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_index, file in enumerate(png_files_sorted, start=1):
        image_path = os.path.join(folder_path, file)
        print(image_path)
        #break
        previous_description = get_previous_description(output_folder, file_index)
        prompt = create_prompt_with_previous_description(previous_description)
        response = send_image_to_gpt4v(image_path, prompt)
        time.sleep(15)
        
        extracted_text = response.get('choices', [{}])[0].get('message', {}).get('content', 'No text found')
        output_file_path = os.path.join(output_folder, file.replace('.png', '.txt'))
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(extracted_text)

        print(f"Processed and saved OCR text for: {file}")