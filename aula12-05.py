n1 = float(input("qual foi a 1 nota? "))
n2 = float(input("qual foi a 2 nota? "))

media = (n1 + n2) / 2

if media < 5.0:
    print("\33[31mR E P R O V A D O\33[m")
elif 5.0 <= media <= 6.9:
    print("de recuperação >:(")
else:
    print("\33[34mA P R O V A D O *0*\33[m")
