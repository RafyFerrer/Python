import pygame
pygame.init()
ancho = 640
alto = 480
y_cuadrado = alto // 2
x_cuadrado = ancho // 2
running = True
screen = pygame.display.set_mode((ancho,alto))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y_cuadrado = y_cuadrado + 10
            elif event.key == pygame.K_UP:
                y_cuadrado = y_cuadrado - 10
            elif event.key == pygame.K_LEFT:
                x_cuadrado = x_cuadrado - 10
            elif event.key == pygame.K_RIGHT:
                x_cuadrado = x_cuadrado + 10

    screen.fill('blue')
    pygame.draw.rect(screen,'red',(x_cuadrado,y_cuadrado,10,10))
    pygame.display.flip()
pygame.quit()

