import PySimpleGUI as sg

feet_text = sg.Text("Enter feet:")
feet_input = sg.Input()
inches_text = sg.Text("Enter inches")
inches_input = sg.Input()
convert_button = sg.Button("Convert")

window = sg.Window('Converter',
                   [[feet_text, feet_input],
                    [inches_text, inches_input],
                    [convert_button]])

window.read()
window.close()