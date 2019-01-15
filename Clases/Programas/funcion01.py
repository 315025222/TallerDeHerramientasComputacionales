def vabsoluto(x):
    if x >= 0:
        return x
    else:
        return -x


z = 10
while z > 0:
    z = z - 1

print(z)


def raiz(x):
    h = x
    b = 1.0
    e = 0.0001
    while vabsoluto(b - h) > e:
        h = (b + h)/2
        b = x/h
    return b


print(raiz(9))
print(raiz(4))
print(raiz(1000000))


def raiz1(x):
    h = x
    b = 1.0
    e = 0.0001
    z = 0
    while vabsoluto(b - h) > e:
        z += 1
        h = (b + h)/2
        b = x/h

    return [x, b]


lista = raiz1(9)

print("Hice la operación " + str(lista[0]) + " veces y la raíz vale " + str(lista[1]))
