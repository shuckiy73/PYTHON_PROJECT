from dataclasses import dataclass, field


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f'name: {self.name}, age: {self.age}'


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    childs: list = field(default_factory=list)


person = Person('Андрей', 27)
person.childs.append('Сын1')
person.childs.append('Сын2')
print(person)
person2 = Person('Василий', 25)
print(person2)

