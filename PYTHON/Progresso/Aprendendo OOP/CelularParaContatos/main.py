from back import Contatos, Menu, Segurança
from time import sleep

login = Segurança()
acesso, senha, user, admin = login.Verifica()
if acesso:
    print("Primeiramente vamos adicionar um numero.")
    fone = Contatos(acesso=acesso, senha=senha, user=user)
    while acesso:
        Menu(adm=admin)
        try:
            x = int(input("Digite um numero: "))
        except ValueError:
            x = int(input("Seleção invalida! Tente novamente.\nDigite um NUMERO: "))
        if admin:
            if x == 1:
                fone = Contatos(acesso=acesso, senha=senha, user=user)
            elif x == 2:
                print("\n" * 10)
                fone.Ler()
                sleep(2)
            elif x == 3:
                print("\n" * 10)
                fone.Pesquisa()
                sleep(2)
            elif x == 4:
                print("\n" * 10)
                fone.Kamikaze(adm=admin)
                sleep(2)
            elif x == 5:
                print("\n" * 10)
                fone.Deletar()
                sleep(2)
            elif x == 6:
                print("\n" * 10)
                fone.Backup()
                sleep(2)
            elif x == 7:
                print("\n" * 10)
                fone.SeeBackup()
                sleep(2)
            elif x == 8:
                print(("\n" * 5), "Finalizando o programa...")
                sleep(2)
                break
            elif x == 9:
                print("\n" * 5)
                login.AcessoAdm()
                sleep(2)
            elif x == 10:
                print("\n" * 5)
                login.TrocaSenha()
                sleep(2)
            elif x == 11:
                print("\n" * 5)
                login.TrocaNome()
                sleep(2)
            elif x == 12:
                print("\n" * 5)
                login.DeletaUser()
                sleep(2)
            elif x == 13:
                print("\n" * 5)
                login.DeletaAdm()
                sleep(2)
            elif x == 14:
                print("\n" * 5)
                login.CriaVariosUser()
                sleep(2)
            elif x == 15:
                print("\n" * 5)
                login.CriaVariosAdmin()
                sleep(2)
            elif x == 16:
                print("\n" * 5)
                login.TabelaUserAdmin()
                sleep(2)
            elif x == 17:
                print("\n" * 5)
                login.TabelaUser()
                sleep(2)
            elif x == 18:
                print("\n" * 5)
                login.TabelaAdmin()
                sleep(2)
            elif x == 19:
                print("\n" * 5)
                login.TabelaSecreta()
                sleep(2)
            elif x == 20:
                print("\n" * 5)
                login.DeletarLinha()
                sleep(2)
            else:
                print(("\n" * 10), "Seleção invalida! Tente novamente.")
        elif not admin:
            if x == 1:
                fone = Contatos(acesso=acesso, senha=senha, user=user)
            elif x == 2:
                print("\n" * 10)
                fone.Ler()
                sleep(2)
            elif x == 3:
                print("\n" * 10)
                fone.Pesquisa()
                sleep(2)
            elif x == 4:
                print("\n" * 10)
                fone.Kamikaze(adm=admin)
                sleep(2)
            elif x == 5:
                print("\n" * 10)
                fone.Deletar()
                sleep(2)
            elif x == 6:
                print("\n" * 10)
                fone.Backup()
                sleep(2)
            elif x == 7:
                print("\n" * 10)
                fone.SeeBackup()
                sleep(2)
            elif x == 8:
                print(("\n" * 5), "Finalizando o programa...")
                sleep(2)
                break
            else:
                print(("\n" * 10), "Seleção invalida! Tente novamente.")
else:
    print("User cancelou a operação...")
    sleep(2)
