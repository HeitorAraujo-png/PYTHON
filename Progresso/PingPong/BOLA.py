from turtle import Turtle

class Bola(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(0.75, 0.75)
        self.speed(0)
        self.color("white")
        self.velocidade = 3
        self.xpogo = self.velocidade
        self.ypogo = self.velocidade
        
    def MoveBola(self):
        xbola = self.xcor() + self.xpogo
        ybola = self.ycor() + self.ypogo
        self.goto(xbola, ybola)
        
    def Pong(self):
        if self.ypogo < self.velocidade: self.ypogo = -self.velocidade
        else: self.ypogo = self.velocidade
        if self.ycor() > 240 or self.ycor() < -230:
            if self.ypogo == self.velocidade:
                self.ypogo = -self.velocidade
            elif self.ypogo == -self.velocidade:
                self.ypogo = self.velocidade
        if self.xcor() < -420 or self.xcor() > 420:
            return True
    
    def Again(self):
        self.velocidade == 3
        self.teleport(0,0)