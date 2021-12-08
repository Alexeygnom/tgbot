import telebot

bot = telebot.TeleBot('5060294107:AAEmco-9d_24GT_gS9jepQ4VsxBUbKvAX5U')

COMMANDS = ['start', 'beginning1', 'beginning2', 'beginning3',
            'beginning4', 'beginning5']

@bot.message_handler(commands=['start', 'beginning1', 'beginning2', 'beginning3', 'beginning4', 'beginning5'])

def welcom(message):
    bot.reply_to(message,'Ещё один... ну привет. У меня один вопрос: ты азергиджанец?')
    #a = message.text
    #bot.reply_to(message, a)
    #bot.reply_to(message, 'Готов начать?')

#def start_message(message) -> None:







bot.polling()