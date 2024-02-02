# a = input('Введи, сколько у тебя литров пива: ')
# b = input('Сколько пива принес друг: ')
# c = int(a) + int(b)
# print('На двоих у вас: ' + str(c) + ' литров пива')

# a = input('Введи, сколько тебе лет: ')
# b = 100 - int(a)
# print('Осталось примерно: ' + str(b) + " лет")

# beer = input('Введите Yes, если пиво есть, и No, если пива нет: ')
# if beer.lower() == 'yes':
#     result = 'Ты взломаешь Пентагон'
# else:
#     result = 'Ты сломаешь свой мозг'
# print(result)

# myname = input('Введите логин: ')
# mypass = input('Введите пароль: ')
# if myname == 'xakep' and mypass == 'superpassword123':
#     result = 'Добро пожаловать, о великий хакер!'
# else:
#     result = 'Ты кто такой, давай до свидания...'
# print(result)


# myname = input('Введите логин: ')
# mypass = input('Введите пароль: ')
# if(myname == 'ivan' and mypass == 'superpassword123') or (myname == 'marina' and mypass == 'marinka93'):
#     result = 'Привет, ' + myname + '. Добро пожаловать!'
# else:
#     result = 'Ты кто такой, давай до свидания...'
# print(result)

v = int(input('Введи, сколько тебе лет: '))
if v < 18:
    print('Привет, юный хацкер')
elif v < 30:
    print('Превед, олдскул')
elif v < 65:
    print('Решил пересесть с ассемблера на Python?')
elif v < 100:
    print('На пенсии — самое время покодить')
elif v < 100000:
    print('Клан бессмертных приветствует тебя!')
