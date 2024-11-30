# importamos las librerías de automatización periódica de ejecución de funciones.
import schedule

# importamos librerías de control de tiempos
from datetime import datetime

#  importamos la librería de Scrapping WEB
import Libreria

# Definimos las variables globales que contendrán la temperatura de Beas y la de Almería
tBeas=""
tAlmeria=""

# Definimos la Tarea 1 que es importar la temperatura de Beas de Segura
def tarea1():
    tBeas = Libreria.meteo('beas-de-segura')
def tarea2():
    tAlmeria = Libreria.meteo('almeria')

# Todos los días vamos a importar el tiempo de Beas de Segura que es Tarea1  y el de Almería cada 4 horas que es Tarea2.
schedule.every().day.do(tarea1)
schedule.every(4).hours.do(tarea2)

while True:
    schedule.run_pending()
    pt = schedule.get_jobs()
    print(f'Existen {len(pt)} tareas pendientes a esta fecha y hora',datetime.now(), end='\r')

    