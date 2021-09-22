# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#   заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import randint, seed

seed(3)
numbers = [randint(0, 50) for i in range(4)]
print(numbers)


def merge_sort(array: list):
    if len(array) > 1:
        split = len(array) // 2

        left_part = array[:split]
        right_part = array[split:]

        # print(left_part, right_part)
        merge_sort(left_part)
        merge_sort(right_part)

        lp = 0
        rp = 0
        i = 0

        while lp < len(left_part) and rp < len(right_part):
            if left_part[lp] < right_part[rp]:
                array[i] = left_part[lp]
                lp += 1
            else:
                array[i] = right_part[rp]
                rp += 1
            i += 1

        while lp < len(left_part):
            array[i] = left_part[lp]
            lp += 1
            i += 1

        while rp < len(right_part):
            array[i] = right_part[rp]
            rp += 1
            i += 1


print(merge_sort(numbers))
print(numbers)