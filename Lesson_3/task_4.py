"""Определить, какое число в массиве встречается чаще всего."""
import random

ARRAY = [random.randint(0, 100) for _ in range(0, 10)]
print(ARRAY)

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
