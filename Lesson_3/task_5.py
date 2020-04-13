"""Числа Фибоначчи"""
import timeit
import cProfile


# 1. Рекурсия
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# print(timeit.timeit('fib(5)', number=100, globals=globals()))  # 0.00024969999999999853
# print(timeit.timeit('fib(10)', number=100, globals=globals()))  # 0.003923199999999998
# print(timeit.timeit('fib(15)', number=100, globals=globals()))  # 0.034420599999999996
# print(timeit.timeit('fib(20)', number=100, globals=globals()))  # 0.3951499
# print(timeit.timeit('fib(25)', number=100, globals=globals()))  # 4.1553006

# cProfile.run('fib(5)')   # 15/1    0.000    0.000    0.000    0.000 task_2.py:6(fib)
# cProfile.run('fib(10)')  # 177/1    0.000    0.000    0.000    0.000 task_2.py:6(fib)
# cProfile.run('fib(15)')  # 1973/1    0.001    0.000    0.001    0.001 task_2.py:6(fib)
# cProfile.run('fib(20)')  # 21891/1    0.008    0.000    0.008    0.008 task_2.py:6(fib)
# cProfile.run('fib(25)')  # 242785/1    0.112    0.000    0.112    0.112 task_2.py:6(fib)

# 2. Рекурсия + словарь
def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)


# print(timeit.timeit('fib_dict(5)', number=100, globals=globals()))  # 0.00024360000000000354
# print(timeit.timeit('fib_dict(10)', number=100, globals=globals()))  # 0.00047849999999999976
# print(timeit.timeit('fib_dict(15)', number=100, globals=globals()))  # 0.0008176999999999976
# print(timeit.timeit('fib_dict(20)', number=100, globals=globals()))  # 0.001108900000000003
# print(timeit.timeit('fib_dict(25)', number=100, globals=globals()))  # 0.001725400000000002
# print(timeit.timeit('fib_dict(30)', number=100, globals=globals()))  # 0.0015173999999999951
#
# cProfile.run('fib_dict(5)')   # 9/1    0.000    0.000    0.000    0.000 task_2.py:29(_fib_dict)
# cProfile.run('fib_dict(10)')  # 19/1    0.000    0.000    0.000    0.000 task_2.py:29(_fib_dict)
# cProfile.run('fib_dict(15)')  # 29/1    0.000    0.000    0.000    0.000 task_2.py:29(_fib_dict)
# cProfile.run('fib_dict(20)')  # 39/1    0.000    0.000    0.000    0.000 task_2.py:29(_fib_dict)
# cProfile.run('fib_dict(25)')  # 49/1    0.000    0.000    0.000    0.000 task_2.py:29(_fib_dict)

# 3. Цикл
def fib_loop(n):
    if n < 2:
        return n
    first = 0
    second = 1
    for _ in range(2, n + 1):
        first, second = second, first + second
    return second


# print(timeit.timeit('fib_loop(5)', number=100, globals=globals()))   # 6.37999999999958e-05
# print(timeit.timeit('fib_loop(10)', number=100, globals=globals()))  # 8.100000000000468e-05
# print(timeit.timeit('fib_loop(15)', number=100, globals=globals()))  # 0.00010729999999999768
# print(timeit.timeit('fib_loop(20)', number=100, globals=globals()))  # 0.00013380000000000336
# print(timeit.timeit('fib_loop(25)', number=100, globals=globals()))  # 0.00016189999999999954
# print(timeit.timeit('fib_loop(30)', number=100, globals=globals()))  # 0.00021579999999999516

# cProfile.run('fib_loop(5)')   # 1    0.000    0.000    0.000    0.000
# cProfile.run('fib_loop(10)')  # 1    0.000    0.000    0.000    0.000
# cProfile.run('fib_loop(15)')  # 1    0.000    0.000    0.000    0.000
# cProfile.run('fib_loop(20)')  # 1    0.000    0.000    0.000    0.000
# cProfile.run('fib_loop(25)')  # 1    0.000    0.000    0.000    0.000

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')
