# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
# после разбора на уроке, понял, что тут я сделал не совсем так, как предполагалось :)
import string

start_msg = 'Введите первую букву: '
end_msg = 'Введите вторую букву: '
start_letter = input(start_msg).lower()
end_letter = input(end_msg).lower()

while ord(end_letter) < ord(start_letter):
    print('Вторая буква не может быть раньше первой.')
    start_letter = input(start_msg)
    end_letter = input(end_msg)

POSITION_SHIFT = 1
start_letter_position = string.ascii_lowercase.index(start_letter) + POSITION_SHIFT
end_letter_position = string.ascii_lowercase.index(end_letter) + POSITION_SHIFT
letters_spacing = end_letter_position - start_letter_position

print(f'Первая буква {start_letter}. Место в алфавите {start_letter_position}.')
print(f'Вторая буква {start_letter}. Место в алфавите {end_letter_position}.')
print(f'Расстояние между буквами {letters_spacing}.')
