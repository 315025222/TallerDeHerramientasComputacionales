def sumaCubica(n):  # calcula la suma sumando
    sumita = 0
    while n > 0:
        sumita += n ** 3
        n -= 1
    return sumita


def formulaCubica(n):  # calcula la suma con fórmula
    r = (n*(n+1)/2.0)**2
    return r


print("Comparando la suma con la fórmula:")  # los muestro en la consola
for i in range(1, 11):
    print(str(sumaCubica(i)) + " " + str(formulaCubica(i)))
