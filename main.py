# Example file showing a circle moving on screen
import pygame
from tablero import Tablero
# pygame setup
pygame.init()
screen = pygame.display.set_mode((360, 720))
clock = pygame.time.Clock()
running = True
dt= 0
fila_jugador = 0
columna_jugador = 4



#Llamada al Tablero
tablero = Tablero()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    
    # pintar el tablero
    tablero.colorear_tablero()

    pygame.draw.rect(screen, "black", [96, 46, 176, 346], 2)

    keys = pygame.key.get_pressed()
    if(keys[pygame.K_w] and fila_jugador>=0):
        fila_jugador -= 1
    if(keys[pygame.K_s] and fila_jugador<tablero.filas_tablero-1):
        fila_jugador += 1
    if(keys[pygame.K_a] and columna_jugador>=0 and tablero.tablero_color[fila_jugador][columna_jugador-1] != "red"):
        columna_jugador -= 1
    if (keys[pygame.K_d] and columna_jugador<tablero.columnas_tablero-1 and tablero.tablero_color[fila_jugador][columna_jugador+1] != "red"):
        columna_jugador += 1
    

    #Control para que no sobrepase el rango del tablero
    if(fila_jugador<0):
        fila_jugador=0
    if(columna_jugador<0):
        columna_jugador = 0
    if(fila_jugador<tablero.filas_tablero-1):
        fila_jugador += 1
    

    #validar que hacia abajo si se pueda mover
    if(fila_jugador<tablero.filas_tablero-1):    
        if(tablero.tablero_color[fila_jugador+1][columna_jugador] == "red"):
            tablero.tablero_color[fila_jugador][columna_jugador] = "red"
            fila_jugador = 0
            columna_jugador = 4
    if(fila_jugador==tablero.filas_tablero-1):
        tablero.tablero_color[fila_jugador][columna_jugador] = "red"
        fila_jugador = 0
        columna_jugador = 4

    for i in range(20):
        for j in range(10):
            pygame.draw.rect(screen,tablero.tablero_color[i][j],(tablero.tablero[i][j].x,tablero.tablero[i][j].y,15,15))

    pygame.draw.rect(screen,"green",(tablero.tablero[fila_jugador][columna_jugador].x,tablero.tablero[fila_jugador][columna_jugador].y,15,15))


    # flip() the display to put your work on screen
    pygame.display.flip()
    
    
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(5) / 300

pygame.quit()
