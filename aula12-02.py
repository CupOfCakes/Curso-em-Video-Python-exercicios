print("=" * 6+"CONVERSOR DE BASES NUMERICAS"+"=" * 6)
n = int(input("qual numero INTEIRO deseja converter? "))

a = int(input("[1] Binario\n[2] Octadecimal\n[3] Hexadecimal\npara qual deseja converter? escreva o numero indicado: "))

if a == 1:
    print("{} em binario e: {}".format(n, bin(n)[2:]))
elif a == 2:
    print("{} em octal e: {}".format(n, oct(n)[2:]))
elif a == 3:
    print("{} em hexadecimal e: {}".format(n, hex(n)[2:]))
