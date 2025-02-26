def titulo(msg, t=30):
    print("=" * t)
    print(f"{msg:^{t}}")
    print("=" * t)


def linha(t=30):
    print("=" * t)


def menu(*msg):
    for c in range(0, len(msg)):
        print(f"{c + 1} - {msg[c]}")


def arquivoexiste(msg):
    try:
        a = open(msg, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(msg):
    try:
        a = open(msg, "wt+")
        a.close()
    except:
        print("problema na criação do arquivo")
    else:
        print(f" arquivo {msg} criado com sucesso")


def lerarquivo(msg):
    try:
        a = open(msg, "rt")
    except:
        print("erro ao ler o arquivo")
    else:
        titulo("pessoas cadastradas")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<20}{dado[1]:>5} anos")
    finally:
        a.close()


def cadastrar(arq, nome, idade):
    try:
        a = open(arq, "at")
    except:
        print("houve um erro na abertura do arquivo")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Erro ao cadastrar")
        else:
            print(f"{nome} cadastrado com sucesso")
            a.close()
