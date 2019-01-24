import numpy
lab = [[True, True, True, True], [False, False, False, True], [True, True, False, True]]


def resolver(lista, e, d):
    n = len(lista[0])
    x = e[0]
    y = e[1]
    camino = [e]
    if y == d[1] and x == d[0]:
        camino.append(e)
        print(camino)
        return e[0], e[1]
    else:
        if lista[x][y + 1] == False:
            e = [x, y + 1]
            camino.append(e)
            print(camino)
            return resolver(lista, e, d)
        elif lista[x + 1][y] == False:
            e = [x + 1, y]
            camino.append(e)
            print(camino)
            return resolver(lista, e, d)


r = resolver(lab, [1, 0], [2, 2])
print(r)
print(numpy.matrix(lab))
