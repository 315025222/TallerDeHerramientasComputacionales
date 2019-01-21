def listaC(Cmax, Cmin, n):
    gradosC = []
    dC = (Cmax - Cmin)/float(n-1)
    for i in range(n):
        C = Cmin + i*dC
        gradosC.append(C)

    return gradosC


def gradosF(gradosC):
    gradosF = []
    for C in gradosC:
        F = 1.8 * C + 32
        gradosF.append(F)

    return gradosF


def mostrarListas(gradosC, gradosF):
    print(" C      F")
    for i in range(len(gradosC)):
        C = gradosC[i]
        F = gradosF[i]

        print("%5.1f %5.1f" % (C, F))



