# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
#   (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
#   и вывести наименования предприятий, чья прибыль выше среднего
#   и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from random import random, randint, choice
from string import ascii_uppercase

factories_cnt = int(input('Сколько компаний будем вводить?: '))

factories_dict = []
for factory in range(factories_cnt):
    # раскоментить для теста
    factory_name = ''.join(choice(ascii_uppercase) for _ in range(10))
    # factory_name = input(f'Введите название для {factory + 1} компании из {factories_cnt}: ')

    quarters = []
    for quarter in range(1, 5):
        # раскоментить для теста
        quarter_profit = randint(40, 150)
        # quarter_profit = int(input(f'В {quarter} квартеле компанией получено прибыли: '))
        quarters.append(quarter_profit)

    factories_dict.append({
        'factory_name': factory_name,
        'quarters': quarters,
        'average_money': sum(quarters)
    })

average_from_all_companies = 0
for item in factories_dict:
    # print(item)
    average_from_all_companies += item['average_money']

# средняя прибыль среди всех компаний
year_total_avg = average_from_all_companies / len(factories_dict)

more_than_avg = []
less_than_avg = []
for item in factories_dict:
    # раскоменить чтобы увидеть данные по компании, в т.ч. прибыль
    # print(item)
    if item['average_money'] > year_total_avg:
        more_than_avg.append(item['factory_name'])
    elif item['average_money'] < year_total_avg:
        less_than_avg.append(item['factory_name'])

print(f'Средняя прибыль среди компаний: {year_total_avg}')
print(f'More than avg {more_than_avg}')
print(f'Less than avg {less_than_avg}')
