tr = float(input('Qual foi a distancia em KM da sua viagem? '))
if tr <= 200:
    print('Sua viagem custou {}'.format(tr * 0.50))
else:
    print('Sua viagem custou {}'.format(tr * 0.45))