import os
import telebot
import google.generativeai as genai
import json

TELEGRAM_TOKEN = os.getenv("8031656712:AAGJBxJqliV7KskwUUZQcYDU2gf1Fv8g6W8")
GEMINI_API_KEY = os.getenv("AIzaSyCusRWxXMju-lZx0tw2nfUXuYjq5Xk3Dw4")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

MEMORY_FILE = "memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)

memory = load_memory()

def ask_gemini(user_id, message):
    user_memory = memory.get(str(user_id), "")

    prompt = f"""
You are Mr Bear AI created by Vishal.
User memory: {user_memory}
User message: {message}
Reply normally and helpfully.
"""

    response = model.generate_content(prompt)
    reply = response.text

    memory[str(user_id)] = message
    save_memory(memory)

    return reply


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    reply = ask_gemini(message.chat.id, message.text)
    bot.send_message(message.chat.id, reply)


print("Mr Bear AI running...")
bot.infinity_polling()
