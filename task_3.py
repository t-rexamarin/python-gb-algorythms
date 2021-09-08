# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

input_txt = 'Введите число цифрами: '
number = input(input_txt)
while number.isdigit() is False:
    print('Вы ввели не число')
    number = input(input_txt)

number_reversed = []
number = int(number)
while number > 0:
    number_reversed.append(number % 10)
    number //= 10

# number_reversed.reverse()
print(''.join(map(str, number_reversed)))
