from back import Contatos, Menu, Segurança
# Já que nossos objetos estão em outro arquivo vamos importar eles

from time import sleep
# Biblioteca importada para definir o delay de resposta do programa

login = Segurança()
# Faz o login do user

acesso, senha, user, admin = login.Verifica()
# retorna o acesso, senha, user e o ADMIN caso for um ADMIN
# Se o login for bem realizado:  acesso=True, senha=str, user=str e se for ADMIN: admin=True
# Senão: acesso=False, senha=False, user=False

if acesso:
# se o o login der certo
    
    print('Primeiramente vamos adicionar um numero.')
    # Antes de fazermos qualquer coisa nos temos que adicionar ao menos 1 contato
    fone = Contatos(acesso=acesso, senha=senha, user=user)
    # Agora faz mais sentido quando olhamos o outro arquivo
    
    while acesso:
        
        Menu(adm=admin)
        # Mostra o menu
        
        try: # Aqui tem coisa nova
        # O programa vai tentar:
            x = int(input('Digite um numero: '))
            # Se for digita um numero, fé que deu certo

        except ValueError:
        # Basicamente se o usuario digitar uma letra vai voltar erro, então daremos outra chance a ele
            x = int(input('Seleção invalida! Tente novamente.\nDigite um NUMERO: '))
            # SE ele novamente digitar uma letra o programa retorna ValueError e o programa fecha
        
        if admin:
            # Se for admin
            
            if x == 1:
                fone = Contatos(acesso=acesso, senha=senha, user=user)
                # Adiciona mais um contato a lista
                
                sleep(2)
                
            elif x == 2:
                print('\n' * 10)
                fone.Ler()
                # Mostra a lista de contatos
                
                sleep(2)
            
            elif x == 3:
                print('\n' * 10)
                fone.Pesquisa()
                # Pesquisa contato especifico
                
                sleep(2)

            elif x == 4:
                print('\n' * 10)
                fone.Kamikaze(adm=admin)
                # Apaga tudo
                
                sleep(2)

            elif x == 5:
                print('\n' * 10)
                fone.Deletar()
                # Deleta um contato e se tiver duplicado
                
                sleep(2)

            elif x == 6:
                print('\n' * 10)
                fone.Backup()
                # faz backup
                
                sleep(2)

            elif x == 7:
                print('\n' * 10)
                fone.SeeBackup()
                # Mostra o backup
                
                sleep(2)

            elif x == 8:
                print(('\n' * 5),'Finalizando o programa...')
                # Finaliza o programa
                
                sleep(2)
                break
            
            elif x == 9:
                print('\n' * 5)
                login.AcessoAdm()
                # Deixa um user como ADMIN
                
                sleep(2)
                
            elif x == 10:
                print('\n' * 5)
                login.TrocaSenha()
                # Troca a senha de um usuario
                
                sleep(2) 
                
            elif x == 11:
                print('\n' * 5)
                login.TrocaNome()
                # Troca o nome de um usuario
                
                sleep(2)
                
            elif x == 12:
                print('\n' * 5)
                login.DeletaUser()
                # Deleta um user
                
                sleep(2)
                
            elif x == 13:
                print('\n' * 5)
                login.DeletaAdm()
                # Deleta um ADMINI
                
                sleep(2)          
                      
            elif x == 14:
                print('\n' * 5)
                login.CriaVariosUser()
                # Cria varios users
                
                sleep(2)   
                
            elif x == 15:
                print('\n' * 5)
                login.CriaVariosAdmin()
                # Cria varios ADMIN'S
                
                sleep(2)
                
            elif x == 16:
                print('\n' * 5)
                login.TabelaUserAdmin()
                # Mostra uma tabela de acesso dos users e ADMIN'S
                
                sleep(2)
                
            elif x == 17:
                print('\n' * 5)
                login.TabelaUser()
                # Mostra uma tabela de acesso dos users
                
                sleep(2)
                
            elif x == 18:
                print('\n' * 5)
                login.TabelaAdmin()
                # Mostra uma tabela dos ADMIN'S
                
                sleep(2)
                
            elif x == 19:
                print('\n' * 5)
                login.TabelaSecreta()
                # Mostra uma tabela de acesso e senha dos users e ADMIN'S
                # Eu deixei como TabelaSecreta porque ela é secreta né
                # Também para os ADMIN'S conseguirem ver todos os usuarios e senhas cadastrados
                
                sleep(2)
                
            elif x == 20:
                print('\n' * 5)
                login.DeletarLinha()
                # Deleta qualque linha desejada
                # Essa eu preferi esconder essa funcionalidade porque ela deleta a linha de um ADMIN sem perdir a senha dele
                # Eu poderia muito bem so pedir para que se a linha for de um ADMIN colocar a senha dele para apagar
                # Porem, entretanto, toda via, eu preferi deixa assim porque é muito mais rapido e pratico
                # Porque o principal motivo desse metodo é apagar uma linha de maneira rapida
                # CASO eu fosse colocar ela no menu eu criaria um "ADMIN especial" para usar esse metodo e a tabela secreta
                # Porém eu acho que assim já esta bom   
                
                sleep(2)
                
            else:
                print(('\n' * 10),'Seleção invalida! Tente novamente.')
                
        elif not admin:
            
            if x == 1:
                fone = Contatos(acesso=acesso, senha=senha, user=user)
                # Adiciona mais um contato a lista
            
            elif x == 2:
                print('\n' * 10)
                fone.Ler()
                # Mostra a lista de contatos
                
                sleep(2)
            
            elif x == 3:
                print('\n' * 10)
                fone.Pesquisa()
                # Pesquisa contato especifico
                
                sleep(2)

            elif x == 4:
                print('\n' * 10)
                fone.Kamikaze(adm=admin)
                # Apaga tudo
                
                sleep(2)

            elif x == 5:
                print('\n' * 10)
                fone.Deletar()
                # Deleta um contato e se tiver duplicado
                
                sleep(2)

            elif x == 6:
                print('\n' * 10)
                fone.Backup()
                # faz backup
                
                sleep(2)

            elif x == 7:
                print('\n' * 10)
                fone.SeeBackup()
                # Mostra o backup
                
                sleep(2)

            elif x == 8:
                print(('\n' * 5),'Finalizando o programa...')
                # Finaliza o programa
                
                sleep(2)
                
                break
            
            else:
                print(('\n' * 10),'Seleção invalida! Tente novamente.')
                # Se o user comum digitar um numero maior que 8 ou igual a 0
                
                sleep(2)

else:
# Se o login não der certo...
    
    print('User cancelou a operação...')
    sleep(2)