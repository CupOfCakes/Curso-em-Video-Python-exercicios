print("=" * 6 + "\33[1:32mMERCADINHO\33[m" + "=" * 6)
preco = float(input("qual o preço do produto que ira levar? "))
pagamento = int(input("[1]dinheiro/cheque, 10% de desconto"
                      "\n[2]cartão, 5% de desconto"
                      "\n[3]2x no cartão\n"
                      "[4]3x ou mais o cartão, 20% de juros\n"
                      "Qual sera o metodo de pagamento? "))

if pagamento == 1:
    print("valor da compra = \33[33m{:.2f}\33[m".format(preco*0.90))
elif pagamento == 2:
    print("valor da compra = \33[33m{:.2f}\33[m".format(preco * 0.95))
elif pagamento == 3:
    print("valor da compra = \33[33m{:.2f}\33[m".format(preco))
    print("você tera de pagar \33[34m2\33[m parcelas de \33[33m{:.2f}\33[m".format(preco/2))
elif pagamento == 4:
    parcelas = int(input("ira parcelar quantas vezes? "))
    preco = preco * 1.20
    print("valor da compra = \33[33m{:.2f}\33[m".format(preco))
    print("você tera de pagar \33[34m{}\33[m parcelas de \33[33m{:.2f}\33[m".format(parcelas, preco / parcelas))
else:
    print("\33[31mvc sabe ler????\33[m")
