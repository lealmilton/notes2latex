import pypandoc
from config import BASE_PROCESSED_PATH
import os
import streamlit as t
from src.text_processing.text_utils import clean_and_overwrite_latex_file
from src.text_processing.reasoning import check_and_correct_latex

def convert_md_to_pdf(input_file_path, output_file_path, error_context=""):
    pypandoc.download_pandoc()  # Ensure Pandoc is available
    
    try:
        # Try converting  to PDF
        pypandoc.convert_file(input_file_path, 'pdf', outputfile=output_file_path)
        print(f"PDF successfully created at {output_file_path}")
        return True, None  # Return None for the error message when successful
    except Exception as e:
        print(f"An error occurred: {e}")
        return False, str(e)

def output_pdf(tex_file_path):


    # tex_path: ../data/processed/tmp63trzcnz/formatted_notes.tex


    output_pdf_file = os.path.splitext(tex_file_path)[0] + '.pdf'

    # Clean LaTeX file
    clean_and_overwrite_latex_file(tex_file_path)

    # Attempt LaTeX to PDF conversion with error correction
    max_attempts = 3
    for attempt in range(max_attempts):
        success, error_message = convert_md_to_pdf(tex_file_path, output_pdf_file)
        #st.write(error_message)
        if success:
            print("PDF generated successfully.")
            return output_pdf_file  # Return the path to the generated PDF
        print(f"Attempt {attempt+1}: Correcting LaTeX errors...")
        #st.write(f"Attempt {attempt+1}: Correcting LaTeX errors...")
        check_and_correct_latex(tex_file_path, error_message)
        clean_and_overwrite_latex_file(tex_file_path)

    if not success:
        print("Failed to generate PDF after multiple attempts.")
        return None