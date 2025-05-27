from random import randint
from time import sleep
m = randint(1, 10)
c = 0
t = 0
print('Adivinhe o numero em que estou pensando!(De 1 a 10)')
while c != m:
    c = int(input('Eu acho que é: '))
    t += 1
    if c == m:
        print('Você acertou! O numero secreto era: {}\nTotal de tentativas {}!'.format(m, t))
        sleep(1.5)
    else:
        sleep(1.5)
print('Fim')
    