l = list()
while True:
    n = int(input("digite um valor: "))

    if n not in l:
        l.append(n)
    elif n in l:
        print("digito ja inserido")

    c = str(input("quer continuar?[S/N]: ")).strip().upper()[0]

    while c != "S" and c != "N":
        c = str(input("quer continuar?[S/N] ")).strip().upper()[0]

    if c == "N":
        break
print("=" * 40)
print(f"os numeros que vc digitou em ordem crescente e: {sorted(l)}")
