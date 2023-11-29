import streamlit as st
from src.image_processing.image_utils import convert_pdf_to_png
from src.image_processing.ocr import process_png_images
from src.text_processing.text_utils import concatenate_text_files
from src.text_processing.reasoning import create_tex
from src.pdf_generation.pdf_creator import output_pdf
import os
import tempfile

# Set up the title of the app
st.title("📚 Notes2LaTeX - Ugly Handwritten Math to Pretty PDF! 📝")

# Add a fun description
st.write("Transform your chaotic, coffee-stained notes into a beautifully formatted LaTeX PDF. It's like magic, but with more math! 🧙‍♂️✨")

# File uploader allows the user to upload a PDF
uploaded_file = st.file_uploader("📤 Upload your handwritten equations (in PDF, please!) 📄", type="pdf")

# Initialize the pdf_path variable
pdf_path = None

# When the user uploads a file, process it
if uploaded_file is not None:
    # Display a loading message with a math joke
    st.info("Uploading your PDF... Hang tight! (Did you hear about the mathematician who’s afraid of negative numbers? He'll stop at nothing to avoid them! 😄)")

    # Save the uploaded PDF to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
        tmp.write(uploaded_file.getvalue())
        pdf_path = tmp.name

# Check if a PDF file has been uploaded and processed
if pdf_path is not None:
    # Convert PDF to PNGs and get the png_output_folder path
    png_output_folder = convert_pdf_to_png(pdf_path)
    st.success("PDF transformed into images! (Unlike Pi, this process has an end. 🥧)")

    # Process the PNG images and extract text
    ocr_text_folder = process_png_images(png_output_folder)
    st.success("Text extracted! (Fun fact: parallel lines have so much in common. It’s a shame they’ll never meet. 📏)")

    # Concatenate text files
    combined_text_path = concatenate_text_files(ocr_text_folder)
    st.success("Text concatenated! (Remember, algebra is about finding the x. Don’t ask y! 🤣)")

    # Create tex file
    tex_path = create_tex(combined_text_path)
    st.success("TeX file ready! (Do you know why seven ate nine? Because you’re supposed to eat three squared meals a day!)")

    # Output PDF using the tex file
    output_file_path = output_pdf(tex_path)
    st.success("PDF is ready! (Calculators, the only place where division and multiplication are the same thing. 🧮)")

    # Display a link to download the processed PDF
    if output_file_path:
        with open(output_file_path, "rb") as file:
            btn = st.download_button(
                label="📥 Download Your LaTeX-ified PDF 📄",
                data=file,
                file_name="processed.pdf",
                mime="application/octet-stream"
            )

    # Clean up temporary files if needed
    os.unlink(pdf_path)  # Remove the temporary PDF file

st.write("Thank you for using Notes2LaTeX! Spread the word and help fellow mathematicians turn their chaos into order! 🌟")
