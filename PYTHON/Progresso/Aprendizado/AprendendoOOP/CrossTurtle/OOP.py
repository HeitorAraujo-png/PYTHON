from turtle import *
from random import *

class Carros():
    
    def __init__(self):
        self.Carros = []

    def Cria(self, lvl):
        if randint(lvl, 5) == 5:
            self.localy = randint(-250, 250)
            tartu = Turtle(shape='square')
            tartu.teleport(315, self.localy)
            tartu.penup()
            tartu.speed(1)
            tartu.shapesize(1, 2)
            tartu.color(choice(['red', 'green', 'blue', 'black', 'pink', 'yellow']))
            self.Carros.append(tartu)

    def Trafico(self):
        for i in self.Carros:
            i.backward(5)
            
    def Reset(self):
        for i in self.Carros:
            i.hideturtle()
        self.Carros = []

class Player(Turtle):
    
    def __init__(self):
        super().__init__('turtle')
        self.penup()
        self.setheading(90)
        self.teleport(0, -275)
        
    def Cima(self):
        self.forward(10)
        
class Level(Turtle):
    
    def __init__(self, lvl):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.teleport(-250, 260)
        self.write(align='center', arg=f'Level {lvl}', font=('Arial', 20, 'bold'))
        
    def Passou(self, lvl):
        self.clear()
        self.write(align='center', arg=f'Level {lvl}', font=('Arial', 20, 'bold'))
        
    def Win(self):
        self.clear()
        self.teleport(0,0)
        self.write(align='center', arg='VOCÊ GANHOU!!!', font=('Arial', 50, 'bold'))