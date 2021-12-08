import telebot
from telebot import types

bot = telebot.TeleBot('5060294107:AAEmco-9d_24GT_gS9jepQ4VsxBUbKvAX5U')

COMMANDS = ['start', 'beginning1', 'beginning2', 'beginning3',
            'beginning4', 'beginning5']

@bot.message_handler(commands=['start', 'beginning1', 'beginning2', 'beginning3', 'beginning4', 'beginning5'])

def welcom(message):
    bot.reply_to(message,'Ещё один... ну привет. У меня один вопрос: ты азергиджанец?')
    b = keybord1
    if b == 'Да':
        bot.reply_to(message, 'Юююю..... Окей, будешь холопом')
    if b == 'Нет':
        bot.reply_to(message, 'Отлично!')


def keybord1():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Да')
    btn2 = types.KeyboardButton('Нет')
    markup.add(btn1, btn2)
    return markup










bot.polling()