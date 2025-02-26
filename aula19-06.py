truelist = []
while True:
    fakelist = []
    soma = 0
    jogador = {"nome": str(input("Nome do jogador: ")),
               "jogos": int(input("quantos jogos ele jogou: "))}

    for c in range(0, jogador["jogos"]):
        fakelist.append(int(input(f"quantos gols na partida {c+1}: ")))
        soma += fakelist[-1]

    jogador["gols"] = fakelist.copy()
    jogador["total"] = soma
    truelist.append(jogador.copy())

    e = str(input("quer continuar?[S/N]: ")).strip().upper()[0]
    print("=" * 40)

    while e != "S" and e != "N":
            e = str(input("quer continuar?[S/N] ")).strip().upper()[0]

    if e == "N":
        break

print(f"N {'Nome':<10} {'Total':<10} {'Gols'}  ")
for c in range(0, len(truelist)):
    print(f"{c} {truelist[c]['nome']:<10} {truelist[c]['total']:<10} {truelist[c]['gols']}")

print("=" * 40)
while True:
    r = int(input("Mostrar dados de quais jogador? 999 finaliza o programa: "))
    if -1 < r < len(truelist):
        print(f"dados do jogador(a) {truelist[r]['nome']}: ")
        for c in range(0, truelist[r]["jogos"]):
            print(f"=> Na partida {c+1}, fez {truelist[r]['gols'][c]} gols")
    elif r == 999:
        break
    else:
        print("jogador inexistente")
    print("=" * 40)
