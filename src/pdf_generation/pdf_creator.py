from config import BASE_PROCESSED_PATH
import subprocess
import os
import streamlit as t
from src.text_processing.text_utils import clean_and_overwrite_latex_file
from src.text_processing.reasoning import check_and_correct_latex

    
def convert_tex_to_pdf(input_file_path, output_file_path, error_context=""):
    try:
        command = f"pdflatex -output-directory={os.path.dirname(output_file_path)} {input_file_path}"
        subprocess.run(command, check=True, shell=True)
        print(f"PDF successfully created at {output_file_path}")
        return True, None
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False, str(e)

def output_pdf(tex_file_path):

    output_pdf_file = os.path.splitext(tex_file_path)[0] + '.pdf'

    clean_and_overwrite_latex_file(tex_file_path)

    # Attempt LaTeX to PDF conversion with error correction
    max_attempts = 3
    for attempt in range(max_attempts):
        success, error_message = convert_tex_to_pdf(tex_file_path, output_pdf_file)
        if success:
            print("PDF generated successfully.")
            return output_pdf_file 
        print(f"Attempt {attempt+1}: Correcting LaTeX errors...")
        check_and_correct_latex(tex_file_path, error_message)
        clean_and_overwrite_latex_file(tex_file_path)

    if not success:
        print("Failed to generate PDF after multiple attempts.")
        return None