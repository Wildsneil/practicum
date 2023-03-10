"""Модуль с гороскоп-ботом. """

import random
from telebot import TeleBot, types

import settings

bot = TeleBot(settings.TOKEN)

first = [
    "Сегодня — идеальный день для новых начинаний.",
    "Оптимальный день для того, чтобы решиться на смелый поступок!",
    "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.",
    "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.",
    "Плодотворный день для того, чтобы разобраться с накопившимися делами."
]
second = [
    "Но помните, что даже в этом случае нужно не забывать про",
    "Если поедете за город, заранее подумайте про",
    "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
    "Если у вас упадок сил, обратите внимание на",
    "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"
]
second_add = [
    "отношения с друзьями и близкими.",
    "работу и деловые вопросы, которые могут так некстати помешать планам.",
    "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
    "бытовые вопросы — особенно те, которые вы не доделали вчера.",
    "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."
]
third = [
    "Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
    "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.",
    "Если вы не сможете уменьшить влияние ретроградного Меркурия - хотя бы доведите дела до конца.",
    "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.",
    "Если встретите незнакомца на пути — проявите участие, и встреча посулит вам приятные хлопоты."
]


def buttons(keyboard):
    """Добавляет кнопки со знаками. """

    signs = ["Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева", "Весы",
             "Скорпион", "Стрелец", "Козерог", "Водолей", "Рыбы"]

    for sign in signs:
        keyboard.add(types.InlineKeyboardButton(text=sign, callback_data='zodiac'))


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,
                         "Привет, сейчас я расскажу тебе гороскоп на сегодня.")

        keyboard = types.InlineKeyboardMarkup()
        buttons(keyboard)

        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака',
                         reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "zodiac":
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(
            second_add) + ' ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)
