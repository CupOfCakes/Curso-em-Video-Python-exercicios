n = list()

for c in range(0, 5):
    p = int(input("digite um valor: "))
    n.append(p)
n2 = n[:]
print("=" * 40)
print(f"a lista digitada foi: {n}")

print(f"o maior valor inserido foi {max(n)} na posição {n.index(max(n)) + 1}", end="")

if max(n) in n[n.index(max(n)) + 1:]:
    del n[n.index(max(n))]
    print(f" e {n.index(max(n)) + 2}")
else:
    print("")
n = n2
print(f"o menor valor inserido foi {min(n)} na posição {n.index(min(n)) + 1}", end="")

if min(n) in n[n.index(min(n)) + 1:]:
    del n[n.index(min(n))]
    print(f" e {n.index(min(n)) + 2}")
