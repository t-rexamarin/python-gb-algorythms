# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint, seed
seed(1)
numbers = [randint(-5, 5) for _ in range(1, 11)]

negative_numb_dict = {k: v for k, v in enumerate(numbers) if v < 0}
max_negative_val = max(negative_numb_dict.values())
max_negative_key = list(negative_numb_dict.keys())[list(negative_numb_dict.values()).index(max_negative_val)]

print(numbers)
print(negative_numb_dict)
print(f'Максимальное отрицательное число: {max_negative_val}.\n'
      f'Его индекс: {max_negative_key}.')
