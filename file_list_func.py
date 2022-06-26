import os


def file_list_in_dir():
    file_list = []
    for i in os.listdir():
        if os.path.isfile(i):
            file_list.append(i)
    print(file_list)

def dir_list_in_dir():
    dir_list = []
    for i in os.listdir():
        if os.path.isdir(i):
            dir_list.append(i)
    print(dir_list)