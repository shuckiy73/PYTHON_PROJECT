# 1. До доветочия с чего начинаем
# 2. После доветочия до чего идём
# 3. Идём слева направо
text = 'Мама мыла раму, раму мыла мама!!!'
print(text[:])
print(text)
print(text[:10])
print(text[10:])
print(text[10:15])
print(text[10:])
print(text[-10:])
for symbol in text:
    print(f"{symbol} -------- {type(symbol)}")

text = 'Мама мыла РАМУ, Pаму мыла мама!!!'
print(text)
print(len(text))
print(text.lower())
print(text.upper())
PASSWORD = 'привет'
in_pass = input('Введите пароль: ')
if in_pass.lower() == PASSWORD.lower():
    print(f'Пароль верный({in_pass})')
else:
    print(f'Пароль НЕверный({in_pass})')
text = 'Мама мыла РАМУ, Pаму мыла мама!!!'
print(text)
print(len(text))
print(text.lower())
print(text.upper())

print('=' * 10)

PASSWORD = 'привет'
in_pass = input('Введите пароль: ')
if in_pass.lower() == PASSWORD.lower():
    print(f'Пароль верный({in_pass})')
else:
    print(f'Пароль НЕверный({in_pass})')

text = 'Мама мыла РАМУ, Pаму мыла мама!!!'
for word in text.split(' '):
    print(word)
print(text.replace('мыла', 'подмывала'))
text = 'Мама мыла РАМУ, Pаму мыла мама!!!'
for word in text.split(' '):
    print(word)
print(text.replace('мыла', 'подмывала'))

numbers = ['1', '2', '3', '4']
print(numbers)
print("----".join(numbers))
numbers = ['1', '2', '3', '4']
print(numbers)
print("----".join(numbers))
