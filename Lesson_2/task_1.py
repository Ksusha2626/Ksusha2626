# Блок схемы к 2 лекции: https://drive.google.com/file/d/15GCZoOClCjP6omCUiY-sxUu2Mcw8zwV8/view?usp=sharing


"""Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова
запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя."""


while True:
    x = float(input('Введите 1-е число: '))
    y = float(input('Введите 2-е число: '))
    operator = input('Введите оператор. Для выхода введите 0. ')
    if operator in ('0', '+', '-', '*', '/'):
        if operator == '0':
            break
        elif operator == '+':
            print(f'{x + y:.2f}')
        elif operator == '-':
            print(f'{x - y:.2f}')
        elif operator == '*':
            print(f'{x * y:.2f}')
        elif operator == '/' and y == 0:
            print("На ноль делить нельзя!")
        else:
            print(f'{x / y:.2f}')
        continue
    print('Вы ввели неверный оператор, попробуйте еще разок :)')
