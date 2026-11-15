import os
from dotenv import load_dotenv

from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

MODEL = "gemini-3.5-flash"


response = client.models.generate_content(
    model=MODEL,
    contents="Explain AI agents in one line."
)

print(response.text)
