# class Counter:
#     def __init__(self):
#         self.count = 0
# 
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         return self.count
# 
# 
# counter = Counter()
# print(counter())
# print(counter())
# print(counter())
# print(counter())
# print(counter())
# print(counter())

import time


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        res = self.func()
        finish_time = time.time()
        print(f'Отработала за {finish_time - start_time} секунд')
        return res


@Timer
def do_any_action():
    print('1')
    time.sleep(0.5)
    print('2')
    time.sleep(0.5)
    print('3')
    time.sleep(0.5)
    print('4')


do_any_action()
