def rangef(a, b, c):  # genera rangos con saltos flotantes
    lista = []
    d = a
    while d < b:
        lista.append(d)
        d += c
    return lista


'''def cuadranteLateral(x):
    if x >= 0:
        cotainf = int(x)
        cotamedia = int(x) + 0.5
        cotasup = int(x) + 1
        print(cotainf)
        print(cotasup)
        if cotainf <= x <= cotamedia:
            return [cotainf, cotamedia]
        elif cotamedia <= x <= cotasup:
            return [cotamedia, cotasup]
    else:
        cotainf = int(x)
        cotamedia = int(x) - 0.5
        cotasup = int(x) - 1
        print(cotainf)
        print(cotasup)
        if cotainf >= x >= cotamedia:
            return [cotamedia, cotainf]
        elif cotamedia >= x >= cotasup:
            return [cotasup, cotamedia]


def cuadranteVertical(x):
    if -1 <= x <= 0:
        return [-1, 0]
    elif 0 <= x <= 1:
        return [0, 1]
    elif 1 <= x:
        n = 1
        while 3*n + 1 < x:
            n += 1

        if 3*n - 0.5 <= x <= 3*n + 1:
            return [3*n - 0.5, 3*n + 1]

        elif 3*n - 2 <= x <= 3*n - 0.5:
            return [3*n - 0.5, 3*n + 1]

    elif x <= -1:
        n = 1
        while -3*n - 1 > x:
            n += 1

        if -3*n + 0.5 >= x >= -3*n - 1:
            return [-3*n - 1, -3*n + 0.5]

        elif -3*n + 2 >= x >= -3*n + 0.5:
            return [-3*n + 2, -3*n + 0.5]


d = cuadranteVertical(-3)
print(d)
c = cuadranteLateral(1.4)
print(c)'''


def hacerMalla():  # hace la malla con listas anidadas
    malla = []
    for i in rangef(2.5, 8.0, 1.5):
        for j in rangef(3.5, 5.1, 0.5):
            malla.append([j, i])
        for j in rangef(-5, -3.4, 0.5):
            malla.append([j, i])
    for i in rangef(-7, -2.4, 1.5):
        for j in rangef(3.5, 5.1, 0.5):
            malla.append([j, i])
        for j in rangef(-5, -3.4, 0.5):
            malla.append([j, i])
    return malla


'''m = hacerMalla()
print(len(m))
print(m)'''
