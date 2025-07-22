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
            if self.ypogo == self.velocidade: self.ypogo = -self.velocidade
            elif self.ypogo == -self.velocidade: self.ypogo = self.velocidade
        if self.xcor() < -420 or self.xcor() > 420: return True
    
    def Again(self):
        self.velocidade == 3
        self.teleport(0,0)

class Fundo(Turtle):

    def __init__(self):
        super().__init__()
        self.pensize(3)
        self.pencolor("white")
        self.hideturtle()
        self.speed(0)
        y = -250
        self.teleport(x=0, y=y)
        while True:
            self.goto(y=y, x=0)
            y += 15
            if y % 2 == 0: self.penup()
            else: self.pendown()
            if y > 250: break

class Tabela(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.teleport(-100, 150)
        self.p1 = self.p2 = 0
        self.write(self.p1, align='center', font=('Courier', 80, 'normal'))
        self.teleport(100, 150)
        self.write(self.p2, align='center', font=('Courier', 80, 'normal'))
        
    def upd(self):
        self.clear()
        self.teleport(-100, 150)
        self.write(self.p1, align='center', font=('Courier', 80, 'normal'))
        self.teleport(100, 150)
        self.write(self.p2, align='center', font=('Courier', 80, 'normal'))
    
    def P1(self):
        self.p1 += 1
        self.upd()
        
    def P2(self):
        self.p2 += 1
        self.upd()