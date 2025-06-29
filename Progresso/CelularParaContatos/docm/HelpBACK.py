class Contatos: 
# classe para tudo que vamos usar de importante
    
    def __init__(self): 
        # Metodo
        # Ao iniciarmos a classe "Contatos" 
        # O primeiro metodo obrigatoriamente chamado é esse "__init__"
        # self significa a variavel a ser chamada
        # exemplo: celular = Contatos(), nesse exemplos "celular" vai ser self
        # Agora "celular" é um objeto no qual iremos utilizar para usar qualquer metodo da classe "Contatos
        self.bkp = False
        # Mostra que não tem backup feito
        self.contato = input('Escreva o nome do seu contato: ')
        self.numero = input('Escreva o numero do seu contato: ')
        # O lado positivo de utilizarmos o self ao inves de uma variavel comum é que
        # Ao utilizarmos o self.exemplo como uma "variavel" ela vira global somente na CLASSE que foi declarada
        # Então ela pode ser acessa por qualquer outro metodo dessa classe
        
        with open('data.txt', 'a') as arquivo:
            # basicamente siginifica "abrir e depois fechar", abrir('ArquivoDesejado.txt', 'adicionar linha') como qualquer nome
            # with = abrir o arquivo logo depois fechar
            # open = abrir
            # ('data.txt', 'a') = nome do arquivo, append
            # as Variavel_De_Iteração = assim como for i in o "i" é uma varivel de iteração, ou seja, ele so existe naquele loop 
            
            arquivo.writelines(f'Contato: {self.contato} , Numero: {self.numero}')
            arquivo.write('\n')
            # writelines ou write não pode receber mais de 1 argumento ou seja se tivessemos colocado ('Contato: ', {self.contato}', Numero: ' {self.numero})
            # Não iria dar certo, por isso utilizamos a f string, assim dentro de writelines tera somente 1 argumento 
            # Logo apos o programa para de utilizar o ArquivoDesejado vai fechar
            # SE no seu programa você optar de não usar o with logo de começo no final dele você deve colocar 
            # ArquivoDesejado.close()
            
    def ler(self): 
        # Ler oque há dentro de 'data.txt'
        with open('data.txt', 'r') as arquivo: 
        # Usamos "r" de read, ou seja leitura, sem alteração dos dados
            print(arquivo.read)
            # Vamos imprimit a lista de contatos inteira
    
    def kamikaze(self): 
        # Vamos apagar tudo
        continua = True 
        # Eu te aconselho a fazer esse sistema de verificação com o laço while e com alguma variavel que podemos mudar para False
        while continua:
            certeza = input('Você tem certeza que deseja apagar todos os contatos da sua lista de contatos? [SIM/NãO] ').upper() 
            # usando o .upper() essa linha do input vai tranformar todas as letras em maiusculas 
            # Para saber se o usuario tem certeza que ele quer apagar os contatos deles
            if certeza in ['NÃO', 'NAO']:
                continua = False
            # Caso o usuario não queira excluir os arquivos
            # O laço while acaba pois a condição dele recebe False
            elif certeza == 'SIM':
            # User tem certeza então vamos continuar
                while continua:
                    certeza = input('Você tem a certeza ABSOLUTA que deseja apagar todos os seus contatos para SEMPRE??? [SIM/NãO] ').upper()
                    # Vamos verificar novamente, ele pode ter trocado de ideia(né?)
                    if certeza in ['NÃO', 'NAO']:
                        continua = False
                    # user tem certeza que não quer, os laços while acabam pois todos recebem False
                    elif certeza == 'SIM':
                        if self.bkp == False:
                        # Agora tem uma condição mais especifica
                        # SE o backup não foi feito ele inicia esse laço de repetição
                            while continua:
                                certeza = input('Você ainda não tem o backup feito! Mesmo assim você deseja apagar sua lista de contatos? [SIM/NÃO]' ).upper()
                                # Vamos ver se o user mesmo não tendo o backup deseja apagar a lista de contatos
                                if certeza in ['NÃO', 'NAO']:
                                    continua = False
                                # O user optou por não continuar
                                # a variavel do while vai receber False então os whiles vão ser finalizados
                                elif certeza == 'SIM': 
                                    bkp = input('Deseja fazer o backup? [SIM/NÃO]').upper()
                                    # Verificar se o user deseja ou não fazer o backup
                                    if bkp in ['NÃO', 'NAO']:
                                    # User desejou apagar sem fazer backup, então vamos apagar sem mais nem menos
                                        with open('data.txt', 'w') as arquivo:
                                        # diferente de "r" ou "a" ao utilizarmos "w" nos estamos sobreescrevendo tudo nesse arquivo, algo muito perigoso
                                        # devemos utiliza-la apenas quando nos queremos ou apagar ou modificar um linha
                                            arquivo.write('') 
                                            # O arquivo inteiro é "apagado"
                                        continua = False
                                    elif bkp == 'SIM':
                                        with open('data.txt', 'r') as arquivo:
                                            linhas = arquivo.readlines()
                                        with open('dataBKP.txt', 'w') as backup:
                                            for i in linhas:
                                                backup.write(i)
                                        self.bkp = True
                                        print('backup concluido')       
                                        with open('data.txt', 'w') as arquivo:
                                            arquivo.write('') # O arquivo inteiro é "apagado"
                                        continua = False
                                        print('Contatos apagados')
                        else:
                        # agora SE tiver backup ou seja self.bkp == True
                        # pode apagar sem medo porque temos o backup
                            with open('data.txt', 'w') as arquivo:
                                arquivo.write('') 
                                # O arquivo inteiro é "apagado"
                            continua = False    
            
    def pesquisa(self): 
    # Pesquisar numero
        cade = input('Qual contato ou numero você deseja achar? ')
        # Vamos receber uma string seja nome ou o numero que o usuario deseja procurar
        with open('data.txt', 'r') as arquivo:
            for linha in arquivo: 
            # Para cada linha dentro de 'data.txt'
                if cade in linha: 
                # Se a variavel "cade" estiver na linha
                    print(linha) 
                    # imprimi a linha na qual o contato esta

    def deletar(self): 
    # Deletar unico ou duplicado contato
        obj = input('Qual contato você deseja deletar? ')
        # Novamente recebe uma string recebendo nome ou numero de usuario a ser deletado
        listas = [] 
        # fazemos uma lista vazia
        achou = False 
        # Achamos? não? então é False
        with open('data.txt', 'r') as arquivo:
            listas = arquivo.readlines()
            # essa lista vai receber o arquivo inteiro somente para leitura
        with open('data.txt', 'w') as arquivo:
            for i in listas: 
                # Cada linha dentro da lista
                if obj not in i.lower():
                # Se a string que estamos procurando não estiver na linha
                    arquivo.write(i)
                    # Aqui usamos o "w" para sobreescrever na linha
                    # "Mais Heitor ai todas as linhas não vão receber a mesmas coisa porque ela vai estar sobreescrevendo tudo"
                    # E eu te digo "Não", porque no primeiro laço nos chamos só 1 linha, assim modificando apenas ela
                else:
                # Agora se a string que estamos procurando estiver na linha
                # A linha é "apagada" porque ela não vai ser escrita no "novo" arquivo
                    achou = True
                    # Achamos? Sim? Então é True
            # depois de verificar todas as linhas do arquivo
            if achou: 
            # Achamos quem deveria achar? Se sim...
                print('Contato deletado! ')
            else: 
            # Não achamos ou não existe...
                print('Contato não foi encontrado')
    
    def backup(self):
        with open('data.txt', 'r') as arquivo:
        # Abrir o arquivo principal, para leitura
            linhas = arquivo.readlines()
            # colocar esse arquivo em uma variavel
        with open('dataBKP.txt', 'w') as backup:
            for i in linhas:
                backup.write(i)
        self.bkp = True
        print('backup concluido')
    def SeeBackup(self):
        if self.bkp == True:
        # SE tem backup
            with open('dataBKP.txt', 'r') as bkp:
                print(bkp.read())
                # imprime o backup
        else:
        # SENÃO tem backup  
            print('Faça o backup primeiramente!')
          
class Menu: 
# Classe para o menuzinho
    def __init__(self):
        print('''
    Escolha uma opção:
    1. Adicionar aos contato
    2. Ler Contatos
    3. Pesquisar Contato
    4. Apagar Todos os Contatos (Kamikaze)
    5. Apagar contato
    6. BACKUP
    7. Sair'''
    # Assim que Menu() for chamado ele imprimi isso automaticamente
)
