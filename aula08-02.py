import math
print("======teorema de pitagoras======")
ca = float(input("indique o cateto adjacente: "))
co = float(input("indique o cateto oposto: "))
h = math.sqrt(ca**2 + co**2)
print("a hipotenusa e {:.2f}".format(h))
