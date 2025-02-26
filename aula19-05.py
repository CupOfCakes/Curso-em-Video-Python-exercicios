pessoas = []
soma = 0
while True:
    p = {"nome": str(input("Nome: ")).title().strip(), "idade": int(input("idade: ")),
         'sexo': str(input("Sexo[F/M]: ")).strip().upper()[0]}

    while p['sexo'] != 'M' and p['sexo'] != 'F':
        print("ERRO!!!")
        p['sexo'] = str(input("Sexo[F/M]: ")).strip().upper()[0]

    soma += p["idade"]

    pessoas.append(p.copy())
    p = {}

    c = str(input("quer continuar?[S/N]: ")).strip().upper()[0]

    while c != "S" and c != "N":
        c = str(input("quer continuar?[S/N] ")).strip().upper()[0]

    if c == "N":
        break

media = soma / len(pessoas)

print("=" * 40)
print(f"{len(pessoas)} pessoas foram cadastradas")
print(f"a media de idade do grupo e {media:.0f}")

print("as mulheres do grupo são: ", end="")
for c in range(0, len(pessoas)):
    if pessoas[c]["sexo"] == "F":
        print(f"{pessoas[c]['nome']} ", end="")
print("")

print("as pessoas com idade acima da media são: ", end="")
if c in range(0, len(pessoas)):
    if pessoas[c]["idade"] > media:
        print(f"{pessoas[c]['nome'] }", end="")
