#la integral
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


