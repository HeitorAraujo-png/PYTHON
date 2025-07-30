ma = 0
me = 0
for i in range (1, 6):
    peso = float(input('peso da {} ª pessoa: '.format(i)))
    if i == 1:
            ma = peso
            me = peso
    else:
        if peso > ma:
            ma = peso
        if peso < me:
            me = peso
print('O maior peso lido foi de {}KG'.format(ma))
print('O menor peso lido foi de {}KG'.format(me))