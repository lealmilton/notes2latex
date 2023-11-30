import streamlit as st
from src.image_processing.image_utils import convert_pdf_to_png
from src.image_processing.ocr import process_png_images
from src.text_processing.text_utils import concatenate_text_files
from src.text_processing.reasoning import create_tex
from src.pdf_generation.pdf_creator import output_pdf
import os
import tempfile

# Initialize session state variables
if 'processing_completed' not in st.session_state:
    st.session_state['processing_completed'] = False
if 'tex_path' not in st.session_state:
    st.session_state['tex_path'] = None
if 'output_file_path' not in st.session_state:
    st.session_state['output_file_path'] = None
if 'progress_bar_active' not in st.session_state:
    st.session_state['progress_bar_active'] = False

st.title("Notes2LaTeX (GPT-4 powered) 🤖")

st.subheader("📝 Convert Handwritten Math to LaTeX using AI 📄")
st.write("As of now, please only upload PDFs of up to 3 pages.")
st.write("Longer files have increased error rates and take a long time to generate.")

# Only process new file uploads
uploaded_file = st.file_uploader("Upload your PDF (up to 3 pages)", type="pdf")
if uploaded_file is not None and not st.session_state['processing_completed']:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
        tmp.write(uploaded_file.getvalue())
        pdf_path = tmp.name

    # Create and update the progress bar
    if 'progress_bar' not in st.session_state:
        st.session_state['progress_bar'] = st.progress(0)
        st.session_state['progress_bar_active'] = True

    with st.spinner("Well, it's AI. It takes time. GPUs are running somewhere. Go read a theorem and come back soon 😂."):
        # Convert PDF to PNG
        png_output_folder = convert_pdf_to_png(pdf_path)
        st.session_state['progress_bar'].progress(25)

        # Process PNG images with OCR
        ocr_text_folder = process_png_images(png_output_folder)
        st.session_state['progress_bar'].progress(50)

        # Concatenate text files
        combined_text_path = concatenate_text_files(ocr_text_folder)
        st.session_state['progress_bar'].progress(75)

        # Create LaTeX from text
        tex_path = create_tex(combined_text_path)
        st.session_state['progress_bar'].progress(90)

        # Output final PDF
        output_file_path = output_pdf(tex_path)
        st.session_state['progress_bar'].progress(100)

        # Update session state
        st.session_state['tex_path'] = tex_path
        st.session_state['output_file_path'] = output_file_path
        st.session_state['processing_completed'] = True
        st.session_state['progress_bar_active'] = False  # Reset progress bar state

        # Clean up temporary files
        os.unlink(pdf_path)

# Display download buttons if processing is completed
if st.session_state['processing_completed']:
    st.success('Processing completed!')
    
    if st.session_state['tex_path']:
        with open(st.session_state['tex_path'], "r") as tex_file:
            st.download_button("Download LaTeX Source", tex_file.read(), "raw.tex")

    if st.session_state['output_file_path']:
        with open(st.session_state['output_file_path'], "rb") as file:
            st.download_button("Download LaTeX PDF", file.read(), "processed.pdf")

st.write("Thank you for using Notes2LaTeX!")
