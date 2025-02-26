p = list()
i = list()
l = list()
while True:
    n = int(input("digite um valor: "))
    l.append(n)

    if n % 2 == 0:
        p.append(n)

    if n % 2 == 1:
        i.append(n)

    c = str(input("quer continuar?[S/N]: ")).strip().upper()[0]

    while c != "S" and c != "N":
        c = str(input("quer continuar?[S/N] ")).strip().upper()[0]

    if c == "N":
        break

print("=" * 40)
print(f"a lista digitada foi {l}")
print(f"os numeros pares nela são: {p}")
print(f"os numeros impares nela são: {i}")