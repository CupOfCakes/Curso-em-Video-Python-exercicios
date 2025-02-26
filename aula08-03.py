import math
a = int(input("qual o valor do angulo? "))
ar = math.radians(a)
seno = math.sin(ar)
cosseno = math.cos(ar)
tangente = math.tan(ar)
print("seno = {:.6f}\ncosseno = {:.6f}\ntangente = {:.6f}".format(seno, cosseno, tangente))
