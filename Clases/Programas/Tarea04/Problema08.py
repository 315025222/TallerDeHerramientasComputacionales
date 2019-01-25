import random
x = random.randrange(1, 11)
print(x)
print(type(x))
y = input("elige un número del uno al diez: ")
int(y)
print(y)
if y is x:
    print("¡Has ganado un auto!")
else:
    print("No has ganado nada")
