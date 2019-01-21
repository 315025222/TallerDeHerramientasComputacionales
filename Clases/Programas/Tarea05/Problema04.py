# Sucesión de Fibonacci hasta el n-ésimo término
def Fib(n):
    lista = [1, 1]

    if n == 1:
        return lista[0]
    elif n == 2:
        return lista[1]
    else:
        while n > 2:
            n -= 1
            lista.append(lista[len(lista) - 2] + lista[len(lista) - 1])
        print(lista)
        return lista[len(lista) - 1]




