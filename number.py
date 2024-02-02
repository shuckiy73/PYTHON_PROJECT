# numbers = list(range(1, 101))
# str_result = ''
# for number1 in numbers:
#     for number2 in numbers:
#         str_result += f"{number1 * number2}\t"
#     str_result += '\n'
# print(str_result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
str_result = ''
for number1 in numbers:
    for number2 in numbers:
        str_result += f"{number1 * number2}\t"
    str_result += '\n'
print(str_result)


numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number * 1, number * 2, number * 3, number * 4, number * 5)
