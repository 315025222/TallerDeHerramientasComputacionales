#!/usr/bin/python3.6
#_*_ coding utf-8 _*_
import math as m
from math import sqrt as s
'''
Sandoval Amador Carlos Emiliano
315025222

'''
x = 10.5; y = 1.0/3; z = 15.3
# x, y, z = 10.5, 1.0/3, 15.3
H = '''
El punto en R3 es:
(x, y, z) = (%.2f, %g, %G)


'''%(x, y, z)
print("Hoy es miércoles")
print(H)
G = '''
El punto en R3 es:
(x, y, z) = ({LAx:.2f}, {LAy:g}, {LAz:G})


'''.format(LAx=x, LAy=y, LAz=z)
print(G)
x = 16

x = input("Cuál es el valor al que le quieres\n" + "calcular la raíz")
print("La raíz cuadrada de %2f es %f"%(x, m.sqrt(x)))
print(s(16.5))

