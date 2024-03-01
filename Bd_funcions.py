import sqlite3
import sys
import table_UI

def make_bd(name_bd):
    file_name = name_bd + '.bd'
    bd = sqlite3.connect(f'tournaments\\{file_name}')

    coursor = bd.cursor()

    coursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {name_bd} (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(255),
                    point INTEGER
    );
    ''')

    query_add = f'iNSERT INTO {name_bd} (name, point) VALUES (?, ?)'
    players = sys.stdin
    users_data = list()

    for player in players:
        user_data = (player, 0)
        users_data.append(user_data)

    coursor.executemany(query_add, users_data)

    coursor.execute(f'SELECT name, point FROM {name_bd}')
    print(coursor.fetchall())

    bd.commit()
    bd.close()

def upadate_bd(name_bd, values_dict : dict):
    file_name = name_bd + '.bd'
    bd = sqlite3.connect(f'tournaments\\{file_name}')
    coursor = bd.cursor()

    query_update = (f'''
        UPDATE {name_bd}
        SET point = ?
        WHERE name = ?
    ''')

    coursor.execute(f'SELECT name, point FROM {name_bd}')
    old_points = {}
    for name, point in coursor.fetchall():
        old_points[name] = point

    data = list()
    for name, point in values_dict.items():
        if point.isdigit():
            data.append((point, name))
        
        elif len(point) > 1 and point[1:].isdigit():
            if point[0] == "+":
                point = int(point[1:])
                point = int(old_points[name]) + point
                data.append((point, name))
            elif point[0] == "-":
                point = int(point[1:])
                point = int(old_points[name]) - point
                data.append((point, name))

    coursor.executemany(query_update, data)

    coursor.execute(f'SELECT name, point FROM {name_bd}')
    data = coursor.fetchall()
    bd.commit()
    bd.close()

    table_UI.create_table_UI(name_bd, data)

def show_bd(name_bd):
    file_name = name_bd + '.bd'
    bd = sqlite3.connect(f'tournaments\\{file_name}')
    coursor = bd.cursor()

    coursor.execute(f'SELECT name, point FROM {name_bd}')
    data = coursor.fetchall()
    bd.commit()
    bd.close()

    table_UI.create_table_UI(name_bd, data)