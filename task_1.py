# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

numbers_start = 2
numbers_end = 99
numbers = [i for i in range(numbers_start, numbers_end + 1)]

divisor_start = 2
divisor_end = 9
divisors = [d for d in range(divisor_start, divisor_end + 1)]

result_arr = {}

for d in divisors:
    count = 0
    for i in numbers:

        if i % d == 0:
            count += 1
    result_arr[d] = count

# print(numbers)
print(result_arr)
