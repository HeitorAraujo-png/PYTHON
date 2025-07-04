from OOP import Snake
from time import sleep
from turtle import Screen
snake = Snake()

tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor("black")
tela.title('Snake Game')
tela.tracer(0)
        
tela.onkey(snake.Direita, 'Right')
tela.onkey(snake.Cima, 'Up')
tela.onkey(snake.Esquerda, 'Left')
tela.onkey(snake.Baixo, 'Down')
tela.listen()
On = True
while On:
    tela.update()
    sleep(0.1)
    snake.Move()

tela.exitonclick()