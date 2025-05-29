x = n1 = n2 = 0
while x != 5:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    print("""    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa""")
    x = int(input('    Digite sua opção: '))
    if x == 1:
        print('A soma de {} + {} = {}'.format(n1, n2, n1+ n2))
    elif x == 2:
        print('a multiplicação de {} * {} = {}'.format(n1, n2, n1* n2))
    elif x == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n1 < n2:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('{} tem o mesmo valor que {}'.format(n1, n2))
    elif x == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))        
    elif x == 5:
        print('Parando...')
    else:
        print('opção invalida!')
print('Fim')