s = 0
for c in range(0, 500, 3):
    if c % 2 == 1:
        s += c
print("a soma dos multiplos de 3 entre 1 e 500 é {}".format(s))
