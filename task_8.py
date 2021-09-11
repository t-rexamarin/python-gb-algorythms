# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

from random import randint

rows = 4
column = 4
int_min = 0
int_max = 10

matrix = [[randint(int_min, int_max) for _ in range(rows)] for _ in range(column)]

# в каждую строку добавляем новый элемент, где лежит сумма
for row in matrix:
    row.append(sum(row))

print(matrix)

# если матрица не пуста, собираем результрующую строку
# для последней строки не ставится элемент '\n'
result_row = ''
if len(matrix) > 0:
    for row in matrix[:-1]:
        result_row += '\t'.join(map(str, row)) + '\n'
    for row in matrix[-1:]:
        result_row += '\t'.join(map(str, row))

print(result_row)
