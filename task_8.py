# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = input('Введите год цифрами: ')
while year.isdigit() is False:
    year = input('Введите год цифрами: ')

year = int(year)
if year % 4 != 0:
    print(f'{year} год НЕвисокостный')
elif year % 100 == 0:
    if year % 400 == 0:
        print(f'{year} год високостный')
    else:
        print(f'{year} год НЕвисокостный')
else:
    print(f'{year} год високостный')
