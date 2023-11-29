import os
from config import BASE_DATA_PATH, BASE_PROCESSED_PATH, POPPLER_PATH, TOKEN_THRESHOLD
import tiktoken
from src.utils.prompts import PROMPT_OCR, PREVIOUS_NOTES_CONTEXT_OCR, FIRST_PAGE_CONTEXT_OCR

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
    
def save_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def count_tokens(string: str, encoding_name: str = "cl100k_base"):

    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def get_previous_description(ocr_text_folder, current_file_index):
    """Retrieves the previous description from the OCR text files."""
    previous_file_index = current_file_index - 1
    if previous_file_index > 0:
        previous_file_name = f"{previous_file_index}.txt"
        previous_file_path = os.path.join(ocr_text_folder, previous_file_name)
        if os.path.exists(previous_file_path):
            with open(previous_file_path, 'r', encoding='utf-8') as file:
                return file.read()
    return ""


def create_prompt_with_previous_description(previous_description: str) -> str:
    """Cria um prompt para o GPT-4V que inclui a descrição da página anterior ou lida com o início das anotações."""
    context = PREVIOUS_NOTES_CONTEXT_OCR.format(previous_description=previous_description) if previous_description else FIRST_PAGE_CONTEXT_OCR
    return PROMPT_OCR.format(context=context)


def concatenate_text_files(ocr_text_folder):
    # Ensure the folder exists
    if not os.path.exists(ocr_text_folder):
        print(f"The specified folder '{ocr_text_folder}' does not exist.")
        return None  # Return None if the folder doesn't exist

    # Custom sort key to sort by the numerical value in the file name
    def sort_key(filename):
        # Extract the number from the filename and convert to integer
        return int(filename.split('.')[0])

    # Get all .txt files in the folder and sort them using the custom key
    txt_files = sorted([f for f in os.listdir(ocr_text_folder) if f.endswith('.txt')], key=sort_key)

    # Check if there are any text files to concatenate
    if not txt_files:
        print("No text files found in the folder.")
        return None  # Return None if no text files are found

    # Concatenate the contents of each file
    concatenated_text = ''
    for file in txt_files:
        file_path = os.path.join(ocr_text_folder, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            concatenated_text += f.read() + '\n'  # Add a newline character between files for clarity

    base_directory = os.path.normpath(os.path.dirname(os.path.dirname(ocr_text_folder)))

    # Define the output file path for the combined text
    output_file_path = os.path.join(base_directory, 'combined_text.txt')

    # Write the concatenated text to the output file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(concatenated_text)

    print(f"All text files have been concatenated into '{output_file_path}'.")
    
    # Return the path to the combined text file
    return output_file_path


def clean_and_overwrite_latex_file(file_path):
    unwanted_start = "```latex"
    unwanted_end = "```"

    content = read_file(file_path)

    # Strip off the unwanted markdown from the start and end of the LaTeX content
    if content.startswith(unwanted_start):
        content = content[len(unwanted_start):].strip()
    if content.endswith(unwanted_end):
        content = content[:-len(unwanted_end)].strip()

    save_to_file(file_path, content)
    return content


