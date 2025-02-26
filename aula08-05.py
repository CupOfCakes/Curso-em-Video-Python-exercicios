import random

print("======SORTEIO======")
a1 = input("nome do 1 aluno: ")
a2 = input("nome do 2 aluno: ")
a3 = input("nome do 3 aluno: ")
a4 = input("nome do 4 saluno: ")
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(lista)
