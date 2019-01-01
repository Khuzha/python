import telebot
from telebot import types

bot = telebot.TeleBot("token")

@bot.message_handler(commands=['start'])
def reply(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add('a', 'b')


    bot.send_message(message.from_user.id, 'hi', reply_markup=markup)
    # print(message)


bot.polling()