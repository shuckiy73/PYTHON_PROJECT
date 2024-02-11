import traceback


def run_light():
    1 / 0
    print('Свет включён')


def start_lightning():
    print('Умный дом включен 2 ')
    run_light()


def run():
    print('Умный дом включен 1 ')
    start_lightning()


try:
    run()
except Exception as e:
    traceback.print_exc()

print('Программа продолжает работать')

class CustomException(Exception):
    pass
    """Ошибка для таких-то случаев"""


try:
    raise CustomException('Какая-то ошибка')
except Exception as e:
    print('Ошибка обработана')

