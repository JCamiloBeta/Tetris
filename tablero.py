tablero = [[0 for j in range(10)] for i in range(20)]

# Recorrer la matriz
for i in range(20):
    print()
    for j in range(10):
        elemento = tablero[i][j]
        # Haz algo con el elemento (por ejemplo, imprimirlo)
        print(elemento, end=" ")