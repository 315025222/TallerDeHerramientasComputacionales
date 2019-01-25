from Practica.ej4 import hacerMalla


def f(x, y):
    z = ((x ** 2) / 25.0) - ((y ** 2) / 49)
    return z


malla = hacerMalla()
for punto in malla:
    print("El valor de f(x,y) en el punto {} es {:.3f}".format(punto, f(punto[1], punto[0])))
