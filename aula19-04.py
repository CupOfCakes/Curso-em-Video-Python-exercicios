fakelist = []
soma = 0
jogador = {"nome": str(input("Nome do jogador: ")).title()}
jogador["jogos"] = int(input(f"quantos jogos {jogador['nome']} jogou: "))

for c in range(0, jogador["jogos"]):
    fakelist.append(int(input(f"quantos gols na partida {c+1}: ")))
    soma += fakelist[-1]
jogador["total"] = soma
jogador["gols"] = fakelist.copy()

print("=" * 40)

print(jogador)

print("=" * 40)

for k, v in jogador.items():
    print(f"o campo {k} tem o valor {v}")


print("=" * 40)
for c in range(0, jogador["jogos"]):
    print(f"=> Na partida {c+1}, fez {jogador['gols'][c]}")
print(f"foi um total de {jogador['soma']} gols")
