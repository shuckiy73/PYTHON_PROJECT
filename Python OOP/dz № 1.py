
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = None

    def set_nickname(self, name):
        self.nickname = name

    @staticmethod
    def suitable_age(age):
        return 6 <= age <= 70

    @staticmethod
    def add_nickname(func):
        def wrapper(self, age):
            result = func(self, age)
            if result:
                print(f"{self.first_name} подходит по возрасту и логину {self.nickname}")
            else:
                print(f"{self.first_name} не подходит по возрасту")

        return wrapper

    @classmethod
    def check_suitable_age(cls, age):
        return cls.suitable_age(age)


print(Student.suitable_age(99))  # False
print(Student.suitable_age(27))  # True
s = Student('dima', 'junior')
s.set_nickname('DS')
s.check_suitable_age(51)
