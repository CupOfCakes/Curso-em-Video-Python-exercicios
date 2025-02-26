def metade(num, bool=False):
    num = num / 2
    if bool:
        num = str(f"R${num:.2f}").replace(".", ",")
    return num


def dobro(num, bool=False):
    num = num * 2
    if bool:
        num = str(f"R${num:.2f}").replace(".", ",")
    return num


def aumentar(num, bool=False):
    num = num * 1.10
    if bool:
        num = str(f"R${num:.2f}").replace(".", ",")
    return num


def diminuir(num, bool=False):
    num = num * 0.87
    if bool:
        num = str(f"R${num:.2f}").replace(".", ",")
    return num


def moeda(num):
    moeda = str(f"R${num:.2f}").replace(".", ",")
    return moeda