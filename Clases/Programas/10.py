c = -20
ic = 5
while c <= 40:
    f = 9/5*c + 32
    print("{} celsius ______ {} fahrenheit".format(c, f))
    c = c + ic

'''L = [1, 4, 6, 45]
print(L)
while bool(L):
    L.pop()

print(L)'''
gradosC = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
print("="*50)
print("   C    F")
for grado in gradosC:
    F = (9.0/5) * grado + 32
    print("%5d %5.1f" % (grado, F))

gradosC = []
for C in range(-20, 45, 5):
    gradosC.append(C)
print(gradosC)

gradosC = []
for i in range(0, 21):
    C = -20 + i * 2.5
    gradosC.append(C)
print(len(gradosC))

gradosC = [-20]
i = 0
while gradosC[len(gradosC)-1] != 30:
    C = gradosC[i] + 2.5
    gradosC.append(C)
    i += 1
print(gradosC)
