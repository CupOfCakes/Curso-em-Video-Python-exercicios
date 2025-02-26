print("======FATORIAL======")
n = int(input("qual numero deseja saber o fatorial?: "))
p = n - 1
r = p * n

while p != 2:
    p -= 1
    r = p * r

print("{}! e {}".format(n, r))
