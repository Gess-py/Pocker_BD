import PySimpleGUI as sg
import sys
import table_UI
import Bd_funcions
import new_championship_UI
import main_menu


def main():

    sg.theme('darkgrey8')

    button_new_championship = sg.Button('новый чемпионат',
                    enable_events=True,
                    key='-FUNCTION_NEW_CHAMPIONSHIP-',
                    size=(15, 1),
                    font='Helvetica 16')
    
    tournaments_list = sg.Listbox(sys.stdin, key='-TOURTAMENTS_LIST-',
                                  font='Helvetica 16',
                                  expand_y=True,
                                  expand_x=True,
                                  justification='center',
                                  size=(10, 5),
                                  )
    
    buton_choise = sg.Button('выбрать', key='-BUTTON_CHOISE-',
                             enable_events=True,
                             font='Helvetica 16',
                             size=(10, 1)
                             )
    
    buton_delete = sg.Button('удалить', key='-BUTTON_DELETE-',
                             enable_events=True,
                             font='Helvetica 16',
                             size=(10, 1)
                             )


    layout = [[sg.VPush()],
              [button_new_championship],
              [tournaments_list],
              [buton_choise, buton_delete],
              [sg.VPush()]
              ]

    window = sg.Window(title='main',
                       layout=layout,
                    #    size=(800, 600),
                       element_justification='c',
                       element_padding=10,
                       margins=(100, 100),
                       font='Helvetica 16',
                       )

    while True:
        event, values = window.read()
        print(event, values)

        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        elif event == '-FUNCTION_NEW_CHAMPIONSHIP-':
            window.close()
            new_championship_UI.main()
            break

        elif event == '-BUTTON_CHOISE-' and len(values['-TOURTAMENTS_LIST-']) > 0:
            choise_value = values['-TOURTAMENTS_LIST-'][0]
            window.close()
            Bd_funcions.show_bd(choise_value)
            break

        elif event == '-BUTTON_DELETE-':
            if sg.popup_yes_no('вы уверены?', font='Helvetica 16') == 'Yes':
                if len(values['-TOURTAMENTS_LIST-']) > 0:
                    name_bd = values['-TOURTAMENTS_LIST-'][0]
                    window.close()
                    main_menu.delete_bd(name_bd)
                    main_menu.main()

    window.close()

if __name__ == '__main__':
    main()