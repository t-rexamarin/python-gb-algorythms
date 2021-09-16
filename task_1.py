# 1. Проанализировать скорость и сложность одного любого алгоритма,
#   разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# задача №1 из 3 урока
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
import timeit

numbers_start = 2
numbers_end = 99
divisor_start = 2
divisor_end = 9


# ваша реализация, немного переделанная на мои рельсы
def your_func(n_start, n_end, d_start, d_end):
    init_list = [i for i in range(n_start, n_end + 1)]
    for item in range(d_start, d_end + 1):
        # print(f'{item} - {len(list(filter(lambda x: x % item == 0, init_list)))}')
        result = {item} - {len(list(filter(lambda x: x % item == 0, init_list)))}


# моя
def my_func(n_start, n_end, d_start, d_end):
    numbers = [i for i in range(n_start, n_end + 1)]
    divisors = [d for d in range(d_start, d_end + 1)]

    result_arr = {}

    for d in divisors:
        count = 0
        for i in numbers:

            if i % d == 0:
                count += 1
        result_arr[d] = count

    # print(result_arr)


print('Ваша реализация')
print(timeit.timeit(f'your_func({numbers_start}, {numbers_end}, {divisor_start}, {divisor_end})',
                    setup='from __main__ import your_func',
                    number=100))
print('\nМоя реализаци')
print(timeit.timeit(f'my_func({numbers_start}, {numbers_end}, {divisor_start}, {divisor_end})',
                    setup='from __main__ import my_func',
                    number=100))
