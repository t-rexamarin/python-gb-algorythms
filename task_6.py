# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше
#   введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

from random import randint

int_start = 1
int_end = 100
number_to_guess = randint(int_start, int_end)
MAX_GUESS_TRY = 10
guess_count = MAX_GUESS_TRY
print(number_to_guess)

while guess_count > 0:
    player_guess = input(f'Отгадайте число от {int_start} до {int_end}: ')
    # проверки?
    player_guess = int(player_guess)

    if player_guess == number_to_guess:
        guess_count -= 1  # роли играть не должно, но считаю, что по правильному надо вычитать попытку
        print('Вы отгадали число.')
        break
    elif player_guess > number_to_guess:
        guess_count -= 1
        print(f'Загаданное число меньше {player_guess}. У вас осталось {guess_count} попыток.')
    else:
        guess_count -= 1
        print(f'Загаданное число больше {player_guess}. У вас осталось {guess_count} попыток.')
else:
    print(f'Вам было дано {MAX_GUESS_TRY} попыток, вы не смогли угадать число.'
          f'Загаданное число - {number_to_guess}')
