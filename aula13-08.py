print("="*6 + "POLINDROMO" + "="*6)
f = str(input("escreva a frase que deseja analizar: ")).replace(" ", "").lower()
if f == f[::-1]:
    print("e um polindromo")
else:
    print("não e um polindromo")
