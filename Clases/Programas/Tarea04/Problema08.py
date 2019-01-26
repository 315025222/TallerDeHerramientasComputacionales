import random
x = random.randrange(1, 11)
x = str(x)
# print(x)
y = input("elige un número del uno al diez: ")

# print(y)
if y == x:
    print("¡Has ganado un auto!")
else:
    print("No has ganado nada")
