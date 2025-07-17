md = 0
mi = 0
mh = 0
mv = ''
mn = 0
for i in range(1, 5):
    nm = str(input('Nome: ')).strip()
    id = int(input('Idade: '))
    sx = str(input('Sexo [M/F]: ')).strip()
    md += id
    if i == 1 and sx in 'Mn':
        mh = id
        mv = nm
    if sx in 'Mm' and id > mh:
        mh = id
        mv = nm
    if sx in 'Ff' and id < 20:
        mn += 1
mi = md / 4
print('A media de idade desse grupo é de {} Anos.'.format(mi))
print('O homem mais velho tem {} e seu nome é {}.'.format(mh, mv))
print('Tem no total um numero de {} mulheres com menos de 20 Anos de idade'.format(mn))