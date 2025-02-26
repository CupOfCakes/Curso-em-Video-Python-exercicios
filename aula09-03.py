nome = str(input('escreva o nome da cidade: '))
nome = nome.split()

if 'santo' in nome[0].lower():
    print('começa com santo :)')
else: print('não começa com santo :(')
