# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать
#   ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

def input_check(operand1, operand2, operator):
    if operand1.isdigit() is False:
        msg = f'Первый операнд должен быть числом. Вы ввели "{operand1}", тип {type(operand1)}'
        return msg
    elif operand2.isdigit() is False:
        msg = f'Второй операнд должен быть числом. Вы ввели "{operand2}", тип {type(operand2)}'
        return msg
    elif operator not in operations:
        new_operation = input(f"Вы ввели неверный оператор - {operator}.\n"
                              f"Выберите действие из {', '.join(operations)} (0 - выход): ")
        # забавно, что мне пришла в голову идея сделать тут рекурсию
        # не знаю на сколько это оправдано, но работает как надо
        result = input_check(operand1, operand2, new_operation)
        return result
    else:
        if operator == '0':
            msg = 'Выход из программы'
            return msg
        else:
            result = count(operand1, operand2, operator)
            return result


# обработать float?
def count(operand1, operand2, operator):
    operand1 = int(operand1)
    operand2 = int(operand2)
    # try except?

    if operator == '+':
        result = operand1 + operand2
        return result
    elif operator == '-':
        result = operand1 - operand2
        return result
    elif operator == '*':
        result = operand1 * operand2
        return result
    else:
        if operand2 == 0:
            msg = 'На 0 делить нельзя!'
            return msg
        else:
            result = operand1 / operand2
            return result


operation = None
while operation != '0':
    operations = ('0', '+', '-', '*', '/')
    numb1 = input('Введите первое число: ')
    numb2 = input('Введите второе число: ')
    operation = input(f"Выберите действие из {', '.join(operations)} (0 - выход): ")

    print(input_check(numb1, numb2, operation))
