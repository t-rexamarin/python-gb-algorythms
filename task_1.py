# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

from random import choice
from string import ascii_lowercase
import hashlib

str_len = 10
start_str = ''.join([choice(ascii_lowercase) for i in range(str_len)])
# start_str = 'aabbaa'
# start_str = 'aaaaaa'
print(f'start str: {start_str}')


def func_var1(my_str):
    # долго пытался сообразить как написать, в итоге списал с интернета :(
    # вроде элементарная вещь, но не смог обмозговать
    res = set([my_str[i: j] for i in range(len(my_str)) for j in range(i + 1, len(my_str) + 1)])
    # print(res, len(res))

    set_of_strs = []
    for string in res:
        if hashlib.sha1(string.encode('utf-8')) not in set_of_strs:
            set_of_strs.append(string)

    return len(set_of_strs)


def func_var2(my_str):
    # для проверки, строки как они есть
    list_of_raw_strs = []
    # итоговый, нас интересует он
    list_of_strs = []

    for i in range(len(my_str)):
        for j in range(i + 1, len(my_str) + 1):
            str_hash = hashlib.sha1(my_str[i:j].encode('utf-8')).hexdigest()
            # для проверки
            raw_str = my_str[i:j]

            if str_hash not in list_of_strs:
                list_of_strs.append(str_hash)
                list_of_raw_strs.append(raw_str)

    # для проверки
    # print(list_of_strs, len(list_of_strs))
    # print(list_of_raw_strs, len(list_of_raw_strs))

    return len(list_of_strs)


print(f'first func: {func_var1(start_str)}')
print(f'second func: {func_var2(start_str)}')
