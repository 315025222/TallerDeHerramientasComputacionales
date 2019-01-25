def FaC(F):
    C = (F - 32) / 1.8
    return C


def FaCaprox(F):
    C = (F - 30) / 2.0
    return C


fahrenheit = [f for f in range(0, 55, 5)]
celsius = []
celsiusaprox = []

for f in fahrenheit:
    celsius.append(FaC(f))
    celsiusaprox.append(FaCaprox(f))

print("F               C      Caprox   diferencia")
for f, c, ca in zip(fahrenheit, celsius, celsiusaprox):
    dif = abs(c - ca)
    print("%5f %5f %5f %5f" % (f, c, ca, dif))
