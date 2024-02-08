class Dog:
    animal_type = 'Собака'
    legs_num = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{Dog.animal_type}\n\tКличка: {self.name} \n\tВозраст: {self.age} \n\tКол-во лап: {self.legs_num}'


dog1 = Dog('Тузик', 4)
dog2 = Dog('Бобик', 10)
print(dog1.name)
print(dog2)
print(Dog.animal_type)
