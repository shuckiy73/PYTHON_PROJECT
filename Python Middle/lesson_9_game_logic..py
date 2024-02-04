STATUS_CONTINUE = 'игра продолжается!'
EMPTY = '_'
ROW1 = '1'
ROW2 = '2'
ROW3 = '3'
COLA = 'a'
COLB = 'b'
COLC = 'c'
data = {
    ROW1: {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY,
    },
    ROW2: {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY,
    },
    ROW3: {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY,
    }
}
allowed_symbols = ['X', 'O']
allowed_rows = [ROW1, ROW2, ROW3]
allowed_cols = [COLA, COLB, COLC]


def check_is_game_end():
    winner = STATUS_CONTINUE

    empty_symbols = 0
    for dat in data.values():
        for d in dat.values():
            if d == EMPTY:
                empty_symbols += 1

    # Условия победы по строкам
    if (data[ROW1][COLA] == data[ROW1][COLB]) and (data[ROW1][COLA] == data[ROW1][COLC]) and (data[ROW1][COLA] != EMPTY):
        winner = data[ROW1][COLA]
    elif (data[ROW2][COLA] == data[ROW2][COLB]) and (data[ROW2][COLA] == data[ROW2][COLC]) and (data[ROW2][COLA] != EMPTY):
        winner = data[ROW2][COLA]
    elif (data[ROW3][COLA] == data[ROW3][COLB]) and (data[ROW3][COLA] == data[ROW3][COLC]) and (data[ROW3][COLA] != EMPTY):
        winner = data[ROW3][COLA]
    # Условия победы по колонкам
    elif (data[ROW1][COLA] == data[ROW2][COLA]) and (data[ROW1][COLA] == data[ROW3][COLA]) and (data[ROW1][COLA] != EMPTY):
        winner = data[ROW1][COLA]
    elif (data[ROW1][COLB] == data[ROW2][COLB]) and (data[ROW1][COLB] == data[ROW3][COLB]) and (data[ROW1][COLB] != EMPTY):
        winner = data[ROW1][COLB]
    elif (data[ROW1][COLC] == data[ROW2][COLC]) and (data[ROW1][COLC] == data[ROW3][COLC]) and (data[ROW1][COLC] != EMPTY):
        winner = data[ROW1][COLC]
    # Условия победы по диагоналям
    elif (data[ROW1][COLA] == data[ROW2][COLB]) and (data[ROW1][COLA] == data[ROW3][COLC]) and (data[ROW1][COLA] != EMPTY):
        winner = data[ROW1][COLA]
    elif (data[ROW1][COLC] == data[ROW2][COLB]) and (data[ROW1][COLC] == data[ROW3][COLA]) and (data[ROW1][COLC] != EMPTY):
        winner = data[ROW1][COLC]
    # Все ячейки заполнены, но победа не обнаружена
    elif empty_symbols == 0:
        winner = 'Ничья'

    return winner


def input_value(input_value, value):
    column = input_value[1].lower()
    if column not in allowed_cols:
        return f'[?] Вы ввели неверную колонку: {column}, разрешённые колонки: {allowed_cols}. Вы потеряли ход'

    row = input_value[0]
    if row not in allowed_rows:
        return f'[?] Вы ввели неверную строку: {row}, разрешённые колонки: {allowed_rows}. Вы потеряли ход'

    if (value in allowed_symbols) and (data[row][column] == EMPTY):
        data[row][column] = value
        return 'Ход принят'
    else:
        return f'[?] Вы потеряли ход, так как ввели запрещённый символ: {value}, разрешённые символы: {allowed_symbols}. Или ячейка уже заполнена'


def print_game_field():
    str_result = 'Данные вводятся в формате: 1a\n'
    str_result += f" \t\ta\t\tb\t\tc\n"
    str_result += f"1\t\t{data[ROW1][COLA]}\t\t{data[ROW1][COLB]}\t\t{data[ROW1][COLC]}\n"
    str_result += f"2\t\t{data[ROW2][COLA]}\t\t{data[ROW2][COLB]}\t\t{data[ROW2][COLC]}\n"
    str_result += f"3\t\t{data[ROW3][COLA]}\t\t{data[ROW3][COLB]}\t\t{data[ROW3][COLC]}\n"
    return str_result


def clear_data():
    data[ROW1] = {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY
    }
    data[ROW2] = {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY
    }
    data[ROW3] = {
        COLA: EMPTY,
        COLB: EMPTY,
        COLC: EMPTY
    }


