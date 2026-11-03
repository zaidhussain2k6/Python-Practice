from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

client = genai.Client(api_key=api_key)

while True:
    question = input("Enter your prompt: ")
    if question.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=question,
    )

    print("Response:", response.text)