class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        # return hash((self.name, self.age))
        return 1

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name


dog1 = Dog('Шарик', 2)
dog2 = Dog('Шарик', 5)
dog3 = Dog('Шарик', 5)
print(hash(dog1))
print(hash(dog2))
print(hash(dog3))
print(dog1 == dog2)
print(dog2 == dog3)

data = {}
data[dog1] = '1'
data[dog2] = '2'
data[dog3] = '3'
print(data)


# print(hash(data))
# data[['1']] = 1
