# a, b, *c = ['a', 'b', 'c','d']
# print(a)
# print(b)
# print(c)


# nums = [1, 10]
# print(list(range(1, 5)))
# print(list(range(*nums)))


# print(1, 2, 3)


# def ab(a, b):
#     print(a, b)
# elems = ['a', 'b']
# ab('a', 'b')
# ab(*elems)

#
# def super_sum1(numbers):
#     res = 0
#     for number in numbers:
#         res += number
#         print(f'Сумма = {res}')
# super_sum1([1, 2, 3, 4, 5])
# print('=' * 80)
#
# def super_sum2(*numbers):
#     res = 0
#     for number in numbers:
#         res += number
#         print(f'Сумма = {res}')
# super_sum2(1, 2, 3, 4, 5)
# print('=' * 80)


# print(1, 2, 3, 4)
# print(1, 2, 3, 4, sep='\n')


def func(arg1, arg2, *args, **kwargs):
    print(arg1)
    print(arg2)
    print(args)
    print(kwargs)


func(
    1, 2, 'a', 'b', 'EEEEEEE', [1, 2, 3],
    key1='123', key2='abc', key3='123'
)
