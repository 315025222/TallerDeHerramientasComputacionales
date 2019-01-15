def ulam(x):
    if x < 1 or x.is_integer() == False:
        print("El número %g no es positivo o no es entero" % x)
    else:
        print(x)
        while x > 1:
            if x % 2 == 0:
                x = x/2
                print(x)
            else:
                x = 3*x + 1
                print(x)


ulam(17)
print(17.0.is_integer())
