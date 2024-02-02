def number_plus1(number):
    result = number + 1
    print(result)
    return result


def number_plus2(number):
    plus_number = number + 2
    print(plus_number)
    result = number_plus1(plus_number)
    return result


def number_plus3(number):
    plus_number = number + 3
    print(plus_number)
    result = number_plus2(plus_number)
    return result


def number_x2(number):
    x2_number = number * 2
    print(x2_number)
    result = number_plus3(x2_number)
    return result


print(number_x2(2))


