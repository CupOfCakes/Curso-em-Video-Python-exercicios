pesom = 0
peson = 0
for c in range(0, 5):
    peso = float(input("qual e o seu peso? "))
    if peson == 0:
        peson = peso
    elif peson > peso:
        peson = peso
    if pesom < peso:
        pesom = peso
print("o maior peso foi de {}, e o menor foi de {}".format(pesom, peson))
