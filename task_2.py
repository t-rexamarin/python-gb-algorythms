# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

import timeit


u_input = int(input("вывод простых чисел до числа ... "))


def erat(user_input: int):
    numbers = [i if i > 1 else 0 for i in range(user_input + 1)]
    # print(numbers)

    number = next((v for k, v in enumerate(numbers) if v), 0)
    while number < user_input:
        if numbers[number] != 0:
            number_sqr = number * 2

            while number_sqr < user_input:
                numbers[number_sqr] = 0
                number_sqr += number

        number += 1

    # print(numbers)
    return numbers


# чем длиннее список натуральных чисел, тем больше занимает времени
# в сравнении с первым вариантом:
# - при ряде в 30 этот занимает занимает в 3 раза больше времени
# - при ряде в 300 тоже +- 3 раза
# - при ряде в 3000 в 8 раз
# чем длинне числа, тем больше делителей, что увеличивает время
# при ряде в 1 время выполнения - 0.0032768119999673218
# при ряде в 100 время выполнения - 0.10499290100415237
# при ряде в 200 время выполнения - ~0.24350526600028388
# при ряде в 300 время выполнения - ~0.43933123598981183
# при ряде в 1000 время выполнения - ~1.87789835401054
# при ряде в 10000 время выполнения - ~40.03756903600879
# как определить сложность, я чего то не догоняю
def no_erat(user_input: int):
    numbers = [i if i > 1 else 0 for i in range(user_input + 1)]

    for k, v in enumerate(numbers):
        divisors_cnt = int(pow(v, 0.5))

        # тут бы по хорошему отсеять все что кратно 2 и 3, но не придумал как красиво сделать
        for divisor in range(2, divisors_cnt + 1):
            if v % divisor == 0:
                numbers[k] = 0

    # print(numbers)
    return numbers


print('По эратосфену')
print(timeit.timeit(f'erat({u_input})',
                    setup='from __main__ import erat',
                    number=1000))

print('Без эратосфена')
print(timeit.timeit(f'no_erat({u_input})',
                    setup='from __main__ import no_erat',
                    number=1000))

