# 1.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([elem for elem in a if elem <= 5])
print('=' * 10)

# 2.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = list(filter(lambda elem: elem in b, a))
print('=' * 10)

# 3.
import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
result = dict(sorted(d.items(), key=operator.itemgetter(1)))

result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))


