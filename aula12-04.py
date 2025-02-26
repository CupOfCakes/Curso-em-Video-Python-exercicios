from datetime import date
ano = int(input("qual o ano em que vc nasceu? "))
genero = str(input("qual o seu genero? ")).lower().strip()

if genero == "feminino" or genero == "mulher" or genero == "menina":
    print("vc não precisa de alistar")

if genero == "masculino" or genero == "homem" or genero == "menino":
    if ano + 18 > date.today().year:
        print("no futuro tera de se apresentar, mais exatamente no ano de {}".format(ano + 18))
    elif ano + 18 == date.today().year:
        print("esta na hora de se apresentar")
    else:
        print("vc ja se apresentou, ou deveria, ja passou {} anos da data prevista".format(abs(ano+18-date.today().year)))
