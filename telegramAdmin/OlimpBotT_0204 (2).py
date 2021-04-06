import telebot  # импортируем библиотеки
import sqlite3
import datetime
from telebot import types

bot = telebot.TeleBot('1537716401:AAHYstpS7vejzbL5UkL5iahWfW7-4KxqBL8')

name = ''
surname = ''
level = 0


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # Клавиатура
    bot.reply_to(
        message, "Чтобы начать напиши '/reg', если планируешь регистрироваться и '/noreg', если не будешь  ")  # вступительное сообщение


@bot.message_handler(commands=['reg'])  # процесс регистрации
def send_registration(message):
    bot.send_message(message.from_user.id,
                     "Привет! Давай познакомимся! Как тебя зовут?")
    bot.register_next_step_handler(message, reg_name)  # получаем имя


def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, reg_surname)  # получаем фамилию


def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "В каком ты классе?")
    bot.register_next_step_handler(
        message, reg_level)  # получаем класс ученика


def reg_level(message):
    global level
    while level == 0:
        try:
            level = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Вводите цифрами!")
            # проверка на правильно введение
            bot.register_next_step_handler(message, reg_level)

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Ты в ' + str(level) + \
        ' классе? И тебя зовут: ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text=question,
                     reply_markup=keyboard)  # уточняем верны ли данные пользователя


@bot.callback_query_handler(lambda query: query.data in ["yes", "no"])
def callback_worker(query):
    try:
        if query.data == "yes":
            bot.send_message(
                query.message.chat.id, "Приятно познакомиться! Для продолжения нажми '/continue')")
            # Не команда, а авто переход
        elif query.data == "no":
            # повторное введение данных
            bot.send_message(query.message.chat.id, "Попробуем еще раз!")
            bot.send_message(query.message.chat.id,
                             "Привет! Давай познакомимся! Как тебя зовут?")
            bot.register_next_step_handler(query.message, reg_name)
    except Exception as e:
        print(repr(e))


@bot.message_handler(commands=['continue'])
def inline_key(a):
    mainmenu = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Физика', callback_data='key1')
    key2 = types.InlineKeyboardButton(text='Информатика', callback_data='key2')
    key8 = types.InlineKeyboardButton(text='Математика', callback_data='key8')
    mainmenu.add(key1, key2, key8)
    bot.send_message(a.chat.id, 'Выбери направление',
                     reply_markup=mainmenu)  # выбор направлений

    next_menu = types.InlineKeyboardMarkup()
    key3 = types.InlineKeyboardButton(text='1', callback_data='key3')
    key5 = types.InlineKeyboardButton(text='2', callback_data='key5')
    key6 = types.InlineKeyboardButton(text='3', callback_data='key6')
    next_menu.add(key3, key5, key6)
    bot.send_message(a.chat.id, 'Выбери уровень:', reply_markup=next_menu)


# после выбора направления кнопки сменяются кнопками выбора уровней
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    con = sqlite3.connect('olimpbotic.db', check_same_thread=False)
    cur = con.cursor()
    cur.execute('')
    con.commit()
    if call.data == "key1":
        if call.data == "key3":
            bot.send_message(call.message.chat.id, "Олимпиада школьников «Физтех»")
            bot.send_message(call.message.chat.id, "Олимпиада «Росатом»")
        elif call.data =="key5":
            bot.send_message(call.message.chat.id, "«Покори Воробьевы горы!»")

    # elif call.data == "key5":
    #     bot.send_message(call.message.chat.id, "Олимпиада «Высшая проба»")
    #     bot.send_message(call.message.chat.id,
    #                      "Всесибирская олимпиада школьников")
    #     bot.send_message(call.message.chat.id,
    #                      "Олимпиада школьников «Ломоносов»")
    #     bot.send_message(call.message.chat.id,
    #                      "Олимпиада по программированию «ТехноКубок»")


@bot.message_handler(commands=['noreg'])  # единоразовое пользование
def send_noreg(message):
    bot.reply_to(message, "В каком ты классе? ")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text in ['6', '7', '8', '9', '10', '11']:
        # для продолжения возвращаемся к команде 'continue'
        bot.send_message(message.from_user.id,
                         "Принял, нажми '/continue', чтобы продолжить")
    else:
        bot.send_message(message.from_user.id,
                         "Я тебя не понимаю. Напиши /help.")


# в случае введения команды, которую бот не может распознать
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, " Извини, я не понял твою команду(")



@bot.message_handler(commands=['admin'])
def addsubject(message):
    # если ID пользователя совпадает с перечнем идентификаторов администраторов, то перейте в режим администрирования
        bot.register_next_step_handler(query.message, admin_mode)
    #
    # mainmenu = types.InlineKeyboardMarkup()
    # key1 = types.InlineKeyboardButton(text='Физика', callback_data='key1')
    # key2 = types.InlineKeyboardButton(text='Информатика', callback_data='key2')
    # key8 = types.InlineKeyboardButton(text='Математика', callback_data='key8')
    # mainmenu.add(key1, key2, key8)
    # bot.send_message(a.chat.id, 'Выбери направление',
    #                  reply_markup=mainmenu)  # выбор направлений
    #
    # next_menu = types.InlineKeyboardMarkup()
    # key3 = types.InlineKeyboardButton(text='1', callback_data='key3')
    # key5 = types.InlineKeyboardButton(text='2', callback_data='key5')
    # key6 = types.InlineKeyboardButton(text='3', callback_data='key6')
    # next_menu.add(key3, key5, key6)
    # bot.send_message(a.chat.id, 'Выбери уровень:', reply_markup=next_menu)

#def reg_name(message):
    # global name
    # name = message.text
    # bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
    # bot.register_next_step_handler(message, reg_surname)  # получаем фамилию


# спрашивавет у бота не пришли ли ему новые сообщения
bot.polling(none_stop=True, interval=0)
