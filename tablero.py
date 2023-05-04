import pygame

class Tablero():
        
    def __init__(self):
        self.filas_tablero = 20
        self.columnas_tablero = 10
        self.tablero = [[0 for j in range(self.columnas_tablero)] for i in range(self.filas_tablero)]
        self.tablero_color = [[0 for j in range(self.columnas_tablero)] for i in range(self.filas_tablero)]

    def colorear_tablero(self):
        for i in range(20):
            posy = 50+i*17
            for j in range(10):
                posx = 100+j*17
                if(self.tablero_color[i][j] != "red" and self.tablero_color[i][j] != "green"):
                    self.tablero_color[i][j] = "blue"
                self.tablero[i][j] = pygame.Vector2(posx, posy)
    