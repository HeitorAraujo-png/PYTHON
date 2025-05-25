n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Reprovado')
elif m >= 5 or m <= 6.9:
    print('Recuperacão')
else:
    print('Aprovado')