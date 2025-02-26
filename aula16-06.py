p = ("cachoeira", "chocolate", "golfinho", "aurora boreal", "flores", "arvore")

for c in range(0, len(p)):
    print(f"a palavra {p[c].upper()} tem as vogais:", end="")
    for l in range(0, len(p[c])):
        if p[c][l] == "a":
            print(" a", end="")
        if p[c][l] == "e":
            print(" e", end="")
        if p[c][l] == "i":
            print(" i", end="")
        if p[c][l] == "o":
            print(" o", end="")
        if p[c][l] == "u":
            print(" u", end="")
    print("")

'''palavras = ("cachoeira", "chocolate", "golfinho", "aurora boreal", "flores", "arvore")

for p in palavras:
    print(f"\nNa palavra {p.upper()} temos", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")'''
