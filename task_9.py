# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

rows = 4
column = 4
int_min = 0
int_max = 10

matrix = [[randint(int_min, int_max) for _ in range(rows)] for _ in range(column)]
# matrix = [[10, 4, 0, 9], [7, 2, 10, 5], [10, 8, 7, 10], [2, 2, 0, 1]]
dict_of_columns = {}

print(matrix)

# не самое простое и очевидное решение проблемы :) но пришло в голову только такое
# я собираю словарь, где по индексам из строк матрицы собираю значения столбцов
# ключ - индекс значения столбца
for row in matrix:
    # [3, 0, 6, 6]
    for i in range(len(row)):
        if dict_of_columns.get(row.index(row[i])):
            dict_of_columns[i] += [row[i]]
        else:
            dict_of_columns[i] = [row[i]]

print(dict_of_columns)

mins_of_columns = [min(value) for key, value in dict_of_columns.items()]
# mins_of_columns = []
# for key, value in dict_of_columns.items():
#     mins_of_columns.append(min(value))

max_of_mins = max(mins_of_columns)

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_of_mins}')
