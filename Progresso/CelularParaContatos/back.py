class Contatos:   
    def __init__(self): 
        self.bkp = False
        self.contato = input('Escreva o nome do seu contato: ')
        self.numero = input('Escreva o numero do seu contato: ')
        with open('data.txt', 'a') as arquivo:
            arquivo.writelines(f'Contato: {self.contato} , Numero: {self.numero}')
            arquivo.write('\n')
    def ler(self): 
        with open('data.txt', 'r') as arquivo: 
            lista = arquivo.read() 
            print(lista)
    def kamikaze(self): 
        continua = True
        while continua: 
            certeza = input('Você tem certeza que deseja apagar todos os contatos da sua lista de contatos? [SIM/NãO] ').upper()
            if certeza in ['NÃO', 'NAO']:
                continua = False
            elif certeza == 'SIM':
                while continua:
                    certeza = input('Você tem a certeza ABSOLUTA que deseja apagar todos os seus contatos para SEMPRE??? [SIM/NãO] ').upper()
                    if certeza in ['NÃO', 'NAO']:
                        continua = False
                    elif certeza == 'SIM':            
                        if self.bkp != True:
                            while continua:
                                certeza = input('Você ainda não tem o backup feito! Mesmo assim você deseja apagar sua lista de contatos? [SIM/NÃO]' ).upper()
                                if certeza in ['NÃO', 'NAO']:
                                    continua = False
                                elif certeza == 'SIM': 
                                    while continua:
                                        bkp = input('Deseja fazer o backup? [SIM/NÃO]').upper()
                                        if bkp in ['NÃO', 'NAO']:
                                            with open('data.txt', 'w') as arquivo:
                                                arquivo.write('') 
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
                                                arquivo.write('') 
                                            continua = False
                                            print('Contatos apagados')
                        else:
                            with open('data.txt', 'w') as arquivo:
                                arquivo.write('') 
                            continua = False    
    def pesquisa(self): 
        cade = input('Qual contato ou numero você deseja achar? ')
        with open('data.txt', 'r') as arquivo:
            for linha in arquivo: 
                if cade in linha: 
                    print(linha) 
    def deletar(self): 
        obj = input('Qual contato você deseja deletar? ')
        listas = [] 
        achou = False 
        with open('data.txt', 'r') as arquivo:
            listas = arquivo.readlines()
        with open('data.txt', 'w') as arquivo:
            for i in listas: 
                if obj not in i.lower():
                    arquivo.write(i)
                else:
                    achou = True
            if achou: 
                print('Contato deletado! ')
            else: 
                print('Contato não foi encontrado')    
    def backup(self):
        with open('data.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        with open('dataBKP.txt', 'w') as backup:
            for i in linhas:
                backup.write(i)
        self.bkp = True
        print('backup concluido')
    def SeeBackup(self):
        if self.bkp == True:
            with open('dataBKP.txt', 'w') as bkp:
                print(bkp.read())
        else:
          print('Faça o backup primeiramente!')      
class Menu:
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
)
