"""Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков."""
import random
import timeit
import cProfile

"""Определить, какое число в массиве встречается чаще всего."""


def freq_1(arr):
    x = 0
    max_count = 0
    num = 0
    for i in list(set(arr)):
        for el in arr:
            if i == el:
                x += 1
        if x >= max_count:
            max_count = x
            num = i
        x = 0
    return num, max_count


# print(timeit.timeit('freq_1([random.randint(0, 10) for _ in range(10)])', number=100, globals=globals()))  # 0.0020055
# print(timeit.timeit('freq_1([random.randint(0, 10) for _ in range(100)])', number=100, globals=globals()))  # 0.024987
# print(timeit.timeit('freq_1([random.randint(0, 10) for _ in range(1000)])', number=100, globals=globals()))  # 0.2800216
# print(timeit.timeit('freq_1([random.randint(0, 10) for _ in range(10000)])', number=100, globals=globals())) # 2.6130535
# print(timeit.timeit('freq_1([random.randint(0, 100) for _ in range(100)])', number=100, globals=globals()))  # 0.0407488
# print(timeit.timeit('freq_1([random.randint(0, 100) for _ in range(1000)])', number=100, globals=globals())) # 0.7012116
# print(timeit.timeit('freq_1([random.randint(0, 100) for _ in range(10000)])', number=100, globals=globals())) # 6.6772912
# print(timeit.timeit('freq_1([random.randint(0, 1000) for _ in range(10000)])', number=100, globals=globals())) # 53.3215395

# cProfile.run('freq_1([random.randint(0, 10) for _ in range(10)])')  # 14    0.000    0.000    0.000    0.000
# cProfile.run('freq_1([random.randint(0, 10) for _ in range(100)])')  # 145    0.000    0.000    0.000    0.000
# cProfile.run('freq_1([random.randint(0, 10) for _ in range(1000)])')  # 1455    0.000    0.000    0.000    0.000
# cProfile.run('freq_1([random.randint(0, 10) for _ in range(10000)])')  # 14703    0.003    0.000    0.003    0.000
# cProfile.run('freq_1([random.randint(0, 100) for _ in range(100)])')  # 123    0.000    0.000    0.000    0.000
# cProfile.run('freq_1([random.randint(0, 100) for _ in range(1000)])')  # 1268   0.000    0.000    0.000    0.000
# cProfile.run('freq_1([random.randint(0, 100) for _ in range(10000)])')  # 12689    0.000    0.000    0.003    0.000
# cProfile.run('freq_1([random.randint(0, 1000) for _ in range(10000)])')  # 10220    0.000    0.000    0.003    0.000


# Вариант 2

def freq_2(arr):
    counter = {}
    frequency = 1
    num = None

    for item in arr:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

        if counter[item] > frequency:
            frequency = counter[item]
            num = item
    return num, frequency


# print(timeit.timeit('freq_2([random.randint(0, 10) for _ in range(10)])', number=100, globals=globals()))  # 0.0020159
# print(timeit.timeit('freq_2([random.randint(0, 10) for _ in range(100)])', number=100, globals=globals()))  # 0.0198494
# print(timeit.timeit('freq_2([random.randint(0, 10) for _ in range(1000)])', number=100, globals=globals()))  # 0.258928
# print(timeit.timeit('freq_2([random.randint(0, 10) for _ in range(10000)])', number=100, globals=globals())) # 2.1827861
# print(timeit.timeit('freq_2([random.randint(0, 100) for _ in range(100)])', number=100, globals=globals()))  # 0.0146117
# print(timeit.timeit('freq_2([random.randint(0, 100) for _ in range(1000)])', number=100, globals=globals())) # 0.1590392
# print(timeit.timeit('freq_2([random.randint(0, 100) for _ in range(10000)])', number=100, globals=globals())) # 1.787997
# print(timeit.timeit('freq_2([random.randint(0, 1000) for _ in range(10000)])', number=100, globals=globals())) # 2.1565125

# cProfile.run('freq_2([random.randint(0, 10) for _ in range(10)])')  # 11    0.000    0.000    0.000    0.000
# cProfile.run('freq_2([random.randint(0, 10) for _ in range(100)])')  # 155    0.000    0.000    0.000    0.000
# cProfile.run('freq_2([random.randint(0, 10) for _ in range(1000)])')  # 1442    0.000    0.000    0.000    0.000
# cProfile.run('freq_2([random.randint(0, 10) for _ in range(10000)])')  # 14552    0.002    0.000    0.002    0.000
# cProfile.run('freq_2([random.randint(0, 100) for _ in range(100)])')  # 120    0.000    0.000    0.000    0.000
# cProfile.run('freq_2([random.randint(0, 100) for _ in range(1000)])')  # 1275   0.000    0.000    0.000    0.000
# cProfile.run('freq_2([random.randint(0, 100) for _ in range(10000)])')  # 12740    0.002    0.000    0.002    0.000
# cProfile.run('freq_2([random.randint(0, 1000) for _ in range(10000)])')  # 10260    0.002    0.000    0.002    0.000


def freq_3(arr):
    num = None
    frequency = 0

    for item in arr:
        el = arr.count(item)
        if el > frequency:
            frequency = el
            num = item
    return num, frequency


# print(timeit.timeit('freq_3([random.randint(0, 10) for _ in range(10)])', number=100, globals=globals()))  # 0.0033726
# print(timeit.timeit('freq_3([random.randint(0, 10) for _ in range(100)])', number=100, globals=globals()))  # 0.0430053
# print(timeit.timeit('freq_3([random.randint(0, 10) for _ in range(1000)])', number=100, globals=globals()))  # 2.4824592
# print(timeit.timeit('freq_3([random.randint(0, 10) for _ in range(10000)])', number=100, globals=globals())) # 220.3307457
# print(timeit.timeit('freq_3([random.randint(0, 100) for _ in range(100)])', number=100, globals=globals()))  # 0.0327221
# print(timeit.timeit('freq_3([random.randint(0, 100) for _ in range(1000)])', number=100, globals=globals())) # 2.1928268

# очень долго (не дождалась)
# print(timeit.timeit('freq_3([random.randint(0, 100) for _ in range(10000)])', number=100, globals=globals()))

# очень долго (не дождалась)
# print(timeit.timeit('freq_3([random.randint(0, 1000) for _ in range(10000)])', number=100, globals=globals()))

# cProfile.run('freq_3([random.randint(0, 10) for _ in range(10)])')  # 11    0.000    0.000    0.000    0.000
# cProfile.run('freq_3([random.randint(0, 10) for _ in range(100)])')  # 143    0.000    0.000    0.000    0.000
# cProfile.run('freq_3([random.randint(0, 10) for _ in range(1000)])')  # 1401    0.000    0.000    0.000    0.000
# cProfile.run('freq_3([random.randint(0, 10) for _ in range(10000)])')  # 14482    0.000    0.000    0.000    0.000
# cProfile.run('freq_3([random.randint(0, 100) for _ in range(100)])')  # 126    0.000    0.000    0.000    0.000
# cProfile.run('freq_3([random.randint(0, 100) for _ in range(1000)])')  # 1247   0.000    0.000    0.000    0.000
# cProfile.run('freq_3([random.randint(0, 100) for _ in range(10000)])')  # 12664    0.002    0.000    0.002    0.000
# cProfile.run('freq_3([random.randint(0, 1000) for _ in range(10000)])')  # 10233    0.002    0.000    0.002    0.000

# ВЫВОД

"""
1 алгоритм имеет предположительно квадратичную сложность и показывает более медленую работу на больших массивах с 
большимы данными.
2 алгоритм обладает линейной сложность так как проходится по каждому элементу массива и время прохождения такого 
алгоритма прямо зависит от длинны массива. Выигрывает при работе с большими массивами.
3 алгоритм тоже предположительно имеет линейную сложность так как использует встроенную функцию count.
 Такой алгоритм не выдерживает работы с большыми данными.
 
Лучший результат в итоге показывает 2 алгоритм, он немного выигрывает у 1. 
 
"""
