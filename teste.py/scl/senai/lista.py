lista = []
x = ''
print('Digite "fim" para acabar a lista')
while x != 'Fim':
    x = input('Adicione um item na lista: ').strip().capitalize(); lista.append(x)
print(lista)