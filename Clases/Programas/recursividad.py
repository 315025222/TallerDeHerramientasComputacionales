def fib(n):
    if n > 2:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1


#print(fib(1))
#print(fib(10))


def fib2(n, lfib):
    if n > len(lfib):
        lfib.append(fib(n - 1) + fib(n-2))
        return [fib(n - 1) + fib(n-2), lfib]
    if n == len(lfib):
        return [lfib[n - 1], lfib]
    if n < len(lfib):
        return [lfib[n - 1], lfib]
    if n < 2 and len(lfib) < 2:
        lfib = [1, 1]
        return [1, lfib]


x = fib2(5, [1, 1])
print(x)


def suma(n):
    if n > 1:
        return 1
    else:
        return n + suma(n-1)


#print(suma(9))


def printr(lista):
    if len(lista) == 0:
        printr(lista)
    elif len(lista) == 1:
        print(lista[0])
    else:
        print(lista[len(lista) - 1]), #le puse las comas, sin embargo no se imprime en lineas separadas.
        printr(lista[:len(lista) - 1])


lisa = [1, 2, 3, 4, 5, 6, 7]
#printr(lisa)
