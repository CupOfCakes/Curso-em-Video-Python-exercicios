n = int(input("escreva um numero de 0 a 9999: "))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('milhar:',m)
print('centena:',c)
print('dezena:',d)
print('unidade:',u)
