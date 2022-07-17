import os.path

if not os.path.isfile('bank_account'):
    with open('bank_account', 'w') as f:
        f.write('0')
else:
    with open('bank_account', 'r') as f:
        bank_account = int(f.read())






