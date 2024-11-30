# Importamos las librerias que necesitamos para crear las ventanas y componentes de la aplicación de escritorio
from tkinter import *
from tkinter import ttk

# importamos esta librería que es donde está la función que hace el WEB Scrapping. Como la voy a usar en otro programa, la he separado en otro fichero
import Libreria

# Esta variable Global es la que va a ir guardando las temperaturas que vaya capturando con el WEB Scrapping.
temperatura =""

# Definimos la función a la que va a llamar el Botón de la ventana para capturar la temperatura, que lo hará usando wl WEB Scrapping que hay en la librería externa
def coge_meteo():
    zona = zona_meteo.get()
    temperatura = Libreria.meteo(zona)
    labeltemp = Label(ventana_base, text=temperatura, bg="white", fg="black", justify=CENTER, font=("Arial",90))
    labeltemp.place(x=300,y=300)

# Componemos la ventana y todos sus componentes
# Empezamos con la ventana base.
ventana_base = Tk()
ventana_base.title("Temperatura máxima de población en fecha actual")
ventana_base.geometry("800x600+50+50")

# Dentro de la ventana base, hacemos un frame en la parte superior que es donde irá el combo de selección de población y botón para obtener la temperatura.
frame_arriba = Frame(ventana_base,bg="#18c947", width=800, height=150)
frame_arriba.grid(row=0, column=0)

#Dentro del Frame de la parte superior colocamos una etiqueta que le indica al usuario que seleccione en el combo una población y pulse en botón
etiqueta_primera=Label(frame_arriba, text="SELECCIONA POBLACIÓN Y PULSA EN BOTÓN CAPTURAR", bg="#18c947", fg="black", justify=CENTER, font=("Arial"))
etiqueta_primera.place(x=75, y=50)

#Defimos el combo y los valores que contiene. Colocamos el primer valor como valor por defecto.
valores_poblacion = ["beas-de-segura", "almeria"]
zona_meteo = ttk.Combobox(frame_arriba,values=valores_poblacion,font=("Arial"),width=15)
zona_meteo.current(0)
zona_meteo.place (x=75,y=90)

#Definimos el botón y la función a la que llama cuando se le hace click.
boton = Button(frame_arriba,text="CAPTURAR",font=("Arial"),command=coge_meteo)
boton.place(x=300,y=90)

#Aquí llamamos a la función de capturar la meteorología ya que, como el combo tiene un valor por defecto seleccionado, aparezca la temperatura de este valor por defecto.
coge_meteo()

# Generar un loop para que la ventana se mantenga.
ventana_base.mainloop()

