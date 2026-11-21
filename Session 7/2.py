# task : translater
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-3.5-flash-lite"

topic = input("What you want to translate:")

prompt = f"Translate {topic} in URDU language"

response = client.models.generate_content(model=MODEL, contents=prompt)

print(response.text)
