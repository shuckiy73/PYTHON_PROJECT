# 1. Найти сумму цифр числа, кроме самой левой цифры(Самый старший разряд)
def sum_of_digits_excluding_first(number):
    digits = [int(d) for d in str(number)][1:]  # Преобразуем число в список цифр, удаляем первую цифру
    result = sum(digits)  # Находим сумму цифр
    return result

# Пример использования
number = 98765
result = sum_of_digits_excluding_first(number)
print(f"Сумма цифр числа {number}, за исключением самой левой цифры, равна {result}")
print('=' * 10)

# 2. Найти минимальное нечётное число из случайного набора чисел(Сгенерировать случайный набор чисел)
import random

# Генерируем случайный набор чисел
random_numbers = [random.randint(1, 100) for _ in range(10)]

min_odd_number = None
# Находим минимальное нечётное число
for number in random_numbers:
    if number % 2 != 0:
        if min_odd_number is None or number < min_odd_number:
            min_odd_number = number

print("Случайный набор чисел:", random_numbers)
print("Минимальное нечётное число:", min_odd_number)
print('=' * 10)


# 3. ДЗ. Отсортировать список от большему к меньшему не используя функцию sort()

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Пример использования
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = insertion_sort(my_list)
print(sorted_list)
