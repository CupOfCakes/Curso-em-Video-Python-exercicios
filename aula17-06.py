p = str(input("escreva a equação, deixe ela dentro de parenteses: "))

print("=" * 40)

if p.count("(") != p.count(")"):
    print("equação invalida")
else:
    print("equação valida :)")
