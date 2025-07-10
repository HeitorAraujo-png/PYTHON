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
    pygame.mixer.music.load()
    print('PARABENS!!!')
else:
    print('Legal...')