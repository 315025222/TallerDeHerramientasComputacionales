#Convertir fahrenheit a celsius y viceversa
def FaC(F):
    C = (F - 32) / 1.8
    return [C]


def CaF(C):
    F = (C * 1.8) + 32
    return [F]


