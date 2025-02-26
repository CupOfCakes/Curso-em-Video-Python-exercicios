d = int(input("por quantos dias o carro foi alugado? "))
k = float(input("quantos quilometros o carro andou? "))
print("o total a ser pago e {:.2f}".format(d * 60 + 0.15 * k))
