import os


def create_file(file_name):
    with open(file_name, "w") as file:
        for i in range(1, 100):
            file.write(f"1111111111: {i}\n")


def create_folder(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)


def move_file(old_path, new_path):
    os.rename(old_path, new_path)


print('Поехали!!!')
create_file('test_text.txt')
print('Файл создан')
create_folder(r'test_folder')
move_file('test_text.txt', 'test_folder/test_text.txt')
