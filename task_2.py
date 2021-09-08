# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

input_txt = 'Введите число цифрами: '
number = input(input_txt)
while number.isdigit() is False:
    print('Вы ввели не число')
    number = input(input_txt)

even_cnt = 0
odd_cnt = 0

for digit in number:
    if int(digit) % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

print(f'В числе {number}, четных цифр - {even_cnt} и нечетных {odd_cnt}.')
