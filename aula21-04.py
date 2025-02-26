def leiaint(msg):
    while True:
        if msg.isnumeric():
            break
        else:
            print("erro, digite um numero valido")
            msg = input("Digite um numero: ")
    return msg


n = leiaint(input("Digite um numero: "))
print(f"voce acabou de digitar {n}")
