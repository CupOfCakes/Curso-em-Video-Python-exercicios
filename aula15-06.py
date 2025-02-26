print("======BANCO CEV======")

valor = int(input("quanto quer sacar?: "))
rest = 0
valor50 = 0
valor20 = 0
valor10 = 0
valor1 = 0

while True:
    if valor >= 50:
        valor50 = valor // 50
        rest = valor % 50

        print(f'''total de {valor50} cedulas de 50''')

        if rest == 0:
            break
    else:
        rest = valor

    if rest >= 20:
        valor20 = rest // 20
        rest = rest % 20

        print(f'''total de {valor20} de 20''')

        if rest == 0:
            break
    else:
        rest = rest

    if rest >= 10:
        valor10 = rest // 10
        rest = rest % 10
        print(f'''total de {valor10} cedulas de 10''')

        if rest == 0:
            break
    else:
        rest = rest

    if rest >= 1:
        valor1 = rest // 1
        rest = rest % 1
        print(f'''total de {valor1} cedulas de 1''')

        if rest == 0:
            break
