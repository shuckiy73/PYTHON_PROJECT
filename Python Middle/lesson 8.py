# pip install pyTelegramBotAPI
# https://t.me/BotFather

import telebot

bot = telebot.TeleBot("6650515366:AAFoySxqf22C8um8T8WOZynsxa6Fhmjv35I")

@bot.message_handler(content_types=['text'])

def answer(message):
  bot.send_message(message.chat.id, f'Ты написал мне: {message.text}')

bot.infinity_polling()
