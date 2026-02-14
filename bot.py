import os
import telebot
import google.generativeai as genai

# ENV variables
TELEGRAM_TOKEN = os.getenv("AIzaSyCusRWxXMju-lZx0tw2nfUXuYjq5Xk3Dw4")
GEMINI_API_KEY = os.getenv("8031656712:AAGJBxJqliV7KskwUUZQcYDU2gf1Fv8g6W8")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# Create bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)


# Start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! Main Mr Bear AI hoon. Mujhse kuch bhi pucho.")


# Handle all messages
@bot.message_handler(func=lambda message: True)
def reply(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Error: " + str(e))


# Run bot
print("Bot is running...")
bot.infinity_polling()
