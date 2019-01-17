# Dados 10 datos indicar el mayor, el menor y el promedio.
def MmP(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):  # devuelve el mayor, el menor y el promedio en una lista en ese orden
    lista = []
    lista.append(x1)
    lista.append(x2)
    lista.append(x3)
    lista.append(x4)
    lista.append(x5)
    lista.append(x6)
    lista.append(x7)
    lista.append(x8)
    lista.append(x9)
    lista.append(x10)
    lista.sort()
    menor = lista[0]
    mayor = lista[9]
    promedin = (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10) / 10
    return [mayor, menor, promedin]

