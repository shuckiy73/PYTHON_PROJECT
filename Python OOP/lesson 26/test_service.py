import traceback

from utils import Utils
import datetime


class TestService:
    RETURN_STATUS = "STOP"

    def __init__(self, repo):
        self.repo = repo

    @staticmethod
    def start_test(student):
        right_answers = 0
        for i in range(1, 6):
            try:
                question, answer = Utils.generate_random_test()
                print(f'Реши пример: {question}')
                user_answer = int(input('Ваш ответ: '))
                if answer == user_answer:
                    right_answers += 1
            except Exception as e:
                print('Вы ввели ерунду и потеряли шанс получить баллы')

        mark = right_answers * 2
        student.marks.append((datetime.datetime.now(), mark))
        print(f'Твоя отметка: {mark}')

    @staticmethod
    def show_student_info(student_name, students):
        if student_name in students.keys():
            to_print = f'Все отметки ученика: {student_name}\n'
            data = students[student_name]
            for counter, mark in enumerate(data.marks):
                to_print += f'{counter}. {mark[1]}  ->  {mark[0]}\n'
            print(f"{'=' * 80}\n{to_print}\n{'=' * 80}")
        else:
            print(f"{'=' * 80}\nСтудента с именем {student_name} не существует\n{'=' * 80}")

    @staticmethod
    def show_average_info(students):
        to_print = 'Средний бал всех учеников:\n'
        counter = 1
        by_school_marks_sum = 0
        by_school_marks_count = 0
        for name, data in students.items():
            int_marks = list(map(lambda el: el[1], data.marks))
            to_print += f'{counter}. {name}: {sum(int_marks) / len(int_marks) if len(int_marks) != 0 else "Нету отметок"}\n'
            counter += 1
            for mark in data.marks:
                by_school_marks_count += 1
                by_school_marks_sum += mark[1]
        to_print += f'Средний по школе {round(by_school_marks_sum / by_school_marks_count, 2)}, всего {by_school_marks_count} отметок'
        to_print = f"{'=' * 80}\n{to_print}\n{'=' * 80}"
        print(to_print)

    def students_menu(self, student, students):
        chosen_item = input('Выберите пункт меню: ')
        if chosen_item == "1":
            TestService.start_test(student)
        elif chosen_item == "10":
            print('Все данные успешно сохранены')
            self.repo.save_data(students)
            return self.RETURN_STATUS

    def admins_menu(self, students):
        chosen_item = input('Выберите пункт меню: ')
        if chosen_item == "1":
            self.show_average_info(students)
        elif chosen_item == "2":
            student_name = input('Введите имя ученика: ').lower()
            self.show_student_info(student_name, students)
        elif chosen_item == "10":
            print('Программа заверишила работу')
            return self.RETURN_STATUS

    def show_menu(self, students, student, config):
        while True:
            current_role = student.role
            current_menu = config[current_role]
            print(current_menu)
            try:
                if current_role == Utils.STUDENT_ACCESS:
                    res = self.students_menu(student, students)
                elif current_role == Utils.ADMIN_ACCESS:
                    res = self.admins_menu(students)
                else:
                    res = self.RETURN_STATUS
                if res == self.RETURN_STATUS:
                    return
            except Exception as e:
                traceback.print_exc()
                print('Такого пункта в меню не существует')

    def try_to_show_menu(self, students, student, config):
        self.show_menu(students, student, config) if student is not None else print(
            'Ты не смог залогиниться в программе')
