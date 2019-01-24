# Programe una función que determine si un número entero suministrado como argumento es primo.
def divisores(x):
    if x == 0:
        return [1]
    else:
        x = abs(x)
        candidato = x
        lista = []
        while candidato > 0:
            if x % candidato == 0:
                lista.append(candidato)
            candidato -= 1

        return lista


def primo(c):
    divisorsones = divisores(c)
    if len(divisorsones) == 2:
        return True
    else:
        return False


