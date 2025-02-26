print("=" * 6 + "PROGRESSÃO ARITMETICA" + "=" * 6)
n = int(input("qual o numero da PA: "))
r = int(input("quantos sera o pulo: "))

print(n)

for c in range(1, 10):
    n += r
    print(n)
