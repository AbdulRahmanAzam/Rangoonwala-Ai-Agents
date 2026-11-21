# Task 6: Weather stylist (API + LLM)
import requests
from google import genai

client = genai.Client(api_key="PASTE_YOUR_API_KEY_HERE")
MODEL = "gemini-2.5-flash"

# Step 1: Get Karachi's temperature from Open-Meteo
url = "https://api.open-meteo.com/v1/forecast?latitude=24.86&longitude=67.01&current=temperature_2m"
data = requests.get(url).json()
temperature = data["current"]["temperature_2m"]

print(f"Karachi temperature right njow: {temperature}°C\n")

# Step 2: Ask Gemini what to wear
prompt = f"It is {temperature}°C in Karachi today. What should I wear? Answer in 3 short lines."
response = client.models.generate_content(model=MODEL, contents=prompt)

print("Stylist says:")
print(response.text)