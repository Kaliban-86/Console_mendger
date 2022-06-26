#Основной модуль для запуска и отображения основного меню
from Victory import play_victory
from bank import bank
while True:
    print('*КОНСОЛЬНЫЙ ФАЙЛОВЫЙ МЕНДЖЕР*')
    print('')
    print('выбирите действие:')
    print('1. Создать папку')
    print('2. Удалить (файл/папку')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Посмотреть информацию об операционной системе')
    print('9. Создатель программы')
    print('10. Играть в викторину')
    print('11. Мой бансковский счет')
    print('12. Смена рабочей директории')
    print('13. Выход')

    choice_num = int(input('Введите номер операции: '))

    if choice_num == 13:
        break
    elif choice_num == 9:
        print('Вадим Викторович')
    elif choice_num == 10:
        play_victory()
    elif choice_num == 11:
        bank()