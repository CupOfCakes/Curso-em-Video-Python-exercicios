def area(a, b):
    print("=" * 30)
    v = a * b
    print(f"a area de um terreno {a} x {b} e de {v:.2f}")


area(float(input("qual a largura da area: ")), float(input("qual o comprimento da area: ")))
