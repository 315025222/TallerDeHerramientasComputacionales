# Determine el propósito del siguiente algoritmo y determine un buen nombre para la función
def normaMayor(l):  # determina la norma más grande entre pares de números reales contenidos en una lista.
    a = 0
    for i in l:
        for j in l:
            if abs(i - j) > a:
                a = abs(i - j)
    return a


