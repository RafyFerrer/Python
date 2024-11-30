from tkinter import *

def envia_boton():
    VentanaNueva = Toplevel()
    VentanaNueva.geometry("300x200")
    VentanaNueva.title("Ventana secundaria")
    valor_entrada = entrada.get()
    etiqueta = Label(VentanaNueva,text = valor_entrada)
    etiqueta.grid(row=2)

def otraventana():
    VentanaNueva2 = Toplevel()
    VentanaNueva2.geometry("400x400")
    VentanaNueva2.title("Ventana terciaria")

raiz = Tk()
raiz.title("Ventana primera")
raiz.geometry("300x100")
entrada = Entry(raiz,width=35)
entrada.grid(row=0)
enviar = Button(raiz,text="Acpetar",command=envia_boton)
enviar.grid(row=1,column=0)
otroboton = Button(raiz,text="abrir otra ventana",command=otraventana)
otroboton.grid(row=1,column=1)

mainloop()
