# Diseñe y programe un algoritmo recursivo que encuentre la salida de un laberinto, teniendo en cuenta que el laberinto
# se toma como entrada y que es una matriz de valores True, False, (x,y), (a,b), donde True indica un obstáculo;
# False, una celda por la que se puede caminar; (x,y) el punto donde comienza a buscarse la salida
# y (a,b), la salida del laberinto
import numpy
labEnfrente = [[True, True, True], [False, False, False], [True, True, True]]
labAbajo = [[True, True, True, True], [False, False, False, True], [True, True, False, True]]
labArriba = [[True, True, False, True], [False, False, False, True], [True, True, True, True]]


def resolver(lista, e, d, registro=[]):
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
            registro.append([x, y])
            e = [x, y + 1]
            camino.append(e)
            print(camino)
            return resolver(lista, e, d, registro)

        elif lista[x + 1][y] == False:
            registro.append([x, y])
            e = [x + 1, y]
            camino.append(e)
            print(camino)
            return resolver(lista, e, d, registro)

        elif lista[x - 1][y] == False:
            registro.append([x, y])
            e = [x - 1, y]
            camino.append(e)
            print(camino)
            return resolver(lista, e, d, registro)


print("La ruta del laberinto cuya salida está enfrente")
r = resolver(labEnfrente, [1, 0], [1, 2])
print(r)
print(numpy.matrix(labEnfrente))

print("La ruta del laberinto cuya salida está abajo")
r = resolver(labAbajo, [1, 0], [2, 2])
print(r)
print(numpy.matrix(labAbajo))

print("La ruta del laberinto cuya salida está arriba")
r = resolver(labArriba, [1, 0], [0, 2])
print(r)
print(numpy.matrix(labArriba))

'''print("La ruta del laberinto cuya salida está en el mismo lado que la entrada")
r = resolver(labArriba, [1, 0], [0, 2])
print(r)
print(numpy.matrix(labArriba))'''

