def contar_v1(adn, base):
    adn = list(adn)
    i = 0
    for c in adn:
        if c == base:
            i += 1
    return i


def contar_v2(adn, base):
    i = 0
    for c in adn:
        if c == base:
            i += 1
    return i


def contar_v3(adn, base):
    i = 0
    for c in range(0, len(adn)):
        if adn[c] == base:
            i += 1
    return i


def contar_v4(adn, base):
    i = 0
    j = 0
    while j < len(adn):
        if adn[j] == base:
            i += 1
            j += 1
    return i


adn1 = "ATGCGACCTAT"
base = "C"
print(contar_v1(adn1, base))
print(contar_v2(adn1, base))
print(contar_v3(adn1, base))
print(contar_v4(adn1, base))
