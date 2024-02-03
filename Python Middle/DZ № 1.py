# 1. Написать функцию, которая принимает 2 параметра: число часов и число минут и выводит число секунд на экран
def get_to_seconds(hours, minutes):
 return (hours * 3600) + (minutes * 60)

hours = int(input("Введите число часов: "))
minutes = int(input("Введите число минут: "))

seconds = hours * 3600 + minutes * 60
# seconds = hours_to_seconds(hours, minutes)
print(seconds)

# 2. Написать функцию, которая принимает 2 параметра и возвращает список чисел от первого до второго
def get_range(from_number, to_number):
    numbers = []
    for i in range(first, second + 1):
        numbers.append(i)
    return numbers

first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
result = get_range(first, second)

for number in result:
    print(number)

# # 3. Написать функцию, которая принимает список чисел и возвращает наибольшее из чисел, встроенные функции использовать нельзя
def max_number(numbers):
    if len(numbers) == 0:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

numbers = [int(x) for x in input('Введите числа через пробел: ').split()]
print('Максимальное число:', max_number(numbers))
