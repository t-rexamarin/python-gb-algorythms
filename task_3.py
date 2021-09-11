# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint, seed

seed(42)

numbers = [randint(1, 100) for _ in range(1, 11)]
# numbers = [82, 95, 4, 95, 36, 32, 29, 18, 95, 14]
print(f'Стартовый массив {numbers}')

max_int = numbers.index(max(numbers))
min_int = numbers.index(min(numbers))

numbers[max_int], numbers[min_int] = numbers[min_int], numbers[max_int]

print(f'Итоговый массив {numbers}')
# print(max_int, min_int)
