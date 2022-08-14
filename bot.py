import os
# from dotenv import load_dotenv
import telebot
from telebot import types

#load_dotenv()

#BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot('5547802687:AAHjoyUmsX61_psRwTG5sIJqqkqn9bGTOfc')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, message.text)


# @bot.message_handler(func=lambda message:True)
# def echo(message):
#     bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands=['menu'])
def menu(message):
    menu = types.ReplyKeyboardMarkup()

    menu_item1 = types.KeyboardButton('Анекдоты')
    menu_item2 = types.KeyboardButton('Видео Димы Ботева')
    menu_item3 = types.KeyboardButton('Сюрприз')

    menu.add(menu_item1, menu_item2, menu_item3)

    bot.send_message(message.chat.id, 'Выберите команду:', reply_markup=menu)


@bot.message_handler(regexp='Видео Димы Ботева')
def video(message):
    video = open('botev.mp4', 'rb')
    bot.send_video(message.chat.id, video)


bot.polling(none_stop=True)