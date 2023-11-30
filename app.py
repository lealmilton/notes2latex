import streamlit as st
from src.image_processing.image_utils import convert_pdf_to_png
from src.image_processing.ocr import process_png_images
from src.text_processing.text_utils import concatenate_text_files
from src.text_processing.reasoning import create_tex
from src.pdf_generation.pdf_creator import output_pdf
import os
import tempfile
from tqdm import tqdm

st.title("Notes2LaTeX (GPT-4 powered) 🤖")

st.subheader("📝 Convert Handwritten Math to LaTeX using AI 📄")

st.write("As of now, please only upload PDFs of up to 3 pages.")

st.write("Longer files have increased error rates and take a long time to generate.")

uploaded_file = st.file_uploader("Upload your PDF (up to 3 pages)", type="pdf")

pdf_path = None

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
        tmp.write(uploaded_file.getvalue())
        pdf_path = tmp.name

    if pdf_path:
        with st.spinner("Well, it's AI. It takes time. GPUs are running somewhere. Go read a theorem and come back in a few minutes."):
            progress_bar = st.progress(0)
            # Convert PDF to PNG
            png_output_folder = convert_pdf_to_png(pdf_path)
            progress_bar.progress(20)

            # Process PNG images with OCR
            ocr_text_folder = process_png_images(png_output_folder)
            progress_bar.progress(40)

            # Concatenate text files
            combined_text_path = concatenate_text_files(ocr_text_folder)
            progress_bar.progress(60)

            # Create LaTeX from text
            tex_path = create_tex(combined_text_path)
            progress_bar.progress(80)

            # Output final PDF
            output_file_path = output_pdf(tex_path)
            progress_bar.progress(100)
        
        if tex_path:
            with open(tex_path, "r") as tex_file:
                st.download_button("Download LaTeX Source", tex_file, "raw.tex")

        if output_file_path:
            with open(output_file_path, "rb") as file:
                st.download_button("Download LaTeX PDF", file, "processed.pdf")

        os.unlink(pdf_path)

st.write("Thank you for using Notes2LaTeX!")

