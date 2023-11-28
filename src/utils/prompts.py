

def create_prompt_with_previous_description(previous_description):
    """Cria um prompt para o GPT-4V que inclui a descrição da página anterior ou lida com o início das anotações."""
    if previous_description:
        previous_notes_context = f"Baseado nas notas anteriores fornecidas, que são: '{previous_description}',"
    else:
        previous_notes_context = "Parece ser a primeira página de anotações manuscritas, sem conteúdo anterior para referência."

    prompt = (
        f"{previous_notes_context} você agora receberá uma imagem de anotações manuscritas de um curso de Matemática. "
        f"Após o texto, seguirá uma imagem. Sua tarefa é processar esta imagem em duas partes:\n\n"
        f"##OBSERVAÇÕES##\n"
        f"Forneça considerações gerais sobre o conteúdo na imagem. Descreva quaisquer gráficos, desenhos ou elementos que não estejam claramente distinguíveis. "
        f"Inclua sua compreensão do contexto do conteúdo, especialmente se ele se relacionar ou contrastar com quaisquer notas anteriores. Mencione qualquer coisa que possa ser omitida durante a transcrição.\n\n"
        f"##TRANSCRIÇÃO EFETIVA##\n"
        f"Transcreva todo o conteúdo visível da imagem. Converta todas as expressões matemáticas e equações para o formato LaTeX adequado. "
        f"Inclua cada pedaço de texto, garantindo que a transcrição seja o mais precisa e completa possível."
    )
    return prompt