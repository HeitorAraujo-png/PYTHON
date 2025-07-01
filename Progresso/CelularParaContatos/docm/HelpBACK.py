from re import search
# Importamos essa biblioteca re(regular espression) é uma ferramentea essencia que iremos mostrar como ela é util mais tarde
# O codigo esta TOTALMENTE DOCUMENTADO
class Contatos:
# classe para tudo que vamos usar de importante sobre os contatos

    def __init__(self, acesso, senha, user):# Metodo
        # Ao iniciarmos a classe "Contatos" 
        # O primeiro metodo obrigatoriamente chamado é esse "__init__"
        # self significa a variavel a ser chamada'
        # exemplo: celular = Contatos(), nesse exemplos "celular" vai ser self
        # Agora "celular" é um objeto no qual iremos utilizar para usar qualquer metodo da classe "Contatos
        # Podemos ver que depois de "self" tem: acesso, senha, user
        
        if acesso:
        # se acesso for igual verdadeiro
        # acesso é um parametro booleano(True or False)
            
            self.bkp = False
            # Mostra que não tem backup feito
            
            self.user_acesso = acesso
            self.senha = senha
            # senha de login do user 
            
            self.user = user
            # user de dlogin do user
            
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
                arquivo.write(f'Contato: {self.contato} , Numero: {self.numero}')
                arquivo.write('\n')
                # writelines ou write não pode receber mais de 1 argumento ou seja se tivessemos colocado ('Contato: ', {self.contato}', Numero: ' {self.numero})
                # Não iria dar certo, por isso utilizamos a f string, assim dentro de writelines tera somente 1 argumento 
                # Logo apos o programa para de utilizar o ArquivoDesejado vai fechar
                # SE no seu programa você optar de não usar o with logo de começo no final dele você deve colocar 
                # ArquivoDesejado.close()
                
    def Ler(self):
        # Ler oque há dentro de 'data.txt'
        with open('data.txt', 'r') as arquivo: 
        # Usamos "r" de read, ou seja leitura, sem alteração dos dados
            print(arquivo.read)
            # Vamos imprimit a lista de contatos inteira
            
    def Kamikaze(self, adm):
        # Vamos apagar tudo
        continua = True
        # Variavel tipo boolean para o laço de repetição
        self.user_acesso = False
        # Acesso vai irar False/Negado
        self.admin_acesso = adm
        # Se for adm recebe True
        
        if not self.admin_acesso:
        # Se não for ADMIN
            while self.user_acesso != True:
            # Enquanto o acesso do user for false
                
                user = input('Digite seu usuario: ').strip()
                # O strip é para evitar espaço desnecessarios no input exemplo: "    heitor    " vai virar "heitor"
                tentativas = input('Digite a sua senha: [Escreva "Sair" para cancelar]: ').strip()
                if tentativas.lower() == 'sair':
                # se fosse tentativas == "Sair" se o user escrevesse "sair" o programa não ia reconhecer pois "Sair" != "sair"
                # assim usamos o .lower() porque ela vai transformar a linha em minuscula 
                    return
                    # Se o user escrever "sair" vai cancelar o processo
                
                else:
                #  Se o user não cancelar o processo
                    
                    if tentativas == self.senha and user == self.user:
                    # Se a senha e usuario for realmente verdadeira
                        self.user_acesso = True
                        # Acesso permitido
                    else:
                    # Se não...
                        print('Ou usuario ou senha esta incorreta')
                        self.user_acesso = False
            
            while continua: 
                certeza = input('Você tem certeza que deseja apagar todos os contatos da sua lista de contatos? [SIM/NãO] ').upper().strip()
                # Vamos verificar se ele tem certeza do que ele quer
                if certeza == 'SIM':
                    while continua:
                        
                        certeza = input('Você tem a certeza ABSOLUTA que deseja apagar todos os seus contatos para SEMPRE??? [SIM/NãO] ').upper().strip()
                        if certeza == 'SIM':
                        # Vamos verificar novamente, se ele ter certeza
                            
                            if self.bkp != True:
                            # Se o backup não estiver feito
                                
                                while continua:
                                    certeza = input('Você ainda não tem o backup feito! Você não é ADMIN então não pode apagar a lista sem um backup! Você deseja fazer o backup? [SIM/NÃO]' ).upper().strip()
                                    # Vamos avisar que o user não tem backup e perguntar se ele quer fazer o backup
                                    if certeza == 'SIM': 
                                    # Se ele quer fazer o backup
                                        
                                        self.Backup()
                                        # Para usarmos um metodo dentro de outro metodo usamos "self.metodo()"
                                        print('backup concluido')       
                                        # Agora o backup esta feito!
                                        with open('data.txt', 'w') as arquivo:
                                            arquivo.write('') 
                                        continua = False
                                        print('Contatos apagados')
                                        # Kamikaze fez um trabalho bem feito
                                    
                                    # Apartir daqui é caso em algum momento o usuario tem escrito "NÃO" OU "NAO" inves de "SIM"
                                    elif certeza in ['NÃO', 'NAO']:
                                        continua = False
                                    else:
                                        print('Seleção invalida! Tente novamente.')
                            
                            # Aqui é um caso diferente 
                            else:
                            # se o usuario não quiser fazer o backup
                                with open('data.txt', 'w') as arquivo:
                                    arquivo.write('') 
                                continua = False
                        
                        elif certeza in ['NÃO', 'NAO']:
                            continua = False
                        else:
                            print('Seleção invalida! Tente novamente.')
                
                elif certeza in ['NÃO', 'NAO']:
                    continua = False
                else:
                    print('Seleção invalida! Tente novamente.')
        
        else:
        # Caso o usuario for um ADMIN
            if self.bkp != True:
            # Se o backup não tiver ter sido feito
            # Apartir daqui não sera nada de muito novo
                while continua:
                    certeza = input('Você deseja apagar todos os contatos da sua lista de contatos? [SIM/NãO] ').upper().strip()
                    if certeza == 'SIM':
                    
                        while continua:
                            certeza = input('Você ainda não tem o backup feito! Mesmo assim você deseja apagar sua lista de contatos? [SIM/NÃO]' ).upper().strip()
                            if certeza == 'SIM':
                    
                                while continua:
                                    bkp = input('Deseja fazer o backup? [SIM/NÃO]').upper().strip()
                    
                                    if bkp in ['NÃO', 'NAO']:
                                        with open('data.txt', 'w') as arquivo:
                                            arquivo.write('') 
                                        continua = False
                    
                                    elif bkp == 'SIM':
                                        self.Backup
                                        self.bkp = True
                                        print('backup concluido')       
                                        with open('data.txt', 'w') as arquivo:
                                            arquivo.write('') 
                                        continua = False
                                        print('Contatos apagados')
                    
                            elif certeza in ['NÃO', 'NAO']:
                                continua = False
                    
                    elif certeza in ['NÃO', 'NAO']:
                        continua = False
 
            # Como o user é um ADMIN e o backup tiver ter sido feito
            else:
            # Pode apagar tranquilo
                with open('data.txt', 'w') as arquivo:
                    arquivo.write('') 
                continua = False  
                             
    def Pesquisa(self): 
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
                    
    def Deletar(self): 
        # Deletar contato unico ou duplicado
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
            
            if achou: 
            # depois de verificar todas as linhas do arquivo
            # Achamos o contato? Se sim...
                print('Contato deletado! ')
            
            else: 
            # Não achamos ou não existe...
                print('Contato não foi encontrado')
        
    def Backup(self):
        while self.user_acesso != True:
            user = input('Digite seu usuario: ').strip()
            tentativas = input('Digite a sua senha: [Escreva "Sair" para cancelar]: ').strip()
            # novamente fazemos o login
            
            if user.lower != 'sair':
                if tentativas == self.senha and user == self.user:
                    self.user_acesso = True
                else:
                    print('Ou usuario ou senha esta incorreta')
                    self.user_acesso = False
            else:
                print('saindo...')
                return
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
        while self.user_acesso != True:
            user = input('Digite seu usuario: ').strip()
            tentativas = input('Digite a sua senha: [Escreva "Sair" para cancelar]: ').strip()
            # Login novamente
            
            if user != '':
                if tentativas == self.senha and user == self.user:
                    self.user_acesso = True
                else:
                    print('Ou usuario ou senha esta incorreta')
                    self.user_acesso = False
            else:
                print('saindo...')
                return
        if self.bkp == True:
        # SE tem backup
            with open('dataBKP.txt', 'r') as bkp:
                print(bkp.read())
                # imprime o backup
        else:
        # SENÃO tem backup  
            print('Faça o backup primeiramente!')

class Segurança:
# Classe para fazer a parte da segurança

    def __init__(self):
        self.user_acesso = self.admin_acesso = False
        # Tanto o acesso do User e do ADMIN estão negadas
        
        self.Acesso = 'User'
        # Todo usuario que for cadastrado ele e automaticamente um usuario
        
        while True:
            definir = input('Você quer fazer [LOGIN/CADASTRO]? ').upper().strip()
            # Perguntamos ao user se ele quer fazer o LOGIN (Se ele estiver cadastrado) ou CADASTRAR (Se for o primeiro acesso)
            
            if definir == 'CADASTRO':
            # Se o user quiser fazer o cadastro
            
                while True:
                    while True:
                        achamos = False
                        self.user = input('Digite seu user: ').strip()
                        # Pedimos para que o user digite seu nome
                        
                        with open('AdmUser.txt', 'r') as log:
                            texto = log.readlines()
                        for linha in texto:
                            if f'Usuario: {self.user}' in linha:
                            # Se outro user tiver o mesmo nome
                                achamos = True
                                # Se achamos... 
                        if achamos:
                            print(f'Nome de usuario "{self.user}" já cadastrado. Tente outro...')
                            # Fala para o user digitar outro nome porque o nome que ele digitou esta cadastrado
                        else:
                            # Se o nome do usuario for unico
                            break # Acaba esse laço e começa o outro
                    while True:
                        verifica, senha = self.VerificaSenha()
                        # self.VerificaSenha() é um metodo que eu vou explicar depois
                        # Verifica volta uma lista e a senha do user
                        
                        if not verifica:
                        # Se a lista estiver vazia 
                            self.senha = senha
                            # Senha do user vai virar a senha "padrão"
                            
                            with open('AdmUser.txt', 'a') as cadastrar:
                                cadastrar.writelines(f'Usuario: {self.user} | Senha: {self.senha} | Acesso: {self.Acesso} \n')
                                # Cadastro o novo usuario
                            self.user_acesso = True
                            self.admin_acesso = False
                            # acesso são liberados
                            break
                        
                        else:
                        # Se a lista tiver alguma coisa:
                            print(', '.join(verifica),'.')
                            # Como verifica é uma lista ela vai voltar: 
                            # ['A senha deve ter 8 digitos','A senha deve ter ao menos 1 digito','A senha deve ter ao menos uma letra maiuscula','A senha deve ter ao menos uma letra minuscula']
                            # o ', '.join(e a lista) vai retornar: A senha deve ter 8 digitos, A senha deve ter ao menos 1 digito, A senha deve ter ao menos uma letra maiuscula, A senha deve ter ao menos uma letra minuscula
            
            elif definir == 'LOGIN':
            # Se o user ja for cadastrado

                while True:
                    with open('AdmUser.txt', 'r') as arquivo:
                        texto = arquivo.readlines()
                    # texto vai receber as linha de AdmUser.txt
                    user = input('Digite seu usuario: ').strip()
                    tentativas = input('Digite a sua senha: [Escreva "Sair" para cancelar]: ').strip()
                    # User vai digitar o User dele e a Senha
                    
                    if tentativas.lower() != 'sair':
                        for linha in texto:
                            if f'Usuario: {user}' in linha and f'Senha: {tentativas}' in linha and tentativas != '':
                            # Resumo: Se o usuario e senha estiver na mesma linha
                            # Explicação: 
                            # usamos a f-string para fazer uma comparação
                            # Se f'Usuario: Heitor' e f'Senha: Abcd1234' estiverem na limha e a tentiva de senha for dirente de ''
                                
                                self.user_acesso = True
                                # Libera o acesso
                                
                                self.senha = tentativas
                                self.user = user
                                # E a senha e o user viram o padrao
                                
                                if 'Acesso: ADMIN' in linha:
                                # Se na mesma linha de login o acesso for de um ADMIN
                                    self.admin_acesso = True
                                    # O acesso do admin vira verdadeiro
                                print('Usuario Logado com sucesso!')
                                # Da um retorno ao user que ele esta logado
                                return # Finaliza o metodo
                        
                        if not self.user_acesso:
                        # Se o user ou senha estiverem errado
                            print('Usuario ou senha incorreta!')
                    
                    else:
                        print('saindo...')
                        # Se o user quiser cancelar o processo por inteiro
                        self.user_acesso = self.senha = self.user = self.admin_acesso = False
                        # Tudo vira False
                        
                        return
            else:
                print('Tente novamente!')
                # Se o user escreveu errado
                
    def VerificaSenha(self):
    # Verificador de senha
        erro = []
        # Lista para mostrar os erros e mostrar ao user oque falta para a senha dele estar "Padrão"
        senha = input('Digite a senha desse usuario: ').strip()
        confirma = input('Digite novamente a senha: ').strip()
        # O user tem que escrever a senha dele 2 vezes para caso na primeira ele ter escrito errado
        
        if confirma != senha:
        # Se a senha for diferente da confirmação de senha
            erro.append('As senhas devem ser iguais')
            # erro vai ter um novo item na lista
            
        if len(senha) < 8:
            # Se a quantidade de digitos for menos que 8
            erro.append('A senha deve ter pelo menos 8 caracteres')
            
        if not search(r'\d', senha):
            # Aqui vamos mostrar como a biblioteca 're' é poderosa, mais precisamente o 'search'
            # Basicamente podemos dizer que search vai retornar True e False
            # a linha 415 diz basicamente esta escrita "se não for verdadeiro: pesquisar(re'\numero', senha)"
            # se não tiver nenhum numero na senha
            # como usamos o 'f' antes de uma string vamos user o 'r' também 
            # search(r'\d', senha)
            # concorda comigo se so digitarmos (r'\d') não faz sentido né? porque nos vamos estar dizendo para ele preocurar um digito de lugar nenhuma
            # Então colocamos de onde queremos procurar esse digito, que é a variavel senha
            erro.append('A senha deve ter ao menos 1 digito')
            
        if not search(r'[A-Z]', senha):
            # aqui o search vai procurar se tem alguma letra de A a Z em maiusculo
            # E sim tem que ser todo juntinho '[A-Z]' se colocar espaço '[A - Z]' ele vai dar errado
            erro.append('A senha deve ter ao menos uma letra maiuscula')
            
        if not search(r'[a-z]', senha):
            # Faz a mesma coisa que o anterior, agora verificando se tem letra minuscula
            erro.append('A senha deve ter ao menos uma letra minuscula')
        
        if not erro:
            # Se a lista de erro estiver vazia(False)
            # porque (lista = []) == False 
            # Motivo: Se tiver alguma coisa dentro de qualquer coisa (Tupla, dicionario, listas, variaveis, constantes) em binario ela é igual a 1 que é True
            return erro, senha
        
        else:
            # Se a lista voltar com algum erro
            # porque (lista = ['As senhas devem ser iguais']) == True
            # Motivo: Se algo estiver vazio/null é igual a 0 que em binario é False
            return erro, senha
        
    def VerificaAdmin(self):
    # Verificadores de ADMIN
        while True:
            usuario = input('Digite seu usuario (ADMIM): ').strip()
            senha = input('Digite a sua senha: [Escreva "Sair" para cancelar]: ').strip()
            # Pede para o user digitar o login e senha
            if senha.lower() != 'sair':
                with open('AdmUser.txt', 'r') as log:
                    for linha in log:
                        if f'Usuario: {usuario}' in linha and f'Senha: {senha}' in linha and f'Acesso: ADMIN' in linha:
                            # Se o login e senha e o acesso for de ADMIN estiverem na mesma linha
                            return True # Retorna Verdadeiro
            else:
                # Caso o user cancele a operação
                return False # Retorna Falso
            
            # Se o user digou login ou senha errado
            print('Usuario ou senha invalida')
            
    def Verifica(self):
    # verificador
        if self.user_acesso:
        # Se o user logou
            return self.user_acesso, self.senha, self.user, self.admin_acesso
            # Retorna o acesso a senha o login e se for ADMIN retorna o acesso
        else:
            # Caso user não logou ele retorna também, porem, tudo falso
            return self.user_acesso, self.senha, self.user, self.admin_acesso
        
    def AcessoAdm(self):
    # Transformando user padrão em ADMIN
        if self.admin_acesso:
        # Se o user esta usando esse metodo é ADMIN
            
            verifica = self.VerificaAdmin()
            # O ADMIN tem que logar 
            # ADMIN logou == True
            # ADMIN não logou == False
            
            if verifica:
            # Se o ADMIN logou
                while True:
                    user = input('Qual usuario você deseja deixa como ADMIN? [Digite "Sair" para parar] ').strip()
                    # Pede o nome do usuario para deixar como ADMIN
                    
                    if user.lower() != 'sair':
                        
                        with open('AdmUser.txt', 'r') as leitura:
                            texto = leitura.readlines()
                        
                        with open('AdmUser.txt', 'w') as escreve:
                            for linha in texto:
                                
                                if f'Usuario: {user}' in linha:
                                # Se acharmos o usuario...
                                    escreve.write(f'{linha[:linha.find('Acesso: User')]} Acesso: ADMIN')
                                    # Aqui entramos em uma parte complicada, que é a manipulação de uma string
                                    # f'({linha[]})' lembra que usamos o colchetes para indicar posição né?
                                    # f'({linha[linha.find('Acesso: User')]})' == f'({linha[25]})(um exemplo ok?)
                                    # f'({linha[:linha.find('Acesso: User')]})' agora adicionamos um simples : que muda tudo
                                    # f'({linha[antes:depois:]' os : indica é antes ou depois que a string começa ou para
                                    # f'({linha[:linha.find('Acesso: User')]} Acesso: ADMIN')'ou seja...
                                    # Essa linha vai escrever ate ela achar 'Acesso: User' quando ela achar ela vai parar de escrever e finalizar com Acesso: ADMIN
                                    
                                    print(f'Usuario: {user} agora é ADMIN!')
                                    # Feedback caso acharmos o user
                                
                                else:
                                # Se não...
                                    escreve.write(linha)
                            break # quando ler todas as linha
                    
                    elif user.lower() == 'sair':
                        break
                    
    def TrocaNome(self):
    # Trocar nome do user
    
        if self.admin_acesso:
            verifica = self.VerificaAdmin()
            if verifica:
                while True:
                    pesquisa = input('Qual o nome do usuario que você deseja trocar de nome? ').strip()
                    # Pergunta qual o nome do user para trocar o nome
                    troca = input('Qual vai ser o novo nome? ').strip()
                    # Qual se a o novo nome
                    if pesquisa == '' or troca == '':
                        return
                    with open('AdmUser.txt', 'r') as leitura:
                        texto = leitura.readlines()
                    with open('AdmUser.txt', 'w') as escreve:
                        for linha in texto:
                            if f'Usuario: {pesquisa}' in linha:
                                escreve.write(f'Usuario: {troca}{linha[(linha.find(' | Senha: ')):]}')
                                # Novamente manipulação de string
                                # Agora a linha so vai imprimir depois achar onde começa a senha
                                # f'Usuario: {troca}{linha[(linha.find(' | Senha: ')) : ]}' 
                                # exemplo: f'Usuario: {troca}{linha[(linha.find(18:]}'
                                # então o programa sabe onde ele começa e não sabe onde termina, então ele vai escrever ate onde dá
                                
                                print(f'Nome trocado!')
                            
                            else:
                                escreve.write(linha)
                        return

    def TrocaSenha(self):
    # Troca a senha de um usuario
        if self.admin_acesso:
            verifica = self.VerificaAdmin()
            if verifica:
                while True:
                    User = Password = False
                    # sempre recebe False no incio do laço
                    
                    user = input('Qual o nome do usuario que você deseja trocar de senha? ').strip()
                    password = input('Qual é a senha dele atual? ')
                    # pergunta o login e senha desse user
                    
                    if user == '' or password == '':
                        return
                    
                    with open('AdmUser.txt', 'r') as log2:
                        for linha2 in log2:
                            if f'Usuario: {user}' in linha2:
                                # Se o user estiver na linha
                                User = True

                            if f'Senha: {password}' in linha2:
                                # Se a senha estiver na mesma linha
                                Password = True
                    
                        if Password == False or User == False:
                        # Se um dos 2 for False
                            print('Usuario ou senha invalido! Tente novamente.')
                            
                    while User and Password:
                    # Se User e Password for True
                        verificar, senha = self.VerificaSenha()
                        if not verificar:
                            # se a lista estiver vazia então a senha é "Ok"
                            break
                        
                        else:
                            # Se a lista tiver alguma coisa
                            print(', '.join(verificar),'.')
                            
                    with open('AdmUser.txt', 'r') as log:
                        texto = log.readlines()
                    with open('AdmUser.txt', 'w') as escreve:
                        for linha in texto:
                            
                            if f'Usuario: {user}' in linha and f'Senha: {password}' in linha:
                                escreve.write(f'Usuario: {user} | Senha: {senha} | Acesso: {linha[(linha.find('Acesso: ')):]} \n')
                                print(f'Senha trocada!')
                            
                            else:
                                escreve.write(linha)
                        return  
                       
    def DeletaUser(self):
    # Deletar login de um user comum
        if self.admin_acesso:
            condicao = self.VerificaAdmin()
            if condicao:
                pesquisa = input('Qual o usuario que você deseja deletar? ').strip()
                # Pergunta qual user o ADMIN quer deletar
                with open('AdmUser.txt', 'r') as log:
                    texto = log.readlines()
                with open('AdmUser.txt', 'w') as escreve:
                    for linha in texto:
                        if f'Usuario: {pesquisa}' in linha and not f'Acesso: ADMIN' in linha:
                        # Se o user estiver na linha e acesso não for de um ADMIN
                            escreve.write('')
                            print(f'Usuario deletado!')
                            # Deleta o user
                            
                        else:
                            escreve.write(linha)
                    return

    def DeletaAdm(self):
    # Deletar o login de um ADMIN
        if self.admin_acesso:
            condicao = self.VerificaAdmin()
            while condicao:
                
                pesquisa = input('Qual o ADMIN que você deseja deletar? ').strip()
                pesquisa_senha_admin = input('Qual a senha desse ADMIN?').strip()
                # Pergunta login e senha de ADMIN que deseja deletar
                
                while True:
                    ok = input('Você esta prestes a apagar um ADMIN, você tem CERTEZA disso[SIM/NAO]? ').upper().strip()
                    # pergunta se ADMIN que esta fazendo a opeção tem certeza doque esta fazendo
                    
                    if ok == 'SIM':
                    # Se ele tem certeza acaba o laço e continua para deletar ADMIN
                        break
                    
                    else:
                    # Se ele não quer finaliza o metodo
                        return

                with open('AdmUser.txt', 'r') as log:
                    texto = log.readlines()
                with open('AdmUser.txt', 'w') as escreve:
                    for linha in texto:
                        if f'Usuario: {pesquisa}' in linha and f'Senha: {pesquisa_senha_admin}' in linha and f'Acesso: ADMIN' in linha:
                            escreve.write('')
                            print(f'ADMIN deletado!')
                            # Deleta o ADMIN
                        else:
                            escreve.write(linha)
                    return   

    def CriaVariosUser(self):
    # Cadastrar varios usuarios
        if self.admin_acesso:
            condicao = self.VerificaAdmin()
            
            if condicao:
                while True:
                # Aqui sera como no __init__ dessa classe, nada muito novo
                    while True:
                        Cria = input('Qual o nome do usuario que você deseja criar? [Escreva "Sair" para cancelar] ').strip()
                        achou = False
                        
                        if Cria.lower() == 'sair':
                            return
                        with open('AdmUser.txt', 'r') as log:
                            texto = log.readlines()
                        
                        for linha in texto:
                            if f'Usuario: {Cria}' in linha:
                                achou = True
                        
                        if achou:
                            print(f'Nome de usuario "{Cria}" já cadastrado. Tente outro...')
                        
                        else:
                            break
                    
                    while True:
                        verificar, senha = self.VerificaSenha()
                        
                        if not verificar:
                            break
                        
                        else:
                            print(', '.join(verificar),'.')
                    
                    with open('AdmUser.txt', 'a') as escreve:
                        escreve.writelines(f'Usuario: {Cria} | Senha: {senha} | Acesso: User \n')
                        # Cadastra o novo usuario
                        print(f'User {Cria} cadastrado')
                        # E certifica que usuario foi cadastrado
                        self.user_acesso = True
                        
    def CriaVariosAdmin(self):
    # Cadastra varios ADMIN'S
        if self.admin_acesso:
            condicao = self.VerificaAdmin()
            if condicao:
                while True:
                    while True:
                        Cria = input('Qual o nome do usuario que você deseja criar? [Escreva "Sair" para cancelar] ').strip()
                        achou = False
                        if Cria.lower() == 'sair':
                            return
                        with open('AdmUser.txt', 'r') as log:
                            texto = log.readlines()
                        for linha in texto:
                            if f'Usuario: {Cria}' in linha:
                                achou = True
                        if achou:
                            print(f'Nome de usuario "{Cria}" já cadastrado. Tente outro...')
                        else:
                            break
                    while True:
                        verifica, senha = self.VerificaSenha()
                        if not verifica:
                            break
                        else:
                            print(', '.join(verifica),'.')
                    with open('AdmUser.txt', 'a') as escreve:
                        
                        escreve.writelines(f'Usuario: {Cria} | Senha: {senha} | Acesso: ADMIN \n')
                        # Agora inves do acesso ser user, agora é ADMIN já que estamos cadastrando um ADMIN
                        print(f'ADMIN {Cria} cadastrado')
                        # Feedback que ADMIN foi cadastrado
                        
                        self.user_acesso = True
                        self.admin_acesso = True     
                           
    def TabelaUserAdmin(self):
    # Mostra o User e Acesso de todos cadastrados
         with open('AdmUser.txt', 'r') as log:
            for linha in log:
                print(f"{linha[:(linha.find('Senha:'))]}{linha[(linha.find('Acesso: ')):]}")
                # Aqui vai escrever ate achar 'Senha: ', quando achar para e so começa quando achar quando começa 'Acesso: '

    def TabelaUser(self):
    # Mostra somente o usuario e acesso dos Users comuns
         with open('AdmUser.txt', 'r') as log:
            for linha in log:
                if f'Acesso: User' in linha:
                    print(f"{linha[:(linha.find('Senha:'))]}{linha[(linha.find('Acesso: ')):]}")
                    
    def TabelaAdmin(self):
    # Faz a mesma coisa porém so com os ADMINS
         with open('AdmUser.txt', 'r') as log:
            for linha in log:
                if f'Acesso: ADMIN' in linha:
                    print(f"{linha[:(linha.find('Senha:'))]}{linha[(linha.find('Acesso: ')):]}")
                    
    def TabelaSecreta(self):
    # Essa tabela mostrar TUDO, usuario, senha e acesso
        condicao = self.VerificaAdmin()
        if condicao:
            with open('AdmUser.txt', 'r') as ler:
                self.leitura = ler.read()
            print(self.leitura)
            
    def DeletarLinha(self):
    # Esse metodo apaga a linha
        if self.admin_acesso:
            verifica = self.VerificaAdmin()
            
            if verifica:
                
                counter = 1 # Numero atual da linha
                with open('AdmUser.txt', 'r') as log:
                    texto = log.readlines()
                    
                    self.TabelaUserAdmin()
                    # Mostra a tabela "Normal" com todos os user e ADMIN'S
                    quantia = int(input('qual linha você deseja apagar? [Digite 0 para parar] '))
                    # pergunta qual linha o ADMIN quer apagar
                    
                    if quantia != 0:
                        with open('AdmUser.txt', 'w') as escreve:
                            for linha in texto:
                                if quantia == counter:
                                # Se a linha que o ADMIN apagar for o numero da linha 
                                    
                                    if f'Acesso: ADMIN' in linha:
                                        # Se na linha que for para ser apagar é de um ADMIN...
                                        certeza = input(f'A linha {counter} é a linha do ADMIN {linha[linha.find('Usuario: '):linha.find(' |')]}, você tem certeza que quer deletar essa linha? [SIM/NAO]')
                                        # Fala que a linha atual é de um admin e pergunta se mesmo assim ele quer apagar
                                        if certeza.upper() == 'SIM':
                                        # Se a resposta for sim...
                                            escreve.write('')
                                            print('Linha apagada!')
                                    
                                    else:
                                    # se não for de um ADMIN e sim de um usuario comum
                                        escreve.write('')
                                
                                else:
                                # Se a linha não for a que o ADMIN quer apagar
                                    escreve.write(linha)
                                counter += 1 # vai para a proxima linha então counter = counter + 1

class Menu:
# Classe para mostrar o menu
    def __init__(self, adm):
        if adm:
        # Se for um ADMIN que iniciou o programa
            while True:
                
                escolha = input('Deseja ver os comandos de ADMIN ou do USER [ADMIN/USER]? ').strip().upper()
                # Pergunta ele quer ver os comandos de ADMIN ou User padrão
                
                if escolha == 'ADMIN':
                    print(f'''
    {'ADM':^25}
    Escolha uma opção:
    9. Acesso ADM 
    10. Trocar de senha
    11. Trocar de nome
    12. Deletar usuario
    13. Deletar ADMIN
    14. Criar varios Usuarios
    15. Criar varios ADMIN's
    16. Tabela De User e Admin
    17. Tabela de User
    18. Tabela de Admin''')
                    break
                elif escolha == 'USER':
                    print(f'''{'USER':^25}
    Escolha uma opção:
    1. Adicionar aos contato
    2. Ler Contatos
    3. Pesquisar Contato
    4. Apagar Todos os Contatos (Kamikaze)
    5. Apagar contato
    6. BACKUP
    7. VER BACKUP
    8. Sair\n''')
                    break
                else:
                    print('Escolha invalida')
        else:
        # Se não for um ADMIN e sim um user

            print(f'''{'USER'^25}
            Escolha uma opção:
            1. Adicionar aos contato
            2. Ler Contatos
            3. Pesquisar Contato
            4. Apagar Todos os Contatos (Kamikaze)
            5. Apagar contato
            6. BACKUP
            7. VER BACKUP
            8. Sair\n''')