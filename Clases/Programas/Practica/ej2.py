def sumaCuadrada(n):
    sumita = 0
    while n > 0:
        sumita += n ** 2
        n -= 1
    return sumita


def formulaCuadrada(n):
    r = (n*(n+1)*(2*n + 1))/6.0
    return r


print("Comparando la suma con la fórmula:")
for i in range(1, 11):
    print(str(sumaCuadrada(i)) + " " + str(formulaCuadrada(i)))
