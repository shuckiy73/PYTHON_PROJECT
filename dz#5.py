# 1.ДЗ. Вывести на экран произведение чисел от -10 до 7
result = 1
for i in range(-10, 8):
    result *= i
print(result)
print('=' * 10)

# 2. ДЗ. Найти сумму чётных чисел от N до M, включая N и M, где N и M вводятся через input(). Учесть условие когда первое число больше второго
N = int(input("Введите N: "))
M = int(input("Введите M: "))
if N > M:
    N, M = M, N  # Если N больше M, меняем их местами
sum_even = 0
for i in range(N, M + 1):
    if i % 2 == 0:
        sum_even += i
print(f"Сумма чётных чисел от {N} до {M} равна {sum_even}.")
print('=' * 10)
# 3. ДЗ. Найти количество кратных 10 (10, 20, 30 ...) чисел в списке
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
count = 0
for number in numbers:
    if number % 10 == 0:
        count += 1
print("Количество кратных 10 чисел в списке:", count)
print('=' * 10)
# 4.  ДЗ. Вывести первые 7 степеней числа 3
base = 3
for i in range(1, 8):
    result = base ** i
    print(f"{base} в степени {i} равно {result}")
