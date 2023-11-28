import pypandoc

def convert_md_to_pdf(input_file_path, output_file_path):

    # This will download Pandoc to a location accessible by pypandoc
    pypandoc.download_pandoc()
    
    try:
        # Convert Markdown to PDF
        pypandoc.convert_file(input_file_path, 'pdf', outputfile=output_file_path)
        print(f"PDF successfully created at {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")