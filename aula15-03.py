from random import randint
print("======PAR OU IMPAR======")
vitoria = 0

while True:
    player = str(input("escolha par ou impar[P/I]: ")).strip().upper()[0]
    
    while player != "P" and player != "I":
        print("digito invalido")
        player = str(input("escolha par ou impar[P/I]: ")).strip().upper()[0]
    
    jogada = int(input("qual valor ira jogar: "))
    pc = randint(0, 100)

    if (jogada + pc) % 2 == 0 and player == "P":
        print(f"voce ganhou\no computador jogou {pc}\nVamos jogar de novo")
        vitoria += 1
        print("=" * 25)
    elif (jogada + pc) % 2 == 1 and player == "I":
        print(f"voce ganhou\no computador jogou {pc}\nVamos jogar de novo")
        vitoria += 1
        print("=" * 25)
    else:
        print(f"\33[31mVoce Perdeu\33[m\no computador jogou {pc}\nvc teve {vitoria} vitorias consecutivas")
        break
