from datetime import date
print("======ANO BISSEXTO======")
n = int(input("qual o ano: "))

if n == 0:
    n = date.today().year

if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print("e um ano bissexto :)")
else:
    print("não e bissexto :(")

print(n)
