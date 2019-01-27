from pythonFacil.problema06 import hanoi
num = 4
torre = ["o", 4, 3, 2, 1]
desti = ["d"]
aux = ["a"]
print("La solución a las torres de hanoi para %d discos es:" % num)
print("{} {} {}".format(torre, aux, desti))
hanoi(num, torre, desti, aux)
