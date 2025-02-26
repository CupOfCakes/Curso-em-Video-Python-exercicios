def leiaint():
    while True:
        try:
            n = int(input("Digite um numero inteiro: "))
        except ValueError:
            print("\33[31mERRO!!! Digito invalido, Tente novamente\33[m")
        except KeyboardInterrupt:
            print("\33[31m programa interrompido\33[m")
            n = 0
            return n
        else:
            return n


def leiafloat():
    while True:
        try:
            n = float(input("Digite um numero real: "))
        except ValueError:
            print("\33[31mERRO!!! Digito invalido, Tente novamente\33[m")
        except KeyboardInterrupt:
            print("\33[31m programa interrompido\33[m")
            n = 0
        else:
            return n


n = leiaint()
f = leiafloat()
print(f"voce acabou de digitar {n} como numero inteiro e {f} como numero real")