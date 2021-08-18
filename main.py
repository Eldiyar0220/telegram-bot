import telebot
import random

from telebot import types
from key import key

bot = telebot.TeleBot(key)

button = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('Да', callback_data='Yes')
btn2 = types.InlineKeyboardButton('Нет', callback_data='No')
button.add(btn1,btn2)

round = 3
count = 0

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Привет! меня зовут Эльдияр, сможешь победить меня?! поиграем?", reply_markup=button )


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'Yes':
        chat_id = c.message.chat.id
        bot.send_message(chat_id, 'хорошо у нас будет 3 раунда Для начала игры пишите /play')
    elif c.data == 'No':
        chat_id = c.message.chat.id
        bot.send_message(chat_id, 'ну ладно! если что я тут и готов победить тебя!!!!')

@bot.message_handler(commands=['play'])
def game_start(message):
    # Build keyboard
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Ножницы')
    btn2 = types.KeyboardButton('Бумага')
    btn3 = types.KeyboardButton('Бумага')
    keyboard.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Камень, ножницы, бумага, раз, два, три!!! Выберите жест->', reply_markup=keyboard,)


@bot.message_handler(content_types=['text'])
def game(message):
    choice = random.choice(['Камень', 'Ножницы', 'Бумага'])
    if message.text == choice:
        bot.send_message(message.chat.id, 'ничья! Для начала новой игры пишите /play')
    else:
        if message.text == 'Ножницы':
            if choice == 'Бумага':
                bot.send_message(message.chat.id,'Поздравляю ты победил! У меня была {}. Для начала новой игры пишите /play для выхода из игры /exit'.format(choice))
            else:
                bot.send_message(message.chat.id,'Извените, но Вы проиграли. У меня был(и/a) {}. Для начала новой игры пишите /play для выхода из игры /exit'.format(choice))
        elif message.text == 'Камень':
            if choice == 'Ножницы':
                bot.send_message(message.chat.id,'Поздравляю с победой! У меня была {}. Для начала новой игры пишите /play для выхода из игры /exit'.format(choice))
            else:
                bot.send_message(message.chat.id,'Извените, но Вы проиграли. У меня был(и/a) {}. Для начала новой игры пишите /play для выхода из игры /exit'.format(choice))
        elif message.text == 'Бумага':
            if choice == 'Камень':
                bot.send_message(message.chat.id,'Поздравляю с победой! У меня была {}. Для начала новой игры пишите /play для выхода из игры /exit'.format(choice))
            else:
                bot.send_message(message.chat.id,'Извените, но Вы проиграли. У меня был(и/a) {}. Для начала новой игры пишите /play | для выхода из игры /exit'.format(choice))


@bot.message_handler(commands=['/exit'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Пока!!")

if __name__ == '__main__':
    bot.infinity_polling()