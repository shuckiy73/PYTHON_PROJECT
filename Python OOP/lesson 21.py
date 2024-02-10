class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(f'Меня зовут: {self.name}')

    def do_sound(self):
        print('Звук животного')


class Dog(Animal):

    def do_sound(self):
        print('Собака лает Гав-Гав')

    def play_game(self):
        print('Я собака, я несу палку')


class Ovcharka(Dog):
    def ovcharka_method(self):
        print('Метод только для овчарок')


dog = Ovcharka('Собака Фёдор')

# animal.do_sound()
# animal.get_name()

dog.play_game()
dog.get_name()
dog.do_sound()
dog.ovcharka_method()
