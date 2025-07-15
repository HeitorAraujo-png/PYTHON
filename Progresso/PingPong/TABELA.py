from turtle import Turtle
class Tabela(Turtle):
    
    def __init__(self):
        super().__init__()
        self.clear()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-100, 150)
        self.write(self.ponto1, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 150)
        self.write(self.ponto2, align='center', font=('Courier', 80, 'normal'))
        self.upd()
        
    def upd(self):
        self.clear()
        self.goto(-100, 150)
        self.write(self.p1, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 150)
        self.write(self.p2, align='center', font=('Courier', 80, 'normal'))
    
    def P1(self):
        self.p1 += 1
        self.upd()
        
    def P2(self):
        self.p2 += 1
        self.upd