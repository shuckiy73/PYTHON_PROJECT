# +1. Регистрация и вход в приложение по логину и паролю
# +2. Решение тестов и получение отметок
# +3. Сохранение в xls журнала отметок
# -4. Функции для статистики по ученикам для администратора
# -а) Средний бал всех учеников и общий средний балл по школе
# -б) Перечень всех отметок по ученику
# -5. Подгрузка отметок при запуске

import datetime
import random
import xlsxwriter

ADMIN_ACCESS = 'ADMIN_ACCESS'
STUDENT_ACCESS = 'STUDENT_ACCESS'
INVALID_CREDENTIALS = 'INVALID_CREDENTIALS'
logins = {
    'admin': ('12345', ADMIN_ACCESS),
    'мария': ('12345', STUDENT_ACCESS),
    'иван': ('12345', STUDENT_ACCESS),
    'гоша': ('12345', STUDENT_ACCESS)
}
MENU = {
    ADMIN_ACCESS: {
        1: 'Посмотреть статистику 1',
        2: 'Посмотреть статистику 2',
        10: 'Выйти'
    },
    STUDENT_ACCESS: {
        1: 'Пройти тест',
        2: 'Посмотреть свои отметки',
        10: 'Выйти и сохраниться'
    }
}
students = {}


def check_is_registered():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    if login.lower() in logins.keys():
        valid_password = logins[login.lower()][0]
        if password == valid_password:
            return logins[login.lower()][1], login
        else:
            return INVALID_CREDENTIALS, login
    else:
        return INVALID_CREDENTIALS, login


def generate_random_test():
    number1 = random.randint(1, 100)
    znak = ['-', '+', '*'][random.randint(0, 2)]
    number2 = random.randint(1, 100)
    question = f'{number1} {znak} {number2}'
    return question, eval(question)


def start_test(login):
    right_answers = 0
    for i in range(1, 6):
        question, answer = generate_random_test()
        print(f'Реши пример: {question}')
        user_answer = int(input('Ваш ответ: '))
        if answer == user_answer:
            right_answers += 1

    mark = right_answers * 2
    if login in students:
        students[login].append((datetime.datetime.now(), mark))
    else:
        students[login] = [(datetime.datetime.now(), mark)]
    print(f'Твоя отметка: {mark}')


def save_data():
    workbook = xlsxwriter.Workbook('marks.xlsx')
    bold = workbook.add_format({'bold': True})
    for student, marks in students.items():
        worksheet = workbook.add_worksheet(student)
        worksheet.write('A1', 'Дата', bold)
        worksheet.write('B1', 'Отметка', bold)
        counter = 2
        for mark in marks:
            worksheet.write(f'A{counter}', str(mark[0]))
            worksheet.write(f'B{counter}', mark[1])
    workbook.close()


def show_menu(access_role, login):
    while True:
        current_menu = MENU[access_role]
        print(current_menu)
        chosen_item = int(input('Выберите пункт меню: '))
        if access_role == STUDENT_ACCESS and chosen_item == 1:
            start_test(login)
        elif access_role == ADMIN_ACCESS and chosen_item == 10:
            print('Программа завершила работу')
            return
        elif access_role == STUDENT_ACCESS and chosen_item == 10:
            print('Все данные успешно сохранены')
            save_data()
            return


def run_study_program():
    access_role, login = check_is_registered()
    if access_role != INVALID_CREDENTIALS:
        show_menu(access_role, login)
    else:
        print('Ты не смог залогиниться в программе')


run_study_program()
