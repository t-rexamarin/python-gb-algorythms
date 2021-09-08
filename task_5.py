# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

# тут тоже, возможно, не самое оптимальное решение

ascii_start = 32
ascii_end = 127

my_arr = []
line = {}

for i in range(ascii_start, ascii_end + 1):
    if len(line) < 10:
        line[str(ord(chr(i)))] = chr(i)

        if i == ascii_end:
            my_arr.append(line.copy())
    else:
        my_arr.append(line.copy())
        line.clear()

# print(my_arr)
for line in my_arr:
    row = ''
    # print(list(line)[-1])
    # if line.:

    # не нашел пока решения, как отделить последнюю строку от других, думаю
    for key, val in line.items():
        row += f'{key}:{val}\t'

    # else:
    #     for key, val in line.items():
    #         row += f'{key}:{val}'

    print(row)
