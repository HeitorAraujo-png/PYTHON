from OOP import Snake
from time import sleep
from turtle import Screen
while True:
    resposta = input('Você deseja jogar ou ver o placar de jogadores? [PLACAR/JOGAR/SAIR] ').strip()
    if resposta.lower() == 'placar':
        with open('Pontucao.txt', 'r') as placar:
            print(placar.read())
    elif resposta.lower() == 'jogar':
        sleep(0.5)
        On = True
        print('Vamos definifir as cores e as formas da cobra!')
        while True:
            cor = input('''
    1 - Vermelho
    2 - Preto
    3 - Branco
    4 - Amarelo
    5 - Verde
    6 - Azul
    7 - Laranja
    8 - Roxa
    9 - Rosa
    10 - Ciano
    11 - Magenta
    12 - Cinza
    13 - Marrom
    Digite: ''')
            if cor == '1': cor = 'red'; break; 
            elif cor == '2': cor = 'black'; break
            elif cor == '3': cor = 'white'; break
            elif cor == '4': cor = 'yellow'; break
            elif cor == '5': cor = 'green'; break
            elif cor == '6': cor = 'blue'; break
            elif cor == '7': cor = 'orange'; break
            elif cor == '8': cor = 'purple'; break
            elif cor == '9': cor = 'pink'; break
            elif cor == '10': cor = 'cyan'; break
            elif cor == '11': cor = 'magenta'; break
            elif cor == '12': cor = 'gray'; break
            elif cor == '13': cor = 'brown'; break
            else: print('Tentativa invalida! tente novamente.')
        while True:
            forma = input('''
    1 - Quadrada
    2 - Circulo
    3 - TARTARUGA
    4 - Triagulo
    5 - Flecha
    6 - Classica
    Digite: ''')   
            if forma == '1': forma = 'square'; break
            elif forma == '2': forma = 'circle'; break
            elif forma == '3': forma = 'turtle'; break
            elif forma == '4': forma = 'triangle'; break
            elif forma == '5': forma = 'arrow'; break 
            elif forma == '6': forma = 'classic'; break
            else: print('Tentativa invalida! tente novamente.')
        tela = Screen()
        tela.textinput('COMEÇOU!', 'VOCÊ ESTA PRONTO?')
        while On:
            snake = Snake(cor, forma)
            tela.setup(width=600, height=600)
            if cor != 'black':
                tela.bgcolor('black')
            else:
                tela.bgcolor('white')
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
                        tela.clear()
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