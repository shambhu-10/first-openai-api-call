from dotenv import load_dotenv
load_dotenv()

import openai 
import os

############    for multi-time response (chatting)

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [{"role": "system", "content": "You are a helpful assistant."}]

print("NOTE: Enter 'exit or quit' to terminate the chat")
while True:
    
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=100
    )

    assistant_reply = response.choices[0].message.content
    token_count = response.usage.total_tokens

    print("Assistant:", assistant_reply, ("Token count:", token_count))

    messages.append({"role": "assistant", "content": assistant_reply})

