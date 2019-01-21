import grados
import math
L1 = grados.listaC(-15, 32, 10)
L2 = grados.gradosF(L1)
grados.mostrarListas(L1, L2)
print(L1)
print(list(enumerate(L1)))
'''a = input("cuál es el extremo izquierdo del intervalo ")
b = input("cuál es el extremo derecho del intervalo ")
n = input("Cuántos subintervalos ")
a = int(a)
b = int(b)
n = int(n)
print(type(a))
print(type(b))
print(type(n))
L1 = grados.listaC(a, b, n)
L2 = grados.gradosF(L1)
grados.mostrarListas(L1, L2)'''


def sumar5(lista):
    for i in range(len(lista)):
        lista[i] += 5


print(L1)
sumar5(L1)
print(L1)


def f(x):
    y = 2 * x + 5 * x ** 2 - 6 * x ** 3 + 12
    return y


def df(x):
    y = 2 + 20 * x - 18 * x ** 2
    return y


def raices(a, b, c):
    t1 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    t2 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return [t1, t2]


gradosC = [-5 + i * 0.5 for i in range(12)]
gradosF = [(C * 1.8) + 32 for C in gradosC]
print(gradosC)
print(gradosF)
C_mas_5 = [C+5 for C in gradosC]

print(gradosC)
print(gradosF)
for c, f in zip(gradosC, gradosF):
    print(c, f)

s = [[c, f] for c, f in zip(gradosC, gradosF)]
print(s)
