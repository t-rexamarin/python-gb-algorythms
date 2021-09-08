# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

# как строка
numbers = input('Введите длинное число (последовательнось): ')
number_to_count = input('Введите цифру, которую будем считать в последователньости: ')
number_count = numbers.count(number_to_count)

print(number_count)

# как число
number_count = 0
numbers = int(numbers)
number_to_count = int(number_to_count)
while numbers:
    if numbers % 10 == number_to_count:
        number_count += 1

    numbers //= 10

print(number_count)
