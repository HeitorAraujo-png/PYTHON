from turtle import Turtle
from random import choice
from time import sleep

class Snake:

    def __init__(self):
        linha = self.linha()
        self.Player1()
        self.Player2()
        self.yblock1 = []
        self.yblock2 = []

    def Player1(self):
        self.block1 = []
        listablock= [(390, 40), (390, 20), (390, 0), (390, -20), (390, -40)]
        for i in listablock:   
            plr1 = Turtle("square")
            plr1.penup()
            plr1.speed(0)
            plr1.goto(i)
            plr1.color("white")
            self.block1.append(plr1)

    def Player2(self):
        self.block2 = []
        listablock= [(-390, 40), (-390, 20), (-390, 0), (-390, -20), (-390, -40)]
        for i in listablock:   
            plr2 = Turtle("square")
            plr2.penup()
            plr2.speed(0)
            plr2.goto(i)
            plr2.color("white")
            self.block2.append(plr2)
            

    def linha(self):
        linha = Turtle("square")
        linha.shapesize(2, 2)
        linha.pencolor("white")
        linha.hideturtle()
        linha.speed(0)
        y = -250
        linha.teleport(x=0, y=y)
        while True:
            linha.goto(y=y, x=0)
            y += 15
            if y % 2 == 0:
                linha.penup()
            else:
                linha.pendown()
            if y > 250:
                break

    def Cima1(self):
        if self.block1[0].ycor() < 240:
            for i in range(0 ,len(self.block1)):
                self.block1[i].teleport(x=390, y=((self.block1[i].pos())[1] + 10))
    def Baixo1(self):
        if self.block1[-1].ycor() > -230:
            for i in range(0 ,len(self.block1)):
                self.block1[i].teleport(x=390, y=((self.block1[i].pos())[1] - 10))

    def Cima2(self):
        if self.block2[0].ycor() < 240:
            for i in range(0 ,len(self.block2)):
                self.block2[i].teleport(x=-390, y=((self.block2[i].pos())[1] + 10))

    def Baixo2(self):
        if self.block2[-1].ycor() > -230:
            for i in range(0 ,len(self.block2)):
                self.block2[i].teleport(x=-390, y=((self.block2[i].pos())[1] - 10))
    
    def Listas(self):
        try:
            if self.block1[0].ycor() + 10 != ycblock1[0][0]:
                self.yblock1 = []
                for i in range(0, len(self.block1)):
                    self.yblock1.append((round(self.block1[i].ycor() + 10), round(self.block1[i].ycor() - 10)))
        except UnboundLocalError:
            if self.yblock1 == []:
                for i in range(0, len(self.block1)):
                    self.yblock1.append((round(self.block1[i].ycor() + 10), round(self.block1[i].ycor() - 10)))
        try:
            if self.block2[0].ycor() + 10 != ycblock2[0][0]:
                self.yblock2 = []
                for i in range(0, len(self.block2)):
                    self.yblock2.append((round(self.block2[i].ycor() + 10), round(self.block2[i].ycor() - 10)))
        except UnboundLocalError:
            if self.yblock2 == []:
                for i in range(0, len(self.block2)):
                    self.yblock2.append((round(self.block2[i].ycor() + 10), round(self.block2[i].ycor() - 10)))
        ycblock1 = list(range(self.yblock1[0][0], self.yblock1[-1][-1], -1))
        ycblock2 = list(range(self.yblock2[0][0], self.yblock2[-1][-1], -1))
        return ycblock1, ycblock2
        
    def Bola(self):
        lista = choice((choice(range(0, 46)), choice(range(135, 226)), choice(range(315, 361))))
        self.bola = Turtle("square")
        self.bola.penup()
        self.bola.shapesize(0.75, 0.75)
        self.bola.setheading(lista)
        self.bola.speed(0)
        self.bola.color("white")

    def Ping(self):
        self.Bola()
        while True:
            if self.Pong():
                break
            self.bola.forward(3)
            
            
    def Pong(self):
        if self.bola.ycor() > 240 or self.bola.ycor() < -230:
            if  90 > self.bola.heading() >= 0:
                self.bola.right(90)
            elif 180 > self.bola.heading() >= 90:
                self.bola.left(90)
            elif 270 > self.bola.heading() >= 180:
                self.bola.right(90)
            elif 360 > self.bola.heading() >= 270:
                self.bola.left(90)
        if self.bola.xcor() < -420 or self.bola.xcor() > 420:
            return True
        
        cordblock1, cordblock2 = self.Listas()
        vira = choice(range(160, 201))
        corbola = (round(self.bola.ycor()), round(self.bola.xcor()))
        if corbola[0] in cordblock1 and corbola[1] > 380:
            self.bola.setheading(self.bola.heading() + vira)
        if corbola[0] in cordblock2 and corbola[1] < -380:
            self.bola.setheading(self.bola.heading() - vira)
        