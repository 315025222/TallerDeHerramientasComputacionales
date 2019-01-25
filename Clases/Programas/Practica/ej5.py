from Practica.ej4 import hacerMalla


def f(x, y):  # hacemos la función de la silla de montar
    z = ((x ** 2) / 25.0) - ((y ** 2) / 49)
    return z


malla = hacerMalla()
for punto in malla:  # calcula la función en cada punto de la malla
    print("El valor de f(x,y) en el punto {} es {:.3f}".format(punto, f(punto[1], punto[0])))
