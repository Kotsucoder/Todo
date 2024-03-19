import PySimpleGUI as sg

sg.theme('Black')

feet_label = sg.Text("Enter feet: ")
feet_input = sg.InputText(key='feet')
inches_label = sg.Text("Enter inches: ")
inches_input = sg.InputText(key='inches')
convert_button = sg.Button('Convert')
output_text = sg.Text(key='output')
exit_button = sg.Button("Exit")

layout = [[feet_label, feet_input],
          [inches_label, inches_input],
          [convert_button, exit_button, output_text]]

window = sg.Window('Convertor', layout=layout, font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(f'Event: {event}')
    print(f'Values: {values}')
    match event:
        case 'Convert':
            try:
                feet = float(values['feet'])
                inches = float(values['inches'])
                feet_to_meters = feet / 3.281
                inches_to_meters = inches / 39.37
                meters = round(feet_to_meters + inches_to_meters, 3)
                window['output'].update(value=f"{meters} m")
            except ValueError:
                sg.popup("Please provide two numbers.", font=('Helvetica', 20))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()