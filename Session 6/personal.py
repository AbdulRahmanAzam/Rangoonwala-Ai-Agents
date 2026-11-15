import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

MODEL = "gemini-3.1-flash-lite"

config = types.GenerateContentConfig(
    system_instruction="You are a helpful funny kitten, whose work is to help people with their pets problems. Answer in 2 short lines."
)

chat = client.chats.create(model=MODEL, config=config)

history = []

while True:
    ask = input("You: ")

    if ask.lower() == "stop":
        break

    response = chat.send_message(ask)


    reply = response.text
    history.append((ask, reply))
    print("Bot: " + reply)
