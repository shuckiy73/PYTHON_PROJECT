import time
import traceback

data = ['a', 'b', 'Андрей']

# # 1. Проверка количества элементов
# if len(data) >= 6:
#     print(data[6])
# else:
#     print('В списке меньше 6 элементов')

# 2. С обраткой исключений
try:
    print(data[6])
    # 1 / 0
    # print()
except (ArithmeticError, IndexError):
    print('ArithmeticError или IndexError')
except Exception as e:
    print('Другая ошибка')
else:
    print('Ошибок не было')
finally:
    print('Блок finally')

print('Следующая строчка кода')


def f1(n1, n2):
    try:
        print('try')
        return n1 / n2
    except:
        print('except')
        return 0
    finally:
        print('finally')


print(f1(1, 2))
