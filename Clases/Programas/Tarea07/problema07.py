# Determine el propósito del siguiente algoritmo y determine un buen nombre para la función


def diferenciaPyN(l):  # hace la diferencia de números positivos menos números negativos, si el resultado es positivo,
    # hay más positivos, si es negativo hay más negativos y si es cero el número de positivos y de negativos es el mismo
    a = 0
    b = 0
    for i in l:
        if i > 0:
            a += 1
        else:
            a -= 1
    return a + b


lista = [-1, -2, 3, 4, 5]

c = diferenciaPyN(lista)
print(c)
