import os
from config import BASE_DATA_PATH, BASE_PROCESSED_PATH, POPPLER_PATH, TOKEN_THRESHOLD
import requests
import time
from src.image_processing.image_utils import encode_image_to_base64
from src.text_processing.text_utils import get_previous_description
from src.text_processing.text_utils import create_prompt_with_previous_description

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


def process_png_images(png_folder_path):
    """Processes all PNG images in the specified folder and saves the extracted text."""

    # The folder path is now directly passed to the function
    folder_path = png_folder_path
    # You need to adjust the output_folder path according to your directory structure
    ocr_text_folder = os.path.join(png_folder_path, 'ocr_text')

    files = os.listdir(folder_path)
    png_files = [file for file in files if file.endswith('.png')]
    png_files_sorted = sorted(png_files, key=lambda x: int(x.split('.')[0]))

    if not os.path.exists(ocr_text_folder):
        os.makedirs(ocr_text_folder)

    for file_index, file in enumerate(png_files_sorted, start=1):
        image_path = os.path.join(folder_path, file)
        print(image_path)
        #break
        previous_description = get_previous_description(ocr_text_folder, file_index)
        prompt = create_prompt_with_previous_description(previous_description)
        response = send_image_to_gpt4v(image_path, prompt)
        time.sleep(15)
        
        extracted_text = response.get('choices', [{}])[0].get('message', {}).get('content', 'No text found')
        output_file_path = os.path.join(ocr_text_folder, file.replace('.png', '.txt'))
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(extracted_text)

        print(f"Processed and saved OCR text for: {file}")
    
    # Return the path where all the text files were saved
    return ocr_text_folder