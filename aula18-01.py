p = list()
g = list()
maior = menor = 0

while True:
    dado = list()
    dado.append(str(input("Qual seu nome: ")))
    dado.append(int(input("Qual seu peso: ")))

    if maior < dado[1] or p == []:
        maior = dado[1]

    if menor > dado[1] or p == []:
        menor = dado[1]

    p.append(dado[:])

    c = str(input("quer continuar?[S/N]: ")).strip().upper()[0]

    while c != "S" and c != "N":
        c = str(input("quer continuar?[S/N] ")).strip().upper()[0]

    if c == "N":
        break

print("=" * 30)
print(f"vc cadastrou {len(p)} pessoas")
print(f"o mais gordo foi de {maior}Kg, de ", end="")
for c, i in enumerate(p):
    if p[c][1] == maior:
        print(f"{p[c][0]}, ", end="")
print("")
print(f"o mais magro foi de {menor}Kg, de ", end="")
for c, i in enumerate(p):
    if p[c][1] == menor:
        print(f"{p[c][0]},  ", end="")
