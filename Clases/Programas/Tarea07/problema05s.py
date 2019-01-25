import numpy
from Tarea07.problema05 import resolver

labEnfrente = [[True, True, True], [False, False, False], [True, True, True]]
labAbajo = [[True, True, True, True], [False, False, False, True], [True, True, False, True]]
labArriba = [[True, True, False, True], [False, False, False, True], [True, True, True, True]]
labRegreso = [[False, False, False, True], [True, True, False, True], [False, False, False, True],
              [True, True, True, True]]

print("La ruta del laberinto cuya salida está enfrente")
r = resolver(labEnfrente, [1, 0], [1, 2], registro=[])
print(r)
print(numpy.matrix(labEnfrente))
print(" ")
print("La ruta del laberinto cuya salida está abajo")
r = resolver(labAbajo, [1, 0], [2, 2], registro=[])
print(r)
print(numpy.matrix(labAbajo))
print(" ")
print("La ruta del laberinto cuya salida está arriba")
r = resolver(labArriba, [1, 0], [0, 2], registro=[])
print(r)
print(numpy.matrix(labArriba))
print(" ")
print("La ruta del laberinto cuya salida está en el mismo lado que la entrada")
r = resolver(labRegreso, [2, 0], [0, 0], registro=[])
print(r)
print(numpy.matrix(labRegreso))

