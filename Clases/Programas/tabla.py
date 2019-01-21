# Construye una lista con grados fahrenheit dada un con celsius y construye una lista anidada.
gradosC = [-5 + i * 0.5 for i in range(12)]
gradosF = [(C * 1.8) + 32 for C in gradosC]
listaAnidada = [[c, f] for c, f in zip(gradosC, gradosF)]
print(gradosC)
print(gradosF)
print(listaAnidada)
