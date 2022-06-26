import os


def change_dir():
    new_dir_name = input('Введите название новой директории: ')
    os.chdir(new_dir_name)
