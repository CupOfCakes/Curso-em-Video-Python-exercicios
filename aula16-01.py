n = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze",
     "quatorze", "quinze", "dezesseis", "dezesete", "dezoito", "dezenove", "vinte")

print("======NUMERO POR EXTENSO======")
while True:
    e = int(input("qual numero entre 0 e 20 deseja ver: "))

    if 0 <= e <= 20:
        print("o numero que digitou em extenso e " + n[e].upper())
        c = str(input("quer continuar?[S/N]: ")).strip().upper()[0]
        if c == "N":
            break
    else:
        print("digito invalido")
