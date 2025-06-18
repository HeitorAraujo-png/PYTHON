from back import Contatos, Menu 
# Como nossas classe estão em outro arquivo nos importamos elas
continua = True
# Aquela condição basica para o laço while funfar
print('Primeiramente vamos adicionar um numero.')
fone = Contatos()
# Usamos a classe contatos logo de inicio porque temos que adicionar pelo menos 1 contato para fazermos qualquer coisa
while continua:
    Menu() # Chama o menu como foi explicado
    x = int(input('Digite um numero: ')) 
    # recebe um numero inteiro 
    # E de acordo com oque o usar digitar usando o menu de referencia 
    if x == 1:
        fone = Contatos() # adiciona mais 1 contato
    elif x == 2:
        print('\n' * 20)
        fone.ler() # lê todos os contatos
    elif x == 3:
        print('\n' * 20)
        fone.pesquisa() # Chama o metodo de pesquisar
    elif x == 4:
        print('\n' * 20)
        fone.kamikaze() # apaga a lista de contato
    elif x == 5:
        fone.deletar() # apaga contato especifico 
    elif x == 6: # Acabou né
        break 
    else: # Caso user não saiba ler ou tem dedos gordos
        print('Seleção invalida! Tente novamente.')