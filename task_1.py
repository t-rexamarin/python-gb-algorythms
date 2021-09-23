# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
#   заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

from random import randint, seed

seed(3)
numbers = [randint(-100, 100) for i in range(20)]
print(numbers)


def my_sort(array: list):
    n = 1

    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

        n += 1

    return array


print(my_sort(numbers))
