# Definimos una matriz 3x3
matriz = [[9, 2, 5], [4, 7, 1], [6, 3, 8]]

def ordenar_fila(matriz, fila):
    # Usamos el algoritmo de ordenación Bubble Sort
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1] :
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]
    return matriz

# Imprimimos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenamos la primera fila (fila 0)
matriz_ordenada = ordenar_fila(matriz, 0)

# Imprimimos la matriz con la fila ordenada
print("\nMatriz con la primera fila ordenada:")
for fila in matriz_ordenada:
    print(fila)