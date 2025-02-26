n1 = int(input("digite um numero: "))
n2 = int(input("digite um numero: "))
n3 = int(input("digite um numero: "))
n4 = int(input("digite um numero: "))

tn = (n1, n2, n3, n4)
p = c3 = n9 = 0

for c in range(len(tn)):
    if tn[c] == 9:
        n9 += 1
    if tn[c] % 2 == 0:
        p += 1
    if tn[c] == 3 and c3 == 0:
        c3 = c

print("=" * 20)
if p != 0:
    print(f"foram indentificados {p} numeros pares") #tn.count(9)
if n9 != 0:
    print(f"e {n9} numeros 9")
if c3 != 0:
    print(f"o primeiro 3 digitado esta na posição {c3 + 1}") #tn.index(3)+1

