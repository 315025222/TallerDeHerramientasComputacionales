# Programe una función que reciba una matríz de enteros y devuelva una tupla con la lista o vector
# de la suma de cada fila y otro vector con la suma de cada columna


def sumaFyC(matriz):
    listaF = []
    listaC = []
    sumaF = 0
    sumaC = 0

    for fila in range(0, len(matriz)):
        for columna in range(0, len(matriz[fila])):
            sumaF += matriz[fila][columna]
        listaF.append(sumaF)
        sumaF = 0

    for columna in range(0, len(matriz[0])):
        for fila in range(0, len(matriz)):
            sumaC += matriz[fila][columna]
        listaC.append(sumaC)
        sumaC = 0
    return tuple([listaF, listaC])


