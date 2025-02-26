print("======CALCULADORA DE IMC======")
altura = float(input("qual a sua altura em metros? "))
peso = float(input("qual e o seu peso em Kg? "))

imc = peso / altura**2

print("seu imc e de {:.2f}".format(imc))

if imc < 18.5:
    print("vc esta abaixo do peso")
elif 18.5 >= imc < 25:
    print("vc esta no peso ideal")
elif 25 <= imc < 30:
    print("vc esta sobrepeso")
elif 30 <= imc <= 40:
    print("vc esta obeso")
else:
    print("vc sofre de obesidade morbida, SUA BALEIA")
