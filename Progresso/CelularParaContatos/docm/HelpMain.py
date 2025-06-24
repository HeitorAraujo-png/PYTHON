from back import Contatos, Menu
# Já que nossos objetos estão em outro arquivo vamos importar eles
from time import sleep
# Biblioteca importada para definir o delay de resposta do programa
# Variavel para 
print('Primeiramente vamos adicionar um numero.')
fone = Contatos()
# Antes de fazermos qualquer coisa nos temos que adicionar ao menos 1 contato
while True:
    Menu()
    x = int(input('Digite um numero: '))
    if x == 1:
        fone = Contatos()
        # Adiciona 1 contato
    elif x == 2:
        print('\n' * 10)
        fone.ler()
        # Lê toda a lista de contatos
        sleep(5)
        # Traduzindo Dormir(5 segundos)
        # Vai ter 5 segundos de delay para a resposta do programa
    elif x == 3:
        print('\n' * 10)
        fone.pesquisa()
        # Pesquisa 1 contato especifico (Se houver numero ou nome duplicado vai aparecer todos)
        sleep(5)
    elif x == 4:
        print('\n' * 10)
        fone.kamikaze()
        # Apaga todos os contatos
        sleep(5)
    elif x == 5:
        print('\n' * 10)
        fone.deletar()
        # Deleta apenas 1 contato
        sleep(5)
    elif x == 6:
        print('\n' * 10)
        fone.backup()
        # Faz o backup
        sleep(5)
    elif x == 7:
        print('\n' * 10)
        fone.SeeBackup()
        # Mostra o backup
        sleep(5)
    elif x == 8:
        print('\n' * 10)
        sleep(5)
        print('Finalizando o programa...')
        sleep
        break
        # Acaba o programa
    else:
        print('\n' * 10)
        print('Seleção invalida! Tente novamente.')
        # User fez alguma coisa de errado