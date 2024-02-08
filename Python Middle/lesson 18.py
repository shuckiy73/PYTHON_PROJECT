# pip install XlsxWriter
# pip install pandas
# pip install openpyxl

# +1. Регистриация и вход в прилжение по логину и паролю
# +2. Решение тестов и получение отметок
# +3. Сохранение в xls журнала отметок
# +4. Функции для статистики по ученикам для администратора
# +а) Средний бал всех учеников и общий средний балл по школе
# +б) Перечень всех отметок по ученику
# +5. Подргузка отметок при запуске

import datetime
import random
import xlsxwriter
import pandas
import os

STUDENTS_FILE_NAME = 'marks.xlsx'
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
        1: 'Средний бал всех учеников и общий средний балл по школе',
        2: 'Перечень всех отметок по ученику',
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
    number1 = random.randint(1, 10)
    znak = ['-', '+', '*'][random.randint(0, 2)]
    number2 = random.randint(1, 10)
    question = f'{number1} {znak} {number2}'
    return question, eval(question)


def start_test(login):
    right_answers = 0
    for i in range(1, 6):
        try:
            question, answer = generate_random_test()
            print(f'Реши пример: {question}')
            user_answer = int(input('Ваш ответ: '))
            if answer == user_answer:
                right_answers += 1
        except Exception as e:
            print('Вы ввели ерунду и потеряли шанс получить баллы')

    mark = right_answers * 2
    if login in students:
        students[login].append((datetime.datetime.now(), mark))
    else:
        students[login] = [(datetime.datetime.now(), mark)]
    print(f'Твоя отметка: {mark}')


def save_data():
    workbook = xlsxwriter.Workbook(STUDENTS_FILE_NAME)
    bold = workbook.add_format({'bold': True})
    for student, marks in students.items():
        worksheet = workbook.add_worksheet(student)
        worksheet.write('A1', 'Дата', bold)
        worksheet.write('B1', 'Отметка', bold)
        counter = 2
        for mark in marks:
            worksheet.write(f'A{counter}', str(mark[0])[:16])
            worksheet.write(f'B{counter}', mark[1])
            counter += 1
    workbook.close()


def show_student_info():
    student_name = input('Введите имя ученика: ')
    if student_name in students.keys():
        to_print = f'Все отметки ученика: {student_name}\n'
        marks = students[student_name]
        for counter, mark in enumerate(marks):
            to_print += f'{counter}. {mark[1]}  ->  {mark[0]}\n'
        print(to_print)
    else:
        print(f'Студента с именем {student_name} не существует')


def show_average_info():
    to_print = 'Средний бал всех учеников:\n'
    counter = 1
    by_school_marks_sum = 0
    by_school_marks_count = 0
    for name, marks in students.items():
        int_marks = list(map(lambda el: el[1], marks))
        to_print += f'{counter}. {name}: {sum(int_marks) / len(int_marks)}\n'
        counter += 1
        for mark in marks:
            by_school_marks_count += 1
            by_school_marks_sum += mark[1]
    to_print += f'Средний по школе {round(by_school_marks_sum / by_school_marks_count, 2)}, всего {by_school_marks_count} отметок'
    print(to_print)


def show_menu(access_role, login):
    while True:
        current_menu = MENU[access_role]
        print(current_menu)
        try:
            chosen_item = int(input('Выберите пункт меню: '))
            if access_role == STUDENT_ACCESS and chosen_item == 1:
                start_test(login)
            elif access_role == ADMIN_ACCESS and chosen_item == 10:
                print('Программа заверишила работу')
                return
            elif access_role == STUDENT_ACCESS and chosen_item == 10:
                print('Все данные успешно сохранены')
                save_data()
                return
            elif access_role == ADMIN_ACCESS and chosen_item == 1:
                show_average_info()
            elif access_role == ADMIN_ACCESS and chosen_item == 2:
                show_student_info()
        except Exception as e:
            print('Такого пункта в меню не существует')


def load_students():
    if os.path.exists(STUDENTS_FILE_NAME):
        xlsx_data = pandas.ExcelFile(STUDENTS_FILE_NAME)
        for sheet in xlsx_data.sheet_names:
            df1 = pandas.read_excel(xlsx_data, sheet)
            marks = df1.values.tolist()
            students[sheet] = list(
                map(
                    lambda el:
                    (
                        datetime.datetime(
                            year=int(el[0][:4]),
                            month=int(el[0][5:7]),
                            day=int(el[0][8:10]),
                            hour=int(el[0][11:13]),
                            minute=int(el[0][14:16]),
                            second=0
                        ),
                        el[1]),
                    marks
                )
            )


def run_study_program():
    load_students()
    access_role, login = check_is_registered()
    if access_role != INVALID_CREDENTIALS:
        show_menu(access_role, login)
    else:
        print('Ты не смог залогиниться в программе')


run_study_program()
