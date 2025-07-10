from OOP import Snake
from time import sleep
from turtle import Screen
while True:
    resposta = input('Você deseja jogar ou ver o placar de jogadores? [PLACAR/JOGAR/SAIR] ').strip()
    if resposta.lower() == 'placar':
        with open('Pontucao.txt', 'r') as placar:
            print(placar.read())
    elif resposta.lower() == 'jogar':
        sleep(5)
        On = True
        tela = Screen()
        tela.textinput('COMEÇOU!', 'VOCÊ ESTA PRONTO?')
        while On:
            snake = Snake()
            tela.setup(width=600, height=600)
            tela.bgcolor('black')
            tela.title('Snake Game')
            tela.tracer(0)
            tela.onkey(snake.Direita, 'Right') or tela.onkey(snake.Direita, 'd')
            tela.onkey(snake.Cima, 'Up') or tela.onkey(snake.Cima, 'w')
            tela.onkey(snake.Esquerda, 'Left') or tela.onkey(snake.Esquerda, 'a')
            tela.onkey(snake.Baixo, 'Down') or tela.onkey(snake.Baixo, 's')
            tela.listen()
            while On:
                tela.update()
                sleep(0.1)
                snake.Move()
                if snake.Bateu():
                    resposta = tela.textinput('DERROTA', 'Você perdeu! Deseja continuar? [SIM/NÃO]').strip()
                    if resposta.lower() == 'sim':
                        tela.resetscreen()
                        snake.LocalFruta()
                        break
                    else:
                        On = False
        tela.exitonclick()
        snake.Pontuacao()
        break
    elif resposta.lower() == 'sair':
        break
    else:
        print('Erro! Tente novamente.')