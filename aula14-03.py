escolha = 0

while escolha != 5:
    n1 = float(input("qual o primeiro digito: "))
    n2 = float(input("qual o segundo digito: "))
    lista = [n1, n2]

    escolha = int(input('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Numeros
[5] Sair do Programa
o que deseja fazer: '''))

    if escolha == 1:
        print("\na soma entre {} e {} igual a {}".format(n1, n2, n1+n2))
        escolha = int(input("se quiser terminar o programa digite 5, se  não clicke qualquer teclada: "))
    elif escolha == 2:
        print("\na multiplicação entre {} e {} igual a {}".format(n1, n2, n1 * n2))
        escolha = int(input("se quiser terminar o programa digite 5, se  não clicke qualquer teclada: "))
    elif escolha == 3:
        print("\no maior numero entre {} e {} e {}".format(n1, n2, max(lista)))
        escolha = int(input("se quiser terminar o programa digite 5, se  não clicke qualquer teclada: "))
    elif escolha == 4:
        print("\n")
    else:
        print("opção invalida")
