import json
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Gemini API key
genai.configure(api_key="AIzaSyCusRWxXMju-lZx0tw2nfUXuYjq5Xk3Dw4")

# Load memory
with open("memory.json", "r") as f:
    brain = json.load(f)

model = genai.GenerativeModel("gemini-2.5-flash")

# Reply function
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    prompt = f"""
You are {brain['name']}.
Personality: {brain['personality']}
Creator: {brain['creator']}

User message: {user_message}

Reply like a smart AI assistant.
"""

    response = model.generate_content(prompt)

    await update.message.reply_text(response.text)

# Main function
def main():
    TELEGRAM_TOKEN = "8031656712:AAGJBxJqliV7KskwUUZQcYDU2gf1Fv8g6W8"

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Mr Bear AI is running with Gemini...")
    app.run_polling()

if __name__ == "__main__":
    main()
