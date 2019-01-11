i = 62
r = 189876545.7654675432

# imprime los números con comillas "" de forma que
# veamos la longitud del campo
print('"%d"' % i)       # campo mínimo

print('"%5d"' % i)      # campo de longitud de 5 caracteres
print('"%05d"' % i)     # pad with zeros

print('"%g"' % r)       # r es un número grande así que usamos notación científica
print('"%G"' % r)       # E en el exponente
print('"%e"' % r)       # notación científica compacta
print('"%E"' % r)       # notación científica compacta
print('"%20.2E"' % r)   # 2 decimales, campo de longitud 20
print('"%30g"' % r)     # campo de longitud 30 (ajustado hacia la derecha)
print('"%-30g"' % r)    # ajustado hacia la izquierda
print('"%-30.4g"' % r)  # 3 decimales

print('%s' % i)  # puede convertir i a string automáticamente
print('%s' % r)

# Usa %% para imprimir el signo de porcentaje
print('%g %% of %.2f Euro is %.2f Euro' %
      (5.1, 346, 5.1/100*346))
