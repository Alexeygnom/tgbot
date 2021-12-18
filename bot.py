import telebot


bot = telebot.TeleBot('', parse_mode='html')


"""
Этот бот является итоговым проектом по дисциплине "Алгоритмизация и программирование".
Бот создан студентами группы БИБ211 Таньчев Алексеем и Тумановым Александром
"""


db = {'geo': {
    'q1': {
        'txt': 'Столица Габона?',
        'variants': ['Либревиль', 'Бисау', 'Прая', 'Масеру'],
        'good': 'Либревиль'
    },
    'q2': {
        'txt': 'Кто не является географическим соседом России?',
        'variants': ['США', 'Япония', 'Молдова', 'Норвегия'],
        'good': 'Молдова'
    },
    'q3': {
        'txt': 'В акватории какого океана находится Марианская впадина?',
        'variants': ['Атлантического', 'Тихого', 'Индийского', 'Южного'],
        'good': 'Тихого'
    },
    'q4': {
        'txt': 'Окуносима-это?',
        'variants': ['Гора', 'Остров', 'Страна', 'Город'],
        'good': 'Остров'
    },
    'q5': {
        'txt': 'Какое тёплое течение является самым мощным?',
        'variants': ['Антильское', 'Бразильское', 'Ирмингера', 'Гольфстрим'],
        'good': 'Гольфстрим'
    }
},
    'hist': {
        'q1': {
            'txt': 'В каком году крестили Русь?',
            'variants': ['998', '988', '989', '999'],
            'good': '988'
        },
        'q2': {
            'txt': 'Год начала столетней войны?',
            'variants': ['1335', '1331', '1334', '1337'],
            'good': '1337'
        },
        'q3': {
            'txt': 'В каком году началась Вторая мировая война?',
            'variants': ['1938', '1939', '1940', '1941'],
            'good': '1939'
        },
        'q4': {
            'txt': 'В каком году начался первый крестовый поход?',
            'variants': ['1096', '1097', '1196', '1197'],
            'good': '1096'
        },
        'q5': {
            'txt': 'В каком году произошло падение Западной Римской империи?',
            'variants': ['470', '476', '480', '486'],
            'good': '476'
        }
    },
    'bio': {
        'q1': {
            'txt': 'Чем водоросли отличаются от высших растений?',
            'variants': ['Размножаются с помощью гомет', 'Не имеют дифференцированных тканей', 'Цветом',
                         'Нет фотосинтеза'],
            'good': 'Не имеют дифференцированных тканей'
        },
        'q2': {
            'txt': 'На каком расстоянии большинство паукообразных способны различать предметы?',
            'variants': ['Не более 30см', 'Не более 20см', 'Более 200см', 'Более 100см'],
            'good': 'Более 30см'
        },
        'q3': {
            'txt': 'Самые быстролетающие насекомые?',
            'variants': ['Пчёлы', 'Подёнки', 'Саранча', 'Стрекозы'],
            'good': 'Стрекозы'
        },
        'q4': {
            'txt': 'Какая структура у гемоглобина белка?',
            'variants': ['Вторичная', 'Первичная', 'Четвертичная', 'Третичная'],
            'good': 'Четвертичная'
        },
        'q5': {
            'txt': 'Какая часть тела может страдать от катаракты?',
            'variants': ['Голова', 'Глаз', 'Желудок', 'Нога'],
            'good': 'Глаз'
        }
    },
    'astr': {
        'q1': {
            'txt': 'Самое большое созвездие?',
            'variants': ['Большая медведица', 'Гидра', 'Дева', 'Кит'],
            'good': 'Гидра'
        },
        'q2': {
            'txt': 'На какой планете Солнечной системы сутки длиннее года?',
            'variants': ['Нептун', 'Марс', 'Венера', 'Меркурий'],
            'good': 'Венера'
        },
        'q3': {
            'txt': 'Ближайшая точка орбиты планеты к Солнцу?',
            'variants': ['Апогей', 'Перигелий', 'Перигей', 'Апогелий'],
            'good': 'Перигелий'
        },
        'q4': {
            'txt': 'Название фазы Луны во время солнечного затмения?',
            'variants': ['Первая четверть', 'Полнолуние', 'Новолуние', 'Третья четверть'],
            'good': 'Новолуние'
        },
        'q5': {
            'txt': 'Сколько планет Солнечной системы относятся к классу ледяных гигантов?',
            'variants': ['1', '2', '3', '4'],
            'good': '2'
        }
    }
}
"""
Данный словарь является глобальной переменной. Он содержит в себе 4 ключа: 'geo', 'hist', 'bio', 'astr'.
Каждый из них содержит ещё 5 ключей: 'q1', 'q2', 'q3', 'q4', 'q5', каждый из которых содержит в себе ещё 3 ключа:
'txt' - текст вопроса
'variants' - 4 варианта ответа на этот вопрос
'good' - правильный ответ
"""


@bot.message_handler(commands=['start', 'victorina'])
def main(message):

    """
    Функция является главной и обрабатывает две команды:
    Если поступает команда "/start", бот приветствует пользователя и предлагает поучавствовать в викторине, для начала которой нужно отправить команду "/victorina"
    Если поступает команда "/victorina", бот приступает к началу викторины, вызвав функцию "ask_for_option"
    """

    if message.text == '/start':
        bot.send_message(message.chat.id, f'Ещё один... \nНу привет, <b>{message.from_user.username}</b> \nЯ проверяю твои знания вопросами по следующим темам: география, история, биология, астрономия\nДля того, чтобы начать, напиши\n/victorina')
    elif message.text == '/victorina':
        ask_for_option(message)


def ask_for_option(message):

    """
    Функция генерирует клавиатуру-кнопки для выбора темы вопросов и запускает функцию "gen_questions"
    """

    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('География', 'История')
    keyboard.row('Биология', 'Астрономия')

    bot.send_message(message.chat.id, 'Выбери тему, на вопросы которой хочешь отвечать:', reply_markup=keyboard)
    bot.register_next_step_handler(message, gen_questions)


def gen_questions(message):

    """
    Если ответ пользователя совпадает с одной из предложенных тем, то функция выводит пользователю первый вопрос из данной темы, предлагая варианты ответов на него. Затем запускает функцию "q_2"
    Если ответ пользователя не совпадает ни с одной из тем, то бот выводит сообщение о том, что пользователь отправил неверное сообщение
    """

    if 'география' in message.text.lower():
        counter = 0

        q = db['geo']['q1']

        q_txt = q['txt']
        variants = q['variants']
        answer = q['good']

        keyboard = gen_answer_keyboard(variants)
        bot.send_message(message.chat.id, f'Вы выбрали географию, и вот ваш первый вопрос:\n\n<b>{q_txt}</b>',reply_markup=keyboard)

        bot.register_next_step_handler(message, q_2, answer, counter, 'geo')

    elif 'история' in message.text.lower():
        counter = 0

        q = db['hist']['q1']

        q_txt = q['txt']
        variants = q['variants']
        answer = q['good']

        keyboard = gen_answer_keyboard(variants)
        bot.send_message(message.chat.id, f'Вы выбрали историю, и вот ваш первый вопрос:\n\n<b>{q_txt}</b>',reply_markup=keyboard)

        bot.register_next_step_handler(message, q_2, answer, counter, 'hist')

    elif 'биология' in message.text.lower():
        counter = 0

        q = db['bio']['q1']

        q_txt = q['txt']
        variants = q['variants']
        answer = q['good']

        keyboard = gen_answer_keyboard(variants)
        bot.send_message(message.chat.id, f'Вы выбрали биологию, и вот ваш первый вопрос:\n\n<b>{q_txt}</b>',reply_markup=keyboard)

        bot.register_next_step_handler(message, q_2, answer, counter, 'bio')

    elif 'астрономия' in message.text.lower():
        counter = 0

        q = db['astr']['q1']

        q_txt = q['txt']
        variants = q['variants']
        answer = q['good']

        keyboard = gen_answer_keyboard(variants)
        bot.send_message(message.chat.id, f'Вы выбрали астрономию, и вот ваш первый вопрос:\n\n<b>{q_txt}</b>',reply_markup=keyboard)

        bot.register_next_step_handler(message, q_2, answer, counter, 'astr')

    else:
        bot.send_message(message.chat.id, 'Ты че дебил? Сказали же выбрать одну из 4')


def q_2(message, right_answer, counter, chapter):

    """
    Функция проверяет ответ пользователя на правильность:
    Если ответ пользователя совпадает с правильным, то счётчик правильных ответов увеличивается на один, пользователю выводится следующий вопрос и создаётся клавиатура с вариантами ответа на него. Запускается функция "q_3"
    Если ответ пользователя не совпадает с верным, пользователю выводится следующий вопрос и предлагаются варианты ответа на него. Запускается функция "q_3"

    Функция принимает следующие парамметры:
    message - ответ пользователя на вопрос
    right_answer - правильный ответ на вопрос
    counter - счётчик правильных ответов пользователя
    chapter - тема вопросов
    """
    if str(right_answer).strip() == str(message.text).strip():
        counter += 1
        bot.send_message(message.chat.id, f'Не, ну ты реально красавчик, едем дальше')

    else:
        bot.send_message(message.chat.id, f'Ты че даун? Правильный ответ: <b>{right_answer}</b>')

    q = db[chapter]['q2']

    q_txt = q['txt']
    variants = q['variants']
    answer = q['good']

    keyboard = gen_answer_keyboard(variants)
    bot.send_message(message.chat.id, f'Лови следующий вопрос: <b>{q_txt}</b>', reply_markup=keyboard)
    bot.register_next_step_handler(message, q_3, answer, counter, chapter)


def q_3(message, right_answer, counter, chapter):

    """
    Функция проверяет ответ пользователя на правильность:
    Если ответ пользователя совпадает с правильным, то счётчик правильных ответов увеличивается на один, пользователю выводится следующий вопрос и создаётся клавиатура с вариантами ответа на него. Запускается функция "q_4"
    Если ответ пользователя не совпадает с верным, пользователю выводится следующий вопрос и предлагаются варианты ответа на него. Запускается функция "q_4"

    Функция принимает следующие парамметры:
    message - ответ пользователя на вопрос
    right_answer - правильный ответ на вопрос
    counter - счётчик правильных ответов пользователя
    chapter - тема вопросов
    """

    if str(right_answer).strip() == str(message.text).strip():
        counter += 1
        bot.send_message(message.chat.id, f'Не, ну ты реально красавчик, едем дальше')

    else:
        bot.send_message(message.chat.id, f'Ты че даун? Правильный ответ: <b>{right_answer}</b>')

    q = db[chapter]['q3']

    q_txt = q['txt']
    variants = q['variants']
    answer = q['good']

    keyboard = gen_answer_keyboard(variants)
    bot.send_message(message.chat.id, f'Лови следующий вопрос: <b>{q_txt}</b>', reply_markup=keyboard)
    bot.register_next_step_handler(message, q_4, answer, counter, chapter)


def q_4(message, right_answer, counter, chapter):

    """
    Функция проверяет ответ пользователя на правильность:
    Если ответ пользователя совпадает с правильным, то счётчик правильных ответов увеличивается на один, пользователю выводится следующий вопрос и создаётся клавиатура с вариантами ответа на него. Запускается функция "q_5"
    Если ответ пользователя не совпадает с верным, пользователю выводится следующий вопрос и предлагаются варианты ответа на него. Запускается функция "q_5"

    Функция принимает следующие парамметры:
    message - ответ пользователя на вопрос
    right_answer - правильный ответ на вопрос
    counter - счётчик правильных ответов пользователя
    chapter - тема вопросов
    """

    if str(right_answer).strip() == str(message.text).strip():
        counter += 1
        bot.send_message(message.chat.id, f'Не, ну ты реально красавчик, едем дальше')

    else:
        bot.send_message(message.chat.id, f'Ты че даун? Правильный ответ: <b>{right_answer}</b>')

    q = db[chapter]['q4']

    q_txt = q['txt']
    variants = q['variants']
    answer = q['good']

    keyboard = gen_answer_keyboard(variants)
    bot.send_message(message.chat.id, f'Лови следующий вопрос: <b>{q_txt}</b>', reply_markup=keyboard)
    bot.register_next_step_handler(message, q_5, answer, counter, chapter)


def q_5(message, right_answer, counter, chapter):

    """
    Функция проверяет ответ пользователя на правильность:
    Если ответ пользователя совпадает с правильным, то счётчик правильных ответов увеличивается на один, пользователю выводится следующий вопрос и создаётся клавиатура с вариантами ответа на него. Запускается функция "finish"
    Если ответ пользователя не совпадает с верным, пользователю выводится следующий вопрос и предлагаются варианты ответа на него. Запускается функция "finish"

    Функция принимает следующие парамметры:
    message - ответ пользователя на вопрос
    right_answer - правильный ответ на вопрос
    counter - счётчик правильных ответов пользователя
    chapter - тема вопросов
    """

    if str(right_answer).strip() == str(message.text).strip():
        counter += 1
        bot.send_message(message.chat.id, f'Не, ну ты реально красавчик')

    else:
        bot.send_message(message.chat.id, f'Ты че даун? Правильный ответ: <b>{right_answer}</b>')

    q = db[chapter]['q5']

    q_txt = q['txt']
    variants = q['variants']
    answer = q['good']

    keyboard = gen_answer_keyboard(variants)
    bot.send_message(message.chat.id, f'Лови следующий вопрос: <b>{q_txt}</b>', reply_markup=keyboard)
    bot.register_next_step_handler(message, finish, answer, counter)


def finish(message, right_answer, counter):

    """
    Функция проверяет ответ пользователя на правильность:
    Если ответ пользователя совпадает с правильным, то счётчик правильных ответов увеличивается на один
    Если ответ пользователя не совпадает с верным, то счётчик правильных ответов остаётся неизменным
    Затем бот выводит пользователю его результат (его количество правильных ответов из максимально возможного)

    Функция принимает следующие парамметры:
    message - ответ пользователя на вопрос
    right_answer - правильный ответ на вопрос
    counter - счётчик правильных ответов пользователя
    """

    if str(right_answer).strip() == str(message.text).strip():
        counter += 1
        bot.send_message(message.chat.id, f'Не, ну ты реально красавчик')

    else:
        bot.send_message(message.chat.id, f'Ты че даун? Правильный ответ: <b>{right_answer}</b>')

    bot.send_message(message.chat.id, f'Ну короче, ты крутой мужик, вот твой результат: {counter}/5. Но помни, что ты отвечал по вариантам, а так любой лох сможет. Задумайся)',reply_markup=None)


def gen_answer_keyboard(variants):

    """
    Функция генерирует клавиатуру-кнопки с вариантами ответа на каждый вопрос из выбранной темы

    Функция принимает парамметр variants, в котором содержатся 4 варианта ответа на вопрос из массива
    """
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(variants[0], variants[1])
    keyboard.row(variants[2], variants[3])

    return keyboard


bot.polling()