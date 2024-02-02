# print(f"В часе {1 * 60 * 60} секунд")
# seconds_per_hour = 1 * 60 * 60
# seconds_per_day = seconds_per_hour * 24
# print(f"В сутках {seconds_per_day} секунд")
# print(seconds_per_day / seconds_per_hour)
# print(seconds_per_day // seconds_per_hour)


years_list = [1973, 1974, 1975, 1976, 1977, 1978]
print('Мой третий день рождения:', years_list[2])
print('Я самый старый:', years_list[-1])
things = ["mozzarella", "cinderella", "salmonella"]
print(things)
print(things[1].title())
print(things[1][0].upper() + things[1][1:])
print(things[0].upper())
print(things)
# things.pop(2)
things.remove('salmonella')
print(things)

surprise = ['Grouch', 'Chico', 'harpo']
print(surprise)
surprise.remove('harpo')
surprise.append('Harpo')
print(surprise)
print(surprise[2].title())

print('=' * 80)
e2f = {
    'do': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}
print(e2f['walrus'])
f2e = {}
for eng, france in e2f.items():
    f2e[france] = eng
print(e2f)
print(f2e)
print(f2e['chien'])
print(list(e2f.keys()))

print('=' * 80)

life = {
    'animals': {
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': {},
        'emus': {},
    },
    'plants': {},
    'other': {},
}
print(life)
print(list(life.keys()))
print(list(life['animals'].keys()))
print(life['animals']['cats'])
