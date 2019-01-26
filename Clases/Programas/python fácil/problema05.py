# Diseñe y programe un algoritmo recursivo que encuentre la salida de un laberinto, teniendo en cuenta que el laberinto
# se toma como entrada y que es una matriz de valores True, False, (x,y), (a,b), donde True indica un obstáculo;
# False, una celda por la que se puede caminar; (x,y) el punto donde comienza a buscarse la salida
# y (a,b), la salida del laberinto
import numpy
# mi función pide un laberinto en forma de matriz, la entrada, la salida y un registro vacio.
def resolver(lista, e, d, registro=[]):
    x = e[0]
    y = e[1]
    camino = [e]
    if y == d[1] and x == d[0]:
        camino.append(e)
        print(camino)
        return e[0], e[1]
    else:
        if lista[x][y + 1] == False and not (x, y + 1) in registro:
            registro.append((x, y))
            e = [x, y + 1]
            camino.append(e)
            print(camino)
            return resolver(lista, e, d, registro)

        elif lista[x + 1][y] == False and not (x + 1, y) in registro:
            registro.append((x, y))
            e = [x + 1, y]
            camino.append(e)
            print(camino)
            return resolver(lista, e, d, registro)

        elif lista[x - 1][y] == False and not (x - 1, y) in registro:
            registro.append((x, y))
            e = [x - 1, y]
            camino.append(e)
            print(camino)
            return resolver(lista, e, d, registro)

        elif lista[x][y - 1] == False and not (x, y - 1) in registro:
            registro.append((x, y))
            e = [x, y - 1]
            camino.append(e)
            print(camino)
            return resolver(lista, e, d, registro)

