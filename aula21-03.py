def ficha(msg, num):
    if msg == "":
        msg = "<desconhecido>"
    if num.isnumeric():
        num = int(g)
    else:
        num = 0
    print(f"o jogador {msg} fez {num} gol(s) no campeonato")


n = str(input("nome do jogador: "))
g = input("numeros de gols: ")
ficha(n, g)
