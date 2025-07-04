from turtle import Turtle
class Snake:
    
    def __init__(self):
        self.segm = []
        self.Cobra()
    def Cobra(self):
        comeca = [(0,0), (-20, 0), (-40, 0)]
        for i in comeca:
            nvlinha = Turtle('square')
            nvlinha.color('white')
            nvlinha.penup()
            nvlinha.goto(i)
            self.segm.append(nvlinha)
    
    def Move(self):
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