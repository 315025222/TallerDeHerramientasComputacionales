def rangeF(a, b, c):
    lista = []
    d = a
    while d < b:
        lista.append(d)
        d += c
    return lista


x = rangeF(-30, -20, 3.4)
print(x)
