alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k' ,'l' ,'m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
codificado = []
codigo = 0
while True:
    direcao = str(input('Você deseja "Codificar" ou "Descodificar"?\n')).lower()
    if 'codificar' == direcao or 'descodificar' == direcao:
        break
    else:
        print('Erro! Tente novamente.')
texto = str(input('Digite o texto desejado: \n')).lower()
shift = int(input('Numero de Shift: \n'))
if 'codificar' == direcao:
    for letters in texto:
        if letters not in alfabeto:
            codificado.append(letters)
        else:
            codigo = alfabeto.index(letters)
            codigo += shift
            if codigo >= 26:
                codigo -= 26
                codificado.append(alfabeto[codigo])
            else:
                codificado.append(alfabeto[codigo])
    print(''.join(codificado))
elif 'descodificar' == direcao:
    for letters in texto:
        if letters not in alfabeto:
            codificado.append(letters)
        else:
            codigo = alfabeto.index(letters)
            codigo -= shift
            codificado.append(alfabeto[codigo])
    print(''.join(codificado))