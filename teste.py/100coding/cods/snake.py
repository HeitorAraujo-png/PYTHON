from turtle import Turtle, Screen

tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor("black")
tela.title('Snake Game')

comeca = [(0,0), (-20, 0), (-40, 0)]

segm = []

for i in comeca:
    nvlinha = Turtle('square')
    nvlinha.color('white')
    nvlinha.penup()
    nvlinha.goto(i)
    segm.append(nvlinha)
on = True
while on:
    for j in segm:
        j.forward(20)

linha1 = Turtle('square')
linha1.color('white')

linha2 = Turtle('square')
linha2.color('white')
linha2.goto(-20, 0)

linha3 = Turtle('square')
linha3.color('white')
linha3.goto(-40, 0)



tela.exitonclick()