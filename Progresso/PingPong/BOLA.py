from turtle import Turtle
# from RAQUETE import Players

class Bola(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(0.75, 0.75)
        self.speed(0)
        self.color("white")
        self.xpogo = 5
        self.ypogo = 5
        
    def MoveBola(self):
        xbola = self.xcor() + self.xpogo
        ybola = self.ycor() + self.ypogo
        self.goto(xbola, ybola)
    
    def Pong(self):
        if self.ycor() > 240 or self.ycor() < -230:
            if self.ypogo == 5:
                self.ypogo = -5
            elif self.ypogo == -5:
                self.ypogo = 5
    
    def Ping(self):
        while True:
            self.MoveBola()
            self.Pong()