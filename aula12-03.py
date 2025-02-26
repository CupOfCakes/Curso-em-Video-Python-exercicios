n1 = int(input("digite o 1 numero: "))
n2 = int(input("digite o 2 numero: "))
lista = [n1, n2]

if n1 != n2:
    print("o maior valor e {} e o menor e {}".format(max(lista), min(lista)))
else:
    print("e pra escrever numero diferentes \33[31mBOBALHÃO\33[m")
