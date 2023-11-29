from openai import OpenAI

def gpt4_completion(context, file_content, prompt):
    client = OpenAI()  # Initialize the OpenAI client
    full_prompt = context + file_content + "\n\n" + prompt
    completion = client.chat.completions.create(
        model="gpt-4-1106-preview", 
        messages=[
            {"role": "system", "content": "You are a math editor."},
            {"role": "user", "content": full_prompt}
        ],
        max_tokens=4096,
    )
    return completion.choices[0].message.content