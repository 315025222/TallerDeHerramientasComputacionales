# Sucesión de Fibonacci hasta el n-ésimo término
def Fib(n):
    x1 = 1
    x2 = 1
    if n == 1:
        return x1
    elif n == 2:
        return x2
    else:
        while n > 2:
            n -= 1
            guardador = x2
            x2 = x1 + x2
            x1 = guardador
        return x2



