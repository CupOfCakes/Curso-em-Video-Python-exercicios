s = 0
m2 = 0
velho = "indefinido"
idadevelho = 0
for c in range(0, 4):
    nome = str(input("qual e o seu nome? "))
    idade = int(input("qual e a sua idade? "))
    sexo = int(input('''[1] Masculino
[2] feminino
qual e o seu sexo? '''))
    print("="*20)

    s += idade
    if sexo == 1 and idade > idadevelho:
        velho = nome
        idadevelho = idade

    if idade < 20 and sexo == 2:
        m2 = m2 + 1

media = s / 4

print("{} e o homem mais velho com {} anos,"
      "{} são mulheres e tem menos de 20 anos,"
      "e a media de idade do gruopo e {:.0f}".format(velho, idadevelho, m2, media))
