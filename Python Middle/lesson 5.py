data = {
    '1': {
        'a': '_',
        'b': 'x',
        'c': '_',
    },
    '2': {
        'a': '_',
        'b': '_',
        'c': '0',
    },
    '3': {
        'a': 'x',
        'b': '_',
        'c': '_',
    }
}

def input_value(input_value):
    column = input_value[1]
    row = input_value[0]
    value = input_value[2]
    data[row][column] = value


def print_game_field():
    print('Данные вводятся в формате: 1a-0')
    print(f"\t\ta\t\tb\t\tc\n")
    print(f"1\t\t{data['1']['a']}\t\t{data['1']['b']}\t\t{data['1']['c']}\n")
    print(f"2\t\t{data['2']['a']}\t\t{data['2']['b']}\t\t{data['2']['c']}\n")
    print(f"3\t\t{data['3']['a']}\t\t{data['3']['b']}\t\t{data['3']['c']}\n")


def run_game():
    print('Игра "Крестики-Нолики" началась!')
    print_game_field()
    input_value(input('Введите знак: '))
    print_game_field()
    print_game_field()
    input_value(input('Введите знак: '))
    print_game_field()
    print_game_field()
    input_value(input('Введите знак: '))
    print_game_field()


run_game()
