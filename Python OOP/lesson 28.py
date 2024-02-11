list1 = list(range(1, 21))
print(list1)

list2 = []
for elem in list1:
    list2.append(elem * elem)
print(list2)


def plus_2(elem):
    return elem + 2


print([elem * elem for elem in list1])
print([plus_2(elem) for elem in list1 if elem < 10])
print(list(map(lambda elem: plus_2(elem), list1)))
print(120 * '=')

dict1 = {elem: elem * elem for elem in list1}
print(dict1)
data = [
    'Молоко',
    'мама',
    'Кефир'
]
print(data)
dict2 = {}
for el in data:
    dict2[el] = len(el)
print(dict2)
print({word: len(word) for word in data})
print({word: len(word) for word in data if len(word) > 4})

print(120 * '=')
data2 = {word: len(word) for word in data}
print(data2)
print({word.upper(): word_len for word, word_len in data2.items()})
