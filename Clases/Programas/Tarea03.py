import math
def diana(x, y):
    if x < 5:
        if y < 10:
            return 3
        if 10 <= y <= 30:
            return 5
        if 30 < y:
            return 3
    if 5 <= x <= 25:
        if y < 10:
            return 7
        if 10 <= y <= 30:
            return 10
        if 30 < y:
            return 7
    if 25 < x:
        if y < 10:
            return 3
        if 10 <= y <= 30:
            return 5
        if 30 < y:
            return 3



z = diana(5, 10) # RADIO 10 CENTRO (15,20)
print(z)
def checarCirculo(x, y):
    Dx = abs(15 - x)
    Dy = abs(20 - y)
    distancia = math.sqrt(Dx ** 2 + Dy ** 2)
    if distancia < 10:
        return True
    else:
        return False


def diana2(x, y):
    if x < 5:
        if y < 10:
            return 3
        if 10 <= y <= 30:
            return 5
        if 30 < y:
            return 3

    if 5 <= x <= 25:
        if y < 10:
            return 7

        if 10 <= y <= 30:
            if checarCirculo(x, y):
                return 10
            else:
                return 100
        if 30 < y:
            return 7
    if 25 < x:
        if y < 10:
            return 3
        if 10 <= y <= 30:
            return 5
        if 30 < y:
            return 3


