from datetime import date
m = 0
n = 0
for c in range(0, 7):
    ano = int(input("em que ano vc nasceu? "))

    if ano + 18 > date.today().year:
        m = m + 1
    elif ano + 18 < date.today().year:
        n = n + 1

print("{} de vc sao maiores de idade, e {} são menores".format(m, n))
