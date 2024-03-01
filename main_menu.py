import PySimpleGUI as sg
import sqlite3
import sys
import os
import table_UI
import Bd_funcions
import User_interface

def delete_bd(name_bd):
    name_file = name_bd + '.bd'
    path = "tournaments"
    print(f'{path}\\{name_file}')
    try:
        os.remove(f'{path}\\{name_file}')
    except FileNotFoundError:
        print('Нету файла')

def main():
    path = "tournaments"
    if not os.path.isdir(path):
        os.mkdir(path)
    tournaments_name = [file[:-3] for file in os.listdir(path) if file.endswith('.bd')]

    User_interface.sys.stdin = tournaments_name
    User_interface.main()


if __name__ == '__main__':
    main()