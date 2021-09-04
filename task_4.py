# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

import random

user_int_min = int(input('Генерируем целое число от: '))
user_int_max = int(input('Генерируем целое число до: '))

user_float_min = int(input('Генерируем вещественное число от: '))
user_float_max = int(input('Генерируем вещественное число до: '))

user_char_min = input('Генерируем случайный символ от: ')
user_char_max = input('Генерируем случайный символ до: ')

output_int = random.randint(user_int_min, user_int_max)
output_float = round(random.uniform(user_float_min, user_float_max), 2)
output_char = chr(random.randint(ord(user_char_min), ord(user_char_max)))

print(f'Cлучайное целое число - {output_int}.')
print(f'Cлучайное вещественное число - {output_float}.')
print(f'Cлучайный символ - {output_char}.')
