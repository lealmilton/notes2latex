import os
from pdf2image import convert_from_path
import base64
from config import BASE_DATA_PATH, POPPLER_PATH

def convert_pdf_to_png(file_name):

        # Get paths from the config
    base_data_path = BASE_DATA_PATH
    poppler_path = POPPLER_PATH

    # Construct the PDF path
    pdf_path = os.path.join(base_data_path, 'notes', f'{file_name}.pdf')

    # Extracting the base name of the PDF file to name the folder
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    # Creating the main directory inside 'data/processed/'
    main_output_folder = os.path.join('../data', 'processed', base_name)
    if not os.path.exists(main_output_folder):
        os.makedirs(main_output_folder)

    # Creating a sub-directory for PNG files
    png_output_folder = os.path.join(main_output_folder, 'pngs')
    if not os.path.exists(png_output_folder):
        os.makedirs(png_output_folder)

    # Convert PDF to a list of images
    images = convert_from_path(pdf_path, poppler_path=poppler_path)

    # Save each page as a PNG
    for i, image in enumerate(images):
        image_path = os.path.join(png_output_folder, f'{i + 1}.png')
        image.save(image_path, 'PNG')


def encode_image_to_base64(image_path):
    """Encodes the image to base64 format."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')