from dataclasses import dataclass


class MainSaver:
    def __init__(self):
        print('MainSaver.__init__')
        super().__init__()

    def main_save(self):
        print(f'MainSaver {self}')



class XLSXSaver:
    def __init__(self):
        print('XLSXSaver.__init__')
        super().__init__()
        super().__init__()
    def save_to_excel(self):
        print(f'Сохранено в EXCEL: {self}')

    def main_save(self):
        print(f'XLSXSaver {self}')


class DbSaver:
    def __init__(self):
        print('DbSaver.__init__')
        super().__init__()

    def main_save(self):
        print(f'DbSaver {self}')


class Car(DbSaver, MainSaver, XLSXSaver):
    def __init__(self, model, year):
        print('Car.__init__')
        super().__init__()
        self.model = model
        self.year = year

    def __repr__(self):
        return f'{self.model} {self.year}'


class Student(MainSaver, DbSaver, XLSXSaver):
    def __init__(self, name, last_name):
        print('Student.__init__')
        super().__init__()
        self.name = name
        self.last_name = last_name

    def __repr__(self):
        return f'{self.name} {self.last_name}'


car = Car('Ферари SF 900', 2018)
student = Student('Петров', 'Иван')
to_save_elems = [car, student]

print('=' * 120)
for elem in to_save_elems:
    elem.main_save()


# print(Car.__mro__)
# print(Student.__mro__)

