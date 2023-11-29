from typing import Final

#PREVIOUS_NOTES_CONTEXT_OCR: Final = "Baseado nas notas anteriores fornecidas, que são: '{previous_description}',"
#
#FIRST_PAGE_CONTEXT_OCR: Final = "Parece ser a primeira página de anotações manuscritas, sem conteúdo anterior para referência."
#
##PROMPT_OCR: Final = ("{context} você agora receberá uma imagem de anotações manuscritas de um curso de Matemática. Após o texto, seguirá uma imagem. Sua tarefa é processar esta imagem em duas partes:\n\n##OBSERVAÇÕES##\nForneça considerações gerais sobre o conteúdo na imagem. Descreva quaisquer gráficos, desenhos ou elementos que não estejam claramente distinguíveis. Inclua sua compreensão do contexto do conteúdo, especialmente se ele se relacionar ou contrastar com quaisquer notas anteriores. Mencione qualquer coisa que possa ser omitida durante a transcrição.\n\n##TRANSCRIÇÃO EFETIVA##\nTranscreva todo o conteúdo visível da imagem. Converta todas as expressões matemáticas e equações para o formato LaTeX adequado utilizando sempre $ sign. Nunca utilize o modo \[ para o modo matemático. Inclua cada pedaço de texto, garantindo que a transcrição seja o mais precisa e completa possível.")
##
##
#PROMPT_OCR: Final = ("{context} você agora receberá uma imagem de anotações manuscritas de um curso de Matemática. Após o texto, seguirá uma imagem. Sua tarefa é processar esta imagem em duas partes:\n\n##OBSERVAÇÕES##\nForneça considerações gerais sobre o conteúdo na imagem. Descreva quaisquer gráficos, desenhos ou elementos que não estejam claramente distinguíveis. Inclua sua compreensão do contexto do conteúdo, especialmente se ele se relacionar ou contrastar com quaisquer notas anteriores. Mencione qualquer coisa que possa ser omitida durante a transcrição.\n\n##TRANSCRIÇÃO EFETIVA##\nTranscreva todo o conteúdo visível da imagem. Converta todas as expressões matemáticas e equações para o formato LaTeX adequado utilizando sempre $ sign. Nunca utilize o modo \[ para o modo matemático. Inclua cada pedaço de texto, garantindo que a transcrição seja o mais precisa e completa possível.")
#
#
##PROMPT_MD: Final = ("Traduza as anotações de aula originais para o inglês, mantendo total fidelidade ao conteúdo. Apresente o resultado em Markdown, integrando código LaTeX onde necessário. Não inclua '```markdown' no início. Adicione títulos e subtítulos relevantes. Revise o trabalho para corrigir quaisquer erros de LaTeX, garantindo que não haja erros. O texto final deve ser limpo, em inglês, e formatado em Markdown, utilizando o modo matemático (math mode) do LaTeX. Evite erros como: 'Package amsmath Error: \dot allowed only in math mode."
##
##)
#
#
#PROMPT_MD: Final = ("Traduza as anotações de aula originais para o inglês, mantendo total fidelidade ao conteúdo. Apresente o resultado em LaTeX. Adicione títulos e subtítulos relevantes. Revise o trabalho para corrigir quaisquer erros de LaTeX, garantindo que não haja erros. O texto final deve ser limpo, em inglês, e formatado em um arquivo .tex, utilizando o modo matemático (math mode) do LaTeX ($). Evite erros como: 'Package amsmath Error: \dot allowed only in math mode. Certifique-se de retornar somente o conteúdo entre ```latex e ```"
#
#)
#
#PROMPT_CHECK_LATEX: Final = ("Revise o conteúdo para identificar e corrigir quaisquer erros de sintaxe LaTeX. Retorne apenas o texto original com as correções aplicadas. Garanta a precisão do seu trabalho, focando exclusivamente nas correções de LaTeX no texto fornecido."
#
#)
#


from typing import Final

# Based on the previous notes provided, which are: '{previous_description}',
PREVIOUS_NOTES_CONTEXT_OCR: Final = "Based on the previous notes provided, which are: '{previous_description}',"

# Seems to be the first page of handwritten notes, with no previous content for reference.
FIRST_PAGE_CONTEXT_OCR: Final = "Seems to be the first page of handwritten notes, with no previous content for reference."

# You will now receive an image of handwritten notes from a Mathematics course. After the text, an image will follow. Your task is to process this image in two parts:
# OBSERVATIONS
# Provide general considerations about the content in the image. Describe any graphs, drawings, or elements that are not clearly distinguishable. Include your understanding of the content's context, especially if it relates to or contrasts with any previous notes. Mention anything that might be omitted during the transcription.
# ACTUAL TRANSCRIPTION
# Transcribe all visible content in the image. Convert all mathematical expressions and equations to the proper LaTeX format always using $ sign. Never use the \[ mode for math mode. Include every piece of text, ensuring that the transcription is as accurate and complete as possible.
PROMPT_OCR: Final = ("{context} you will now receive an image of handwritten notes from a Mathematics course. After the text, an image will follow. Your task is to process this image in two parts:\n\n##OBSERVATIONS##\nProvide general considerations about the content in the image. Describe any graphs, drawings, or elements that are not clearly distinguishable. Include your understanding of the content's context, especially if it relates to or contrasts with any previous notes. Mention anything that might be omitted during the transcription.\n\n##ACTUAL TRANSCRIPTION##\nTranscribe all visible content in the image. Convert all mathematical expressions and equations to the proper LaTeX format always using $ sign. Never use the \[ mode for math mode. Include every piece of text, ensuring that the transcription is as accurate and complete as possible.")

# Translate the original class notes into English, maintaining complete fidelity to the content. Present the result in LaTeX. Add relevant titles and subtitles. Review the work to correct any LaTeX errors, ensuring there are no mistakes. The final text should be clean, in English, and formatted in a .tex file, using LaTeX math mode ($). Avoid errors like: 'Package amsmath Error: \dot allowed only in math mode. Be sure to return only the content between ```latex and ```
PROMPT_MD: Final = ("As a Math editor, your task is to transform the input into a well-written, mathematically rigorous LaTeX document. The input originates from handwritten notes. Incorporate all the information present in the input. Add relevant titles and subtitles to enhance the structure. Carefully review and correct any LaTeX errors to ensure accuracy and avoid issues like 'Package amsmath Error: \dot allowed only in math mode'. The final document should be clean, in English, and properly formatted for a .tex file, consistently using LaTeX math mode ($). It's crucial that your output consists exclusively of pure LaTeX code, starting with \documentclass{}, and should not include any markdown or other syntax like ```latex or ```. Focus on delivering a ready-to-compile LaTeX document. Don't use Markdown")


# Review the content to identify and correct any LaTeX syntax errors. Return only the original text with the applied corrections. Ensure the accuracy of your work, focusing exclusively on LaTeX corrections in the provided text.
PROMPT_CHECK_LATEX: Final = ("Review the content to identify and correct any LaTeX syntax errors. Return only the original text with the applied corrections. Ensure the accuracy of your work, focusing exclusively on LaTeX corrections in the provided text.")
