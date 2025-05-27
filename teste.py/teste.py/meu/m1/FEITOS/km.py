usei = int(input('Por quantos dias o carro foi usado? '))
percorri = float(input('Quantos KM você percorreu? '))
dias = usei * 60
km = percorri * 0.15
total = dias + km
print('Você deve um total de R${} !'.format(total))