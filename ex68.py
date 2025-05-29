from random import randint
j = m = s = c = 0
print('Vamos jogar par e impar!')
while True:
    m = randint(0, 10)
    j = int(input('Digite um valor: '))
    pi = str(input('Par ou impar [P/I]? '))
    s = j + m
    if pi in 'Pp':
        if s % 2 == 0:
            print('O jogador ganhou! ')
            c += 1
        elif s % 2 == 1:
            print('O jogador perdeu!')
            break
    elif pi in 'Ii':
        if s % 2 == 0:
            print('O jogador perdeu!')
            break
        elif s % 2 == 1:
            print('O jogador Ganhou!')
            c += 1
    print('Jogue novamente!')
if c > 0:
    print(f'O jogador ganhou {c} vezes consecutivas!')
            
            
    
    