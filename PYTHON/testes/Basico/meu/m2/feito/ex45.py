# jOKEMPO 
from random import randint
jokempo = randint(0,2)
print('\033[41mVAMOS JOGAR PEDRA, PAPEL OU TESOURA!!!\033[m')
jogo = ['pedra', 'papel', 'tesoura']
maquina = jogo[jokempo]
eu = str(input('Escolha entre pedra, papel ou tesoura: ')).strip().lower()
if 'papel' in eu:
    if 'tesoura' in maquina:
        print('O jogador escolheu {} e a maquina... {} \nA maquina ganhou'.format(eu, maquina))
    elif 'pedra' in maquina:
        print('O jogador escolheu {} e a maquina... {} \nO jogador ganhou'.format(eu, maquina))
    else:
        print('O jogador escolheu {} e a maquina... {} \nO jogo empatou'.format(eu, maquina))
elif 'pedra' in eu:
    if 'papel' in maquina:
        print('O jogador escolheu {} e a maquina... {} \nA maquina ganhou'.format(eu, maquina))
    elif 'tesoura' in maquina:
        print('O jogador escolheu {} e a maquina... {} \nO jogador ganhou'.format(eu, maquina))
    else:
        print('O jogador escolheu {} e a maquina... {} \nO jogo empatou'.format(eu, maquina))
elif 'tesoura' in eu:
    if 'pedra' in maquina:
        print('O jogador escolheu {} e a maquina... {} \nA maquina ganhou'.format(eu, maquina))
    elif 'papel' in maquina:
        print('O jogador escolheu {} e a maquina... {} \nO jogador ganhou'.format(eu, maquina))
    else:
        print('O jogador escolheu {} e a maquina... {} \nO jogo empatou'.format(eu, maquina))