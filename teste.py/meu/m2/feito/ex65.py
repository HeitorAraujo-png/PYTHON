maior = menor = x = c = m = s = 0
z = ''
while z != 'n':
    c += 1
    x = int(input('Digite um numero: '))
    z = str(input('Deseja continuar [S/N]? ')).strip().lower()
    s += x    
    m = s / c
    if c == 1:
        menor = x
    if x > maior:
        maior = x
    elif x < menor:
        menor = x
print('O maior numero foi de {}'.format(maior))
print('o menor numero foi de {}'.format(menor))
print('E a media de todos os numero ({}) foi de: {}'.format(c, m))