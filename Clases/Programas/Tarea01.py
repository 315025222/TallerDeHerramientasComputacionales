# Sandoval Amador Carlos Emiliano
# Problema propio.
# Lanzas una pelota verticalmente desde el techo de un edificio alto en el borde de este. La bola deja tu mano a una
# velocidad de 15m/s. Encuentra la posicion y la velocidad de la bola 1 segundo y 4 segundos despues.
# Primero resolvemos para el tiempo de 1 segundo.
v0 = 15
t = 1
g = 9.81
x = v0*t +1/2*g*t**2
v = v0 + g*t
print("Cuando el tiempo es 1 segundo")
print("La posición es " + str(x) + " m")  # imprimimos la posicion y la velocidad en ese tiempo.
print("La velocidad es " + str(v) + " m/s")
print("\n")
# Luego resolvemos para el tiempo de 4 segundos.
v0 = 15
t = 4
g = 9.81
x = v0 * t + 1/2 * g * t ** 2
v = v0 + g * t
print("Cuando el tiempo es 4 segundos")
print("La posición es " + str(x) + " m")  # imprimimos la posicion y la velocidad en ese tiempo.
print("La velocidad es " + str(v) + " m/s")
