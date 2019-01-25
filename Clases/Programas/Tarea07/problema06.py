# Programe una solución recursiva al conocido juego de las torres de Hanoi
def printbien(a, b, c):
    if a[0] == "o":
        if b[0] == "d":
            print("{} {} {}".format(a, c, b))
    if a[0] == "o":
        if c[0] == "d":
            print("{} {} {}".format(a, b, c))

    if b[0] == "o":
        if a[0] == "d":
            print("{} {} {}".format(b, c, a))
    if b[0] == "o":
        if c[0] == "d":
            print("{} {} {}".format(b, a, c))

    if c[0] == "o":
        if a[0] == "d":
            print("{} {} {}".format(c, b, a))
    if c[0] == "o":
        if b[0] == "d":
            print("{} {} {}".format(c, a, b))


def hanoi(ndiscos, origen, destino, auxiliar):
    if ndiscos == 1:
        x = origen.pop()
        destino.append(x)
        printbien(origen, destino, auxiliar)
    else:
        hanoi(ndiscos - 1, origen, auxiliar, destino)
        x = origen.pop()
        destino.append(x)
        printbien(origen, destino, auxiliar)
        hanoi(ndiscos - 1, auxiliar, destino, origen)

