from datetime import datetime
import pygame
dia = input('Que dia você nasceu? ')
mes = int(input('Que mês você nasceu? '))
if mes < 10:
    mes = f'0{mes}'
if len(dia) < 2:
    dia = f'0{dia}'
if dia == (datetime.today()).strftime(format="%d") and mes == (datetime.today()).strftime(format="%m"):
    pygame.mixer.init()
    pygame.mixer.music.load(r'manoel-gomes-parabens.mp3')
    pygame.mixer.music.play()
    print('PARABENS!!!')
    while pygame.mixer.music.get_busy():
        continue
else:
    print('Legal...')