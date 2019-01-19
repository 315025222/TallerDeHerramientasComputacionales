import Tarea04Listas.Problema03 as p3
lista = []
for i in range(0, 11):
    lista.append(i)

fahrenheit = 234
for i in lista:
    celsius = p3.FaC(fahrenheit)
    print("{} F es igual a {} C".format(fahrenheit, celsius[0]))
    fahrenheit += 10

print("=" * 50)

celsius = 353
for i in lista:
    fahrenheit = p3.CaF(celsius)
    print("{} C es igual a {} F".format(celsius, fahrenheit[0]))
    celsius += 10
