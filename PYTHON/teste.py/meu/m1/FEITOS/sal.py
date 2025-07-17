s = float(input('Digite seu salario: '))
if s <= 1250:
    print('Seu salario subiu para: {}'.format(s + (s * 0.15)))
else:
    print('Seu salario subiu para: {}'.format(s + (s * 0.10)))