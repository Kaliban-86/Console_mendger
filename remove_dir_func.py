import os


def remove_dir():
    type_to_remove = input('Удалить файл или папку?: ')
    if type_to_remove == 'файл':
        direct_to_remove = input('Укажите имя удаляемого файла: ')
        if os.path.exists(direct_to_remove):
            os.remove(direct_to_remove)
        else:
            print(f'Файла с именеи: "{direct_to_remove}" не существует!')
    elif type_to_remove == 'папку':
        direct_to_remove = input('Укажите имя удаляемой папки: ')
        if os.path.exists(direct_to_remove):
            os.rmdir(direct_to_remove)
        else:
            print(f'Папки с именеи: "{direct_to_remove}" не существует!')
