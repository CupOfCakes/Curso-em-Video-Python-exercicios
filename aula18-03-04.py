matriz = []
dado = list()
f = 0
sp = 0
suc = 0
m2 = 0

while f != 3:
    for c in range(0, 3):
        dado.append(int(input(f"adicione um digito na posição [{f}][{c}]: ")))
        if dado[-1] % 2 == 0:
            sp += dado[-1]

        if c == 2:
            suc += dado[-1]

        if m2 < dado[-1] and f == 1:
            m2 = dado[-1]

    matriz.append(dado[:])

    c = 0
    f += 1
    dado = []

print("=" * 30)
for c in range(0, 3):
    print(f"[ {matriz[c][0]} ]", end="")
    print(f"[ {matriz[c][1]} ]", end="")
    print(f"[ {matriz[c][2]} ]", end="")
    print("")
print("=" * 30)
print(f"a soma dos valores pares foi de {sp}")
print(f"a soma dos valores da ultima coluna foi de {suc}")
print(f"o mair valor da 2 linha foi {m2}")
