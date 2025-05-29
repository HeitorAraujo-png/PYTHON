import datetime
x = int(input('Que ano você nasceu? '))
dt = datetime.date.today()
y =  (dt.year) - x
if y <= 9:
    print('Classe: Mirim')
elif y <= 14:
    print('Classe: Infantil')
elif y <= 19:
    print('Classe: Junior')
elif y <= 20:
    print('Classe: Sênior')
else:
    print('Master')