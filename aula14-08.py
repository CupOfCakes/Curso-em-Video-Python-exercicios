print("======SOMADOR DE NUMEROS======")
print("se quiser parar digite 999")


s = 0
c = 0

n = int(input("digite o valor: "))
while True:
    if n == 999:
        break
    s += n
    c += 1
    n = int(input("digite o valor: "))

print("voce digitou {} numeros a soma deles e {}".format(c, s))
