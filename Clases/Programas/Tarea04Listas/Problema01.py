# Encontrar el mcd de dos números
def divisores(x):
    if x == 0:
        return [1]
    else:
        x = abs(x)
        candidato = x
        lista = []
        while candidato > 0:
            if x % candidato == 0:
                lista.append(candidato)
            candidato -= 1

        return lista


def mcd(x, y):
    divx = divisores(x)
    divy = divisores(y)
    longx = len(divx)
    longy = len(divy)
    lista = []
    if x == 0 and y == 0:
        return -1
    elif x == 0:
        return divy[0]
    elif y == 0:
        return divx[0]
    else:
        for i in range(0, longx):
            for j in range(0, longy):
                if divx[i] == divy[j]:
                    lista.append(divx[i])

        lista.sort()
        mayor = lista[len(lista) - 1]
        return mayor


