import os
from pdf2image import convert_from_path
import base64
from config import BASE_DATA_PATH, POPPLER_PATH

def convert_pdf_to_png(file_name):
    pdf_path = file_name

    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    main_output_folder = os.path.join('../data', 'processed', base_name)
    if not os.path.exists(main_output_folder):
        os.makedirs(main_output_folder)

    png_output_folder = os.path.join(main_output_folder, 'pngs')
    if not os.path.exists(png_output_folder):
        os.makedirs(png_output_folder)

    images = convert_from_path(pdf_path)

    for i, image in enumerate(images):
        image_path = os.path.join(png_output_folder, f'{i + 1}.png')
        image.save(image_path, 'PNG')
        
    return png_output_folder


def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')