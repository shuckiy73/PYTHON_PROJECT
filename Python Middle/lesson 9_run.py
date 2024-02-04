# pip install pyTelegramBotAPI
# https://t.me/BotFather

import telebot
import lesson_9_game_logic

bot = telebot.TeleBot("6650515366:AAFoySxqf22C8um8T8WOZynsxa6Fhmjv35I")
CURRENT_PLAYER = ['X']


@bot.message_handler(commands=['start'])
def start_game(message):
	lesson_9_game_logic.clear_data()
	bot.send_message(message.chat.id, f'Новая игра началась')
	bot.send_message(message.chat.id, lesson_9_game_logic.print_game_field())
	bot.send_message(message.chat.id, f'Ваш ход: {CURRENT_PLAYER[0]}')


@bot.message_handler(content_types=['text'])
def start_game(message):
	bot.send_message(
		message.chat.id,
		lesson_9_game_logic.input_value(message.text, CURRENT_PLAYER[0])
	)
	if lesson_9_game_logic.check_is_game_end() == lesson_9_game_logic.STATUS_CONTINUE:
		bot.send_message(
			message.chat.id,
			lesson_9_game_logic.print_game_field()
		)
		if CURRENT_PLAYER[0] == 'X':
			CURRENT_PLAYER[0] = 'O'
		else:
			CURRENT_PLAYER[0] = 'X'
		bot.send_message(
			message.chat.id,
			f'Сейчас ходит: {CURRENT_PLAYER[0]}'
		)
	else:
		bot.send_message(message.chat.id, f'Игра закончена, победа: {lesson_9_game_logic.check_is_game_end()}')


bot.infinity_polling()
