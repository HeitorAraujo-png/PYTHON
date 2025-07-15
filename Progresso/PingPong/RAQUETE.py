from turtle import Turtle

class Players(Turtle):
    
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed(0)
        self.shapesize(5, 1)
        self.color("white")
        self.goto(pos)
        
    def Cima(self):
        if round(self.ycor()) + 50 < 250: self.teleport(x=self.xcor(), y=(self.ycor() + 20))

    def Baixo(self):
        if round(self.ycor()) - 50 > -240: self.teleport(x=self.xcor(), y=(self.ycor() - 20))
