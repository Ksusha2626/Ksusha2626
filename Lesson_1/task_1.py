# Блок схемы на 1 лекцию: https://drive.google.com/file/d/1E_O1ccJ-6vfrymEHteTBZoMHAwpf6D_i/view?usp=sharing

"""Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."""

x = int(input('Введите трехзначное число '))

a = x // 100
b = x % 10
c = (x // 10) % 10

sum = a + b + c
prod = a * b * c

print(f'Сумма чисел равна: {sum}')
print(f'Произведение чисел равно: {prod}')
