from abc import ABC, abstractmethod


class BirthDay(ABC):
    @abstractmethod
    def get_name(self):
        pass

    def congritulate(self):
        # ...
        print(f'Поздравляем тебя {self.get_name()} с днём рождения')
        # ...
        # ...
        # ...


class Car(BirthDay):
    def get_name(self):
        return 'Машина'


class Dog(BirthDay):
    def get_name(self):
        return 'Шарик'


class Cat(BirthDay):
    def get_name(self):
        return 'Шурик'


car = Car()
dog = Dog()
cat = Cat()
printables = [car, dog, cat]
for obj in printables:
    obj.congritulate()
