# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# не совсем элегантно

from random import randint

numbers = [randint(-5, 5) for _ in range(1, 11)]

min_idx = numbers.index(min(numbers))
max_idx = numbers.index(max(numbers))
min_of_idxs = min(min_idx, max_idx)
max_of_idxs = max(min_idx, max_idx)
# сдвигаем нижнюю границу, чтобы не брать само минимальное значение
data_for_sum = numbers[min_of_idxs + 1:max_of_idxs]
sum_between_min_max = sum(data_for_sum)

print(f'Стартовый массив: {numbers}')
print(f'Индекс минимального ({numbers[min_idx]}): {min_idx}, '
      f'индекс максимального ({numbers[max_idx]}): {max_idx}.')
print(f'Какие данные суммируем: {data_for_sum}')
print(f'Сумма: {sum_between_min_max}')
