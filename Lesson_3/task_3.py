"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
import random

ARRAY = [random.randint(0, 100) for _ in range(0, 10)]
print(ARRAY)

m = 0
low = ARRAY[0]
for i in ARRAY:
    if i > m:
        m = i
    if i <= low:
        low = i
ARRAY[ARRAY.index(low)] = m
ARRAY[ARRAY.index(m)] = low
print(ARRAY)
print(f'Максимальное число массива - {m}\nМинимальное число массива - {low}')
