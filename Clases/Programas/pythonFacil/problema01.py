# Programe una función que determine si dos listas son iguales. Dos listas se consideran iguales
# si tienen igual longitud y sus elementos en cada índice también lo son.


def listasIguales(lista1, lista2):
    if len(lista1) == len(lista2):
        for i, j in zip(lista1, lista2):
            if i != j:
                return False
        return True
    else:
        return False


