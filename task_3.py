# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
#   которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

# n / 2 раз - мое решение
# брать значение и смотреть сколько больше сколько меньше, и если они равны
# граничные значение если несколько одлинаковых значений медиан

from random import randint, seed

m = 2
size = 2 * m + 1

# seed(3)
seed(2)
numbers = [randint(1, 100) for i in range(size)]
print(numbers)
# print(len(numbers))
print(sorted(numbers), sum(numbers), sum(numbers) // len(numbers))

med_index = (len(numbers) // 2) + 1
print(f'длинна {len(numbers)}, индекс медианы {med_index}')
# min_val = min(numbers)
# print(f'min {min_val}')

# вариант 1
# сложность n / 2
# mediana = None
# while med_index:
#     min_val = numbers.index(min(numbers))
#     print(min_val)
#     # numbers.pop(min_val)
#     mediana = numbers.pop(min_val)
#     med_index -= 1

# вариант 2
# брать значение и смотреть сколько больше сколько меньше, и если они равны
mediana = numbers[0]
count_stop = len(numbers) // 2
i_count_more = 0
i_count_less = 0

for i in numbers[1:]:
    for t in numbers[1:]:
        if i_count_more <= count_stop and i_count_less <= count_stop:
            if mediana < t:
                i_count_more += 1
            else:
                i_count_less += 1
        elif i_count_more > count_stop or i_count_less > count_stop:
            i_count_more = 0
            i_count_less = 0

    if i_count_more == count_stop == i_count_less:
        print(f'mediana {i}')
        iter_stop = 1
        break

    mediana = i



    # print(i, i_count_more, i_count_less)
# print(mediana)
