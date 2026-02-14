import telebot
import google.generativeai as genai

# TOKENS
TELEGRAM_TOKEN = "8031656712:AAGJBxJqliV7KskwUUZQcYDU2gf1Fv8g6W8"
GEMINI_API_KEY = "AIzaSyCusRWxXMju-lZx0tw2nfUXuYjq5Xk3Dw4"

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# Create bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def reply(message):
    try:
        user_text = message.text
        response = model.generate_content(user_text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Error: " + str(e))

print("Bot started...")

bot.infinity_polling()
