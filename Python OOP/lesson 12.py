

def hands_washer(func):
    def inner(*args, **kwargs):
        print('Моем руки')
        res = func(*args, **kwargs)
        print('Моем руки')
        return res

    return inner


def clear_eat2(func, meal1, meal2):
    print('Моем руки')
    res = func(meal1, meal2)
    print('Моем руки')
    return res


@hands_washer
def eat(meal1, meal2):
    print(f'Кушаю: {meal1}, {meal2}')
    return 'Приём пиши закончен'


# clear_eat = hands_washer(eat)
# print(clear_eat('Мясо', 'Пюре'))
print(eat('Мясо', 'Пюре'))
# print(clear_eat2(eat, 'Мясо', 'Пюре'))
