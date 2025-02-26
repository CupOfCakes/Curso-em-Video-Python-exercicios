def metade(num):
    num = num / 2
    return num


def dobro(num):
    num = num * 2
    return num


def aumentar(num):
    num = num * 1.10
    return num


def diminuir(num):
    num = num * 0.87
    return num


def moeda(num):
    moeda = str(f"R${num:.2f}").replace(".", ",")
    return moeda


def resumo(a, b=0, c=0):
    print("=" * 50)
    print(f"{'RESUMO DO VALOR':^50}")
    print("=" * 50)
    print(f"{'Preço analisado:':<42}{a:>8.2f}")
    print(f"{'Dobro do preço':<42}{a*2:>8.2f}")
    if b != 0:
        t = 1 + b/100
        print(f"{b}{'% de aumento':<40}{a*t:>8.2f}")
    if c != 0:
        t = 1 - c / 100
        print(f"{c}{'% de desconto':<40}{a*t:>8.2f}")
    print("=" * 50)




