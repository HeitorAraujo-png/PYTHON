resposta = produto = ''
tabela_produto = []
tabela_preco = []
yet = mais = soma = contador = preco = menor_valor = 0.0
x = ''
while True:
    produto = str(input('Qual o nome do produto? '))
    tabela_produto.append(produto)
    preco = float(input('Quanto custa esse produto? '))
    tabela_preco.append(preco)
    contador += 1
    soma = soma + preco
    if contador == 1:
        menor_valor = preco
    elif preco < menor_valor:
        menor_valor = preco
    if preco > 1000:
        mais += 1
    while True:
        resposta = str(input('Você quer continuar [S/N]?'))
        if resposta in 'Ss':
            break
        if resposta in 'Nn':
            break
        else:
            print('Erro! Tente novamente.')
    if resposta in 'Nn':
        break
x = tabela_preco.index(menor_valor)
print(f'''
      R${soma:.2f} Gastos no total!
      {mais:.0f} Itens que custam mais que R$1000,00
      O {tabela_produto[x]} tem o menor preço! custa apenas R${menor_valor}
      ''')