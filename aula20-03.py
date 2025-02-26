def contador(a, b, c):
    print("=" * 40)
    if c == 0:
        c = 1
    if c > 0:
        print(f"contagem de {a} ate {b} de {c} em {c}")
        for c in range(a, b+1, c):
            print(f"{c} ", end="")
    elif c < 0:
        print(f"contagem de {a} ate {b} de {abs(c)} em {abs(c)}")
        for c in range(a, b-1, c):
            print(f"{c} ", end="")
    print()


contador(1, 10, 1)
contador(10, 0, -2)

print("=" * 40)
print("faça uma contagem personalizada *0*")
print("*se quiser fazer uma contagem regressiva o pula devera ser negativo")
contador(int(input("inicio: ")), int(input("fim: ")), int(input("pulo: ")))
