from datetime import datetime
dia = input('Que dia você nasceu? ')
mes = int(input('Que mês você nasceu? '))
if mes < 10:
    mes = f'0{mes}'
if len(dia) < 2:
    dia = f'0{dia}'
if dia == (datetime.today()).strftime(format="%d") and mes == (datetime.today()).strftime(format="%m"):
    print('PARABENS!!!')
else:
    print('Legal...')