import datetime
pessoa = {"nome": str(input("Nome: "))} 
data = int(input("ano de nascimento: "))
pessoa["idade"] = datetime.date.today().year - data
pessoa["ctps"] = int(input("carteira de trabalho (0 não tem): "))

if pessoa["ctps"] != 0:
    pessoa["contratação"] = int(input("ano de contratação: "))
    pessoa["salario"] = int(input("salario: "))
    pessoa["aposentadoria"] = pessoa["contratação"] - data + 30

print("=" * 40)
for k, v in pessoa.items():
    print(f"{k} tem o valor {v}")
