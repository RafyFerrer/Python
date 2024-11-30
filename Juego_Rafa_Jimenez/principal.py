import Juego
import random
espaciojuego=Juego.terreno(15,17)
serpiente=Juego.serpiente(5,5,3)
ancho_manzana=random.randrange(0,espaciojuego.get_ancho())
alto_manzana=random.randrange(0,espaciojuego.get_alto())
control=""

while serpiente.get_vivo()==1:
    control_anterior=control
    control=input()
    if (control=="w" and control_anterior!="s"):
        serpiente.arriba(1,espaciojuego)
    elif (control=="d" and control_anterior!="a"):
        serpiente.derecha(1,espaciojuego)
    elif (control=="a" and control_anterior!="d"):
        serpiente.izquierda(1)
    elif (control=="s" and control_anterior!="w"):
        serpiente.abajo(1)
    print(str(serpiente.get_posicionx()))
    print(str(serpiente.get_posiciony()))