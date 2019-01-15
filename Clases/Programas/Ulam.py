def ulam(x):
    x = float(x)
    if x < 1 or x.is_integer() == False:
        print("El número %g no es positivo o no es entero" % x)
    else:
        print(x)
        i = 0
        while x > 1:
            if x % 2 == 0:  #se puede poner el contador en el mismo nivel del else y del if
                x = x/2
                i += 1
                print(x)
            else:
                x = 3*x + 1
                i += 1
                print(x)
        print("El algoritmo se repitió " + str(i) + " veces")


ulam(1509)
