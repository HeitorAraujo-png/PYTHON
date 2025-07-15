from turtle import Screen
from RAQUETE import Players
from BOLA import Bola
# from import
janela = Screen(); janela.setup(820, 500);janela.bgcolor('black');janela.title('SNAKE GAME');janela.tracer(0)
player1 = Players((390, 0))
player2 = Players((-390, 0))
bola = Bola()
bola.Ping()
janela.onkey(player1.Cima, 'Up');janela.listen()
janela.onkey(player2.Cima, 'w');janela.listen()
janela.onkey(player1.Baixo, 'Down');janela.listen()
janela.onkey(player2.Baixo, 's');janela.listen()
while True:
    janela.update()
    
janela.exitonclick()