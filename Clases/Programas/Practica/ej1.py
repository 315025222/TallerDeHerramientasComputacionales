def FaC(F):  # hace la conversión exacta de fahrenheit a celsius
    C = (F - 32) / 1.8
    return C


def FaCaprox(F):  # hace la conversión aproximada de fahrenheit a celsius
    C = (F - 30) / 2.0
    return C


fahrenheit = [f for f in range(0, 55, 5)]  # hacemos una lista de fahrenheit
celsius = []
celsiusaprox = []

for f in fahrenheit:  # hacemos una lista de celsius y de celsius aproximados
    celsius.append(FaC(f))
    celsiusaprox.append(FaCaprox(f))

print("F               C      Caprox   diferencia")
for f, c, ca in zip(fahrenheit, celsius, celsiusaprox):  # Los comparamos en una tabla
    dif = abs(c - ca)
    print("%5f %5f %5f %5f" % (f, c, ca, dif))
