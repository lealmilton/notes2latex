from typing import Final

PREVIOUS_NOTES_CONTEXT_OCR: Final = "Based on the previous notes provided, which are: '{previous_description}',"


FIRST_PAGE_CONTEXT_OCR: Final = "Seems to be the first page of handwritten notes, with no previous content for reference."

PROMPT_OCR: Final = ("{context} you will now receive an image of handwritten notes from a Mathematics course. After the text, an image will follow. Your task is to process this image in two parts:\n\n##OBSERVATIONS##\nProvide general considerations about the content in the image. Describe any graphs, drawings, or elements that are not clearly distinguishable. Include your understanding of the content's context, especially if it relates to or contrasts with any previous notes. Mention anything that might be omitted during the transcription.\n\n##ACTUAL TRANSCRIPTION##\nTranscribe all visible content in the image. Convert all mathematical expressions and equations to the proper LaTeX format always using $ sign. Never use the \[ mode for math mode. Include every piece of text, ensuring that the transcription is as accurate and complete as possible.")

PROMPT_MD: Final = ("As a Math editor, your task is to transform the input into a well-written, mathematically rigorous LaTeX document. The input originates from handwritten notes. Incorporate all the information present in the input. Add relevant titles and subtitles to enhance the structure. Carefully review and correct any LaTeX errors to ensure accuracy and avoid issues like 'Package amsmath Error: \dot allowed only in math mode'. The final document should be clean, in English, and properly formatted for a .tex file, consistently using LaTeX math mode ($). It's crucial that your output consists exclusively of pure LaTeX code, starting with \documentclass{}, and should not include any markdown or other syntax like ```latex or ```. Focus on delivering a ready-to-compile LaTeX document. Don't use Markdown. You should include all Math that is coming from the input, absolutely every single equation. Don't miss any")

PROMPT_CHECK_LATEX: Final = ("Review the content to identify and correct any LaTeX syntax errors. Return only the original text with the applied corrections. Ensure the accuracy of your work, focusing exclusively on LaTeX corrections in the provided text.")
