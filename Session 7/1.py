# task : explain like i am 10
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-flash-lite"

topic = input("Enter a topic to explain like you are 10: ")

prompt = f"Explain {topic} like I am 10 years old in exactly 3 short lines, and in simple words."

response = client.models.generate_content(model=MODEL, contents=prompt)

print(response.text)
