class Person:
    MIN_AGE = 0
    MAX_AGE = 99
    data = []

    def __init__(self, name2, age):
        self.name = name2
        self.age = age

    def __repr__(self):
        return f"{self.name} {self.age}"


person1 = Person('Андрей', 48)
print(person1)
person2 = Person('Василий', 28)
print(person2)
print(person1)

print(person1.__dict__)
print(Person.__dict__)

print('=' * 120)
person1.data.append('1')
person1.data.append('2')
person1.data.append('3')
print(person1.data)
print(person2.data)
