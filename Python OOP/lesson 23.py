class Animal:
    def __init__(sel):
        print('Animal - __init__')


class Dog(Animal):
    def __init__(self, name):
        super().__init__()
        print('Dog - __init__')


class Ovcharka(Dog):
    def __init__(self, name):
        super().__init__(name)
        print('Ovcharka - __init__')


ovcharka1 = Ovcharka('Жучка')
