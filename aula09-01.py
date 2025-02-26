nome = str(input("digite seu nome "))
print(nome.upper())
print(nome.lower())

#quantida de letras sem espaço
s = nome.split()
j = "".join(s)

print('o nome tem {} letras'.format(len(j)))
print('o 1 nome tem {} letras '.format(len(s[0])))
