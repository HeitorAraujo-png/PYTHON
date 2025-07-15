from turtle import Turtle
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