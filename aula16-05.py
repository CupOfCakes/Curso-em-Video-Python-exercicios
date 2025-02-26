p = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "estojo", 25.00, "transferidor", 4.20)

for c in range(0, len(p), 2):
    print(f"{p[c]:.<30}R$ {p[c + 1]:.2f}")
