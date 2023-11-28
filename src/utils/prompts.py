from typing import Final

PREVIOUS_NOTES_CONTEXT_OCR: Final = "Baseado nas notas anteriores fornecidas, que são: '{previous_description}',"

FIRST_PAGE_CONTEXT_OCR: Final = "Parece ser a primeira página de anotações manuscritas, sem conteúdo anterior para referência."

#PROMPT_OCR: Final = ("{context} você agora receberá uma imagem de anotações manuscritas de um curso de Matemática. Após o texto, seguirá uma imagem. Sua tarefa é processar esta imagem em duas partes:\n\n##OBSERVAÇÕES##\nForneça considerações gerais sobre o conteúdo na imagem. Descreva quaisquer gráficos, desenhos ou elementos que não estejam claramente distinguíveis. Inclua sua compreensão do contexto do conteúdo, especialmente se ele se relacionar ou contrastar com quaisquer notas anteriores. Mencione qualquer coisa que possa ser omitida durante a transcrição.\n\n##TRANSCRIÇÃO EFETIVA##\nTranscreva todo o conteúdo visível da imagem. Converta todas as expressões matemáticas e equações para o formato LaTeX adequado utilizando sempre $ sign. Nunca utilize o modo \[ para o modo matemático. Inclua cada pedaço de texto, garantindo que a transcrição seja o mais precisa e completa possível.")
#
#
PROMPT_OCR: Final = ("{context} você agora receberá uma imagem de anotações manuscritas de um curso de Matemática. Após o texto, seguirá uma imagem. Sua tarefa é processar esta imagem em duas partes:\n\n##OBSERVAÇÕES##\nForneça considerações gerais sobre o conteúdo na imagem. Descreva quaisquer gráficos, desenhos ou elementos que não estejam claramente distinguíveis. Inclua sua compreensão do contexto do conteúdo, especialmente se ele se relacionar ou contrastar com quaisquer notas anteriores. Mencione qualquer coisa que possa ser omitida durante a transcrição.\n\n##TRANSCRIÇÃO EFETIVA##\nTranscreva todo o conteúdo visível da imagem. Converta todas as expressões matemáticas e equações para o formato LaTeX adequado utilizando sempre $ sign. Nunca utilize o modo \[ para o modo matemático. Inclua cada pedaço de texto, garantindo que a transcrição seja o mais precisa e completa possível.")


#PROMPT_MD: Final = ("Traduza as anotações de aula originais para o inglês, mantendo total fidelidade ao conteúdo. Apresente o resultado em Markdown, integrando código LaTeX onde necessário. Não inclua '```markdown' no início. Adicione títulos e subtítulos relevantes. Revise o trabalho para corrigir quaisquer erros de LaTeX, garantindo que não haja erros. O texto final deve ser limpo, em inglês, e formatado em Markdown, utilizando o modo matemático (math mode) do LaTeX. Evite erros como: 'Package amsmath Error: \dot allowed only in math mode."
#
#)


PROMPT_MD: Final = ("Traduza as anotações de aula originais para o inglês, mantendo total fidelidade ao conteúdo. Apresente o resultado em LaTeX. Adicione títulos e subtítulos relevantes. Revise o trabalho para corrigir quaisquer erros de LaTeX, garantindo que não haja erros. O texto final deve ser limpo, em inglês, e formatado em um arquivo .tex, utilizando o modo matemático (math mode) do LaTeX ($). Evite erros como: 'Package amsmath Error: \dot allowed only in math mode. Certifique-se de retornar somente o conteúdo entre ```latex e ```"

)

PROMPT_CHECK_LATEX: Final = ("Revise o conteúdo para identificar e corrigir quaisquer erros de sintaxe LaTeX. Retorne apenas o texto original com as correções aplicadas. Garanta a precisão do seu trabalho, focando exclusivamente nas correções de LaTeX no texto fornecido."

)
