print("======LOJINHA======")

mpreco = -1
mname = ""
soma = 0
more = 0
produtos = 0

while True:
    name = str(input("nome do produto: "))
    preco = float(input("preço: "))

    if mpreco >= preco or mpreco == -1:
        mpreco = preco
        mname = name

    if preco >= 1000:
        more += 1

    soma += preco
    produtos += 1

    c = str(input("quer continuar[S/N]: ")).strip().upper()[0]

    while c != "S" and c != "N":
        c = str(input("digito invalido\nquer continuar[S/N]: ")).strip().upper()[0]

    print("=" * 20)

    if c == "N":
        break

print(f'''você compru {produtos} produtos
o valor da compra foi {soma}
{more} desses produtos valem mais de R$ 1000
o produto mais barato foi a/o {mname} que custa {mpreco}''')
