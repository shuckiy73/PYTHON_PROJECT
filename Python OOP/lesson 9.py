class Dog:
    __MIN_AGE = 0
    __MAX_AGE = 40
    __MIN_NAME_LEN = 3

    @classmethod
    def __check_age(cls, age):
        if type(age) != int:
            raise TypeError(f'Возраст может быть только числом, а получено: {age}')
        elif not (cls.__MIN_AGE <= age <= cls.__MAX_AGE):
            raise TypeError(f'Возраст может быть в диапазоне ({cls.__MIN_AGE}, {cls.__MAX_AGE}): {age}')

    @classmethod
    def __check_name(cls, name):
        if type(name) != str:
            raise TypeError(f'Имя может быть только строкой, а получено: {name}')
        elif len(name) < cls.__MIN_NAME_LEN:
            raise TypeError(f'Имя должно быть длинне чем {cls.__MIN_NAME_LEN} символов: {name}')

    def __init__(self, name, age):
        self.__check_age(age)
        self.__check_name(name)

        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__check_name(name)
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__check_age(age)
        self.__age = age


dog1 = Dog('Тузик', 10)
print(dog1.name, dog1.age)
dog1.name = 'Тузииииииик2'
print(dog1.name, dog1.age)
dog1.age = 17
print(dog1.name, dog1.age)
