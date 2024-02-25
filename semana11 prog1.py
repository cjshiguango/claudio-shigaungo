# Definimos una matriz 3x3
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Definimos el valor que queremos buscar
valor_a_buscar = 5

def buscar_en_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"El valor {valor} se encontró en la posición ({i}, {j}) de la matriz."
    return f"El valor {valor} no se encontró en la matriz."

# Llamamos a la función y mostramos el resultado
print(buscar_en_matriz(matriz, valor_a_buscar))

