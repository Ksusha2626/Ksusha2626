"""В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""
import timeit


def multi():
    multi = {}
    for i in range(2, 10):
        multi[i] = []
        for n in range(2, 100):
            if n % i == 0:
                multi[i].append(n)
        print(f'Для числа {i} кратны {len(multi[i])} чисел(ла)')


print(timeit.timeit('multi', number=100, globals=globals()))  # 2.3999999999996247e-06


# Вариант 2

def multi_2():
    for i in range(2, 10):
        print(f'{i}\t{99 // i}')


print(timeit.timeit('multi_2', number=100, globals=globals()))  # 2.2000000000008124e-06
