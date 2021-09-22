# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
#   в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# 2 урок, задание 2
# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

# python 3.6 os 64
from pympler import tracker
from sys import getsizeof

track_str = tracker.SummaryTracker()
numbers = '346854662669584569836569516934596823687234659362956239' * 100
# 5449. len(numbers) = 54 * 100  = 5400 + 49
# print(getsizeof(numbers))
# методичке указано, что для 64 os str = 37+длинна
# но если запросить getsizeof(str()), то вернет 49 (не учитывая длинну). Особенность версий питона?

number_to_count = '5'
# 50 = 49 + len(number_to_count) = 49 + 1
# print(getsizeof(number_to_count))

number_count = numbers.count(number_to_count)
# 50 = 49 + len(number_count) = 49 + 1
# print(getsizeof(number_to_count))

# 5449 + 50 + 50 = 5549 байта, что не вяжется ни с одним из показателей ниже
# я не понимаю как это все считается

track_str.print_diff()
#                      types |   # objects |    total size
# ========================== | =========== | =============
#                       list |        4200 |     394.01 KB
#                        str |        4158 |     290.27 KB
#                        int |         929 |      25.40 KB
#                       dict |           2 |     632     B
#      function (store_info) |           1 |     136     B
#                       cell |           2 |      96     B
#   functools._lru_list_elem |           1 |      80     B
#                     method |          -1 |     -64     B
#                       code |          -7 |   -1008     B
#                      tuple |         -30 |   -2648     B
