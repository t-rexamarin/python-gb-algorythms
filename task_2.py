# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
#   то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
#   т.к. именно в этих позициях первого массива стоят четные числа.

from random import randint, seed

seed(42)

numbers = [randint(1, 100) for _ in range(1, 11)]
print(numbers)

# even_indexes = [i for i in (map((lambda x: x % 2 == 0), numbers))]
even_indexes = [numbers.index(i) for i in numbers if i % 2 == 0]

print(list(even_indexes))
