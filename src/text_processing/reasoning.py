import os
from config import BASE_DATA_PATH, BASE_PROCESSED_PATH, POPPLER_PATH, TOKEN_THRESHOLD
from openai import OpenAI

from src.text_processing.text_utils import read_file, save_to_file
from src.utils.prompts import PROMPT_CHECK_LATEX
from src.text_processing.text_utils import count_tokens, read_file, save_to_file
from src.utils.prompts import PROMPT_MD

api_key = os.getenv('OPENAI_API_KEY')

def gpt4_completion(context, file_content, prompt):
    client = OpenAI()  # Initialize the OpenAI client
    full_prompt = context + file_content + "\n\n" + prompt
    completion = client.chat.completions.create(
        model="gpt-4-1106-preview", 
        messages=[
            {"role": "system", "content": "You are a math editor."},
            {"role": "user", "content": full_prompt}
        ],
        max_tokens=4096,
    )
    return completion.choices[0].message.content


def check_and_correct_latex(input_file_path, error_message):
    file_content = read_file(input_file_path)
    error_context = f"LaTeX error detected: {error_message}\n\n"
    full_prompt = PROMPT_CHECK_LATEX + error_context
    corrected_content = gpt4_completion("", file_content, full_prompt)
    save_to_file(input_file_path, corrected_content)


def create_tex(file_name):

    input_file_path = os.path.join(BASE_PROCESSED_PATH, file_name, 'combined_text.txt')

    # Generate the output file path based on the file name
    output_file_path = os.path.join(BASE_PROCESSED_PATH, file_name, 'formatted_notes.tex')

    # Read the file content
    file_content = read_file(input_file_path)
    
    # Count the number of tokens in the file content
    total_tokens = count_tokens(file_content)
    print("TOTAL TOKENS:", total_tokens)

    # Process the content if the token count is within the threshold
    if total_tokens <= TOKEN_THRESHOLD:
        response = gpt4_completion("", file_content, PROMPT_MD)
        save_to_file(output_file_path, response)
        print(f"Formatted notes saved to {output_file_path}")
    else:
        print("File is too large. Try with a smaller one.")