"""Гороскоп. """

# Подключаем модуль случайных чисел
import random


def get_signs():
    """Вернёт знаки зодиака. """

    signs = ["Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева", "Весы",
             "Скорпион", "Стрелец", "Козерог", "Водолей", "Рыбы"]

    # signs = {1: "Овен", 2: "Телец", 3: "Близнецы", 4: "Рак",
    #          5: "Лев", 6: "Дева", 7: "Весы", 8: "Скорпион",
    #          9: "Стрелец", 10: "Козерог", 11: "Водолей", 12: "Рыбы"}

    for i in range(len(signs)):
        print(f'{i+1} - {signs[i]}')
        i += 1


def zodiac_message():
    """Выводит послание. """

    # Заготовка для первого предложения
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
        "И доверяй только себе.",
        "Ну, или просто посиди дома.",
        "Но я бы не рисковал.",
        "Но я бы не ебал себе мозги.",
        "А может и нет."
    ]

    # знаки зодиака
    get_signs()

    # Спрашиваем у пользователя про его знак
    zodiac = int(
        input("{blue}Какой у тебя знак зодиака? Выбери число с ним "
              "{endcolor}".format(blue="\033[96m", endcolor="\033[0m"))
    )

    # Если введённое значение есть в списке — выдаём гороскоп
    if 0 < zodiac < 13:
        print(
            random.choice(first),
            random.choice(second),
            random.choice(second_add),
            random.choice(third)
            )
    else:
        print(f"Здесь нет такого знака, проверь ещё раз. ")


zodiac_message()
