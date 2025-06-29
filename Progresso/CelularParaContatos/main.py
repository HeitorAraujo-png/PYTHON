from back import Contatos, Menu, Segurança
from time import sleep
login = Segurança()
acesso, senha, user, admin = login.Verifica()
if acesso:
    print('Primeiramente vamos adicionar um numero.')
    fone = Contatos(acesso=acesso, senha=senha, user=user)
    while acesso:
        Menu(adm=admin)
        try:
            x = int(input('Digite um numero: '))
        except ValueError:
            x = int(input('Seleção invalida! Tente novamente.\nDigite um NUMERO: '))
        if x == 1:
            fone = Contatos(acesso=acesso, senha=senha, user=user)
        elif x == 2:
            print('\n' * 10)
            fone.Ler()
            sleep(2)
        elif x == 3:
            print('\n' * 10)
            fone.Pesquisa()
            sleep(2)
        elif x == 4:
            print('\n' * 10)
            fone.Kamikaze(adm=admin)
            sleep(2)
        elif x == 5:
            print('\n' * 10)
            fone.Deletar()
            sleep(2)
        elif x == 6:
            print('\n' * 10)
            fone.Backup()
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
        if admin:
            if x == 9:
                login.AcessoAdm()
                sleep(1)
            elif x == 10:
                login.TrocaSenha()
                sleep(1) 
            elif x == 11:
                login.TrocaNome()
                sleep(1)
            elif x == 12:
                login.DeletaUser()
                sleep(1)
            elif x == 13:
                login.DeletaAdm()
                sleep(1)                
            elif x == 14:
                login.CriaVariosUser()
                sleep(1)   
            elif x == 15:
                login.CriaVariosAdmin()
                sleep(1)
            elif x == 16:
                login.TabelaUserAdmin()
                sleep(1)
            elif x == 17:
                login.TabelaUser()
                sleep(1)
            elif x == 18:
                login.TabelaAdmin()
                sleep(1)
            elif x == 19:
                login.TabelaSecreta()
                sleep(1)
            elif x == 20:
                login.DeletarLinha()
                sleep(1)
            else:
                print('\n' * 10)
                print('Seleção invalida! Tente novamente.')
        else:
            print('\n' * 10)
            print('Seleção invalida! Tente novamente.')
else:
    print('User cancelou a operação...')
    sleep(2)
