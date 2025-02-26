print("======VIAGEM======")
print("R$0.50 ate 200 KM;\nR$0.45 para uma maior distancia")

d = float(input("quantos quilimetros ira viajar: "))
if d <= 200:
    print("a viagem custara {}".format(d*0.50))
else:
    print("a viagem custara {}".format(d*0.45))
