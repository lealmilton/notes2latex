import pypandoc

def convert_md_to_pdf(input_file_path, output_file_path, error_context=""):
    pypandoc.download_pandoc()  # Ensure Pandoc is available
    
    try:
        # Try converting Markdown to PDF
        pypandoc.convert_file(input_file_path, 'pdf', outputfile=output_file_path)
        print(f"PDF successfully created at {output_file_path}")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False, str(e)