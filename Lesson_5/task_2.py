"""Написать программу сложения и *умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]"""
from collections import deque

letter_to_digit = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
digit_to_letter = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def user_digits():
    user_num = []
    lst = []
    # Собираем числа для сложения и переводим буквы в числа
    for i in range(1, 3):
        num = input(f'Введите {i} число в шестнадцатеричной системе счисления: ')
        for el in num:
            if el in letter_to_digit.keys():
                el = letter_to_digit[el]
            lst.append(int(el))
        lst.reverse()
        user_num.append(lst)
        lst = []
    # Уравнивание чисел
    while len(user_num[0]) != len(user_num[1]):
        if len(user_num[0]) > len(user_num[1]):
            user_num[1].append(0)
        else:
            user_num[0].append(0)
    num_1 = user_num[0]
    num_2 = user_num[1]
    return num_1, num_2


def summ_digits():
    num_1, num_2 = user_digits()
    mind = 0
    total = deque()
    for index, num in enumerate(num_1):
        result = num + num_2[index] + mind
        mind = 0
        if result >= 16:
            mind += 1
            result = result - 16
        if result in letter_to_digit.values():
            total.appendleft(digit_to_letter[result])
        else:
            total.appendleft(result)
    return total


print(summ_digits())
