import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в AIStore!\n\n"
        "Магазин цифровых товаров и подписок.\n"
        "Бот находится в разработке — скоро здесь появится каталог товаров."
    )

bot.infinity_polling()
