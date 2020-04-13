"""Определить, какое число в массиве встречается чаще всего."""
import random

ARRAY = [random.randint(0, 100) for _ in range(0, 10)]
print(ARRAY)


def freq_1():
    x = 0
    max_count = 0
    num = 0

    for i in list(set(ARRAY)):
        for el in ARRAY:
            if i == el:
                x += 1
        if x >= max_count:
            max_count = x
            num = i
        x = 0
    if max_count > 1:
        print(f'Цифра {num} встречается {max_count} раз(а)')
    else:
        print('Все цифры уникальны')


import timeit

print(timeit.timeit('freq_1', number=100, globals=globals()))  # 3.099999999998937e-06


# Вариант 2

def freq_2():
    counter = {}
    frequency = 1
    num = None

    for item in ARRAY:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

        if counter[item] > frequency:
            frequency = counter[item]
            num = item

    if num is not None:
        print(f'Цифра {num} встречается {frequency} раз(а)')
    else:
        print('Все цифры уникальны')


print(timeit.timeit('freq_2', number=100, globals=globals()))  # 2.7000000000013125e-06
