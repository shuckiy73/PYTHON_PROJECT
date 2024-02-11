import random


class Utils:
    ADMIN_ACCESS = 'ADMIN_ACCESS'
    STUDENT_ACCESS = 'STUDENT_ACCESS'

    @staticmethod
    def input_login_pass():
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        return login, password

    @staticmethod
    def check_is_registered(students, login, password):
        res = None
        if login.lower() in students.keys():
            student = students[login.lower()]
            valid_password = student.password
            if password == valid_password:
                res = student
        return res

    @staticmethod
    def generate_random_test():
        number1 = random.randint(1, 10)
        znak = ['-', '+', '*'][random.randint(0, 2)]
        number2 = random.randint(1, 10)
        question = f'{number1} {znak} {number2}'
        return question, eval(question)
