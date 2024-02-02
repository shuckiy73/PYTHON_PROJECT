import random

from_number = 1
to_number = 1000
number = random.randint(from_number, to_number)
user1 = input('Ваше имя игрок1: ')
user2 = input('Ваше имя игрок2: ')
print(f"Рыба карась, игра началась. [{from_number} - {to_number}]")

while True:
    number1 = int(input(f'{user1} ваш ход: '))
    if number1 == number:
        print(f'{user1} ПОБЕДИЛ!!! УРАА!!!')
        break
    elif number1 > number:
        print('Загаданное число меньше')
    else:
        print('Загаданное число больше')

    number2 = int(input(f'{user2} ваш ход: '))
    if number2 == number:
        print(f'{user2} ПОБЕДИЛ!!! УРАА!!!')
        break
    elif number2 > number:
        print('Загаданное число меньше')
    else:
        print('Загаданное число больше')
