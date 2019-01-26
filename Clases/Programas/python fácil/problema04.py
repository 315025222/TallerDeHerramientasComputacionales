# Programe una función que dado un número x devuelva una lista infinita con todos los múltiplos de x.
def infinite(x):
    n = 0
    while True:
        yield x * n
        n += 1


generator = infinite(2) # esto devuelve un generador que es un objeto iterable como las listas, solo que
# solo se puede iterar una vez

# lista = list(generator)  este código nos devulve la lista que queremos, pero lamentablemente nunca acaba
