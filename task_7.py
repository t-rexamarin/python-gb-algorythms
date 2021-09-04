# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

side_err_msg = 'Сторона должна быть больше нуля.'
side_a_txt = 'Длинна стороны A: '
side_b_txt = 'Длинна стороны B: '
side_c_txt = 'Длинна стороны C: '

side_a = input(side_a_txt)
while side_a.isdigit() is False or int(side_a) <= 0:
    print(side_err_msg)
    side_a = input(side_a_txt)

side_b = input(side_b_txt)
while side_b.isdigit() is False:
    print(side_err_msg)
    side_b = input(side_b_txt)

side_c = input(side_c_txt)
while side_c.isdigit() is False:
    print(side_err_msg)
    side_c = input(side_c_txt)

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    if side_a == side_c == side_b:
        print('Равносторонний')
    elif (side_a == side_b and side_a != side_c)\
            or (side_a == side_c and side_a != side_b)\
            or (side_b == side_c and side_b != side_a):
        print('Равнобедренный')
    else:
        print('Разносторонний')
else:
    print(f'Невозможно построить треугольник из сторон {side_a}, {side_a} и {side_c}')
