from OOP import *
from time import sleep
from turtle import Screen

while True:
    sleep(0.5)
    On = True
    opa = False
    print("Vamos definifir as cores e as formas da cobra!")
    while True:
        cor = input(
            """
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
    Digite: """
        )
        if cor == "1":
            cor = "red"
        elif cor == "2":
            cor = "black"
        elif cor == "3":
            cor = "white"
        elif cor == "4":
            cor = "yellow"
        elif cor == "5":
            cor = "green"
        elif cor == "6":
            cor = "blue"
        elif cor == "7":
            cor = "orange"
        elif cor == "8":
            cor = "purple"
        elif cor == "9":
            cor = "pink"
        elif cor == "10":
            cor = "cyan"
        elif cor == "11":
            cor = "magenta"
        elif cor == "12":
            cor = "gray"
        elif cor == "13":
            cor = "brown"
        else:
            print("Tentativa invalida! tente novamente.")
        break
    while True:
        forma = input(
            """
    1 - Quadrada
    2 - Circulo
    3 - TARTARUGA
    4 - Triagulo
    5 - Flecha
    6 - Classica
    Digite: """
        )
        if forma == "1":
            forma = "square"
        elif forma == "2":
            forma = "circle"
        elif forma == "3":
            forma = "turtle"
        elif forma == "4":
            forma = "triangle"
        elif forma == "5":
            forma = "arrow"
        elif forma == "6":
            forma = "classic"
        else:
            print("Tentativa invalida! tente novamente.")
        break
    tela = Screen()
    tela.textinput("COMEÇOU!", "VOCÊ ESTA PRONTO?")
    while On:
        snake = Snake(cor, forma)
        Hs = Pontos(cor, 0)
        Hs.More(0, opa)
        tela.setup(width=600, height=600)
        if cor != "black":
            tela.bgcolor("black")
        else:
            tela.bgcolor("white")
        tela.title("Snake Game")
        tela.tracer(0)
        tela.onkey(snake.Direita, "Right") or tela.onkey(snake.Direita, "d")
        tela.onkey(snake.Cima, "Up") or tela.onkey(snake.Cima, "w")
        tela.onkey(snake.Esquerda, "Left") or tela.onkey(snake.Esquerda, "a")
        tela.onkey(snake.Baixo, "Down") or tela.onkey(snake.Baixo, "s")
        tela.listen()
        while On:
            Hs.More(opa, snake.pontos)
            tela.update()
            sleep(0.1)
            snake.Move()
            if snake.Bateu():
                resposta = tela.textinput(
                    "DERROTA", "Você perdeu! Deseja continuar? [SIM/NÃO]"
                ).strip()
                if resposta.lower() == "sim":
                    snake.Pontuacao()
                    tela.resetscreen()
                    tela.clear()
                    snake.LocalFruta()
                    opa = Hs.HighScore(cor)
                    Hs.More(cor, snake.pontos)
                else:
                    snake.Pontuacao()
                    Hs.GameOver()
                    On = False
                break
    tela.exitonclick()
    break
