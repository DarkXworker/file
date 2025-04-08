
import telebot

BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm alive and running on Railway!")

print("Bot is running...")
bot.infinity_polling()
