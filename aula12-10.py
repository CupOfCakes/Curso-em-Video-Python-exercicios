import random
print("======JOKENPO======")
lista = ["pedra", "papel", "tesoura"]
pc = random.choice(lista)

print("pedra, papel ou tesoura")
player = str(input("o que ira jogar? ")).lower().strip()

if pc == player.lower():
    print("deu impate o computador jogou", pc)
elif pc == "pedra" and player == "papel":
    print("você ganhou *0*, o computador jogou", pc)
elif pc == "pedra" and player == "tesoura":
    print("voce perdeu :(, o computador jogou", pc)
elif pc == "papel" and player == "tesoura":
    print("você ganhou *0*, o computador jogou", pc)
elif pc == "papel" and player == "pedra":
    print("voce perdeu :(, o computador jogou", pc)
elif pc == "tesoura" and player == "pedra":
    print("você ganhou *0*, o computador jogou", pc)
elif pc == "tesoura" and player == "papel":
    print("voce perdeu :(, o computador jogou", pc)
else:
    print("\33[31mescreve direito PNC\33[m")
