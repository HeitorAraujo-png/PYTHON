from turtle import Turtle

class Snake:
    
    def __init__(self):
        traco = self.Linha()
        self.ponto1 = 0
        self.ponto2 = 0
        self.xpogo = 5
        self.ypogo = 5
        
    def Linha(self):
        linha = Turtle("square")
        linha.pensize(3)
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
            
    def Ping(self):
        self.Bola()
        while True:
            if self.Pong():
                self.Pontos()
                break
            self.MoveBola()
            

    
