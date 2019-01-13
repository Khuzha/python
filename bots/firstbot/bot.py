import telebot
from telebot import types

bot = telebot.TeleBot("715496484:AAH3wjf4NBntcXUOW_yhtSCnBjsKaHY3ST8")

@bot.message_handler(commands=['start'])
def reply(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add('a', 'b')


    bot.send_message(message.from_user.id, 'hi', reply_markup=markup)
    # print(message)


bot.polling()