r = s = ''
i = h = m = c = 0
while True:
    i = int(input('Digite sua idade: '))
    while True:
        s = str(input('Qual é o seu sexo [M/F]? '))
        if s in 'Mm':
            break
        if s in 'Ff':
            break
        else:
            print('Tente novamente!')
    if i >= 18:
        c += 1
    elif r in 'Mm':
        h += 1
    elif r in 'Ff':
        if i < 20:
            m += 1
    while True:
        r = str(input('Quer continuar [S/N]?'))
        if r in 'Ss':
            break
        if r in 'Nn':
            break
        else:
            print('Digite novamente')
    if r in 'Nn':
        break
print(f'''
{c} Pessoas com mais de 18 anos
{h} Homens cadastrados
{m} Mulheres com menos de 20 anos
''')