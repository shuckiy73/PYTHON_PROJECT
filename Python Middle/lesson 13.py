import shutil


def create_file(file_name):
    with open(file_name, "w") as file:
        for i in range(1, 100):
            file.write(f"1111111111: {i}\n")


create_file('test_files1/test_files/test_text.txt')


for i in range(1, 10000):
    shutil.copyfile('test_files1/test_files/test_text.txt', f'test_files1/test_files/test_text_{i}.txt')

shutil.make_archive('compressed_files', 'zip', 'test_files1/test_files/')
shutil.make_archive('compressed_files', 'tar', 'test_files1/test_files/')
