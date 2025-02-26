def notas(*num, bool=False):
    """
    -> cria um dicionario dos valores dados
    :param num: pega varios numeros
    :param bool: se for True mostra a situação da sala
    :return: retorna um dicionario com o maior, menor e a media dos valores
    """
    fakelist = []
    tot = 0

    for c in range(0, len(num)):
        fakelist.append(num[c])
    for c in range(0, len(fakelist)):
        tot += fakelist[c]
        c += 1

    dic = {"quantidade": len(fakelist), "maior": max(fakelist), "menor": min(fakelist), "media": tot / len(fakelist)}

    if bool:
        if dic["media"] < 5:
            print("situação pessima")
        elif 5 <= dic["media"] < 7:
            print("situação mediocre")
        elif dic["media"] >=7:
            print("situação boa")

    return dic


r = notas(2, 3, 1, 7, 12, bool=True)
print(r)
