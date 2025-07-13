import colorgram
from random import choice
from turtle import *
# Verificar se arquivo não esta corrompido :)
cor = colorgram.extract("maluco.jpg", 100)
# Não funciona no OneDrive/Nuvem
ponto_zero = -150.00
end = len(cor)
lista_cores = []
frank = Turtle()
frank.pensize(20)
frank.speed(0)
colormode(255)
for i in range(0, end):
    color = cor[i]
    cores = color.rgb
    rgb = cores.r, cores.g, cores.b
    lista_cores.append(rgb)
def rgb_random():
    x = choice(lista_cores)
    rgb = (x[0],x[1],x[2])
    return frank.pencolor(rgb)
def pintar():
    frank.pendown()
    rgb_random()
    frank.forward(0)
    frank.penup()
def andando():
    pintar()
    for i in range (1, 8):
        frank.forward(25)
        pintar()
def teletransportar():
    global ponto_zero
    frank.teleport(-150.00, ponto_zero)
    andando()
for i in range(1,6):
    teletransportar()
    ponto_zero += 50
tela = Screen()
tela.exitonclick()
