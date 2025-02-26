import random
escolhido = random.randint(1,5)

n = int(input("tente acerta o numero q o computador escolheu entre 1 e 5: "))

if escolhido == n:
    print("acertou maldito!!")
else:
    print("errou bobão, ele pensou no {}".format(escolhido))
