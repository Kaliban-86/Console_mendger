import os.path
import json


def bank():
    if not os.path.isfile('bank_account'):
        with open('bank_account', 'w') as f:
            f.write('0')

        with open('bank_account', 'r') as f:
            bank_account = int(f.read())
    else:
        with open('bank_account', 'r') as f:
            bank_account = int(f.read())

    if not os.path.isfile('history.json'):
        with open('history.json', 'w') as f:
            history = {}
            json.dump(history, f)
        with open('history.json', 'r') as f:
            history = json.load(f)
    else:
        with open('history.json', 'r') as f:
            history = json.load(f)

    def bank_account_replenishment(bank_account, amount_of_money):
        bank_account += amount_of_money
        return bank_account

    def buy_function(bank_account, price):
        if bank_account >= price:
            purchase_name = input('Введите имя покупки: ')
            bank_account -= price
            return [bank_account, purchase_name, price]
        else:
            print('Денег не достаточно для покупки!')
            return

    while True:
        print(" ")
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. Состояние счета')
        print('5. выход')

        try:
            choice = int(input('Выберите пункт меню: '))
        except Exception as e:
            print('Вы ввели не число!')
            print(e)
            break

        if choice == 1:
            bank_account = bank_account_replenishment(bank_account,
                                                      amount_of_money=int(input('Введите сумму для пополнения: ')))
            print(f'На вашем счету: {bank_account} денег')

        elif choice == 2:
            func_res = buy_function(bank_account, price=int(input('Введите стоимость  покупки: ')))
            if func_res is not None:
                bank_account = func_res[0]
                history[func_res[1]] = func_res[2]
                print(f'вы купили {func_res[1]} за {func_res[2]} рублей, осталось на счете {bank_account} рублей')

        elif choice == 3:
            print(history)

        elif choice == 4:
            print(bank_account)

        elif choice == 5:
            with open('bank_account', 'w') as f:
                f.write(str(bank_account))

            with open('history.json', 'w') as f:
                json.dump(history, f)
            break
        else:
            print('Неверный пункт меню')
