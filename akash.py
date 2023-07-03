import openai
openai.api_key='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'

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]


while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat.choices[0].message.contents
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})