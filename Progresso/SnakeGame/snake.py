from turtle import Turtle, Screen, onkey
from time import sleep
tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor("black")
tela.title('Snake Game')
tela.tracer(0)
comeca = [(0,0), (-20, 0), (-40, 0)]

segm = []

for i in comeca:
    nvlinha = Turtle('square')
    nvlinha.color('white')
    nvlinha.penup()
    nvlinha.goto(i)
    segm.append(nvlinha)
on = True
def direita():
    if segm[0].heading() != 180:
        segm[0].setheading(0)
def cima():
    if segm[0].heading() != 270:
        segm[0].setheading(90)
def esquerda():
    if segm[0].heading() != 0:
        segm[0].setheading(180)
def baixo():
    if segm[0].heading() != 90:
        segm[0].setheading(270)


while on:
    tela.update()
    sleep(0.1)
    for segnum in range(len(segm)- 1, 0, -1 ):
        nx = segm[segnum -1].xcor()
        ny = segm[segnum -1].ycor()
        segm[segnum].goto(nx, ny)
    segm[0].forward(20)
    tela.onkey(direita, 'd')
    tela.onkey(cima, 'w')
    tela.onkey(esquerda, 'a')
    tela.onkey(baixo, 's')
    tela.listen()

linha1 = Turtle('square')
linha1.color('white')


linha2 = Turtle('square')
linha2.color('white')
linha2.goto(-20, 0)

linha3 = Turtle('square')
linha3.color('white')
linha3.goto(-40, 0)

tela.exitonclick()