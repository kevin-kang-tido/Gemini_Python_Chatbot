import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is loaded
if not api_key:
    raise ValueError("API key not found. Make sure it's set in the .env file.")

# Configure Gemini
genai.configure(api_key=api_key)

# Create Gemini-Pro chat model with history support
model = genai.GenerativeModel(model_name="gemini-2.0-flash")
chat = model.start_chat(history=[])

print("🤖 Gemini Chatbot (type 'exit' or 'bye' to quit)")

# Simple loop for chat
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit" , 'bye'] : 
        break

    try:
        response = chat.send_message(user_input)
        print("Gemini:", response.text)
    except Exception as e: 
        print("⚠ Error:",e)
