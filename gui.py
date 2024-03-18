import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('KotsuCoder Todo App', layout=[[label], [input, add_button]])
window.read()
print("Hello")
window.close()