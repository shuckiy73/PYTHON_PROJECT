# def sum_x2(num1, num2):
#     return (num1 + num2) * 2
#
#
# sum_x2_lambda = lambda num1, num2: (num1 + num2) * 2
# print((3 + 3) * 2)
# print(sum_x2(3, 3))
# print(sum_x2_lambda(3, 3))


# filter, map, sort
numbers = list(range(1, 100))
print(numbers)
# Classic
numbers2 = []
for number in numbers:
    if number % 2 == 0:
        numbers2.append(number)
print(numbers2)
# Lambda
numbers3 = list(filter(lambda number: number % 2 == 0, numbers))
print(numbers3)
# filter with classic function
def filter_function(number):
    return number % 2 == 0
numbers4 = list(filter(filter_function, numbers))
print(numbers4)


# numbers = list(range(1, 1000))
# print(numbers)
# numbers2 = list(filter(lambda number: number % 2 == 0, numbers))
# numbers3 = list(filter(lambda number: number % 10 == 0, numbers2))
# numbers4 = list(filter(lambda number: number % 5 == 0, numbers3))
# numbers5 = list(filter(lambda number: number % 100 == 0, numbers4))
# print(numbers5)
