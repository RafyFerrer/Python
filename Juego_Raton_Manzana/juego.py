import Libreria_Clases
import pygame
import random
pygame.init()
espaciojuego=Libreria_Clases.terreno(640,480)
ancho=espaciojuego.get_ancho()
alto=espaciojuego.get_alto()
dimension_ventana=(ancho,alto)
x_raton=ancho//2
y_raton=alto//2
raton_vacilon=Libreria_Clases.raton(x_raton,y_raton)
x_manzana=random.randrange(0,ancho)
y_manzana=random.randrange(0,alto)
manzana_verde=Libreria_Clases.manzana(x_manzana,y_manzana,1)
contador=0
running=True
ventana = pygame.display.set_mode(dimension_ventana)
while running:
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                raton_vacilon.avanzar_y(espaciojuego,10)
                contador+=1
            elif event.key == pygame.K_UP:
                raton_vacilon.retroceder_y(10)
                contador+=1
            elif event.key == pygame.K_LEFT:
                raton_vacilon.retroceder_x(10)
                contador+=1
            elif event.key == pygame.K_RIGHT:
                raton_vacilon.avanzar_x(espaciojuego,10)
                contador+=1
            if contador >=20:
                x_manzana = random.randrange(0, ancho)
                y_manzana = random.randrange(0, alto)
                manzana_verde.set_px(x_manzana)
                manzana_verde.set_py(y_manzana)
                contador=0
    ventana.fill('#eb4034')
    pygame.draw.rect(ventana,'#4f3d3b',(raton_vacilon.get_px(),raton_vacilon.get_py(),20,20))
    pygame.draw.circle(ventana,'#afde16',(manzana_verde.get_px(),manzana_verde.get_py()),20)
    pygame.display.flip()
pygame.quit()

