print("CADASTRE UMA PESSOA")

a = b = c = 0
while True:
    idade = int(input("qual a idade?: "))
    sexo = str(input("qual seu genero?[M/F]: ")).strip().upper()[0]

    while sexo != "F" and sexo != "M":
        sexo = str(input("qual seu genero?[M/F]: ")).strip().upper()[0]

    if idade >= 18:
        a += 1
    if sexo == "M":
        b += 1
    if sexo == "F" and idade <= 20:
        c += 1

    e = str(input("quer continuar?[S/N] ")).strip().upper()[0]
    while e != "S" and e != "N":
        e = str(input("quer continuar?[S/N] ")).strip().upper()[0]
    print("-=" * 25)

    if e == "N":
        break


print(f"{a} tem mais de 18 anos, {b} sao homens, {c} mulheres tem menos de 20 anos")
