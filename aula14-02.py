from random import randint
n = randint(0, 10)
tentativas = 0

print("o computador pensou em um numero entre 0 e 10")
player = int(input("qual numero vc acha q o computador pensou: "))

while player != n:
    print("\33[31mvc errou, LOSER\33[m \ntente novamente")
    player = int(input("qual numero vc acha q o computador pensou: "))
    tentativas += 1

if n == player:
    print("\33[36myou win\33[m")
    print("vc precisou de {} tentativas".format(tentativas))
