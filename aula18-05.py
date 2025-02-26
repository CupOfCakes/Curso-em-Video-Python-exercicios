from random import randint
lista = []
fakelist = []
cont = 0
print("=" * 6 + "MEGA SENA" + "=" * 6)

n = int(input("quantos jogos quer jogar: "))
print("=" * 30)

for c in range(0, n):
    for i in range(0, 6):
        num = randint(1, 60)
        while num in fakelist:
            num = randint(1, 60)
        if num not in fakelist:
            fakelist.append(num)

    lista.append(fakelist)
    fakelist = []

for c in range(0, n):
    print(f"jogo {c+1} : {lista[c]}")
