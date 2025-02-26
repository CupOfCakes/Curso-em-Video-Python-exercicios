l = list()
while True:
    n = int(input("digite um valor: "))
    l.append(n)

    c = str(input("quer continuar?[S/N]: ")).strip().upper()[0]

    while c != "S" and c != "N":
        c = str(input("quer continuar?[S/N] ")).strip().upper()[0]

    if c == "N":
        break

print("=" * 30)
print(f"foram digitados {len(l)} numeros")
print(f"o numeros em ordem decrescente são: {sorted(l)[::-1]}")
if 5 in l:
    print("o numero 5 esta na lista")
else:
    print("o numero 5 não esta na lista")
