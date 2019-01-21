def listaC(Cmax, Cmin, n):
    gradosC = []
    dC = (Cmax - Cmin)/float(n-1)
    for i in range(n):
        C = Cmin + i*dC
        gradosC.append(C)
        return gradosC


def gradosF(gradosC):
    gradosF = []
    for i in gradosC:
        F = 1.8 * gradosC[i] + 32
        gradosF.append(F)

    return gradosF
