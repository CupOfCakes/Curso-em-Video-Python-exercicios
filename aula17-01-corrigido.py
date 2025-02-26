n = list()
min = max = 0

for c in range(0, 5):
    p = int(input("digite um valor: "))
    n.append(p)
    if max < p or c == 0:
        max = p
    if min > p or c == 0:
        min = p

print("=" * 30)
print(f"a lista digitada foi {n}")
print(f"o maior valor foi de: {max}, nas posições: ", end="")
for i, v in enumerate(n):
    if v == max:
        print(f"{i + 1}, ", end="")
print("")
print(f"o menor valor foi de: {min}, nas posições: ", end="")
for i, v in enumerate(n):
    if v == min:
        print(f"{i + 1}, ", end="")
