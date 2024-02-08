class Cat:
    # age = 2
    # name = 'Муся'
    def __init__(self, name='Кот', age=1):
        self.name = name
        self.age = age
        print(f'Привет мир, кот {self.name} родился')

    def __del__(self):
        pass
        # print(f'Кот {self.name} закончился')


cat1 = Cat('Вася', 3)
cat2 = Cat('Муся', 3)

cat4 = {
    'name': 'Василий',
    'age': 2
}

print(cat1.name)
# print(cat1.__dict__)
# print(cat4)
