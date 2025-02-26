s = 0
q = 0
for c in range(1, 7):
    n = int(input("digite um numero: "))
    if n % 2 == 0:
        s += n
        q += 1
if s == 0:
    print("\33[31mvc não digitou nenhum numero par\33[m")
else:
    print("vc digitou {} numeros pares, a soma deles e {}".format(q, s))
