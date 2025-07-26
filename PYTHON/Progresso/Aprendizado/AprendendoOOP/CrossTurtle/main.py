from turtle import Screen
from random import *
from OOP import *
from time import sleep
nivel = 0
player = Player()
cars = Carros()
score = Level(nivel)
janela = Screen();janela.setup(600, 600);janela.tracer(0)
janela.onkey(player.Cima, 'w')
janela.onkey(player.Cima, 'Up')
lista = []
janela.listen()
while True:
    if nivel > 5:
        janela.clear()
        score.Win()
        janela.exitonclick()
    cars.Cria(nivel)
    cars.Trafico()
    sleep(0.1)
    janela.update()
    for i in cars.Carros:
        if i.distance(player) < 20:
            print(i.xcor(), i.ycor())
            print(player.xcor(), player.ycor())
            janela.exitonclick()
    if player.ycor() > 300:
        nivel += 1
        player.teleport(0, -275)
        score.Passou(nivel)
        cars.Reset()