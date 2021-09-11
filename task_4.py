# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint
from collections import Counter

numbers = [randint(0, 2) for _ in range(1, 21)]
# 1 - 7, 0 - 7, 2 - 6
# numbers = [1, 0, 2, 2, 2, 0, 1, 1, 2, 0, 0, 1, 2, 0, 1, 2, 0, 0, 1, 1]

numbers_counted = {}
for number in numbers:
    if numbers_counted.get(number):
        numbers_counted[number] += 1
    else:
        numbers_counted[number] = 1

max_value = max(numbers_counted.values())
keys_by_max_val = [k for k, v in numbers_counted.items() if v == max_value]

print(f'Стартовый массив: {numbers}')
print(f'Посчитанные значения: {numbers_counted}')
print(f'Число(а), которое встречается чаще всего: {keys_by_max_val}')

# для себя
print(Counter(numbers).most_common(1))
