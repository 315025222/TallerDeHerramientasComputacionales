#Calcular la suma de los primeros n números naturales
def suma(n):
    sumita = 0
    lista = []
    impresion = ""
    contador = 0
    while n > 0:
        lista.append(n)
        sumita += n
        n -= 1
    lista.reverse()
    for i in range(0, len(lista)):

        if contador != len(lista) - 1:
            impresion += str(lista[i]) + " + "
        else:
            impresion += str(lista[i]) + " = " + str(sumita)
        contador += 1
    print(impresion)
    return sumita



