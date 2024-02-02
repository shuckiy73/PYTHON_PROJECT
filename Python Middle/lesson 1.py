import time


def calculate_expression():
    num1 = int(input('Введите число 1: '))
    znak = input('Введите знак: ')
    num2 = int(input('Введите число 2: '))
    if znak == '+':
        print(f'{num1} {znak} {num2} = {num1 + num2}')
    elif znak == '-':
        print(f'{num1} {znak} {num2} = {num1 - num2}')
    elif znak == '*':
        print(f'{num1} {znak} {num2} = {num1 * num2}')
    elif znak == '/':
        print(f'{num1} {znak} {num2} = {num1 / num2}')
    else:
        print(f'Знак {znak} не поддерживается текущей версией программы')


print('1. Урок литературы начался')
time.sleep(1)
print('2. Учитель спросил про домашку')
time.sleep(1)
print('3. В классе тишина, никто не сделал домашку')
time.sleep(1)
print('4. Учитель разозлился и вызвал к доске Вовочку')
time.sleep(1)
print('5. Вовочка начал решать пример')
time.sleep(1)
calculate_expression()
time.sleep(1)
print('6. Вовочка получил 2 балла')
time.sleep(1)
print('7. Учитель вызвал Машу')
time.sleep(1)
print('8. Маша начала решать пример')
time.sleep(1)
calculate_expression()
print('9. Маша получила 5')
time.sleep(1)
print('10. Урок закончился')
time.sleep(1)
