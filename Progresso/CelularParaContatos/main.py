from back import Contatos, Menu, Segurança
from time import sleep
login = Segurança()
adm = login.adm()
Verdade = True
acesso, senha, user = login.verifica()
if acesso == False:
    Verdade = False
if Verdade:
    print('Primeiramente vamos adicionar um numero.')
    fone = Contatos(acesso=acesso, senha=senha, user=user)
    while Verdade:
        Menu(adm=adm)
        x = int(input('Digite um numero: '))
        if x == 1:
            fone = Contatos()
        elif x == 2:
            print('\n' * 10)
            fone.ler()
            sleep(2)
        elif x == 3:
            print('\n' * 10)
            fone.pesquisa()
            sleep(2)
        elif x == 4:
            print('\n' * 10)
            fone.kamikaze(adm=adm)
            sleep(2)
        elif x == 5:
            print('\n' * 10)
            fone.deletar()
            sleep(2)
        elif x == 6:
            print('\n' * 10)
            fone.backup()
            sleep(2)
        elif x == 7:
            print('\n' * 10)
            fone.SeeBackup()
            sleep(2)
        elif x == 8:
            print('\n' * 10)
            print('Finalizando o programa...')
            sleep(2)
            break
        if login.adm():
            if x == 123321:
                login.AcessoAdm()
                sleep(1)
            elif x == 11:
                login.TrocaSenha()
                sleep(1) 
            elif x == 22:
                login.TrocaNome()
                sleep(1)
            elif x == 33:
                login.DeletaUser()
                sleep(1)
            elif x == 44:
                login.DeletaAdm()
                sleep(1)                
            elif x == 55:
                login.CriaVariosUser()
                sleep(1)   
            elif x == 66:
                login.CriaVariosAdmin()
                sleep(1)
            elif x == 77:
                login.TabelaUserAdmin()
                sleep(1)
            elif x == 88:
                login.TabelaUser()
                sleep(1)
            elif x == 99:
                login.TabelaAdmin()
                sleep(1)
            elif x == 000:
                login.TabelaSecreta()
                sleep(1)
        else:
            print('\n' * 10)
            print('Seleção invalida! Tente novamente.')
else:
    print('User cancelou a operação...')
    sleep(2)
