import math
# La integral de Riemman.


def f(x):
    y = (2 * x) + (5 * x ** 2) - (6 * x ** 3) + 12
    return y


def df(x):
    y = 2 + 20 * x - 18 * x ** 2
    return y


def raices(a, b, c):
    t1 = (-b - math.sqrt(b ** 2.0 - 4.0 * a * c)) / (2.0 * a)
    t2 = (-b + math.sqrt(b ** 2.0 - 4.0 * a * c)) / (2.0 * a)
    return [t1, t2]


def integralRiemman(a, b, n):
    p0 = a
    p1 = a + (b-a)/n
    area = 0
    for i in range(0, n):
        base = p1 - p0
        pMedio = (p0 + p1) / 2.0
        altura = f(pMedio)
        area += base * altura
        p0 += (b-a)/n
        p1 += (b-a)/n
    return area

