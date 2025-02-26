v = int(input("qual a velocidade do carro: "))

if v > 80:
    print("VOCÊ FOI MULTADO\ntera que pagar {}".format(7*(v-80)))
else:
    print("segue reto")
