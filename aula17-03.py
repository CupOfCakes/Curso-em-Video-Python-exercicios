l = list()
while True:
    n = int(input("digite um valor: "))

    if not l or n >= l[-1]:
        l.append(n)
    else:
        pos = 0
        while pos < len(l):
            if n <= l[pos]:
                l.insert(pos, n)
                break
            pos += 1

    c = str(input("quer continuar?[S/N]: ")).strip().upper()[0]

    while c != "S" and c != "N":
        c = str(input("quer continuar?[S/N] ")).strip().upper()[0]

    if c == "N":
        break
print("=" * 40)
print(f"os numeros que vc digitou em ordem crescente e {l}")