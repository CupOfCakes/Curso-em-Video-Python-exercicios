from random import randint
numeros = []


def sorteia(list):
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    print(f"os valores sorteados foram {numeros}")


def soma(list):
    soma = 0
    for c in range(0, len(list)):
        if numeros[c] % 2 == 0:
            soma += numeros[c]
    print(f"a soma dos valores pares na listas e {soma}")


sorteia(numeros)
soma(numeros)
