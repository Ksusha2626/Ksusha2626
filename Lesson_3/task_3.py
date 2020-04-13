"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
import random

array = [random.randint(0, 100) for _ in range(0, 10)]
print(array)

idx_max = 0
idx_min = 0
for i in range(len(array)):
    if array[i] > array[idx_max]:
        idx_max = i
    if array[i] <= array[idx_min]:
        idx_min = i

array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)

