from back import Contatos, Menu
from time import sleep
print('Primeiramente vamos adicionar um numero.')
fone = Contatos()
while True:
    Menu()
    x = int(input('Digite um numero: '))
    if x == 1:
        fone = Contatos()
    elif x == 2:
        print('\n' * 10)
        fone.ler()
        sleep(5)
    elif x == 3:
        print('\n' * 10)
        fone.pesquisa()
        sleep(5)
    elif x == 4:
        print('\n' * 10)
        fone.kamikaze()
        sleep(5)
    elif x == 5:
        print('\n' * 10)
        fone.deletar()
        sleep(5)
    elif x == 6:
        print('\n' * 10)
        fone.backup()
        sleep(5)
    elif x == 7:
        print('\n' * 10)
        fone.SeeBackup()
        sleep(5)
    elif x == 8:
        print('\n' * 10)
        sleep(5)
        print('Finalizando o programa...')
        sleep
        break
    else:
        print('\n' * 10)
        print('Seleção invalida! Tente novamente.')
