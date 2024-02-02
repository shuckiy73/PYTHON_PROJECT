# 1. Найти сумму цифр числа
number = 2345
sum_res = 0
number = abs(number)
while number != 0:
    division_res = number % 10
    print('Остаток: ', division_res)
    sum_res += division_res
    number = int(number / 10)
    print('Число', number)

print('Сумма цифр числа = ', sum_res)
print('=' * 10)

# 2. Найти максимальное чётное число из случайного набора чисел(Сгенерировать случайный набор чисел)
import random

numbers = []
counter = 0
while counter < 10:
    numbers.append(random.randint(1, 1000))
    counter += 1
max_number = -99999999999999999999999999999
for number in numbers:
    if number > max_number:
        max_number = number
print(numbers)
print(max_number)
print(sorted(numbers)[-1])
print('=' * 10)

# 3. Отсортировать список от меньшего к большему не используя функцию sort()
# ДЗ. Отсортировать список от большему к меньшему не используя функцию sort()
import random
numbers = []
numbers_sorted = []
counter = 0
while counter < 10:
    numbers.append(random.randint(1, 1000))
    counter += 1
print(numbers)
while len(numbers) != 0:
    min_number = 9999999999
    for number in numbers:
        if number < min_number:
            min_number = number
    numbers.remove(min_number)
    numbers_sorted.append(min_number)
print(numbers_sorted)

