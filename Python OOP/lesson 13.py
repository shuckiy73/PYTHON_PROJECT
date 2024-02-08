import time
import requests


def check_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        finish_time = time.time()
        print(f'Функция выполнилась за {finish_time - start_time} секунд')
        return res

    return inner


@check_time
def f1():
    print('111111')
    time.sleep(3)
    print('222222')
# f1()


@check_time
def fibonachi(num):
    if num in [1, 2]:
        return num
    return fibonachi(num - 1) + fibonachi(num - 2)
# print(fibonachi(25))


@check_time
def f3():
    res = requests.get('https://www.google.by/')
    res1 = requests.get('https://www.google.by/')
    res2 = requests.get('https://www.google.by/')
f3()
