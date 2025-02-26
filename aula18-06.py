media = []
lista = []
fakelist = []
while True:
    fakelist.append(str(input("nome do aluno: ")).title())
    fakelist.append(float(input("1 nota: ")))
    fakelist.append(float(input("2 nota: ")))

    median = (fakelist[-1] + fakelist[-2]) / 2
    media.append(median)
    lista.append(fakelist[:])
    fakelist =[]

    c = str(input("quer continuar?[S/N]: ")).strip().upper()[0]

    while c != "S" and c != "N":
        c = str(input("quer continuar?[S/N] ")).strip().upper()[0]

    if c == "N":
        break

print("=" * 40)
print("N  Nome        Media")
for i in range(0, len(lista)):
    print(f"{i}  {lista[i][0]:<12} {media[i]}")
print("=" * 40)
while True:
    e = int(input("mostra notas de qual aluno? 999 finaliza o programa: "))

    if e < len(lista):
        print(lista[e])
        print("=" * 40)

    if e > len(lista) - 1 and e != 999:
        print("aluno inexistente")
        print("=" * 40)

    if e == 999:
        print("=" * 6 + "programa finalizado" + "=" * 6)
        break
