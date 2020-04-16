"""Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов."""
import cProfile
import timeit


def err(el):
    n = 10000
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    for i in enumerate(res):
        if i[0] == el - 1:
            return i[1]

print(err(170))
# print(timeit.timeit('err(10)', number=100, globals=globals()))  # 0.8223235
# print(timeit.timeit('err(20)', number=100, globals=globals()))  # 0.4604192
# print(timeit.timeit('err(30)', number=100, globals=globals()))  # 0.6310625
# print(timeit.timeit('err(40)', number=100, globals=globals()))  # 0.4777987
# print(timeit.timeit('err(50)', number=100, globals=globals()))  # 0.6728011
# print(timeit.timeit('err(80)', number=100, globals=globals()))  # 0.0520751

# cProfile.run('err(10)')  # 1    0.003    0.003    0.004    0.004 task_2.py:7(err)
# cProfile.run('err(20)')  # 1    0.007    0.007    0.008    0.008 task_2.py:7(err)
# cProfile.run('err(30)')  # 1    0.004    0.004    0.005    0.005 task_2.py:7(err)
# cProfile.run('err(40)')  # 1    0.005    0.005    0.006    0.006 task_2.py:7(err)
# cProfile.run('err(50)')  # 1    0.005    0.005    0.007    0.007 task_2.py:7(err)
# cProfile.run('err(80)')  # 1    0.004    0.004    0.004    0.004 task_2.py:7(err)


def prime(i):
    lst = [2]
    x = 3
    while len(lst) < i:
        for j in lst:
            if x % j == 0:
                break
        else:
            lst.append(x)
        x += 1
    return lst[i - 1]


# print(timeit.timeit('prime(10)', number=100, globals=globals()))  # 0.0022838
# print(timeit.timeit('prime(20)', number=100, globals=globals()))  # 0.0050876
# print(timeit.timeit('prime(30)', number=100, globals=globals()))  # 0.008439
# print(timeit.timeit('prime(40)', number=100, globals=globals()))  # 0.0131118
# print(timeit.timeit('prime(50)', number=100, globals=globals()))  # 0.0212126
# print(timeit.timeit('prime(80)', number=100, globals=globals()))  # 0.0759497

# cProfile.run('prime(10)')  # 28     0.000    0.000    0.000    0.000 {built-in method builtins.len}
# cProfile.run('prime(20)')  # 70     0.000    0.000    0.000    0.000 {built-in method builtins.len}
# cProfile.run('prime(30)')  # 112    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# cProfile.run('prime(40)')  # 172    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# cProfile.run('prime(50)')  # 228    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# cProfile.run('prime(80)')  # 408    0.000    0.000    0.000    0.000 {built-in method builtins.len}

# ВЫВОД

"""
1 алгоритм имеет константную сложность тк зафиксирован размер решета и поэтому время не зависит от искомого простого числа.
Формируется массив константной длины за счет чего расходуется много памяти, а для поиска числа перебираются все числа 
в массиве пока не будет обнаружено нужное что так же сказывается на производительности. 

2 алгоритм скорее всего имеет логарифмическую сложность. Данный алгоритм генерируется массив из простых чиселах только лишь
в диапозоне 0 до N, что существенно экономит памят и позволяет найти число гораздо быстрее. 
 
"""