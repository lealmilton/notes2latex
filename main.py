from src.image_processing import ocr, image_utils
from src.text_processing import text_formatter, reasoning
from src.pdf_generation import pdf_creator
from utils import file_handler

def main():
    pdf_path = 'path/to/your/pdf'  # Define the path to your PDF

    # Step 1: Convert PDF to Images
    images = image_utils.convert_pdf_to_images(pdf_path)

    # Step 2: Extract Text from Images
    texts = ocr.extract_text_from_images(images)

    # Step 3: Format and Structure Text
    formatted_text = text_formatter.format_text(texts)
    structured_text = reasoning.structure_text(formatted_text)

    # Step 4: Generate LaTeX PDF
    pdf_creator.create_pdf(structured_text)

if __name__ == "__main__":
    main()
