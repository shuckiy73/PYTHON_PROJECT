FILE_NAME = "text_info.txt"

# Запись в файл с удалением, предыдущей информации
with open(FILE_NAME, "w") as file:
    for i in range(1, 1000):
        file.write(f"1111111111: {i}\n")


# Читаем файл
with open(FILE_NAME, 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.replace('\n', ''))


# Дописываем файл, не удаляя содержимое
with open(FILE_NAME, "a") as file:
    file.write(f"Ещё одна строка в конец файла\n")
    file.write(f"Ещё одна строка в конец файла\n")
    file.write(f"Ещё одна строка в конец файла\n")


# Дописываем файл, не удаляя содержимое
with open('new_file.txt', "x") as file:
    file.write(f"XXXXXXXXXXXXXXXXXXX\n")
