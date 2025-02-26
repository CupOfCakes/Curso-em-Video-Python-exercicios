valor = float(input("qual o valor da casa que deseja comprar? "))
salario = float(input("qual e o seu salario atual? "))
anos = int(input("em quantos anos planeja pagar? se for pagar em meses digite 0: "))

if anos == 0:
    anos = int(input("em quantos meses deseja pagar? "))
    mensalidade = valor / anos
else:
    mensalidade = valor / (anos * 12)

if mensalidade > salario * 0.30:
    print("você e pobre demais para pagar ")
else:
    print("a mensalidade a ser paga e {:.2f}".format(mensalidade))
