import sys
import random
from collections import defaultdict


# 64-битная разрядная система. Win10. Python 3.7.4

def get_size(x):
    _size = sys.getsizeof(x)
    print(f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                _size += get_size(key)
                _size += get_size(value)
        elif not isinstance(x, str):
            for item in x:
                _size += get_size(item)
    return _size


""" Посчитать, сколько раз встречается определенная цифра в последовательности чисел."""


def summ():
    n = 8  # Нужно ввести 8 цифр
    x = random.randint(0, 9)
    i = 0
    for _ in range(1, n + 1):
        y = int(input("Число " + str(_) + ": "))
        while y > 0:
            if y % 10 == x:
                i += 1
            y //= 10
    vars = locals()
    all_size = 0
    for var in vars.keys():
        all_size += get_size(vars[var])

    return f'Цифра {x} встречается {i} раз\nОбщий размер функции равен: {all_size}'


#  Общий размер функции равен: 132
#  Если с n = [443, 205, 339, 108, 200, 589, 8, 4], то 432 бит
print(summ())


def summ_2():
    n = [443, 205, 339, 108, 200, 589, 8, 4]  # [random.randint(0, 1000) for _ in range(random.randrange(1, 10))]
    x = random.randint(0, 9)
    dict = defaultdict(int)
    for el in n:
        while el > 0:
            if el % 10 == x:
                dict[x] += 1
            el //= 10
    vars = locals()
    all_size = 0
    for var in vars.keys():
        all_size += get_size(vars[var])
    return f'Цифра {x} встречается {dict[x]} раз\nОбщий размер функции равен: {all_size}'


# Общий размер функции равен: 708
# print(summ_2())

def summ_3():
    n = [443, 205, 339, 108, 200, 589, 8, 4]  # [random.randint(0, 1000) for _ in range(random.randrange(1, 10))]
    x = random.randint(0, 9)
    dict = defaultdict(int)
    for el in n:
        while el > 0:
            item = el % 10
            dict[item] += 1
            el //= 10
    print(dict)
    i = dict[x]
    vars = locals()
    all_size = 0
    for var in vars.keys():
        all_size += get_size(vars[var])
    return f'Цифра {x} встречается {i} раз\nОбщий размер функции равен: {all_size}'

# print(summ_3())

# Общий размер функции равен: 1280

# Самой не прожорливой функцией оказалась функция номер 1, так как в ней не происходит сохранение массива ни из входных,
# ни из подсчитанных чисел. Поиск и подсчёт нужной цыфры происходит в момент ввода числа и все лишние цифры сразу
# же отсеиваются.

# Самая прожорливая функция - номер 3, так как скушивается много памяти на формирование словаря с подсчетами всех
# чисел массива.
