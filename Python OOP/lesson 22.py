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


# print(Animal.__name__)
# print(Dog.__name__)
# print(Ovcharka.__name__)
# print(object.__name__)
# print(str.__name__)
# print(int.__name__)


# print(issubclass(Ovcharka, Dog))
# print(issubclass(Dog, Ovcharka))
# print(issubclass(Dog("wefew"), Ovcharka))

# dog1 = Dog('Тузик')
# print(isinstance(dog1, object))
# print(isinstance(dog1, Dog))
# print(isinstance(dog1, Ovcharka))


class superInt(int):
    def __str__(self):
        return f'[{self.real}]'

print(superInt(22) + superInt(3))

