import tkinter as tk
from tkinter import ttk

# Creamos una lista con los datos que queremos mostrar en la tabla
data = [
    ['Juan', 'García', 25],
    ['María', 'López', 32],
    ['Pedro', 'Martínez', 42],
    ['Laura', 'Gómez', 19],
]

# Creamos la ventana principal
root = tk.Tk()
root.title('Tabla de datos')

# Creamos el objeto Tabla y le pasamos como argumentos la ventana y los datos
tabla = ttk.Treeview(root, columns=('Nombre', 'Apellido', 'Edad'))
tabla.heading('#0', text='ID')
tabla.heading('Nombre', text='Nombre')
tabla.heading('Apellido', text='Apellido')
tabla.heading('Edad', text='Edad')

# Insertamos los datos en la tabla
for i, row in enumerate(data):
    tabla.insert(parent='', index='end', iid=i, text=str(i+1), values=row)

# Empaquetamos la tabla en la ventana
tabla.pack(expand=True, fill=tk.BOTH)

# Iniciamos el bucle principal de la ventana
root.mainloop()
