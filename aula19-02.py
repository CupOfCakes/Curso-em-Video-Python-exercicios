from random import randint
from operator import itemgetter
jogadores = {}
ranking = []

for c in range(1, 5):
    jogadores[f"jogador{c}"] = randint(1, 6)

print("======valores sorteados======")
for v, k in jogadores.items():
    print(f"o {v} tirou {k}")
print()

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print("======RANKING======")
for i, v in enumerate(ranking):
    print(f"{i+1} lugar: {v[0]} com {v[1]}")
