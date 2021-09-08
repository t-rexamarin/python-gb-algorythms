# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

# возможно не самое оптимальное решение
# выглядит громоздко. Делал торопясь

numbers_list = []
numbers_limit = 10

while numbers_limit > 0:
    # todo:
    #     - проверки
    number = int(input(f'Введите число (необходимо еще {numbers_limit}): '))
    numbers_list.append(number)
    numbers_limit -= 1

sums_arr = {}
for item in numbers_list:
    item_sum = 0
    item_copy = item

    while item_copy:
        item_sum += item_copy % 10
        item_copy //= 10

    sums_arr[str(item)] = str(item_sum)

max_sum = max(sums_arr.values())
# может быть несколько разных чисел с одинаковой суммой
list_with_max = {}
for number, number_sum in sums_arr.items():
    if number_sum == max_sum:
        list_with_max[number] = number_sum

print(f'Список всех чисел: {numbers_list}')

if len(list_with_max) == 1:
    print(f'Число с максимальной суммой цифр - {list(list_with_max.keys())[0]}. '
          f'Сумма цифр числа - {list(list_with_max.values())[0]}.')
else:
    print(f'Чисел с одинаковой максимальной суммой цифр - {max(list_with_max.keys())}, несколько.')
    for number, number_sum in list_with_max.items():
        print(f'Число - {number}. Сумма - {number_sum}.')
