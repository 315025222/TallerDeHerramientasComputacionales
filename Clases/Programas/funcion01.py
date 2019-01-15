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
    i = 0
    while vabsoluto(b - h) > e:
        i += 1
        h = (b + h)/2
        b = x/h
    print("Hice la operación " + str(i) + " veces")
    return b


print(raiz1(0))
