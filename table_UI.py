import PySimpleGUI as sg
import main_menu
import update_UI
import Bd_funcions

def create_table_UI(name_bd, data_from_bd : list):

    data = []
    i = 1
    for player in sorted(data_from_bd, key=lambda x: (x[1], x[0]), reverse=True):
        name, point = player
        data.append([i, name, point])
        i += 1

    headings = ['место', 'имя', 'очки',]

    button_cancel = sg.Button("отмена", size=(10, 1), key='-BACK-')
    button_update = sg.Button("обновить", size=(10, 1), key="-UPDATE-")

    # ------ Window Layout ------
    layout =[   [sg.Text(name_bd)],
                [sg.Table(
                        values=data, headings=headings, max_col_width=35,
                        # background_color='light blue',
                        auto_size_columns=False,
                        justification='center',
                        num_rows=10,
                        alternating_row_color='black',
                        key='-TABLE-',
                        row_height= 50,
                        font='Helvetica 16',
                        # row_colors=[(0, 'light blue'), (1, 'green'), (2, 'light green')],

                        )
                ],
                [button_cancel, button_update],
           ]
            
            
    # ------ Create Window ------
    window = sg.Window('The Table Element', layout, font='Helvetica 16',
                       element_justification='center',
                       margins=(20, 20),
                       no_titlebar=True,
                       grab_anywhere=True,
                       )

    # ------ Event Loop ------
    while True:
        event, values = window.read()
        print(event, values)

        if event == sg.WIN_CLOSED:
            break
        elif event == '-BACK-':
            window.close()
            main_menu.main()
            break
        elif event == "-UPDATE-":
            window.close()
            update_UI.update_table_ui(name_bd, data)
            break

    window.close()
