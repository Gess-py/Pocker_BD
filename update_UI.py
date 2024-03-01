import PySimpleGUI as sg
import sys
import Bd_funcions
import table_UI

def update_table_ui(name_bd, data):
    data = list(map(lambda x: x[1:], data))
    layout = []
    for name, point in data:
        text_name = sg.Text(name)
        text_point = sg.Text(point)
        input_point = sg.Input(size=(5, 1), justification="center", key=name)
        line = [text_name, sg.Push(), text_point, input_point]
        layout.append(line)

    button_apply = sg.Button("применить", size=(10, 1), key="-BUTTON_APPLY-")
    button_cancel = sg.Button("отмена", size=(10, 1), key='-BACK-')
    layout.append([button_cancel, button_apply])

    window = sg.Window(f"update {name_bd}", layout,
                       font='Helvetica 16',
                       element_justification="center",
                       margins=(20, 20),
                       element_padding=10,
                       grab_anywhere=True,
                       )
    
    while True:
        event, values = window.read()
        print(event, values)

        if event == sg.WIN_CLOSED:
            break

        elif event == '-BACK-':
            window.close()
            table_UI.create_table_UI(name_bd, data)
            break

        elif event == '-BUTTON_APPLY-':
            window.close()
            Bd_funcions.upadate_bd(name_bd, values)
            break

    window.close()
    