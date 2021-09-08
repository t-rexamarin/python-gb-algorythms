# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

input_txt = 'Введите число цифрами: '
row_length = input(input_txt)
while row_length.isdigit() is False:
    print('Вы ввели не число')
    row_length = input(input_txt)

item = 1
result = 0
row_length = int(row_length)

while row_length > 0:
    result += item
    item /= -2
    row_length -= 1

print(result)
