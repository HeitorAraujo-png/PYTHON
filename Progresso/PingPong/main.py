from turtle import Screen
from time import sleep
from OOP import Snake
janela = Screen(); janela.setup(820, 500);janela.bgcolor('black');janela.title('SNAKE GAME')
snk = Snake()
janela.onkeypress(snk.Cima1, 'Up');janela.listen()
janela.onkeypress(snk.Cima2, 'w');janela.listen()
janela.onkeypress(snk.Baixo1, 'Down');janela.listen()
janela.onkeypress(snk.Baixo2, 's');janela.listen()
while True:
    janela.update()
    snk.Ping()