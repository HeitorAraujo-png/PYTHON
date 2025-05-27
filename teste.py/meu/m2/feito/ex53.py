for i in range(10):
    x = str(input('Escreva uma frase: ')).lower().strip()
    y = x.replace(' ', '')
    z = y[::-1]
    if z == y:
        print('A frase "{}" é um palindromo!'.format(x))
    else:
        print('Não é um palindromo!')
print('Fim')