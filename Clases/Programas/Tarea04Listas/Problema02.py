# Encontrar los tiempos dada la posición
from math import sqrt


def tiempos(y, v0):
    t1 = (-v0 + sqrt(v0**2 - 4*(-4.9)*(-y))) / (-9.8)
    t2 = (-v0 - sqrt(v0**2 - 4*(-4.9)*(-y))) / (-9.8)
    return [t1, t2]
