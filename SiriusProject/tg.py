import telebot
from openai import OpenAI
from telebot import types

az = ['a', 'b', 'c', 'd', "а", "б", "в", "г"]
client = OpenAI(api_key="sk-JshQXy1kBfNKeDwa5CYD9yOWoLOvr58l", base_url="https://api.proxyapi.ru/openai/v1")
TOKEN = '6767110842:AAEuBEbAfb9O1jSXUO7jGvGhff-IzTgFtbc'
comma = ['/start', '/info']
bot = telebot.TeleBot(TOKEN)
user_data = {}
numbers = []
infotext=("🤖 SolverBot - твой интеллектуальный помощник в учебе! 📚\n\n SolverBot - это бот с искусственным "
          "интеллектом, разработанный для помощи ученикам и учителям в образовательном процессе. Наш бот предлагает "
          "ряд функций, которые помогут вам эффективно учиться и преподавать:\n\n📚 Подготовка к тестам: Создавайте "
          "персонализированные тесты по различным предметам и темам.\n\n👩‍🏫 Поддержка учителей: Генерируйте "
          "уникальные задания и проверочные работы для своих учеников.\n\n🔄 Интерактивное взаимодействие: Получайте "
          "ответы на ваши вопросы и обратную связь в режиме реального времени.\n\n💬 Удобный интерфейс: Простое и "
          "интуитивно понятное взаимодействие с ботом через кнопки и текстовые команды.\n\nНе теряйте время - начните "
          "использовать SolverBot прямо сейчас и достигайте новых успехов в обучении! 🎓")
menutext = ('Пожалуйста, выбери один из вариантов:\n1.Приступить к тесту.\n2.Изменить роль.\n3.Изменить класс '
            'обучения.\n4.Обратная связь.\n5.Поделиться ботом.')
htext = ("""🚀 Начало работы:

Нажмите /start, чтобы запустить SolverBot.
Выберите свою роль: 👨‍🎓 Ученик или 👩‍🏫 Учитель.

👨‍🎓 Режим Ученика:

Пройдите увлекательный тест по выбранному предмету и теме.
Выберите предмет, тему теста и количество вопросов.
Отвечайте на вопросы, выбирая ответы кнопками. 🤔✅
Получите результаты теста.

👩‍🏫 Режим Учителя:

Создавайте увлекательные тесты и задания для своих учеников.
Выберите предмет, тему теста и укажите количество вопросов.
Ученики могут пройти созданный вами тест и получить результаты.📝

💬 Команды бота:

/start - Поехали!
/info - Узнать больше о SolverBot.
/help - Подсказки и команды.
/feedback - Дайте обратную связь!
🎓 Не теряйте время - начните использовать SolverBot прямо сейчас и достигайте новых успехов в обучении!""")


infotext1 = ("Я SolverBot - твой интеллектуальный помощник в учебе. 🤖💡\nМоя цель - помочь тебе подготовиться к "
             "самостоятельным работам и контрольным проверкам.")
keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
button1 = types.KeyboardButton("Ученик👨‍🎓")
button2 = types.KeyboardButton("Учитель👩‍🏫")
keyboard.add(button1, button2)

keyboardteach = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
button1 = types.KeyboardButton("Ещё тест🔁")
button2 = types.KeyboardButton("В меню📋")
keyboardteach.add(button1, button2)

keyboardstud = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True, one_time_keyboard=True)
button1 = types.KeyboardButton("А")
button2 = types.KeyboardButton("Б")
button3 = types.KeyboardButton("В")
button4 = types.KeyboardButton("Г")
keyboardstud.add(button1, button2, button3, button4)

keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)

keyboard2 = types.ReplyKeyboardMarkup(row_width=5, resize_keyboard=True, one_time_keyboard=True)
button1 = types.KeyboardButton("1🚀")
button2 = types.KeyboardButton("2👨‍🎓👩‍🏫")
button3 = types.KeyboardButton("3📝")
button4 = types.KeyboardButton("4💬")
button5 = types.KeyboardButton("5🌍")
keyboard2.add(button1, button2, button3, button4, button5)

keyboard3 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
keyboard4 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)


def commands(message):
    if message.text.lower() == '/start':
        bot.send_message(message.chat.id, infotext)
        bot.send_message(message.chat.id, menutext, reply_markup=keyboard2)
        bot.register_next_step_handler(message, menu_choice)
    elif message.text.lower() == '/info':
        bot.send_message(message.chat.id, htext)
        bot.send_message(message.chat.id, menutext, reply_markup=keyboard2)
        bot.register_next_step_handler(message, menu_choice)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, infotext)
    bot.send_message(message.chat.id, "Выберите свою роль: Ученик или Учитель", reply_markup=keyboard)
    bot.register_next_step_handler(message, role)


def role1(message):
    if message.text.lower() in ['ученик', 'учитель', 'учитель👩‍🏫', 'ученик👨‍🎓', '1', '2']:
        user_data[message.chat.id]['role'] = message.text.lower()
        bot.send_message(message.chat.id, menutext, reply_markup=keyboard2)
        bot.register_next_step_handler(message, menu_choice)
    else:
        bot.send_message(message.chat.id, "Нужно ввести один из вариантов: Ученик или Учитель", reply_markup=keyboard)
        bot.register_next_step_handler(message, role1)


def role(message):
    if message.text.lower() in ['ученик', 'учитель', "учитель👩‍🏫", "ученик👨‍🎓", '1', '2']:
        user_data[message.chat.id] = {'role': message.text.lower(), 'klass': None, 'subjects': [],
                                      'questions_count': [], 'tema': None, 'studansw': []}
        bot.send_message(message.chat.id, "Выберите свой класс (1-11):")
        bot.register_next_step_handler(message, klass)
    else:
        bot.send_message(message.chat.id, "Нужно ввести один из вариантов: Ученик или Учитель", reply_markup=keyboard)
        bot.register_next_step_handler(message, role)


def klass(message):
    if message.text.isdigit() and int(message.text) in range(1, 12):
        user_data[message.chat.id]['klass'] = message.text
        numbers.append(int(message.text))
        bot.send_message(message.chat.id, menutext, reply_markup=keyboard2)
        bot.register_next_step_handler(message, menu_choice)
    elif message.text in comma:
        commands(message)
    else:
        bot.send_message(message.chat.id, "Нужно ввести номер класса от 1 до 11.")
        bot.register_next_step_handler(message, klass)


"""
def key3o(subjects):
    if len(subjects) > 5:
        subjects.pop(0)
    keyboard3 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    if len(subjects) > 1:
        k = []
        for i in range(len(subjects)):
            if subjects[i] not in k:
                button = types.KeyboardButton(str(subjects[i]))
                keyboard3.add(button)
                k.append(subjects[i])
    elif len(subjects) == 1:
        button = types.KeyboardButton(str(subjects[0]))
        keyboard3.add(button)
"""


def menu_choice(message):
    if 'subjects' not in user_data[message.chat.id] or 'questions_count' not in user_data[message.chat.id]:
        user_data[message.chat.id]['subjects'] = []
        user_data[message.chat.id]['questions_count'] = []

    if message.text in ['1. Приступить к тесту', '1🚀', '1.', '1']:
        bot.send_message(message.chat.id, "Выберите предмет", reply_markup=keyboard3)
        bot.register_next_step_handler(message, handle_subject)

    elif message.text in ['2. Изменить роль', '2.', '2', '2👨‍🎓👩‍🏫']:
        bot.send_message(message.chat.id, "Выберите свою роль: Ученик или Учитель", reply_markup=keyboard)
        bot.register_next_step_handler(message, role1)

    elif message.text in ['3. Изменить класс обучения', '3', '3.', '3📝']:
        keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button = types.KeyboardButton(str(user_data[message.chat.id]['klass']))
        keyboard1.add(button)
        bot.send_message(message.chat.id, "Выберите свой класс (1-11):", reply_markup=keyboard1)
        bot.register_next_step_handler(message, klass)

    elif message.text.lower() in ['4. обратная связь', '4', '4.', 'обратная связь', '4💬']:
        text = ("Спасибо за интерес к обратной связи! Присоединяйся к нашей [приватной группе в Telegram]("
                "https://t.me/+uOWPlesQ664zOWEy), чтобы дать обратную связь, задать вопросы и обсудить предложения с "
                "другими пользователями. Вместе мы можем сделать SolverBot еще лучше! 💬🚀")
        bot.send_message(message.chat.id, text, parse_mode="Markdown")
        bot.send_message(message.chat.id, menutext, reply_markup=keyboard2)
        bot.register_next_step_handler(message, menu_choice)

    elif message.text in ['5. Поделиться ботом', '5🌍', '5', '5.']:
        bot.send_message(message.chat.id, "Благодарим за поддержку! Поделись ботом @GPT_solverbot с теми, "
                                          "кто нуждается в помощи в учебе. Совместными усилиями мы можем сделать "
                                          "обучение еще доступнее и интереснее! 💬👥")
        bot.send_message(message.chat.id, menutext, reply_markup=keyboard2)
        bot.register_next_step_handler(message, menu_choice)
    elif message.text in comma:
        commands(message)
    else:
        bot.send_message(message.chat.id, "Команда не распознана")
        bot.register_next_step_handler(message, menu_choice)


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, htext)
    bot.send_message(message.chat.id, menutext,
                     reply_markup=keyboard2)
    bot.register_next_step_handler(message, menu_choice)


"""
def key4o(questions_count):
    if len(questions_count) > 5:
        questions_count.pop(0)
    keyboard4 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    if len(questions_count) > 1:
        l = []
        for i in range(len(questions_count)-1):
            if questions_count[i] not in l:
                button = types.KeyboardButton(str(questions_count[i]))
                keyboard4.add(button)
    elif len(questions_count) == 1:
        button = types.KeyboardButton(str(questions_count[0]))
        keyboard4.add(button)
"""


def handle_subject(message):
    user_data[message.chat.id]['subjects'].append(message.text)
    bot.send_message(message.chat.id, f"Выбран предмет: {message.text}.\n Теперь введите количество вопросов:",
                     reply_markup=keyboard4)
    bot.register_next_step_handler(message, handle_questions_count)


def handle_questions_count(message):
    if message.text.isdigit() and int(message.text) > 0:
        user_data[message.chat.id]['questions_count'].append(int(message.text))
        bot.send_message(message.chat.id, f"Выбрано количество вопросов: {message.text}\nТеперь введите тему:")
        bot.register_next_step_handler(message, handle_topic)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, введите положительное целое число:")
        bot.register_next_step_handler(message, handle_questions_count)


def handle_topic(message):
    user_data[message.chat.id]['tema'] = message.text
    bot.send_message(message.chat.id, f"Выбрана тема: {message.text}.\nНачинается генерация теста. Это может занять "
                                      f"некоторое время...")
    question, answer, text1, o = AI(user_data[message.chat.id]['subjects'][-1], user_data[message.chat.id]['tema'],
                                    user_data[message.chat.id]['klass'],
                                    int(user_data[message.chat.id]['questions_count'][-1]))

    if user_data[message.chat.id]['role'] in ['учитель', 'учитель👩‍🏫', '2']:
        if len(text1) < 4095:
            bot.send_message(message.chat.id, text1, reply_markup=keyboardteach)
            bot.register_next_step_handler(message, oteach)
        else:
            while len(text1) > 4095:
                bot.send_message(message.chat.id, text1[:4095])
                text1 = text1[4095:]
            bot.send_message(message.chat.id, text1, reply_markup=keyboardteach)
            bot.register_next_step_handler(message, oteach)

    elif user_data[message.chat.id]['role'] in ['ученик', 'ученик👨‍🎓', '1']:
        c = 0
        bot.send_message(message.chat.id, question[c], reply_markup=keyboardstud)
        bot.register_next_step_handler(message, lambda msg: ostud(msg, question, answer, o, c))

    else:
        bot.send_message(message.chat.id, "ошибка")
        bot.send_message(message.chat.id, menutext,
                         reply_markup=keyboard2)
        bot.register_next_step_handler(message, menu_choice)

def ostud(message, question, answer, o, c):
    c += 1
    user_data[message.chat.id]['studansw'].append(message.text.lower())
    if c <= (int(user_data[message.chat.id]['questions_count'][-1]) - 1):
        bot.send_message(message.chat.id, question[c], reply_markup=keyboardstud)
        bot.register_next_step_handler(message, lambda msg: ostud(msg, question, answer, o, c))
    else:
        pransw = 0
        npransw = []
        for i in range(int(user_data[message.chat.id]['questions_count'][-1]) - 1):
            if user_data[message.chat.id]['studansw'][i] == answer[i]:
                pransw += 1
            else:
                npransw.append(i + 1)
        if pransw == int(user_data[message.chat.id]['questions_count'][-1]) + 1:
            bot.send_message(message.chat.id, f'Все ответы верны!', reply_markup=keyboardteach)
        else:
            npransw = ', '.join(map(str, npransw))
            bot.send_message(message.chat.id, f'Ошибки в {npransw}.\n Не забывайте, нейросеть '
                                              f'часто ошибается!')
            bot.send_message(message.chat.id, o, reply_markup=keyboardteach)
            bot.register_next_step_handler(message, ostud1)


def ostud1(message):
    if message.text in ['Ещё тест🔁', 'Ещё тест', 'ещё тест🔁', 'ещё тест', '2']:
        c = 0
        bot.send_message(message.chat.id, "Начинается генерация теста. Это может занять некоторое время...")
        question, answer, text1, o = AI(user_data[message.chat.id]['subjects'][-1], user_data[message.chat.id]['tema'],
                                        user_data[message.chat.id]['klass'],
                                        int(user_data[message.chat.id]['questions_count'][-1]))
        bot.send_message(message.chat.id, question[c], reply_markup=keyboardstud)
        bot.register_next_step_handler(message, lambda msg: ostud(msg, question, answer, o, c))
    else:
        bot.send_message(message.chat.id, menutext, reply_markup=keyboard2)
        bot.register_next_step_handler(message, menu_choice)

def oteach(message):
    if message.text in ['Ещё тест🔁', 'Ещё тест', 'ещё тест🔁', 'ещё тест', '2']:
        bot.send_message(message.chat.id, "Начинается генерация теста. Это может занять некоторое время...")
        question, answer, text1, o = AI(user_data[message.chat.id]['subjects'][-1], user_data[message.chat.id]['tema'],
                                        user_data[message.chat.id]['klass'],
                                        int(user_data[message.chat.id]['questions_count'][-1]))
        bot.send_message(message.chat.id, text1, reply_markup=keyboardteach)
        bot.register_next_step_handler(message, oteach)
    else:
        bot.send_message(message.chat.id, menutext, reply_markup=keyboard2)
        bot.register_next_step_handler(message, menu_choice)


def AI(subject, tema, numklass, kq):
    sistpromt = (f"Вы - репетитор по {subject}. Ваша цель - подготовить {numklass} класс к самостоятельной работе по "
                 f"теме {tema} при помощи создания теста из {kq} вопросов. Тесты должны быть логичными, а ответы - "
                 f"правильными.")
    userpromt = f"""Составьте тест из {kq} вопросов на тему {tema} с 4 вариантами ответа (а, б, в, г). После слов
"правильные ответы:" напишите правильные ответы для каждого вопроса. Буква в вопросе и ответе должна совпадать.
Разделение на отступы сделай как в примере.
Пример: 
1. Вопрос
а) Ответ 1 
б) Ответ 2 
в) Ответ 3 
г) Ответ 4

2. Вопрос
а) Ответ 1
б) Ответ 2
в) Ответ 3
г) Ответ 4

Правильные ответы:
1. а) Ответ 1
2. б) Ответ 2
"""

    completion = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.2,
        messages=[{"role": "system", "content": sistpromt}, {"role": "user", "content": userpromt}]
    )
    text = completion.choices[0].message.content
    return OText(text, kq)


def OText(text, kq):
    question = [''] * kq
    answer = [''] * kq
    text1 = text

    for n in range(kq):  # собираем вопросы по ячейкам массива question
        question[n] = text[:text.find("\n\n")]
        text = text[text.find("\n\n") + 2:]
    o = text
    text = text[text.find("\n") + 1:]
    text = text.lower()
    for i in range(kq):  # собираем ответы в массив answer
        text = text[text.find("."):]
        for j in text:
            if j in az:
                answer[i] = j
                break
        text = text[text.find("\n") + 1:]
    return question, answer, text1, o


bot.polling(none_stop=True)
