from datetime import date
hj = date.today().year
m = 0
n = 0
for i in range(7):
    nas = int(input('Em qual ano você nasceu? '))
    if 21 <= hj - nas:
        m += 1
    else:
        n += 1
print('Numeros de pessoas maiores de idade: {}\nNumero de pessoas menores de idade: {}'.format(m, n))
    