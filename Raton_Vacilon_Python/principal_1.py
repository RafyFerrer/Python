import Libreria
import random
import time
import pygame
espaciojuego=Libreria.terreno(640,640)
ancho_raton=espaciojuego.get_ancho()//2
alto_raton=espaciojuego.get_alto()//2
ancho_manzana=random.randrange(0,espaciojuego.get_ancho())
alto_manzana=random.randrange(0,espaciojuego.get_alto())
saltos_manzana=Libreria.manzana(ancho_manzana,alto_manzana,0)
contador_movimientos=0
contador_saltos=0
puntos=0
raton1=Libreria.raton(ancho_raton,alto_raton,contador_movimientos)
control_anterior=0
inicio=time.time()
a=range(0,1000000)

pygame.init()
ventana= pygame.display.set_mode((espaciojuego.get_ancho(),espaciojuego.get_alto()))
while raton1.get_vivo()==1:
    for i in a:
        j=i
    ventana.fill('white')
    imagen = pygame.image.load('Raton.jpg')
    imagen_redimensionada = pygame.transform.scale(imagen, (20, 20))
    ventana.blit(imagen_redimensionada, (raton1.get_posicionx(), raton1.get_posiciony()))
    pygame.draw.circle(ventana, 'yellow', (ancho_manzana, alto_manzana), 10)
    if control_anterior == 1:
        alto_raton = alto_raton + 20
        raton1.set_posiciony(alto_raton)
        control_anterior = 1
    if control_anterior == 2:
        alto_raton = alto_raton - 20
        control_anterior = 2
        raton1.set_posiciony(alto_raton)
    if control_anterior == 3:
        ancho_raton = ancho_raton + 20
        raton1.set_posicionx(ancho_raton)
        control_anterior = 3
    if control_anterior == 4:
        ancho_raton = ancho_raton - 20
        raton1.set_posicionx(ancho_raton)
        control_anterior = 4
    for event in pygame.event.get():
        hitbox_manzana_ancho = range((ancho_manzana - 25), (ancho_manzana + 25))
        hitbox_manzana_alto = range((alto_manzana - 20), (alto_manzana + 20))
        if event.type == pygame.QUIT:
            raton1.set_vivo(0)
        if event.type == pygame.KEYDOWN:
            #controles
            if event.key == pygame.K_DOWN:
                alto_raton = alto_raton+20
                raton1.set_posiciony(alto_raton)
                control_anterior=1
                contador_movimientos=contador_movimientos+1
            elif event.key == pygame.K_UP:
                alto_raton=alto_raton-20
                control_anterior = 2
                raton1.set_posiciony(alto_raton)
                contador_movimientos = contador_movimientos + 1
            elif event.key == pygame.K_RIGHT:
                ancho_raton=ancho_raton+20
                raton1.set_posicionx(ancho_raton)
                control_anterior = 3
                contador_movimientos = contador_movimientos + 1
            elif event.key == pygame.K_LEFT:
                ancho_raton=ancho_raton-20
                raton1.set_posicionx(ancho_raton)
                control_anterior = 4
                contador_movimientos = contador_movimientos + 1

        if event.type == pygame.KEYUP:
            control_anterior=0
        #para traspasar las paredes
        if alto_raton < 0:
            alto_raton=espaciojuego.get_alto()
        elif alto_raton > (espaciojuego.get_alto()):
            alto_raton=0
        elif ancho_raton < 0:
            ancho_raton= espaciojuego.get_ancho()
        elif ancho_raton > (espaciojuego.get_ancho()):
            ancho_raton=0
        #colision de barrera
        #contador de movimientos

        if contador_movimientos==30:
            ancho_manzana = random.randrange(0, espaciojuego.get_ancho())
            alto_manzana = random.randrange(0, espaciojuego.get_alto())
            contador_saltos=contador_saltos+1
            contador_movimientos=0
        #comerse la manzana

        if ((raton1.get_posicionx()) in (hitbox_manzana_ancho)) and ((raton1.get_posiciony()) in (hitbox_manzana_alto)):
            ancho_manzana = random.randrange(0, espaciojuego.get_ancho())
            alto_manzana = random.randrange(0, espaciojuego.get_alto())
            contador_movimientos=0
            contador_saltos=0
            puntos=puntos+1
        if contador_saltos>3:
            raton1.set_vivo(0)


    pygame.display.flip()
pygame.quit()