class Cat:
    age = 2
    name = 'Василий'


cat1 = {
    'age': 2,
    'name': 'Василий',
}
cat2 = Cat()
cat3 = Cat()

# print(cat)
print(cat1['name'])
print(cat2.name)
print(cat3.age)

print('+' * 5)


class Cat:
    age = 2
    name = 'Муся'


cat1 = {
    'age': 2,
    'name': 'Василий',
}
cat2 = Cat()
cat3 = Cat()

print(cat1['name'])
print(cat2.name)
print(cat3.name)

print(cat1)
print(cat2.__dict__)
