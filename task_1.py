# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

msg = 'Введите трехзначное число цифрами: '
my_number = input(msg)

# отрицательная логика - это боль
# True and False = False
# True or False = True
# пока выполняется хотя бы одно из условий зацикливаем на ввод
# на лекции вы упоминали, что циклы без явного прерывания - это н еочень хорошо
#  можно конечно было бы сделать счетчик попыток, но не стал
while len(my_number) != 3 or my_number.isdigit() is False:
    my_number = input(msg)

my_arr = [int(digit) for digit in my_number]
my_arr_sum = sum(my_arr)

my_arr_mult = 1
for x in my_arr:
    my_arr_mult *= x

print(f'Сумма цифр числа {my_number} - {my_arr_sum}')
print(f'Произведение цифр числа {my_number} - {my_arr_mult}')
