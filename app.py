import streamlit as st
from src.image_processing.image_utils import convert_pdf_to_png
from src.image_processing.ocr import process_png_images
from src.text_processing.text_utils import concatenate_text_files
from src.text_processing.reasoning import create_tex
from src.pdf_generation.pdf_creator import output_pdf
import os
import tempfile


st.title("📚 Notes2LaTeX - Ugly Handwritten Math to Pretty PDF! 📝")


st.write("Transform your chaotic, coffee-stained notes into a beautifully formatted LaTeX PDF. It's like magic, but with more math! 🧙‍♂️✨")


uploaded_file = st.file_uploader("📤 Upload your handwritten equations (in PDF, please!) 📄", type="pdf")


pdf_path = None


if uploaded_file is not None:
    st.info("Uploading your PDF... Hang tight! (Did you hear about the mathematician who’s afraid of negative numbers? He'll stop at nothing to avoid them! 😄)")

    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
        tmp.write(uploaded_file.getvalue())
        pdf_path = tmp.name

if pdf_path is not None:
    png_output_folder = convert_pdf_to_png(pdf_path)
    st.success("PDF transformed into images! (Unlike Pi, this process has an end. 🥧)")

    ocr_text_folder = process_png_images(png_output_folder)
    st.success("Text extracted! (Fun fact: parallel lines have so much in common. It’s a shame they’ll never meet. 📏)")

    combined_text_path = concatenate_text_files(ocr_text_folder)
    st.success("Text concatenated! (Remember, algebra is about finding the x. Don’t ask y! 🤣)")

    tex_path = create_tex(combined_text_path)
    st.success("TeX file ready! (Do you know why seven ate nine? Because you’re supposed to eat three squared meals a day!)")

    output_file_path = output_pdf(tex_path)
    st.success("PDF is ready! (Calculators, the only place where division and multiplication are the same thing. 🧮)")

    if output_file_path:
        with open(output_file_path, "rb") as file:
            btn = st.download_button(
                label="📥 Download Your LaTeX-ified PDF 📄",
                data=file,
                file_name="processed.pdf",
                mime="application/octet-stream"
            )


    os.unlink(pdf_path)
    
st.write("Thank you for using Notes2LaTeX! Spread the word and help fellow mathematicians turn their chaos into order! 🌟")
