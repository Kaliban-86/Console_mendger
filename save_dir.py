import os


def save_lisdir():
    file_list = []
    dir_list = []

    for i in os.listdir():
        if os.path.isfile(i):
            file_list.append(i)

    for i in os.listdir():
        if os.path.isdir(i):
            dir_list.append(i)

    with open('listdir.txt', 'w') as f:
        f.write(f'files: {file_list}\n')
        f.write(f'dirs: {dir_list}\n')
