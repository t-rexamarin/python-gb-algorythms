# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
#   которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

# n / 2 раз - мое решение
# брать значение и смотреть сколько больше сколько меньше, и если они равны
# граничные значение если несколько одлинаковых значений медиан

import timeit
from random import randint, seed


m = 200
size = 2 * m + 1

# seed(3)
# seed(2)
# numbers = [randint(1, 100) for i in range(size)]
# numbers = [8, 12, 12, 11, 47, 22, 11, 23, 12]
# numbers = [12, 12, 12, 12, 12, 12]
numbers = [97, 100, 6, 10, 54, 93, 65, 98, 34, 71, 7, 75, 72, 47, 32, 29, 64, 59, 74, 11, 92, 75, 29, 13, 14, 31, 1, 95, 23, 58, 62, 100, 9, 21, 24, 22, 74, 54, 3, 93, 100, 79, 15, 90, 34, 68, 86, 82, 28, 41, 48, 68, 2, 22, 41, 72, 12, 45, 76, 15, 44, 42, 2, 11, 45, 87, 30, 56, 83, 2, 93, 4, 7, 91, 49, 70, 93, 98, 9, 2, 45, 57, 20, 90, 54, 45, 61, 49, 95, 52, 18, 74, 76, 70, 58, 28, 8, 20, 83, 51, 90, 88, 25, 100, 94, 59, 42, 35, 47, 79, 94, 43, 5, 3, 57, 12, 78, 41, 35, 28, 72, 56, 98, 5, 78, 52, 28, 86, 32, 75, 58, 46, 76, 95, 53, 100, 14, 4, 52, 36, 67, 27, 75, 49, 85, 16, 36, 97, 47, 4, 41, 9, 39, 72, 41, 83, 94, 8, 5, 69, 1, 62, 35, 77, 61, 48, 37, 5, 1, 56, 31, 93, 93, 21, 83, 77, 28, 51, 100, 13, 34, 2, 5, 2, 75, 88, 10, 56, 23, 48, 22, 23, 9, 95, 41, 54, 4, 55, 25, 69, 27, 5, 10, 2, 47, 67, 40, 35, 56, 49, 61, 19, 10, 57, 75, 41, 97, 30, 39, 86, 25, 70, 10, 73, 65, 47, 62, 23, 22, 24, 77, 62, 29, 98, 86, 3, 82, 17, 58, 11, 64, 26, 21, 90, 55, 9, 63, 77, 37, 57, 90, 15, 85, 53, 89, 85, 29, 42, 98, 100, 60, 57, 23, 80, 42, 62, 55, 16, 31, 55, 17, 91, 44, 81, 71, 42, 87, 92, 73, 97, 66, 53, 84, 80, 95, 84, 3, 49, 13, 23, 37, 35, 25, 25, 38, 98, 95, 95, 20, 42, 22, 96, 46, 93, 26, 62, 16, 41, 64, 7, 61, 87, 9, 86, 31, 75, 7, 52, 64, 47, 93, 97, 75, 48, 90, 91, 18, 41, 57, 92, 85, 72, 42, 69, 20, 51, 20, 27, 32, 78, 4, 37, 13, 86, 4, 40, 57, 62, 91, 62, 73, 91, 20, 12, 13, 86, 97, 75, 10, 80, 6, 3, 43, 41, 85, 57, 93, 21, 23, 24, 35, 4, 65, 6, 99, 94, 76, 96, 89, 84, 7, 22, 74, 21, 51, 42, 26, 93, 26, 83, 75, 16, 13, 13, 29, 97, 69, 37, 82, 86, 51]
print(numbers)
print(sorted(numbers))
# print(len(numbers))
# print(sorted(numbers), sum(numbers), sum(numbers) // len(numbers))

# med_position = (len(numbers) // 2) + 1
# print(f'длинна {len(numbers)}, индекс медианы {med_position}')


# вариант 1
def median_var_1(array):
    # сложность n / 2
    med_idx = (len(array) // 2) + 1
    cp_array = array.copy()
    median = None

    while med_idx:
        min_val = cp_array.index(min(cp_array))
        # print(min_val)
        # numbers.pop(min_val)
        median = cp_array.pop(min_val)
        med_idx -= 1

    return median


# вариант 2
def median_var_2(array):
    # брать значение и смотреть сколько больше сколько меньше, и если они равны
    # median = array[0]
    # count_stop = len(array) // 2
    # i_count_more = 0
    i_count_less = 0

    # for i in array[1:]:
    #     for t in array[1:]:
    #         if i_count_more <= count_stop and i_count_less <= count_stop:
    #             if median < t:
    #                 i_count_more += 1
    #             else:
    #                 i_count_less += 1
    #         elif i_count_more > count_stop or i_count_less > count_stop:
    #             i_count_more = 0
    #             i_count_less = 0
    #         # elif i_count_more == count_stop == i_count_less:
    #         #     return i
    #
    #         if i_count_more == count_stop == i_count_less:
    #                 # print(f'median {i}')
    #                 # iter_stop = 1
    #             return i
    # #         # break
    #
    #     median = i




    # print(i, i_count_more, i_count_less)
    # med_idx = len(array) // 2

    for i in array:
        less = [n for n in array if n < i]
        more = [n for n in array if n > i]
        equal = [n for n in array if n == i]

        # print(i)
        # print(less)
        # print(more)
        # print(equal)
        # print('----')
        len_less = len(less)
        len_more = len(more)
        len_eq = len(equal)
        # print(len_less, len_more, len_eq)
        if len(less) == len(more):
            return i
        elif len(less) < len(more) and len(less) + (len(equal) - 1) == len(more):
            return i
        elif len(more) < len(less) and len(more) + (len(equal) - 1) == len(less):
            return i
        else:
            print(i, len_less, len_more, len_eq)


print(median_var_1(numbers))
print(median_var_2(numbers))

print('Время median_var_1')
print(timeit.timeit(f'median_var_1({numbers})',
                    setup='from __main__ import median_var_1',
                    number=100))

print('Время median_var_2')
print(timeit.timeit(f'median_var_2({numbers})',
                    setup='from __main__ import median_var_2',
                    number=100))