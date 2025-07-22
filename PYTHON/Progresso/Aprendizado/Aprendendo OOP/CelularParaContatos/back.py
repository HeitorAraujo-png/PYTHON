from re import search
import hashlib as hl


# O codigo vai ser documentado ainda! Aguarde ate as proximas atualizações...
class Contatos:
    def __init__(self, acesso, senha, user):
        if acesso:
            self.bkp = False
            self.user_acesso = acesso
            self.senha = senha
            self.user = user
            self.contato = input("Escreva o nome do seu contato: ")
            self.numero = input("Escreva o numero do seu contato: ")
            with open("data.txt", "a") as arquivo:
                arquivo.write(f"Contato: {self.contato} , Numero: {self.numero}")
                arquivo.write("\n")

    def Ler(self):
        with open("data.txt", "r") as arquivo:
            lista = arquivo.read()
            print(lista)

    def Kamikaze(self, adm):
        continua = True
        self.user_acesso = False
        self.admin_acesso = adm
        if not self.admin_acesso:
            while self.user_acesso != True:
                user = input("Digite seu usuario: ").strip()
                tentativas = input(
                    'Digite a sua senha: [Escreva "Sair" para cancelar]: '
                ).strip()
                if tentativas.lower() == "sair":
                    return
                else:
                    if tentativas == self.senha and user == self.user:
                        self.user_acesso = True
                    else:
                        print("Ou usuario ou senha esta incorreta")
                        self.user_acesso = False
            while continua:
                certeza = (
                    input(
                        "Você tem certeza que deseja apagar todos os contatos da sua lista de contatos? [SIM/NãO] "
                    )
                    .upper()
                    .strip()
                )
                if certeza == "SIM":
                    while continua:
                        certeza = (
                            input(
                                "Você tem a certeza ABSOLUTA que deseja apagar todos os seus contatos para SEMPRE??? [SIM/NãO] "
                            )
                            .upper()
                            .strip()
                        )
                        if certeza == "SIM":
                            if self.bkp != True:
                                while continua:
                                    certeza = (
                                        input(
                                            "Você ainda não tem o backup feito! Você não é ADMIN então não pode apagar a lista sem um backup! Você deseja fazer o backup? [SIM/NÃO]"
                                        )
                                        .upper()
                                        .strip()
                                    )
                                    if certeza == "SIM":
                                        self.Backup()
                                        print("backup concluido")
                                        with open("data.txt", "w") as arquivo:
                                            arquivo.write("")
                                        continua = False
                                        print("Contatos apagados")
                                    elif certeza in ["NÃO", "NAO"]:
                                        continua = False
                                    else:
                                        print("Seleção invalida! Tente novamente.")
                            else:
                                with open("data.txt", "w") as arquivo:
                                    arquivo.write("")
                                continua = False
                        elif certeza in ["NÃO", "NAO"]:
                            continua = False
                        else:
                            print("Seleção invalida! Tente novamente.")
                elif certeza in ["NÃO", "NAO"]:
                    continua = False
                else:
                    print("Seleção invalida! Tente novamente.")
        else:
            if self.bkp != True:
                while continua:
                    certeza = (
                        input(
                            "Você deseja apagar todos os contatos da sua lista de contatos? [SIM/NãO] "
                        )
                        .upper()
                        .strip()
                    )
                    if certeza == "SIM":
                        while continua:
                            certeza = (
                                input(
                                    "Você ainda não tem o backup feito! Mesmo assim você deseja apagar sua lista de contatos? [SIM/NÃO]"
                                )
                                .upper()
                                .strip()
                            )
                            if certeza == "SIM":
                                while continua:
                                    bkp = (
                                        input("Deseja fazer o backup? [SIM/NÃO]")
                                        .upper()
                                        .strip()
                                    )
                                    if bkp in ["NÃO", "NAO"]:
                                        with open("data.txt", "w") as arquivo:
                                            arquivo.write("")
                                        continua = False
                                    elif bkp == "SIM":
                                        self.Backup
                                        self.bkp = True
                                        print("backup concluido")
                                        with open("data.txt", "w") as arquivo:
                                            arquivo.write("")
                                        continua = False
                                        print("Contatos apagados")
                            elif certeza in ["NÃO", "NAO"]:
                                continua = False
                    elif certeza in ["NÃO", "NAO"]:
                        continua = False
            else:
                with open("data.txt", "w") as arquivo:
                    arquivo.write("")
                continua = False

    def Pesquisa(self):
        cade = input("Qual contato ou numero você deseja achar? ").strip()
        with open("data.txt", "r") as arquivo:
            for linha in arquivo:
                if cade in linha:
                    print(linha)

    def Deletar(self):
        while self.user_acesso != True:
            user = input("Digite seu usuario: ").strip()
            tentativas = input(
                'Digite a sua senha: [Escreva "Sair" para cancelar]: '
            ).strip()
            if user != "":
                if tentativas == self.senha and user == self.user:
                    self.user_acesso = True
                else:
                    print("Ou usuario ou senha esta incorreta")
                    self.user_acesso = False
            else:
                print("saindo...")
                return
        objeto = input("Qual contato você deseja deletar? ")
        listas = []
        achou = False
        with open("data.txt", "r") as arquivo:
            listas = arquivo.readlines()
        with open("data.txt", "w") as arquivo:
            for linha in listas:
                if objeto not in linha.lower():
                    arquivo.write(linha)
                else:
                    achou = True
            if achou:
                print("Contato deletado! ")
            else:
                print("Contato não foi encontrado")

    def Backup(self):
        while self.user_acesso != True:
            user = input("Digite seu usuario: ").strip()
            tentativas = input(
                'Digite a sua senha: [Escreva "Sair" para cancelar]: '
            ).strip()
            if user != "":
                if tentativas == self.senha and user == self.user:
                    self.user_acesso = True
                else:
                    print("Ou usuario ou senha esta incorreta")
                    self.user_acesso = False
            else:
                print("saindo...")
                return
        with open("data.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        with open("dataBKP.txt", "w") as backup:
            for linha in linhas:
                backup.write(linha)
        self.bkp = True
        print("backup concluido")

    def SeeBackup(self):
        while self.user_acesso != True:
            user = input("Digite seu usuario: ").strip()
            tentativas = input(
                'Digite a sua senha: [Escreva "Sair" para cancelar]: '
            ).strip()
            if user != "":
                if tentativas == self.senha and user == self.user:
                    self.user_acesso = True
                else:
                    print("Ou usuario ou senha esta incorreta")
                    self.user_acesso = False
            else:
                print("saindo...")
                return
        if self.bkp == True:
            with open("dataBKP.txt", "r") as backup:
                print(backup.read())
        else:
            print("Faça o backup primeiramente!")


class Segurança:
    def __init__(self):
        self.user_acesso = self.admin_acesso = False
        self.Acesso = "User"
        while True:
            definir = input("Você quer fazer [LOGIN/CADASTRO]? ").upper().strip()
            if definir == "CADASTRO":
                while True:
                    self.user = self.CriaUser()
                    while True:
                        verifica, senha = self.VerificaSenha()
                        if not verifica:
                            self.senha = senha
                            with open("AdmUser.txt", "a") as nmrl:
                                with open("AdmUserHash.txt", "a") as cadastrar:
                                    nmrl.writelines(
                                        f"UsuarioHash: {self.user} | SenhaHash: {self.Hash(senha)} | Acesso: User \n"
                                    )
                                    cadastrar.writelines(
                                        f'{self.Hash(f"UsuarioHash: {self.Hash(self.user)} | SenhaHash: {self.Hash(self.senha)} | Acesso: User")} \n'
                                    )
                                self.user_acesso = True
                                self.admin_acesso = False
                                return
                        else:
                            print(", ".join(verifica), ".")
            elif definir == "LOGIN":
                while True:
                    with open("AdmUserHash.txt", "r") as arquivo:
                        texto = arquivo.readlines()
                    user = input("Digite seu usuario: ").strip()
                    tentativas = input(
                        'Digite a sua senha: [Escreva "Sair" para cancelar]: '
                    ).strip()
                    if tentativas.lower() != "sair":
                        for linha in texto:
                            if (
                                self.Hash(
                                    f"UsuarioHash: {self.Hash(user)} | SenhaHash: {self.Hash(tentativas)} | Acesso: User"
                                )
                                in linha
                            ):
                                self.user_acesso = True
                                self.senha = tentativas
                                self.user = user
                                print("Usuario Logado com sucesso!")
                                return
                            if (
                                self.Hash(
                                    f"UsuarioHash: {self.Hash(user)} | SenhaHash: {self.Hash(tentativas)} | Acesso: ADMIN"
                                )
                                in linha
                            ):
                                self.user_acesso = True
                                self.senha = tentativas
                                self.user = user
                                self.admin_acesso = True
                                print("ADMIN Logado com sucesso!")
                                return
                        if not self.user_acesso:
                            print("Usuario ou senha incorreta!")
                    else:
                        print("saindo...")
                        self.user_acesso = self.senha = self.user = (
                            self.admin_acesso
                        ) = False
                        return
            else:
                print("Tente novamente!")

    def CriaUser(self):
        while True:
            achamos = False
            self.user = input("Digite seu user: ").strip()
            user = self.Hash(self.user)
            with open("AdmUserHash.txt", "r") as log:
                for linha in log.readlines():
                    if f"UsuarioHash: {user}" in linha:
                        achamos = True
                if achamos:
                    print(
                        f'Nome de usuario "{self.user}" já cadastrado. Tente outro...'
                    )
                if self.user == "":
                    print("Usuario invalido!")
                else:
                    return self.user

    def Hash(self, hashble):
        hash = hl.sha256(hashble.encode()).hexdigest()
        return hash

    def VerificaSenha(self):
        erro = []
        senha = input("Digite a senha desse usuario: ").strip()
        confirma = input("Digite novamente a senha: ").strip()
        if confirma != senha:
            erro.append("As senhas devem ser iguais")
        if len(senha) < 8:
            erro.append("A senha deve ter pelo menos 8 caracteres")
        if not search(r"\d", senha):
            erro.append("A senha deve ter ao menos 1 digito")
        if not search(r"[A-Z]", senha):
            erro.append("A senha deve ter ao menos uma letra maiuscula")
        if not search(r"[a-z]", senha):
            erro.append("A senha deve ter ao menos uma letra minuscula")
        if not erro:
            return erro, senha
        else:
            return erro, senha

    def VerificaAdmin(self):
        while True:
            usuario = input("Digite seu usuario (ADMIM): ").strip()
            senha = input(
                'Digite a sua senha: [Escreva "Sair" para cancelar]: '
            ).strip()
            if senha.lower() != "sair":
                with open("AdmUserHash.txt", "r") as log:
                    for linha in log.readlines():
                        if self.Hash(
                            f"UsuarioHash: {self.Hash(usuario)} | SenhaHash: {self.Hash(senha)} | Acesso: ADMIN"
                            in linha
                        ):
                            return True
            else:
                return False
            print("Usuario ou senha invalida")

    def Verifica(self):
        if self.user_acesso:
            return self.user_acesso, self.senha, self.user, self.admin_acesso
        else:
            return self.user_acesso, self.senha, self.user, self.admin_acesso

    def AcessoAdm(self):
        if self.admin_acesso:
            verifica = self.VerificaAdmin()
            if verifica:
                while True:
                    user = input(
                        'Qual usuario você deseja deixa como ADMIN? [Digite "Sair" para parar] '
                    ).strip()
                    senha = input("Qual a senha desse usuario? ")
                    if user.lower() != "sair":
                        with open("AdmUserHash.txt", "r") as leitura:
                            with open("AdmUserHash.txt", "w") as escreve:
                                with open("AdmUser.txt", "w") as nmrl:
                                    for linha in leitura.readlines():
                                        if (
                                            self.Hash(
                                                f"UsuarioHash: {self.Hash(user)} | SenhaHash: {self.Hash(senha)} | Acesso: User"
                                            )
                                            in linha
                                        ):
                                            escreve.write(
                                                f'{self.Hash(f"UsuarioHash: {self.Hash(user)} | SenhaHash: {self.Hash(senha)} | Acesso: ADMIN")} \n'
                                            )
                                            nmrl.write(
                                                f"UsuarioHash: {self.Hash(user)} | SenhaHash: {self.Hash(senha)} | Acesso: ADMIN"
                                            )
                                            print(f"Usuario: {user} agora é ADMIN!")
                                        else:
                                            escreve.write(linha)
                                    for i in nmrl.readlines():
                                        if f"UsuariosHash: {user}" in linha:
                                            nmrl.write(
                                                f"UsuarioHash: {(user)} | SenhaHash: {self.Hash(senha)} | Acesso: ADMIN \n"
                                            )
                                        else:
                                            nmrl.write(i)
                                    break
                    elif user.lower() == "sair":
                        break

    def TrocaNome(self):
        if self.admin_acesso:
            verifica = self.VerificaAdmin()
            if verifica:
                while True:
                    pesquisa = input(
                        "Qual o nome do usuario que você deseja trocar de nome? "
                    ).strip()
                    troca = input("Qual vai ser o novo nome? ").strip()
                    senha = input("Qual a senha desse usuario? ")
                    if troca == "sair" or senha == "sair":
                        return
                    if troca == "":
                        return
                    with open("AdmUserHash.txt", "r") as leitura:
                        with open("Admuser.txt", "w") as nmrl:
                            with open("AdmUserHash.txt", "w") as escreve:
                                for linha in leitura.readlines():
                                    if (
                                        self.Hash(
                                            f"UsuarioHash: {self.Hash(pesquisa)} | SenhaHash: {self.Hash(senha)} | Acesso: User"
                                        )
                                        in linha
                                    ):
                                        escreve.write(
                                            f'{self.Hash(f"UsuarioHash: {self.Hash(troca)} | SenhaHash: {self.Hash(senha)} | Acesso: User")} \n'
                                        )
                                        print(f"Nome trocado!")
                                    else:
                                        escreve.write(linha)
                                for i in nmrl.readlines():
                                    if f"UsuariosHash: {pesquisa}" in linha:
                                        nmrl.write(
                                            f"UsuarioHash: {troca} | SenhaHash: {self.Hash(senha)} | Acesso: ADMIN \n"
                                        )
                                    else:
                                        nmrl.write(i)
                                break

    def TrocaSenha(self):
        if self.admin_acesso:
            verifica = self.VerificaAdmin()
            if verifica:
                while True:
                    user = input(
                        "Qual o nome do usuario que você deseja trocar de senha? "
                    ).strip()
                    password = input("Qual é a senha dele atual? ")
                    if user == "" or password == "" or password == "sair":
                        return
                    while True:
                        verificar, senha = self.VerificaSenha()
                        if not verificar:
                            break
                        else:
                            print(", ".join(verificar), ".")
                    with open("AdmUser.txt", "w") as log:
                        with open("AdmUserHash.txt", "w") as escreve:
                            for linha in log.readlines():
                                if (
                                    self.Hash(
                                        f"UsuarioHash: {self.Hash(user)} | SenhaHash: {self.Hash(password)} | Acesso: User"
                                    )
                                    in linha
                                ):
                                    escreve.write(
                                        f'{self.Hash(f"UsuarioHash: {self.Hash(user)} | SenhaHash: {self.Hash(senha)} | Acesso: User")} \n'
                                    )
                                    print(f"Senha trocada!")
                                else:
                                    escreve.write(linha)
                            for i in log.readlines():
                                if (
                                    f"UsuariosHash: {user}" in linha
                                    and f"SenhaHash: {self.Hash(password)}" in linha
                                    and f"Acesso: User" in linha
                                ):
                                    log.write(
                                        f"UsuarioHash: {(user)} | SenhaHash: {self.Hash(senha)} | Acesso: user \n"
                                    )
                                else:
                                    log.write(i)
                            return

    def DeletaUser(self):
        if self.admin_acesso:
            condicao = self.VerificaAdmin()
            if condicao:
                pesquisa = input("Qual o usuario que você deseja deletar? ").strip()
                senha = input("Qual a senha desse usuario? ")
                with open("AdmUser.txt", "w") as log:
                    with open("AdmUserHash.txt", "w") as escreve:
                        for linha in log.readlines():
                            if (
                                self.Hash(
                                    f"UsuarioHash: {self.Hash(pesquisa)} | SenhaHash: {self.Hash(senha)} | Acesso: User"
                                )
                                in linha
                            ):
                                escreve.write("")
                                print(f"Usuario deletado!")
                            else:
                                escreve.write(linha)
                        for i in log.readlines():
                            if (
                                f"Usuarioshash: {pesquisa}" in linha
                                and f"SenhaHash: {self.Hash(senha)}" in linha
                                and not f"Acesso: ADMIN" in linha
                            ):
                                log.write("")
                            else:
                                log.write(i)
                        return

    def DeletaAdm(self):
        if self.admin_acesso:
            condicao = self.VerificaAdmin()
            while condicao:
                pesquisa = input("Qual o ADMIN que você deseja deletar? ").strip()
                pesquisa_senha_admin = input("Qual a senha desse ADMIN?").strip()
                while True:
                    ok = (
                        input(
                            "Você esta prestes a apagar um ADMIN, você tem CERTEZA disso[SIM/NAO]? "
                        )
                        .upper()
                        .strip()
                    )
                    if ok == "SIM":
                        break
                    else:
                        pass
                with open("AdmUser.txt", "w") as log:
                    with open("AdmUserHash.txt", "w") as escreve:
                        for linha in escreve.readlines():
                            if (
                                self.Hash(
                                    f"UsuarioHash: {self.Hash(pesquisa)} | SenhaHash: {self.Hash(pesquisa_senha_admin)} | Acesso: ADMIN"
                                )
                                in linha
                            ):
                                escreve.write("")
                                print(f"Usuario deletado!")
                            else:
                                escreve.write(linha)
                        for i in log.readlines():
                            if (
                                f"Usuarioshash: {pesquisa}" in linha
                                and f"SenhaHash: {self.Hash(pesquisa_senha_admin)}"
                                in linha
                                and f"Acesso: ADMIN" in linha
                            ):
                                log.write("")
                            else:
                                log.write(i)
                        return

    def CriaVariosUser(self):
        if self.admin_acesso:
            condicao = self.VerificaAdmin()
            if condicao:
                while True:
                    while True:
                        Cria = input(
                            'Qual o nome do usuario que você deseja criar? [Escreva "Sair" para cancelar] '
                        ).strip()
                        achou = False
                        if Cria.lower() == "sair":
                            return
                        with open("AdmUser.txt", "r") as log:
                            for linha in log.readlines():
                                if f"Usuario: {Cria}" in linha:
                                    achou = True
                            if achou:
                                print(
                                    f'Nome de usuario "{Cria}" já cadastrado. Tente outro...'
                                )
                            else:
                                break
                        while True:
                            verificar, senha = self.VerificaSenha()
                            if not verificar:
                                break
                            else:
                                print(", ".join(verificar), ".")
                        with open("AdmUser.txt", "a") as crv:
                            with open("AdmUserHash.txt", "a") as escreve:
                                escreve.writelines(
                                    f'{self.Hash(f"UsuarioHash: {self.Hash(Cria)} | SenhaHash: {self.Hash(senha)} | Acesso: User")} \n'
                                )
                                print(f"User {Cria} cadastrado")
                                self.user_acesso = True
                                crv.write(
                                    f"UsuarioHash: {(Cria)} | SenhaHash: {self.Hash(senha)} | Acesso: User \n"
                                )

    def CriaVariosAdmin(self):
        if self.admin_acesso:
            condicao = self.VerificaAdmin()
            if condicao:
                while True:
                    while True:
                        Cria = input(
                            'Qual o nome do usuario que você deseja criar? [Escreva "Sair" para cancelar] '
                        ).strip()
                        achou = False
                        if Cria.lower() == "sair":
                            return
                        with open("AdmUser.txt", "r") as log:
                            for linha in log.readlines():
                                if f"Usuario: {Cria}" in linha:
                                    achou = True
                            if achou:
                                print(
                                    f'Nome de usuario "{Cria}" já cadastrado. Tente outro...'
                                )
                            else:
                                break
                    while True:
                        verifica, senha = self.VerificaSenha()
                        if not verifica:
                            break
                        else:
                            print(", ".join(verifica), ".")
                    with open("AdmUser.txt", "a") as escreve:
                        with open("AdmUserHash.txt", "a") as texto:
                            escreve.writelines(
                                f"UsuarioHash: {(Cria)} | SenhaHash: {self.Hash(senha)} | Acesso: ADMIN"
                            )
                            texto.write(
                                f"{self.Hash(f'UsuarioHash: {self.Hash(Cria)} | SenhaHash: {self.Hash(senha)} | Acesso: ADMIN')} \n"
                            )
                            print(f"ADMIN {Cria} cadastrado")
                            self.user_acesso = True
                            self.admin_acesso = True

    def TabelaUserAdmin(self):
        with open("AdmUser.txt", "r") as log:
            for linha in log:
                print(
                    f"{linha[:(linha.find('SenhaHash:'))]}{linha[(linha.find('Acesso: ')):]}"
                )

    def TabelaUser(self):
        with open("AdmUser.txt", "r") as log:
            for linha in log:
                if f"Acesso: User" in linha:
                    print(
                        f"{linha[:(linha.find('SenhaHash:'))]}{linha[(linha.find('Acesso: ')):]}"
                    )

    def TabelaAdmin(self):
        with open("AdmUser.txt", "r") as log:
            for linha in log:
                if f"Acesso: ADMIN" in linha:
                    print(
                        f"{linha[:(linha.find('SenhaHash:'))]}{linha[(linha.find('Acesso: ')):]}"
                    )

    def TabelaSecreta(self):
        condicao = self.VerificaAdmin()
        if condicao:
            with open("AdmUser.txt", "r") as ler:
                self.leitura = ler.read()
            print(self.leitura)

    def DeletarLinha(self):
        if self.admin_acesso:
            verifica = self.VerificaAdmin()
            if verifica:
                counter = 1
                with open("AdmUser.txt", "r") as log:
                    texto = log.readlines()
                    quantia = int(
                        input("qual linha você deseja apagar? [Digite 0 para parar] ")
                    )
                    self.TabelaUserAdmin
                    if quantia != 0:
                        with open("AdmUser.txt", "w") as escreve:
                            with open("AdmUserHash.txt", "w") as txt:
                                for linha in texto:
                                    if quantia == counter:
                                        escreve.write("")
                                        print("Linha apagada!")
                                    else:
                                        escreve.write(linha)
                                    counter += 1
                                counter = 1
                                for i in txt:
                                    if quantia == counter:
                                        txt.write("")
                                        print("Linha apagada!")
                                    else:
                                        txt.write(i)
                                    counter += 1


class Menu:
    def __init__(self, adm):
        if adm:
            while True:
                escolha = (
                    input("Deseja ver os comandos de ADMIN ou do USER [ADMIN/USER]? ")
                    .strip()
                    .upper()
                )
                if escolha == "ADMIN":
                    print(
                        f"""
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
    18. Tabela de Admin"""
                    )
                    break
                elif escolha == "USER":
                    print(
                        f"""{'USER':^25}
    Escolha uma opção:
    1. Adicionar aos contato
    2. Ler Contatos
    3. Pesquisar Contato
    4. Apagar Todos os Contatos (Kamikaze)
    5. Apagar contato
    6. BACKUP
    7. VER BACKUP
    8. Sair\n"""
                    )
                    break
                else:
                    print("Escolha invalida")
        else:
            print(
                f"""{'USER':^25}
            Escolha uma opção:
            1. Adicionar aos contato
            2. Ler Contatos
            3. Pesquisar Contato
            4. Apagar Todos os Contatos (Kamikaze)
            5. Apagar contato
            6. BACKUP
            7. VER BACKUP
            8. Sair\n"""
            )