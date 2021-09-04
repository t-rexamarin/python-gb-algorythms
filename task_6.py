# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
import string

msg = 'Введите номер буквы в алфавите числом: '
my_letter = input(msg)

while my_letter.isdigit() is False:
    my_letter = input(msg)

letters = string.ascii_lowercase
# letters_arr = []
# for char in letters:
#     letters_arr.append(char)
letters_arr = [char for char in letters]

try:
    letter_by_number = letters_arr[int(my_letter) - 1]
    print(letter_by_number)
except IndexError:
    err_msg = f'В алфавите нет буквы под номером {my_letter}. Диапазон от 1 до {len(letters_arr)}.'
    print(err_msg)

