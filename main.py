# Основной модуль для запуска и отображения основного меню
import os

from Victory import play_victory
from bank import bank
from sys_func import os_print
from make_dir_func import make_new_dir
from remove_dir_func import remove_dir
from copy_func import copy_file
from file_list_func import file_list_in_dir, dir_list_in_dir

while True:
    print('*****************************')
    print('*КОНСОЛЬНЫЙ ФАЙЛОВЫЙ МЕНДЖЕР*')
    print('*****************************')
    print('выбирите действие:')
    print('1. Создать папку')  # +
    print('2. Удалить (файл/папку')  # +
    print('3. Копировать (файл/папку)')  # +
    print('4. Просмотр содержимого рабочей директории')  # +
    print('5. Посмотреть только папки')  # +
    print('6. Посмотреть только файлы')  # +
    print('7. Посмотреть информацию об операционной системе')  # +
    print('9. Создатель программы')  # +
    print('10. Играть в викторину')  # +
    print('11. Мой бансковский счет')  # +
    print('12. Смена рабочей директории')
    print('13. Выход')  # +

    choice_num = int(input('Введите номер операции: '))

    if choice_num == 13:
        break
    elif choice_num == 1:
        make_new_dir()
    elif choice_num == 2:
        remove_dir()
    elif choice_num == 3:
        copy_file()
    elif choice_num == 4:
        print(os.listdir())
    elif choice_num == 5:
        dir_list_in_dir()
    elif choice_num == 6:
        file_list_in_dir()
    elif choice_num == 7:
        os_print()
    elif choice_num == 9:
        print('Вадим Викторович')
    elif choice_num == 10:
        play_victory()
    elif choice_num == 11:
        bank()
