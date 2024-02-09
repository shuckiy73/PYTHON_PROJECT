import time


def validate_age(min_age, max_age):
    def decorator(func):
        def inner(*args, **kwargs):
            new_args = []
            for arg in args:
                new_arg = None
                if type(arg) == int and min_age <= arg <= max_age:
                    new_arg = arg
                new_args.append(new_arg)
            res = func(*new_args, **kwargs)
            return res

        return inner
    return decorator


@validate_age(min_age=1, max_age=90)
def register_age(age1, age2):
    print('Загружаем информацию')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('..')
    time.sleep(0.5)
    print('..')
    time.sleep(0.5)
    print('...')
    time.sleep(0.5)
    print('....')
    print(f'Возраст {age1}, {age2} сохранён в базу данных')


register_age(10, '14314124')
register_age('rggrgrr', 999)
register_age(20, 10)
register_age(-1, 91)
