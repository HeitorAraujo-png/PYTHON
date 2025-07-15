from turtle import Turtle

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
            if y % 2 == 0:
                self.penup()
            else:
                self.pendown()
            if y > 250:
                break

    
