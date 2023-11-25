# Notes2LaTeX Project

Ugly math hand notes --> pretty Latex

## Overview
The Notes2LaTeX project is designed to convert handwritten notes into formatted LaTeX PDF documents. This process involves extracting text and graphical elements from images, post-processing and structuring the content using GPT-4, and finally, generating a LaTeX PDF document with the formatted content.

## Project Structure

### `/data`
- `/images`: This directory holds the uploaded images of handwritten notes that need to be processed.
- `/processed`: After the images are processed, the extracted text and graphics are stored here before being converted into a PDF.

### `/notebooks`
- Jupyter notebooks used for prototyping and testing the algorithms before integrating them into the main application.

### `/src`
Contains all the source code organized into modules by functionality.

#### `/image_processing`
- `ocr.py`: Interfaces with GPT-4V to extract text from images of handwritten notes.
- `image_utils.py`: Provides utility functions for image preprocessing, such as noise reduction, binarization, and image normalization.

#### `/text_processing`
- `text_formatter.py`: Formats the extracted text into a structure that is compatible with LaTeX.
- `reasoning.py`: Uses GPT-4V to perform logical structuring and reasoning to understand the flow and hierarchy of the document content.

#### `/pdf_generation`
- `pdf_creator.py`: Converts the structured document content into a LaTeX PDF document, handling layout and styling.

#### `/utils`
- `api_client.py`: Manages the API calls to the OpenAI GPT-4V service, including handling authentication and request retries.
- `file_handler.py`: Contains functions to manage file I/O operations such as reading from and writing to disk.

### `/tests`
Contains test cases for each module to ensure code reliability and correctness.

#### `/image_processing`
- Tests for `ocr.py` and `image_utils.py` ensuring that image processing outputs the correct text and graphics.

#### `/text_processing`
- Tests for `text_formatter.py` and `reasoning.py` to validate the text structure and logical content flow.

#### `/pdf_generation`
- Tests for `pdf_creator.py` to check the PDF generation and formatting.

## Usage
To use the Notes2LaTeX system, follow these steps:
1. **Upload Handwritten Notes**: Place your handwritten notes images into the `data/images` directory.
2. **Process Notes**: Run the `ocr.py` script to extract text and `image_utils.py` for image preprocessing.
3. **Generate LaTeX PDF**: Execute the `pdf_creator.py` script to convert the processed content into a LaTeX PDF.
4. **Download PDF**: The final LaTeX PDF will be available in the `data/processed` directory for download.

Examples of input images and the corresponding output PDFs are available in the `examples` directory.

If you encounter any issues, refer to the `troubleshooting.md` (to be done) guide for common problems and their solutions.

## Contributing
We welcome contributions to the Notes2LaTeX project! If you'd like to contribute, please:
- Fork the repository.
- Create a new branch for your feature or fix.
- Follow the code style guidelines provided in `CODE_STYLE.md`. (to be done)
- Write or update tests as necessary.
- Submit a pull request with a clear description of your changes.

For more detailed instructions, see the `CONTRIBUTING.md` file. (to be done)

## License
Notes2LaTeX is released under the MIT License. See the `LICENSE` file for full license text.

## Contact
For support, collaboration, or inquiries, please open an issue in the GitHub repository or contact the maintainer.


