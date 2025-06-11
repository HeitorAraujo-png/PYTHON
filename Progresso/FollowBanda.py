from random import randint
from bd import rock
def rdt(n1=None):
    while True:
        n = randint(1, len(rock) - 1) # we go use the func len for other itens in db
        if n not in n1:
            return n 
def MaiorMenor():
    acertos = 0
    bd1 = rdt()
    bd2 = rdt(n1=bd1)
    while True:
        if acertos == len(rock):
            print('Parabéns, você conseguiu acertar todas as bandas! ')
            return acertos
        print('Qual das bandas abaixo tem mais seguidores?\nFontes: MinhaCabeca.org.br e chatgpt')
        print('Escolha A: ',rock[bd1]['banda'])
        print('Escolha B: ',rock[bd2]['banda'])
        chute = input('Sua escolha sera A ou B? ').upper().strip()
        if chute == 'A':
            if rock[bd1]['follow'] > rock[bd2]['follow']:
                acertos += 1
                bd2 = rdt(n1=bd1)
            elif rock[bd1]['follow'] < rock[bd2]['follow']:
                return acertos
            else:
                acertos += 1
        elif chute == 'B':
            if rock[bd1]['follow'] < rock[bd2]['follow']:
                acertos += 1
                bd1 = rdt(n1=bd2)
            elif rock[bd1]['follow'] > rock[bd2]['follow']:
                return acertos
            else:
                acertos += 1
        else:
            print('Esolha invalida tente novamente! ')
acertou = MaiorMenor()
print(f'Seu numero de acertos foi {acertou}')
