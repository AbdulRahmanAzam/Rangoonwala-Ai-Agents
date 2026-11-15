import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

MODEL = "gemini-3.1-flash-lite"

while True:
    try:
        ask = input("You: ").strip()
    except (EOFError, KeyboardInterrupt):
        break

    if ask.lower() == "stop":
        break
    if not ask:
        continue

    try:
        response = client.models.generate_content(model=MODEL, contents=ask)
    except Exception as e:
        print(f"Bot error: {e}")
        continue

    print("Bot: " + (response.text or "(no reply)"))
