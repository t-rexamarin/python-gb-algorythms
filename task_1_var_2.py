# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
#   в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# 2 урок, задание 2
# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

# python 3.6 os 64

from guppy import hpy  # https://github.com/zhuyifei1999/guppy3
from sys import getsizeof


hp = hpy()
before = hp.heap()

# 5449 bytes
numbers = '346854662669584569836569516934596823687234659362956239' * 100
# 50 bytes
number_to_count = '5'
# 28 bytes
number_to_cnt = numbers.count(number_to_count)
# print(number_to_cnt, getsizeof(number_to_cnt))

after = hp.heap()
leftover = after - before
print(leftover)

# тут значения чуть ближе, но все равно не понимаю как это считается
# Partition of a set of 3 objects. Total size = 5909 bytes.
#  Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
#      0      1  33     5449  92      5449  92 str
#      1      1  33      432   7      5881 100 types.FrameType
#      2      1  33       28   0      5909 100 int
