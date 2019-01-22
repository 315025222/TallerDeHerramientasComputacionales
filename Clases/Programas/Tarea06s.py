from Tarea06 import *
for n in range(1, 101):
    x = integralRiemman(-1, 1, n)
    print("El resultado con " + str(n) + " particiones es " + str(x))
