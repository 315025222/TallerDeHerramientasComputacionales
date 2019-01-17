bandera = True
while bandera:
    print("bienvenido al 911")
    print("Los servicios son:")
    print("1.- Ambulancia")
    print("2.- Policia")
    print("3.- Bomberos")
    x = input("elija algún numero de servicio o presione q para salir: ")
    if x == "1":
        print("La ambulancia está en camino")
        break
    elif x == "2":
        print("La policia está en camino")
        break
    elif x == "3":
        print("Los bomberos están en camino")
        break
    elif x == "q":
        break
    else:
        print("Utilice un valor válido es decir 1, 2, 3 o q")
print("Gracias por utilizar el 911")
