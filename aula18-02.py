lista = []
cont = 0
for c in range(0, 7):
    n = (int(input("digite um numero: ")))

    if n % 2 == 0:
        lista.insert(0, n)
        cont += 1
    if n % 2 == 1:
        lista.append(n)

print("=" * 30)
print(f"a lista digitada e: {lista}")

if 0 < cont < 7:
    print(f"os pares digitados são: {sorted(lista[:cont])}")
    print(f"os impares digitados são {sorted(lista[cont:])}")
elif cont == 7:
    print(f"os pares digitados são: {sorted(lista)}")
    print("não teve numeros impares digitados")
elif cont == 0:
    print("não teve numeros pares digitados")
    print(f"os impares digitados são {sorted(lista)}")


