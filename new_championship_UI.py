import PySimpleGUI as sg
import sys
import main_menu
import Bd_funcions

def item_row(item_num):

    row =  [sg.pin(sg.Col([[
                            sg.In(size=(20,1), justification='center', k=('-DESC-', item_num)),
                            sg.B("X", border_width=0, button_color=(sg.theme_text_color(), sg.theme_background_color()), k=('-DEL-', item_num), tooltip='удалить игрока'),
                            ]],
                            k=('-ROW-', item_num)
                        )
                    )
            ]
    return row


def make_window():

    layout = [  
                [sg.Text('название', font='Helvetica 16')],
                [sg.In(size=(25,1), justification='center', key='-CHEMP_NAME-')],
                [sg.Text('список игроков', font='Helvetica 16')],
                [sg.Column([item_row(i) for i in range(3)], k='-TRACKING SECTION-')],
                [sg.T('+', font='_ 30', enable_events=True, k='Add Item')],
                [sg.B("отмена", size=(10, 1), enable_events=True, k='-BACK-'),
                 sg.B('создать', size=(10, 1), enable_events=True, k='-MAKE-')],
            ]

    window = sg.Window('Window Title', layout,
                       use_default_focus=False,
                       font='Helvetica 16',
                       metadata=2,
                       element_justification='c',
                       margins=(100, 10),
                       )

    return window


def main():

    players = []

    window = make_window()
    while True:
        event, values = window.read()     # wake every hour
        print(event, values)

        if event == sg.WIN_CLOSED:
            break
        elif event == '-BACK-':
            window.close()
            main_menu.main()
            break

        if event == 'Add Item':
            window.metadata += 1
            window.extend_layout(window['-TRACKING SECTION-'], [item_row(window.metadata)])

        elif event[0] == '-DEL-':
                window[('-DESC-', event[1])].update('')
                window[('-ROW-', event[1])].update(visible=False)

        elif event =='-MAKE-':
            if not values['-CHEMP_NAME-']:
                sg.popup_error("Введите название", font='Helvetica 16', background_color='black')
            else:
                chemp_name = values.pop('-CHEMP_NAME-')
                for player in values.values():
                    if player:
                        players.append(player)
                Bd_funcions.sys.stdin = players
                Bd_funcions.make_bd(chemp_name)
                window.close()
                main_menu.main()
                break

    window.close()


