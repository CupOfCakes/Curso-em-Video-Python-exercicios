def leiaDinheiro(msg):
    msg = msg.strip().replace(",", ".")
    while True:
        if msg.isalpha() or msg == "":
            print("\33[31mErro!!! Digite um numero valido\33[m")
            msg = input("Digite um numero: ")
        else:
            break
    return float(msg)
