from re import search
# O codigo vai ser documentado ainda! Aguarde ate as proximas atualizações...
class Contatos:      
    def __init__(self, acesso, senha, user):
        acesso, senha, user = Segurança.Verifica()
        if acesso:
            self.bkp = False
            self.user_acesso = acesso
            self.senha = senha
            self.user = user
            self.contato = input('Escreva o nome do seu contato: ')
            self.numero = input('Escreva o numero do seu contato: ')
            with open('data.txt', 'a') as arquivo:
                arquivo.writelines(f'Contato: {self.contato} , Numero: {self.numero}')
                arquivo.write('\n')
    def Ler(self): 
        with open('data.txt', 'r') as arquivo: 
            lista = arquivo.read() 
            print(lista)
    def Kamikaze(self, adm):
        continua = True
        self.user_acesso = False
        self.admin_acesso = adm
        if self.admin_acesso == False:
            while self.user_acesso != True:
                user = input('Digite seu usuario: ').strip()
                tentativas = input('Digite a sua senha: [Escreva "Sair" para cancelar]: ').strip()
                if user != '':
                    if tentativas == self.senha and user == self.user:
                        self.user_acesso = True
                    else:
                        print('Ou usuario ou senha esta incorreta')
                        self.user_acesso = False
                else:
                    print('saindo...')
                    return
            while continua: 
                certeza = input('Você tem certeza que deseja apagar todos os contatos da sua lista de contatos? [SIM/NãO] ').upper().strip()
                if certeza in ['NÃO', 'NAO']:
                    continua = False
                elif certeza == 'SIM':
                    while continua:
                        certeza = input('Você tem a certeza ABSOLUTA que deseja apagar todos os seus contatos para SEMPRE??? [SIM/NãO] ').upper().strip()
                        if certeza in ['NÃO', 'NAO']:
                            continua = False
                        elif certeza == 'SIM':            
                            if self.bkp != True:
                                while continua:
                                    certeza = input('Você ainda não tem o backup feito! Você não é ADMIN então não pode apagar a lista sem um backup! Você deseja fazer o backup? [SIM/NÃO]' ).upper().strip()
                                    if certeza in ['NÃO', 'NAO']:
                                        continua = False
                                    elif certeza == 'SIM': 
                                        with open('data.txt', 'r') as arquivo:
                                            linhas = arquivo.readlines()
                                        with open('dataBKP.txt', 'w') as backup:
                                            for linha in linhas:
                                                backup.write(linha)
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
        else:
            if self.bkp != True:
                while continua:
                    certeza = input('Você deseja apagar todos os contatos da sua lista de contatos? [SIM/NãO] ').upper().strip()
                    if certeza in ['NÃO', 'NAO']:
                        continua = False
                    elif certeza == 'SIM':
                        while continua:
                            certeza = input('Você ainda não tem o backup feito! Mesmo assim você deseja apagar sua lista de contatos? [SIM/NÃO]' ).upper().strip()
                            if certeza in ['NÃO', 'NAO']:
                                continua = False
                            elif certeza == 'SIM': 
                                while continua:
                                    bkp = input('Deseja fazer o backup? [SIM/NÃO]').upper().strip()
                                    if bkp in ['NÃO', 'NAO']:
                                        with open('data.txt', 'w') as arquivo:
                                            arquivo.write('') 
                                        continua = False
                                    elif bkp == 'SIM':
                                        with open('data.txt', 'r') as arquivo:
                                            linhas = arquivo.readlines()
                                        with open('dataBKP.txt', 'w') as backup:
                                            for linha in linhas:
                                                backup.write(linha)
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
    def Pesquisa(self): 
        cade = input('Qual contato ou numero você deseja achar? ').strip()
        with open('data.txt', 'r') as arquivo:
            for linha in arquivo: 
                if cade in linha: 
                    print(linha) 
    def Deletar(self): 
        while self.user_acesso != True:
            user = input('Digite seu usuario: ').strip()
            tentativas = input('Digite a sua senha: [Escreva "Sair" para cancelar]: ').strip()
            if user != '':
                if tentativas == self.senha and user == self.user:
                    self.user_acesso = True
                else:
                    print('Ou usuario ou senha esta incorreta')
                    self.user_acesso = False
            else:
                print('saindo...')
                return
        objeto = input('Qual contato você deseja deletar? ')
        listas = [] 
        achou = False 
        with open('data.txt', 'r') as arquivo:
            listas = arquivo.readlines()
        with open('data.txt', 'w') as arquivo:
            for linha in listas: 
                if objeto not in linha.lower():
                    arquivo.write(linha)
                else:
                    achou = True
            if achou: 
                print('Contato deletado! ')
            else: 
                print('Contato não foi encontrado')    
    def Backup(self):
        while self.user_acesso != True:
            user = input('Digite seu usuario: ').strip()
            tentativas = input('Digite a sua senha: [Escreva "Sair" para cancelar]: ').strip()
            if user != '':
                if tentativas == self.senha and user == self.user:
                    self.user_acesso = True
                else:
                    print('Ou usuario ou senha esta incorreta')
                    self.user_acesso = False
            else:
                print('saindo...')
                return
        with open('data.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        with open('dataBKP.txt', 'w') as backup:
            for linha in linhas:
                backup.write(linha)
        self.bkp = True
        print('backup concluido')
    def SeeBackup(self):
        while self.user_acesso != True:
            user = input('Digite seu usuario: ').strip()
            tentativas = input('Digite a sua senha: [Escreva "Sair" para cancelar]: ').strip()
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
            with open('dataBKP.txt', 'r') as backup:
                print(backup.read())
        else:
          print('Faça o backup primeiramente!')
class Segurança:
    def __init__(self):
        self.user_acesso = self.admin_acesso = False
        self.Acesso = 'User'
        while True:
            definir = input('Você quer fazer [LOGIN/CADASTRO]? ').upper().strip()
            if definir == 'CADASTRO':
                while True:
                    while True:
                        achamos = False
                        self.user = input('Digite seu user: ').strip()
                        with open('AdmUser.txt', 'r') as log:
                            texto = log.readlines()
                        for linha in texto:
                            if f'Usuario: {self.user}' in linha:
                                achamos = True
                        if achamos:
                            print(f'Nome de usuario "{self.user}" já cadastrado. Tente outro...')
                        else:
                            break
                    while True:
                        verifica = self.VerificaSenha()
                        if verifica == True:
                            with open('AdmUser.txt', 'a') as cadastrar:
                                cadastrar.writelines(f'Usuario: {self.user} | Senha: {self.senha} | Acesso: {self.Acesso} \n')
                            self.user_acesso = True
                            return
                        else:
                            print(', '.join(verifica),'.')
            elif definir == 'LOGIN':
                while True:
                    with open('AdmUser.txt', 'r') as arquivo:
                        texto = arquivo.readlines()
                    user = input('Digite seu usuario: ').strip()
                    tentativas = input('Digite a sua senha: [Escreva "Sair" para cancelar]: ').strip()
                    if tentativas != 'Sair':
                        for linha in texto:
                            if f'Usuario: {user}' in linha and f'Senha: {tentativas}' in linha and tentativas != '':
                                self.user_acesso = True
                                self.senha = tentativas
                                self.user = user
                                if 'Acesso: ADMIN' in linha:
                                    self.admin_acesso = True
                                print('Usuario Logado com sucesso!')
                                return
                        if not self.user_acesso:
                            print('Usuario ou senha incorreta!')
                    else:
                        print('saindo...')
                        self.user_acesso = self.senha = self.user = False
                        return
            else:
                print('Tente novamente!')
    def VerificaSenha(self):
        erro = []
        senha = input('Digite a senha desse usuario: ').strip()
        confirma = input('Digite novamente a senha: ').strip()
        if confirma != senha:
            erro.append('As senhas devem ser iguais')
        if len(senha) < 8:
            erro.append('A senha deve ter pelo menos 8 caracteres')
        if not search(r'\d', senha):
            erro.append('A senha deve ter ao menos 1 digito')
        if not search(r'[A-Z]', senha):
            erro.append('A senha deve ter ao menos uma letra maiuscula')
        if not search(r'[a-z]', senha):
            erro.append('A senha deve ter ao menos uma letra minuscula')
        if not erro:
            return erro, senha
        else:
            print(', '.join(erro),'.')
            return erro, senha
    def VerificaAdmin(self):
        while True:
            usuario = input('Digite seu usuario (ADMIM): ').strip()
            senha = input('Digite a sua senha: [Escreva "Sair" para cancelar]: ').strip()
            if senha.lower() != 'sair':
                with open('AdmUser.txt', 'r') as log:
                    for linha in log:
                        if f'Usuario: {usuario}' in linha and f'Senha: {senha}' in linha and f'Acesso: ADMIN' in linha:
                            return True
            else:
                return False
            print('Usuario ou senha invalida')
    def Verifica(self):
        if self.user_acesso:
            return self.user_acesso, self.senha, self.user
        else:
            return False, self.senha, self.user     
    def Adm(self):
        return self.admin_acesso
    def AcessoAdm(self):
        if self.admin_acesso:
            verifica = self.VerificaAdmin
            if verifica:
                while True:
                    definir = input('Você deseja pesquisar um usuario em especifico ou todos [UNICO/TODOS] digite " " para parar? ').upper().strip()
                    while True:
                        if definir == 'UNICO':
                            user = input('Qual usuario você deseja deixa como ADMIN? ').strip()
                            with open('AdmUser.txt', 'r') as leitura:
                                texto = leitura.readlines()
                            with open('AdmUser.txt', 'w') as escreve:
                                for linha in texto:
                                    fatiado = linha.split()
                                    if f'Usuario: {user}' in linha and f'Acesso: User' in linha:
                                        escreve.write(f'Usuario: {user} | Senha: {fatiado[4]} | Acesso: ADMIN \n')
                                        print(f'Usuario: {user} agora é ADMIN!')
                                    else:
                                        escreve.write(f'Usuario: {fatiado[1]} | Senha: {fatiado[4]} | Acesso: {fatiado[7]} \n')
                                break
                        elif definir == 'TODOS':
                            with open('AdmUser.txt', 'r') as leitura:
                                texto = leitura.readlines()
                            for linha in texto:
                                print(f"{linha[:(linha.find('Senha:'))]}{linha[(linha.find('Acesso: ')):]}")
                            break
                        elif definir == '':
                            return
            else:
                print('Usuario ou senha esta incorreta!')
    def TrocaNome(self):
        if self.admin_acesso:
            while True:
                usuario = input('Digite seu usuario (ADMIM): ').strip()
                senha = input('Digite a sua senha: [Escreva "Sair" para cancelar]: ').strip()
                if senha.lower() != 'sair':
                    with open('AdmUser.txt', 'r') as log:
                        for linha in log:
                            if f'Usuario: {usuario}' in linha and f'Senha: {senha}' in linha and f'Acesso: ADMIN' in linha:
                                while True:
                                    pesquisa = input('Qual o nome do usuario que você deseja trocar de nome? ').strip()
                                    troca = input('Qual vai ser o novo nome? ').strip()
                                    if pesquisa == '':
                                        return
                                    with open('AdmUser.txt', 'r') as leitura:
                                        texto = leitura.readlines()
                                    with open('AdmUser.txt', 'w') as escreve:
                                        for linha in texto:
                                            fatiado = linha.split()
                                            if f'Usuario: {pesquisa}' in linha:
                                                escreve.write(f'Usuario: {troca} | Senha: {fatiado[4]} | Acesso: {fatiado[7]} \n')
                                                print(f'Nome trocado!')
                                            else:
                                                escreve.write(f'Usuario: {fatiado[1]} | Senha: {fatiado[4]} | Acesso: {fatiado[7]} \n')
                                        return
                else:
                    break    
    def TrocaSenha(self):
        if self.admin_acesso:
            while True:
                usuario = input('Digite seu usuario (ADMIM): ').strip()
                senha = input('Digite a sua senha: [Escreva "Sair" para cancelar]: ').strip()
                if senha.lower() != 'sair':
                    with open('AdmUser.txt', 'r') as log:
                        for linha in log:
                            if f'Usuario: {usuario}' in linha and f'Senha: {senha}' in linha and f'Acesso: ADMIN' in linha:
                                while True:
                                    User = Password = False
                                    user = input('Qual o nome do usuario que você deseja trocar de senha? ').strip()
                                    password = input('Qual é a senha dele atual? ').strip()
                                    if user == '' or password == '':
                                        return
                                    with open('AdmUser.txt', 'r') as log2:
                                        for linha2 in log2:
                                            if f'Usuario: {user}' in linha2:
                                                User = True
                                            if f'Senha: {password}' in linha2:
                                                Password = True
                                            if Password == False or User == False:
                                                print('Usuario ou senha invalido! Tente novamente.')
                                    while User and Password:
                                        verificar, senha = self.VerificaSenha()
                                        if not verificar:
                                            break
                                        else:
                                            print(', '.join(verificar),'.')
                                    with open('AdmUser.txt', 'r') as log:
                                        texto = log.readlines()
                                    with open('AdmUser.txt', 'w') as escreve:
                                        for linha in texto:
                                            fatiado = linha.split()
                                            if f'Usuario: {user}' in linha and f'Senha: {password}' in linha:
                                                escreve.write(f'Usuario: {user} | Senha: {senha} | Acesso: {fatiado[7]} \n')
                                                print(f'Senha trocada!')
                                            else:
                                                escreve.write(f'Usuario: {fatiado[1]} | Senha: {fatiado[4]} | Acesso: {fatiado[7]} \n')
                                        return
                else:
                    return                     
    def DeletaUser(self):
        if self.admin_acesso:
            while True:
                usuario = input('Digite seu usuario (ADMIM): ').strip()
                senha = input('Digite a sua senha: [Escreva "Sair" para cancelar]: ').strip()
                if senha.lower() != 'sair':
                    with open('AdmUser.txt', 'r') as log:
                        for login in log:
                            if f'Usuario: {usuario}' in login and f'Senha: {senha}' in login and f'Acesso: ADMIN' in login:
                                while True:
                                    pesquisa = input('Qual o usuario que você deseja deletar? ').strip()
                                    with open('AdmUser.txt', 'r') as log:
                                        texto = log.readlines()
                                    with open('AdmUser.txt', 'w') as escreve:
                                        for linha in texto:
                                            fatiado = linha.split()
                                            if f'Usuario: {pesquisa}' in linha and f'Acesso: User' in linha:
                                                escreve.write('')
                                                print(f'Usuario deletado!')
                                            else:
                                                escreve.write(f'Usuario: {fatiado[1]} | Senha: {fatiado[4]} | Acesso: {fatiado[7]} \n')
                                        return
                else:
                    break     
    def DeletaAdm(self):
        if self.admin_acesso:
            while True:
                usuario = input('Digite seu usuario (ADMIM): ').strip()
                senha = input('Digite a sua senha: [Escreva "Sair" para cancelar]: ').strip()
                if senha.lower() != 'sair':
                    with open('AdmUser.txt', 'r') as log:
                        for linha in log:
                            if f'Usuario: {usuario}' in linha and f'Senha: {senha}' in linha and f'Acesso: ADMIN' in linha:
                                while True:
                                    pesquisa = input('Qual o ADMIN que você deseja deletar? ').strip()
                                    pesquisa_senha_admin = input('Qual a senha desse ADMIN?').strip()
                                    while True:
                                        ok = input('Você esta prestes a apagar um ADMIN, você tem CERTEZA disso[SIM/NAO]?').upper().strip()
                                        if ok == 'SIM':
                                            break
                                        else:
                                            return
                                    with open('AdmUser.txt', 'r') as log:
                                        texto = log.readlines()
                                    with open('AdmUser.txt', 'w') as escreve:
                                        for linha in texto:
                                            fatiado = linha.split()
                                            if f'Usuario: {pesquisa}' in linha and f'Senha: {pesquisa_senha_admin}' in linha and f'Acesso: ADMIN' in linha:
                                                escreve.write('')
                                                print(f'Usuario deletado!')
                                            else:
                                                escreve.write(f'Usuario: {fatiado[1]} | Senha: {fatiado[4]} | Acesso: {fatiado[7]} \n')
                                        return
                else:
                    break    
    def CriaVariosUser(self):
        if self.admin_acesso:
            condicao = self.VerificaAdmin()
            while condicao:
                while True:
                    Cria = input('Qual o nome do usuario que você deseja criar? [Escreva "Sair" para cancelar] ').strip()
                    achou = False
                    if Cria != 'Sair':
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
                    self.user_acesso = True
    def CriaVariosAdmin(self):
        if self.admin_acesso:
            condicao = self.VerificaAdmin()
            while condicao:
                Cria = input('Qual o nome do usuario que você deseja criar? [Escreva "Sair" para cancelar] ').strip()
                achou = False
                if Cria != 'Sair':
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
                self.user_acesso = True
                self.admin_acesso = True        
    def TabelaUserAdmin(self):
         with open('AdmUser.txt', 'r') as log:
            for linha in log:
                print(f"{linha[:(linha.find('Senha:'))]}{linha[(linha.find('Acesso: ')):]}")
    def TabelaUser(self):
         with open('AdmUser.txt', 'r') as log:
            for linha in log:
                if f'Acesso: User' in linha:
                    print(f"{linha[:(linha.find('Senha:'))]}{linha[(linha.find('Acesso: ')):]}")
    def TabelaAdmin(self):
         with open('AdmUser.txt', 'r') as log:
            for linha in log:
                if f'Acesso: ADMIN' in linha:
                    print(f"{linha[:(linha.find('Senha:'))]}{linha[(linha.find('Acesso: ')):]}")
    def TabelaSecreta(self):
        condicao = self.VerificaAdmin()
        if condicao:
            with open('AdmUser.txt', 'r') as ler:
                self.leitura = ler.read()
            print(self.leitura)
class Menu:
    def __init__(self, adm):
        if adm:
            escolha = input('Deseja ver os comandos de ADMIN ou do USER [ADMIN/USER]? ').strip().upper()
            if escolha == 'ADMIN':
                print(f'''
    {'ADM':^25}
    Escolha uma opção:
    123321. Acesso ADM 
    11. Trocar de senha
    22. Trocar de nome
    33. Deletar usuario
    44. Deletar ADMIN
    55. Criar varios Usuarios
    66. Criar varios ADMIN's
    77. Tabela De User e Admin
    88. Tabela de User
    99. Tabela de Admin''')
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
        else:
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
