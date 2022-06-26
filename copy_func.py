import shutil
import os

def copy_file():
    file_name = input('Введите имя файла для копирования: ')
    if os.path.exists(file_name):
        copy_file_name = input(f'Введите имя для копии {file_name}: ')
        shutil.copy(file_name, copy_file_name)
    else:
        print(f'Файла с именем "{file_name}" не существует!')

