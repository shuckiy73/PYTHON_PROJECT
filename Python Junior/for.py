names = ['Андрей', 'Валерий', 'Саша', 'Игнат', 'Витя', '2', '1']
# counter = 0
# while counter < len(names):
#     print(names[counter])
#     counter += 1

# print('=' * 10)
# for name in names:
#     print(name)
for counter, name in enumerate(names):
    print(f"{counter}. {name}")
