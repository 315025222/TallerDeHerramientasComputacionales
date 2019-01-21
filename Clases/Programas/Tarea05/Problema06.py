#Calcular el promedio de 10 datos
def promedio(listota):
    suma = 0
    for i in range(0, len(listota)):
        suma += listota[i]

    promedin = suma / len(listota)
    return promedin


