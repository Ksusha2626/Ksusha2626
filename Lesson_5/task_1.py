"""Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
вывести наименования предприятий, чья прибыль выше среднего и ниже среднего."""
from collections import Counter


def average_profit():
    firm_count = int(input('Сколько будет предприятий? '))
    c = Counter()
    max_average = []
    min_average = []
    for i in range(1, firm_count + 1):
        firm_name = input(f'Введите название {i} компании: ')
        firm_profit = list(map(int, input(f'Введите прибыль {i} компании за 4 квартала через пробел: ').split()))
        c[firm_name] = sum(firm_profit)
    profit = sum(c.values()) / firm_count
    for el in c.items():
        if el[1] > profit:
            max_average.append(el[0])
        if el[1] < profit:
            min_average.append(el[0])
    return f'Средняя прибыль компаний за год равна: {profit}\nПрибыль выше среднего у компании: {max_average}\n' \
           f'Прибыль ниже среднего у компаний: {min_average}'


print(average_profit())
