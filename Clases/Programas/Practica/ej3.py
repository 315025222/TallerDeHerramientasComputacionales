def sumaCubica(n):
    sumita = 0
    while n > 0:
        sumita += n ** 3
        n -= 1
    return sumita


def formulaCubica(n):
    r = (n*(n+1)/2.0)**2
    return r


print("Comparando la suma con la fórmula:")
for i in range(1, 11):
    print(str(sumaCubica(i)) + " " + str(formulaCubica(i)))
