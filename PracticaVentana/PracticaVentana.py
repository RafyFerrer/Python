import PySimpleGUI as sg

from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED
sg.theme ('DarkTeal19')
Layout = [
    [sg.Text('Por favor cumplimente los siguientes campos')],
    [sg.InputText(key='Nombre')],
    [sg.Text('hola esto es lo que se muestra', key='CopiaNombre')],
    [sg.InputText (key='EscribeNombre')],
    [sg.Submit('Envia Datos'), sg.Exit('Cierra')]
    ]
Ventana = sg.Window ('Ejemplo de formulario de entrada de datos', Layout)
# A continuacion se mantiene la ventana activa en un bucle hasta que lo rompes. Luego cierras la ventana con el metodo close
# Cada key que tiene asociado cada widget es una Key que se agrega al diccionario values. Es decir:
# Values es un diccionario que se va armando con todos los valores que se asignas a las keys.
# Event son los eventos que se producen en la ventana, como las pulsaciones de los botones, etc.

while True:
    event, values = Ventana.read()
    if event == sg.WINDOW_CLOSED or event == 'Cierra':
        break
    if event == 'Envia Datos':
        Ventana ['CopiaNombre'].update (values ['Nombre'])
        Ventana ['EscribeNombre'].update (values ['Nombre'])
       
    print (values)
Ventana.close()

