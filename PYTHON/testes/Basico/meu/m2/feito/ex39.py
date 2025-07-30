from datetime import date
x = int(input('Em que ano você nasceu? '))
data = date.today().year
y = (data) - x

if y == 18:
    print('Esta na hora de se alistar ao serviço militar')
elif y > 18:    
    print('Ja passou da hora de se alistar')
    saldo = y - 18
    print('Já se passaram {} anos do tempo certo'.format(saldo))
else:
    print('Você ainda vai se alistar no serviço militar')
    saldo = 18 - y
    print('Falta {} anos para se alistar'.format(saldo))