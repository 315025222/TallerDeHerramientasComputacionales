#Encontrar el mcd de dos números
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
    print(divx)
    print(divy)
    longy = len(divy)
    lista = []

    for i in range(0, longx):
        for j in range(0, longy):
            if divx[i] == divy[j]:
                lista.append(divx[i])

    lista.sort()
    mayor = lista[len(lista) - 1]
    print(lista)
    return mayor


