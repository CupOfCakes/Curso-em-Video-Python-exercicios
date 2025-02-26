print("======MÉDIA======")

d = 0
s = 0
n = 0
p = "indefinido"
maior = 0
menor = 0

while p not in "N":
    n = int(input("digite um valor: "))
    s += n
    p = str(input("quer adicionar outro valor?[S/N]: ")).upper().strip()[0]
    d += 1

    if d == 1:
        menor = maior = n
    else:
        if maior < n:
            maior = n
        elif menor > n:
            menor = n

n = s / d

print("a soma dos valores e {}, foram {} valores, sua media foi de {:.2f}".format(s, d, n))
print("o maior valor foi {} e o menor foi de {}".format(maior, menor))
