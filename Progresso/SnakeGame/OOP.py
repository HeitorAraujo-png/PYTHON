from turtle import Turtle
from random import choice

class Snake:
    
    def __init__(self):
        self.segm = []
        self.Cobra()
        self.Maca()

    def Cobra(self):
        self.comeca = [(0,0), (-20, 0), (-40, 0),]
        for i in self.comeca:
            nvlinha = Turtle('square')
            nvlinha.color('white')
            nvlinha.penup()
            nvlinha.goto(i)
            self.segm.append(nvlinha)
    
    def Move(self):
        self.Comer()
        for segnum in range(len(self.segm) - 1, 0, -1):
            nx = self.segm[segnum -1].xcor()
            ny = self.segm[segnum -1].ycor()
            self.segm[segnum].goto(nx, ny)
        self.segm[0].forward(20)

    def Direita(self):
        if self.segm[0].heading() != 180:
            self.segm[0].setheading(0)

    def Cima(self):
        if self.segm[0].heading() != 270:
            self.segm[0].setheading(90)

    def Esquerda(self):
        if self.segm[0].heading() != 0:
            self.segm[0].setheading(180)

    def Baixo(self):
        if self.segm[0].heading() != 90:
            self.segm[0].setheading(270)
    
    def Bateu(self):
        cord = []
        if self.segm[0].xcor() < -290 or self.segm[0].xcor() > 290 or self.segm[0].ycor() < -290 or self.segm[0].ycor() > 290:
            return True
        for i in range((len(self.segm) -1), 1, -1):
            cord.append(f'{round(self.segm[i].xcor())}, {round(self.segm[i].ycor())}')
        xycord = f'{round(self.segm[0].xcor())}, {round(self.segm[0].ycor())}'
        print(xycord)
        print(cord)
        if xycord in cord:
            return True
        return False
        
    def Maca(self):
        self.fruta = Turtle()
        self.fruta.penup()
        self.fruta.shapesize(0.5, 0.5)
        self.fruta.shape('circle')
        self.fruta.color('red')
        
    def LocalFruta(self):
        xFruta = choice(range(-280, 281, 20))
        yFruta = choice(range(-280, 281, 20))
        print(xFruta, yFruta)
        self.fruta.teleport(xFruta, yFruta)
            
    def Comeu(self):
        self.xcord = ((self.segm[-1].xcor()) - 20)
        self.ycord = (self.segm[-1].ycor())
        linha = Turtle('square')
        linha.color('white')
        linha.penup()
        linha.goto(self.xcord, self.ycord)
        self.segm.append(linha)
        
    def Comer(self):
        if (self.fruta.xcor()) == round(self.segm[0].xcor()) and (self.fruta.ycor()) == round(self.segm[0].ycor()) :
            self.LocalFruta()
            self.Comeu()