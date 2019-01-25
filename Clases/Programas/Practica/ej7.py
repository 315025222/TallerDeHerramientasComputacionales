from math import sin, pi


def H_eps(x, eps=0.01):
    if x < -eps:
        return 0
    elif -eps <= x <= eps:
        y = 1/2.0 + x/(2*eps) + 1/(2*eps)*sin(pi*x/eps)
        return y
    elif x > eps:
        return 1


def prueba_H_eps():
    x = -5
    print("Cuando x < -eps el resultado es {}\n".format(H_eps(x)))
    x = -0.01
    print("Cuando x = -eps el resultado es {}\n".format(H_eps(x)))
    x = 0
    print("Cuando x = 0 el resultado es {}\n".format(H_eps(x)))
    x = 0.01
    print("Cuando x = eps el resultado es {}\n".format(H_eps(x)))
    x = 5
    print("Cuando x > eps el resultado es {}".format(H_eps(x)))


prueba_H_eps()
