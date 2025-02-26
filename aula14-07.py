p = int(input("quantos termos da sequencia de Fibonacci quer ver?: "))
c = 0
n = 0
s = 0
m = 1

while c != p:
    if c == 0:
        print("0", end="")
        s = 1
        n = 1
        c += 1
    print(" -> {}".format(n), end="")
    s = n
    n = m
    m = n + s
    c += 1
