import math
ang = float(input('Digite o angulo desejado '))
seno = math.sin(math.radians(ang))
print('O angulo {} tem o seno de {:.2}'.format(ang, seno))
cos = math.cos(math.radians(ang))
print('O angulo {} tem o coseno de {:.2}'.format(ang, cos))
tg = math.tan(math.radians(ang))
print('O angulo {} tem a tangente de {:.2}'.format(ang, tg))