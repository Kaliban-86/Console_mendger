import random


def play_victory():
    famous_people = {'Tom Cruse': '12.06.1977', 'Ben Aflek': '10.03.1965', 'Kira Naitly': '12.09.82',
                     'Luk Beson': '25.06.1969', 'Gay Richi': '12.12.1972', 'Kollin Farel': '09.11.1980',
                     'Leonardo Dicaprio': '07.06.1986', 'Aleksandra Dadario': '09.05.1988',
                     'Timaty Shalame': '23.04.1991',
                     'Mark Ruffalo': '03.03.1975'}
    random_count = 5

    names = random.sample(list(famous_people.keys()), random_count)
    is_game = True
    true_count = 0

    while is_game:
        for name in names:
            user_answer = input(f'Угадайте дату рождения {name} : ')
            if user_answer == famous_people.get(name):
                print('Верно!!')
                true_count = true_count + 1
            else:
                print(f'Не верно, правильно {famous_people.get(name)} ')

        answer_to_game = input('Продолжить игру? да/нет: ')
        if answer_to_game == 'нет':
            is_game = False

    print(f'Правильных ответов: {true_count}', f'Неправильных ответов: {random_count - true_count}')
