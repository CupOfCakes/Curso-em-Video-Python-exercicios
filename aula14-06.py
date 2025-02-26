n = int(input("digite o numero: "))
r = int(input("digite a razão: "))
c = 0
t = 0

while c != 10:
    print(n, end=" ")
    n = n + r
    c += 1
    t += 1
    if c == 10:
        q = int(input("\nquantos termos a mais quer ver? Se quiser terminar o progama digite 0: "))
        c -= q
        if q == 0:
            print("o programa foi terminado com {} termos".format(t))


        