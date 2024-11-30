import Libreria
import random
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

#barreras

ancho_barreras = random.randrange(0, espaciojuego.get_ancho())
alto_barreras = random.randrange(0, espaciojuego.get_alto())
longitud_barreras = random.randrange(50, 150)
abarreras = ancho_barreras - longitud_barreras
barreras_juego = range(abarreras, ancho_barreras + 15)
barreras_rango_altura = range(alto_barreras, (alto_barreras + 20))
barreras1 = Libreria.barreras(ancho_barreras, alto_barreras, longitud_barreras)

ancho_barreras2 = random.randrange(0, espaciojuego.get_ancho())
alto_barreras2 = random.randrange(0, espaciojuego.get_alto())
longitud_barreras2 = random.randrange(50, 150)
abarreras2 = ancho_barreras2 - longitud_barreras2
barreras_juego2 = range(abarreras2, ancho_barreras2 + 15)
barreras_rango_altura2 = range(alto_barreras2, (alto_barreras2 + 20))
barreras2 = Libreria.barreras(ancho_barreras2, alto_barreras2, longitud_barreras2)

ancho_barreras3 = random.randrange(0, espaciojuego.get_ancho())
alto_barreras3 = random.randrange(0, espaciojuego.get_alto())
longitud_barreras3 = random.randrange(50, 150)
abarreras3 = ancho_barreras3 - longitud_barreras3
barreras_juego3 = range(abarreras3, ancho_barreras3 + 15)
barreras_rango_altura3 = range(alto_barreras3, (alto_barreras3 + 20))
barreras3 = Libreria.barreras(ancho_barreras3, alto_barreras3, longitud_barreras3)

ancho_barreras4 = random.randrange(0, espaciojuego.get_ancho())
alto_barreras4 = random.randrange(0, espaciojuego.get_alto())
longitud_barreras4 = random.randrange(50, 150)
abarreras4 = ancho_barreras4 - longitud_barreras4
barreras_juego4 = range(abarreras4, ancho_barreras4 + 15)
barreras_rango_altura4 = range(alto_barreras4, (alto_barreras4 + 20))
barreras4 = Libreria.barreras(ancho_barreras4, alto_barreras4, longitud_barreras4)

ancho_barreras5 = random.randrange(0, espaciojuego.get_ancho())
alto_barreras5 = random.randrange(0, espaciojuego.get_alto())
longitud_barreras5 = random.randrange(50, 150)
abarreras5 = ancho_barreras5 - longitud_barreras5
barreras_juego5 = range(abarreras5, ancho_barreras5 + 15)
barreras_rango_altura5 = range(alto_barreras5, (alto_barreras5 + 20))
barreras5 = Libreria.barreras(ancho_barreras5, alto_barreras5, longitud_barreras5)

ancho_barreras6 = random.randrange(0, espaciojuego.get_ancho())
alto_barreras6 = random.randrange(0, espaciojuego.get_alto())
longitud_barreras6 = random.randrange(50, 150)
abarreras6 = ancho_barreras6 - longitud_barreras6
barreras_juego6 = range(abarreras6, ancho_barreras6 + 15)
barreras_rango_altura6 = range(alto_barreras6, (alto_barreras6 + 20))
barreras6 = Libreria.barreras(ancho_barreras6, alto_barreras6, longitud_barreras6)

ancho_barreras7 = random.randrange(0, espaciojuego.get_ancho())
alto_barreras7 = random.randrange(0, espaciojuego.get_alto())
longitud_barreras7 = random.randrange(50, 150)
abarreras7 = ancho_barreras7 - longitud_barreras7
barreras_juego7 = range(abarreras7, ancho_barreras7 + 15)
barreras_rango_altura7 = range(alto_barreras7, (alto_barreras7 + 20))
barreras7 = Libreria.barreras(ancho_barreras7, alto_barreras7, longitud_barreras7)

ancho_barreras8 = random.randrange(0, espaciojuego.get_ancho())
alto_barreras8 = random.randrange(0, espaciojuego.get_alto())
longitud_barreras8 = random.randrange(50, 150)
abarreras8 = ancho_barreras8 - longitud_barreras8
barreras_juego8 = range(abarreras8, ancho_barreras8 + 15)
barreras_rango_altura8 = range(alto_barreras8, (alto_barreras8 + 20))
barreras8 = Libreria.barreras(ancho_barreras8, alto_barreras8, longitud_barreras8)

pygame.init()
ventana= pygame.display.set_mode((espaciojuego.get_ancho(),espaciojuego.get_alto()))
while raton1.get_vivo()==1:
    for event in pygame.event.get():
        ventana.fill('white')
        imagen=pygame.image.load('Raton.jpg')
        imagen_redimensionada= pygame.transform.scale(imagen,(20,20))
        ventana.blit(imagen_redimensionada, (raton1.get_posicionx(), raton1.get_posiciony()))
        pygame.draw.circle(ventana, 'yellow', (ancho_manzana, alto_manzana), 10)
        hitbox_manzana_ancho = range((ancho_manzana - 25), (ancho_manzana + 25))
        hitbox_manzana_alto = range((alto_manzana - 20), (alto_manzana + 20))
        if event.type == pygame.QUIT:
            raton1.set_vivo(0)
        elif event.type == pygame.KEYDOWN:
            #controles
            if event.key == pygame.K_DOWN:
                alto_raton = alto_raton+20
                raton1.set_posiciony(alto_raton)
                contador_movimientos=contador_movimientos+1
            elif event.key == pygame.K_UP:
                alto_raton=alto_raton-20
                raton1.set_posiciony(alto_raton)
                contador_movimientos = contador_movimientos + 1
            elif event.key == pygame.K_RIGHT:
                ancho_raton=ancho_raton+20
                raton1.set_posicionx(ancho_raton)
                contador_movimientos = contador_movimientos + 1
            elif event.key == pygame.K_LEFT:
                ancho_raton=ancho_raton-20
                raton1.set_posicionx(ancho_raton)
                contador_movimientos = contador_movimientos + 1
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
        if puntos>=1:
            if ((raton1.get_posiciony()+20) in (barreras_rango_altura)) and ((raton1.get_posicionx()+15) in (barreras_juego)):
                alto_raton=alto_raton-20
                raton1.set_posiciony(alto_raton)
            if ((raton1.get_posiciony()+20) in (barreras_rango_altura)) and ((raton1.get_posicionx()+15) in (barreras_juego)):
                ancho_raton=ancho_raton-15
                raton1.set_posicionx(ancho_raton)
            if ((raton1.get_posiciony()) in (barreras_rango_altura)) and ((raton1.get_posicionx()-5) in (barreras_juego)):
                ancho_raton=ancho_raton+15
                raton1.set_posicionx(ancho_raton)
            if ((raton1.get_posiciony()) in (barreras_rango_altura)) and ((raton1.get_posicionx()-5) in (barreras_juego)):
                alto_raton=alto_raton+20
                raton1.set_posiciony(alto_raton)
            pygame.draw.line(ventana, 'black', (barreras1.get_posicionx(), barreras1.get_posiciony()), (abarreras, barreras1.get_posiciony()), 10)
        if puntos>=2:
            if ((raton1.get_posiciony()+20) in (barreras_rango_altura2)) and ((raton1.get_posicionx()+15) in (barreras_juego2)):
                alto_raton=alto_raton-20
                raton1.set_posiciony(alto_raton)
            if ((raton1.get_posiciony()+20) in (barreras_rango_altura2)) and ((raton1.get_posicionx()+15) in (barreras_juego2)):
                ancho_raton=ancho_raton-15
                raton1.set_posicionx(ancho_raton)
            if ((raton1.get_posiciony()) in (barreras_rango_altura2)) and ((raton1.get_posicionx()-5) in (barreras_juego2)):
                ancho_raton=ancho_raton+15
                raton1.set_posicionx(ancho_raton)
            if ((raton1.get_posiciony()) in (barreras_rango_altura2)) and ((raton1.get_posicionx()-5) in (barreras_juego2)):
                alto_raton=alto_raton+20
                raton1.set_posiciony(alto_raton)
            pygame.draw.line(ventana, 'black', (barreras2.get_posicionx(), barreras2.get_posiciony()), (abarreras2, barreras2.get_posiciony()), 10)
        if puntos>=3:
            if ((raton1.get_posiciony()+20) in (barreras_rango_altura3)) and ((raton1.get_posicionx()+15) in (barreras_juego3)):
                alto_raton=alto_raton-20
                raton1.set_posiciony(alto_raton)
            if ((raton1.get_posiciony()+20) in (barreras_rango_altura3)) and ((raton1.get_posicionx()+15) in (barreras_juego3)):
                ancho_raton=ancho_raton-15
                raton1.set_posicionx(ancho_raton)
            if ((raton1.get_posiciony()) in (barreras_rango_altura3)) and ((raton1.get_posicionx()-5) in (barreras_juego3)):
                ancho_raton=ancho_raton+15
                raton1.set_posicionx(ancho_raton)
            if ((raton1.get_posiciony()) in (barreras_rango_altura3)) and ((raton1.get_posicionx()-5) in (barreras_juego3)):
                alto_raton=alto_raton+20
                raton1.set_posiciony(alto_raton)
            pygame.draw.line(ventana, 'black', (barreras3.get_posicionx(), barreras3.get_posiciony()), (abarreras3, barreras3.get_posiciony()), 10)
        if puntos>=4:
            if ((raton1.get_posiciony()+20) in (barreras_rango_altura4)) and ((raton1.get_posicionx()+15) in (barreras_juego4)):
                alto_raton=alto_raton-20
                raton1.set_posiciony(alto_raton)
            if ((raton1.get_posiciony()+20) in (barreras_rango_altura4)) and ((raton1.get_posicionx()+15) in (barreras_juego4)):
                ancho_raton=ancho_raton-15
                raton1.set_posicionx(ancho_raton)
            if ((raton1.get_posiciony()) in (barreras_rango_altura4)) and ((raton1.get_posicionx()-5) in (barreras_juego4)):
                ancho_raton=ancho_raton+15
                raton1.set_posicionx(ancho_raton)
            if ((raton1.get_posiciony()) in (barreras_rango_altura4)) and ((raton1.get_posicionx()-5) in (barreras_juego4)):
                alto_raton=alto_raton+20
                raton1.set_posiciony(alto_raton)
            pygame.draw.line(ventana, 'black', (barreras4.get_posicionx(), barreras4.get_posiciony()), (abarreras4, barreras4.get_posiciony()), 10)
        if puntos>=5:
            if ((raton1.get_posiciony()+20) in (barreras_rango_altura5)) and ((raton1.get_posicionx()+15) in (barreras_juego5)):
                alto_raton=alto_raton-20
                raton1.set_posiciony(alto_raton)
            if ((raton1.get_posiciony()+20) in (barreras_rango_altura5)) and ((raton1.get_posicionx()+15) in (barreras_juego5)):
                ancho_raton=ancho_raton-15
                raton1.set_posicionx(ancho_raton)
            if ((raton1.get_posiciony()) in (barreras_rango_altura5)) and ((raton1.get_posicionx()-5) in (barreras_juego5)):
                ancho_raton=ancho_raton+15
                raton1.set_posicionx(ancho_raton)
            if ((raton1.get_posiciony()) in (barreras_rango_altura5)) and ((raton1.get_posicionx()-5) in (barreras_juego5)):
                alto_raton=alto_raton+20
                raton1.set_posiciony(alto_raton)
            pygame.draw.line(ventana, 'black', (barreras5.get_posicionx(), barreras5.get_posiciony()), (abarreras5, barreras5.get_posiciony()), 10)
        if puntos>=6:
            if ((raton1.get_posiciony()+20) in (barreras_rango_altura6)) and ((raton1.get_posicionx()+15) in (barreras_juego6)):
                alto_raton=alto_raton-20
                raton1.set_posiciony(alto_raton)
            if ((raton1.get_posiciony()+20) in (barreras_rango_altura6)) and ((raton1.get_posicionx()+15) in (barreras_juego6)):
                ancho_raton=ancho_raton-15
                raton1.set_posicionx(ancho_raton)
            if ((raton1.get_posiciony()) in (barreras_rango_altura6)) and ((raton1.get_posicionx()-5) in (barreras_juego6)):
                ancho_raton=ancho_raton+15
                raton1.set_posicionx(ancho_raton)
            if ((raton1.get_posiciony()) in (barreras_rango_altura6)) and ((raton1.get_posicionx()-5) in (barreras_juego6)):
                alto_raton=alto_raton+20
                raton1.set_posiciony(alto_raton)
            pygame.draw.line(ventana, 'black', (barreras6.get_posicionx(), barreras6.get_posiciony()), (abarreras6, barreras6.get_posiciony()), 10)
        if puntos>=7:
            if ((raton1.get_posiciony()+20) in (barreras_rango_altura7)) and ((raton1.get_posicionx()+15) in (barreras_juego7)):
                alto_raton=alto_raton-20
                raton1.set_posiciony(alto_raton)
            if ((raton1.get_posiciony()+20) in (barreras_rango_altura7)) and ((raton1.get_posicionx()+15) in (barreras_juego7)):
                ancho_raton=ancho_raton-15
                raton1.set_posicionx(ancho_raton)
            if ((raton1.get_posiciony()) in (barreras_rango_altura7)) and ((raton1.get_posicionx()-5) in (barreras_juego7)):
                ancho_raton=ancho_raton+15
                raton1.set_posicionx(ancho_raton)
            if ((raton1.get_posiciony()) in (barreras_rango_altura7)) and ((raton1.get_posicionx()-5) in (barreras_juego7)):
                alto_raton=alto_raton+20
                raton1.set_posiciony(alto_raton)
            pygame.draw.line(ventana, 'black', (barreras7.get_posicionx(), barreras7.get_posiciony()), (abarreras7, barreras7.get_posiciony()), 10)
        if puntos>=8:
            if ((raton1.get_posiciony()+20) in (barreras_rango_altura8)) and ((raton1.get_posicionx()+15) in (barreras_juego8)):
                alto_raton=alto_raton-20
                raton1.set_posiciony(alto_raton)
            if ((raton1.get_posiciony()+20) in (barreras_rango_altura8)) and ((raton1.get_posicionx()+15) in (barreras_juego8)):
                ancho_raton=ancho_raton-15
                raton1.set_posicionx(ancho_raton)
            if ((raton1.get_posiciony()) in (barreras_rango_altura8)) and ((raton1.get_posicionx()-5) in (barreras_juego8)):
                ancho_raton=ancho_raton+15
                raton1.set_posicionx(ancho_raton)
            if ((raton1.get_posiciony()) in (barreras_rango_altura8)) and ((raton1.get_posicionx()-5) in (barreras_juego8)):
                alto_raton=alto_raton+20
                raton1.set_posiciony(alto_raton)
            pygame.draw.line(ventana, 'black', (barreras8.get_posicionx(), barreras8.get_posiciony()), (abarreras8, barreras8.get_posiciony()), 10)
        #contador de movimientos

        if contador_movimientos==20:
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