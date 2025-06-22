import colorgram
from random import choice
from turtle import *
# Verificar se arquivo não esta corrompido :)
cor = colorgram.extract("maluco.jpg", 100)
# Por algum motivo esse programa so funciona aqui: C:\Users\heiti\DH\damianh.py
# Talvez porque no OneDrive não funcione
ponto_zero = -150.00
end = len(cor)
lista_cores = []
tt = Turtle()
tt.pensize(20)
tt.speed(0)
colormode(255)
for i in range(0, end):
    color = cor[i]
    cores = color.rgb
    rgb = cores.r, cores.g, cores.b
    lista_cores.append(rgb)
def rgb_random():
    x = choice(lista_cores)
    rgb = (x[0],x[1],x[2])
    return tt.pencolor(rgb)
def ponto():
    tt.pendown()
    rgb_random()
    tt.forward(0)
    tt.penup()
def andando():
    ponto()
    for i in range (1, 8):
        tt.forward(25)
        ponto()
def teletransportar():
    global ponto_zero
    tt.teleport(-150.00, ponto_zero)
    andando()
for i in range(1,6):
    teletransportar()
    ponto_zero += 50
tela = Screen()
tela.exitonclick()