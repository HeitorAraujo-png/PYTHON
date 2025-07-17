from turtle import Screen
from OOP import *
linha = Fundo()
placar = Tabela()
janela = Screen(); janela.setup(820, 500);janela.bgcolor('black');janela.title('SNAKE GAME')
player1 = Players((390, 0))
player2 = Players((-390, 0))
bola = Bola()
janela.onkey(player1.Cima, 'Up');janela.listen()
janela.onkey(player2.Cima, 'w');janela.listen()
janela.onkey(player1.Baixo, 'Down');janela.listen()
janela.onkey(player2.Baixo, 's');janela.listen()
while True:
    bola.MoveBola()
    if bola.xcor() < -420:placar.P2(); bola.Again()
    if bola.xcor() > 420:placar.P1(); bola.Again()
    if bola.distance(player1) < 50 and bola.xcor() > 370: bola.xpogo = -bola.velocidade
    if  bola.distance(player2) < 50 and bola.xcor() < -370: bola.xpogo = bola.velocidade
    bola.Pong()
    if placar.p1 >= 10 or 10 <= placar.p2: break
    
janela.exitonclick()