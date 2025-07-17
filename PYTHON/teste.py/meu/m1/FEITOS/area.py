altura = float(input('Quantos metros de altura tem parede? '))
largura = float(input('Qual a largura da parede? '))
area = largura * altura
tinta = area / 2

print('A area total tem {0} metros e sera usado {1} Litros de tinta para pintar a parede!'.format(area, tinta))