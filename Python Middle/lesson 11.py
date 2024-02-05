menu = {
    1: 'Использовать калькулятор',
    2: 'Показать все операции',
    10: 'Выход'
}
operations_log = []
FILE_NAME = 'operations_archive.txt'


def calculate():
    number1 = int(input('Введите первое значение: '))
    znak = input('Введите первое знак: ')
    number2 = int(input('Введите второе значение: '))
    res = 'Что-то пошло не по плану'
    if znak == '+':
        res = f'{number1} {znak} {number2} = {number1 + number2}'
    elif znak == '-':
        res = f'{number1} {znak} {number2} = {number1 - number2}'
    elif znak == '*':
        res = f'{number1} {znak} {number2} = {number1 * number2}'
    elif znak == '/':
        res = f'{number1} {znak} {number2} = {number1 / number2}'
    print(res)
    operations_log.append(res)


def show_operations():
    print('=' * 80)
    for counter, operation in enumerate(operations_log):
        print(f"{counter + 1}. {operation}".replace('\n', ''))
    print('=' * 80)


def run():
    with open(FILE_NAME, 'r') as file:
        operations_log.extend(file.readlines())
    while True:
        print('Меню: ', menu)
        choose_menu_item = int(input('Выберите пункт из меню: '))
        if choose_menu_item == 1:
            calculate()
        elif choose_menu_item == 2:
            show_operations()
        elif choose_menu_item == 10:
            with open(FILE_NAME, "w") as file:
                for operation in operations_log:
                    file.write(operation.replace('\n', '') + '\n')
            return
        else:
            print('Такого пункта в меню не существует. Читай внимательнее')


run()
