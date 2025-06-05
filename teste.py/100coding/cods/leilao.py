valor = 0
nome = ''
segredos = {'Valor': valor, 'Nome': nome}
acabou = True
while acabou:
    nome = str(input('Digite é seu nome: \n'))
    lance = int(input('Qual é o valor do seu lance? \nR$'))
    if valor < lance:
        valor = lance
        segredos['Nome'] = nome
        segredos['Valor'] = lance
    while acabou:
        cnt = str(input('Tem mais pessoas no leilão? "Sim" ou "Não"\n')).lower().strip()
        if cnt == 'sim':
            break
        elif cnt in ['nao', 'não']:
            acabou = False
        else:
            print('Erro! Tente novamente')
print(f'O maior lance foi {segredos[nome]} que fez um lance de R${segredos[valor]}')