import time
import random


def generate_random_znak():
    znaks = ['*', '/', '+', '-']
    random_znak = znaks[random.randint(0, 3)]
    return random_znak


def generate_random_number(from_number, to_number):
    if from_number < 0 or to_number < 0:
        return None
    return random.randint(from_number, to_number)


def calculate_expression(num1, znak, num2):
    if num1 is None or num2 is None:
        print('Ученики ещё не проходили отрицательные числа')
    elif znak == '+':
        print(f'{num1} {znak} {num2} = {num1 + num2}')
    elif znak == '-':
        print(f'{num1} {znak} {num2} = {num1 - num2}')
    elif znak == '*':
        print(f'{num1} {znak} {num2} = {num1 * num2}')
    elif znak == '/':
        print(f'{num1} {znak} {num2} = {num1 / num2}')
    else:
        print(f'Знак {znak} не поддерживается текущей версией программы')


def do_lesson_stage(text_to_print, time_to_sleep=1):
    print(text_to_print)
    time.sleep(time_to_sleep)


do_lesson_stage('1. Урок МАТЕМАТИКИ начался')
do_lesson_stage('2. Вовочка начал решать пример')
calculate_expression(
    generate_random_number(1, 50),
    generate_random_znak(),
    generate_random_number(1, 50)
)
time.sleep(1)
do_lesson_stage('8. Маша начала решать пример')
calculate_expression(
    generate_random_number(1, 100),
    generate_random_znak(),
    generate_random_number(10, 100)
)
time.sleep(1)
do_lesson_stage('10. Урок закончился')
