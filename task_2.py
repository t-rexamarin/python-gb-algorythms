# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# из-за недостатка времени, это задание я практически полностью подсмотрел у вас
# как то с ходу не удалось придумать собственного красивого решения
# первое что было в голове, это переводить hex в десятичные числа
# но подумал, что это не то, что требуется в задании
# если смогу, то сяду подумать над самостоятельным решением

from string import ascii_uppercase
from itertools import zip_longest


def sum_func(number1, number2):
    # number1 = number1.upper()
    # number2 = number2.upper()

    hex_list = [str(i) for i in range(10)] + [char for char in (ascii_uppercase[:6])]
    hex_dict = dict(zip(hex_list, list(range(len(hex_list)))))

    result_hex = []
    rest = 0
    for pair in zip_longest(number1[::-1], number2[::-1], fillvalue='0'):
        # print(pair[0], pair[1])
        int1 = hex_dict[pair[0]]
        int2 = hex_dict[pair[1]]
        result_hex.append(hex_list[(int1 + int2 + rest) % 16])
        rest = (hex_dict[pair[0]] + hex_dict[pair[1]] + rest) // 16
        # print((int1 + int2) % 16)
    # else:
    #     my_arr.append(hex_list[rest % 16])

    return result_hex[::-1]


def mult_func(number1, number2):
    # number1 = number1.upper()
    # number2 = number2.upper()

    hex_list = [str(i) for i in range(10)] + [char for char in (ascii_uppercase[:6])]
    mult_result = '0'

    number1 = number1[::-1]
    number2 = number2[::-1]

    for i in range(len(number2)):
        number3 = []

        if i > 0:
            number3 = ['0'] * i

        rest = 0

        for j in number1:
            a = hex_list.index(number2[i])
            b = hex_list.index(j)

            number3.append(hex_list[(a * b + rest) % 16])
            rest = (a * b + rest) // 16

            if j == len(number1):
                break

        number3.append(str(rest))

        n2 = number2[::-1]
        mult_result = sum_func(mult_result, n2)

    return mult_result


numb1 = 'A2'
numb2 = 'C4F'

print(f'Сумма: {sum_func(numb1, numb2)}')
print(f'Произведение: {mult_func(numb1, numb2)}')
