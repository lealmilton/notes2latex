from openai import OpenAI
from src.text_processing.text_utils import read_file, save_to_file
from src.utils.prompts import PROMPT_CHECK_LATEX

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