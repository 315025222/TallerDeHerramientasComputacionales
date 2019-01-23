def fib(n):
    if n > 2:
        return fib(n -1) + fib(n-2)
    else:
        return 1


print(fib(1))
print(fib(10))


def suma(n):
    if n > 1:
        return 1
    else:
        return n + suma(n-1)


print(suma(9))


def printr(lista):
    if len(lista) == 0:
        printr(lista)
    elif len(lista) == 1:
        print(lista[0])
    else:
        print(lista[len(lista) - 1])
        printr(lista[:len(lista) - 1])


lisa = [1, 2, 3, 4, 5, 6, 7]
printr(lisa)
