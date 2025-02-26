from modulos import ex115

arq = "cursoemvideo.txt"

if ex115.arquivoexiste(arq):
    print("arquivo encontrado")
else:
    print("arquivo não encontrado")
    ex115.criararquivo(arq)

while True:
    ex115.titulo("menu")
    ex115.menu("Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair")
    ex115.linha()

    while True:
        try:
            resp = int(input("Sua opção: "))
        except ValueError:
            print("Erro! Digite um valor valido")
        else:
            if not 0 < resp < 4:
                print("Erro! Digite um valor valido")
            else:
                break
    if resp == 1:
        ex115.titulo("opção 1")
        ex115.lerarquivo(arq)

    elif resp == 2:
        ex115.titulo("opção 2")
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        ex115.cadastrar(arq, nome, idade)

    elif resp == 3:
        print("programa finalizado")
        break
