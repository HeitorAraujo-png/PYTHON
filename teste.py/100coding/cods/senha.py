from re import search
def verifica_senha(senha):
    erro = []
    if len(senha) < 8:
        erro.append('A senha deve pelo menos 8 digitos.')
    if not search(r'[A-Z]', senha):
        erro.append('A senha deve ter pelo menos um caracter maiusculo.')
    if not search(r'[a-z]', senha):
        erro.append('A senha deve ter pelo menos um caracter minusculo.')
    if not search(r'\d', senha):
        erro.append('A senha deve ter no minimo um numero.')
    if not erro:
        return True, 'Senha forte! Atende a todos os requisitos'
    else:
        return False, '\n'.join(erro)
if __name__ == '__main__':
    while True:
        senha_digitada = input('Digite sua senha: ')
        valida, mensagem = verifica_senha(senha_digitada)
        print(mensagem)
        if valida:
            break
        else:
            print('Tente novamente: \n')