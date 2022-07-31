import os
from dotenv import load_dotenv
import telebot
from datetime import datetime

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот запущен!")


@bot.message_handler(commands=['help'])
def help(message):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    bot.send_message(message.chat.id, "Текущее время - " + current_time)


@bot.message_handler(commands=['hi'])
def hi(message):
    bot.send_message(message.chat.id, f'<b>Привет</b>, {message.from_user.first_name} {message.from_user.last_name}!', parse_mode='html')


@bot.message_handler(commands=['send_image'])
def send_image(message):
    image = open('image.jpg', 'rb')
    bot.send_photo(message.chat.id, image)


bot.polling(none_stop=True)
