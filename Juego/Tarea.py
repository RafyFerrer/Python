#IMPORTAMOS EL PAQUETE PYGAME Y RANDOM

import pygame
import random

# INICIALIZAMOS EL ENTORNO PYGAME

pygame.init()

# DEFINIDOS LOS PARAMETROS INICIALES: DIMENSIÓN DE LA VENTANA DEL JUEGO, COORDENADAS POR DONDE SE MOVERÁ LA IMAGEN Y VELOCIDAD DE MOVIMIENTO

dimension_ventana = (800,600)
coord_y = dimension_ventana[1] // 2
coord_x = dimension_ventana[0] // 2
velocidad = 10

# INICIALIZAMOS LA VARIABLE QUE CONTROLA EL QUE EL JUEGO SIGA CORRIENDO.

running = True

# INICIALIZAMOS LOS PARÁMETROS ESTÉTICOS, ES DECIR, COLOR DE FONDO, IMAGEN QUE SE MOVERÁ Y LA MÚSICA DE FONDO.

color_fondo = '#7cb310'
imagen = pygame.image.load('.\images\Logo_299_200.png')
ventana = pygame.display.set_mode(dimension_ventana)
pygame.display.set_caption('Rafael Ángel Ferrer Martínez - IES Sierra de Segura')
pygame.display.set_icon(imagen)
pygame.mixer.music.load('.\sonidos\Adele.ogg')
pygame.mixer.music.play()

# EMPEZAMOS A CORRER EL JUEGO EN BUCLE
# FLECHAS MUEVEN LA IMAGEN POR LA VENTANA
# SI SE PULSA LA LETRA a minúscula SE MUEVE SOLA DE FORMA ALEATORIA

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and coord_y < dimension_ventana[1]-200:
                coord_y = coord_y + velocidad
            elif event.key == pygame.K_UP and coord_y > 0:
                coord_y = coord_y - velocidad
            elif event.key == pygame.K_LEFT and coord_x > 0:
                coord_x = coord_x - velocidad
            elif event.key == pygame.K_RIGHT and coord_x < dimension_ventana[0]-299:
                coord_x = coord_x + velocidad
            elif event.key == pygame.K_a:
                coord_x = random.randrange(0,dimension_ventana[0]-299)
                coord_y = random.randrange(0,dimension_ventana[1]-200)


# TRAS DETECTAR LA TECLA PULSADA Y MODIFICAR LAS COORDINADAS PERTINENTES, REPINTAMOS EN LA VENTANA "TRASERA"

    ventana.fill(color_fondo)
    ventana.blit(imagen,(coord_x,coord_y))

# NOS LLEVAMOS LO REPINTADO A LA VENTANA "DELANTERA" ES DECIR, LA QUE VE EL USUARIO.

    pygame.display.flip()

# SE CIERRA EL JUEGO CON LO CUAL MATAMOS EL ENTORNO PYGAME

pygame.quit()

