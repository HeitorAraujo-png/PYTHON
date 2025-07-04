from random import randint; cw = randint(0, 3)
x = str('\ ')
corpo = [
(f'''
      +======+
      0      |
    / | {x}   |
    /   {x}   |
             | '''),
(f'''
      +======+
      0      |
    / | {x}   |
    /        |
             | '''),
(f'''
      +======+
      0      |
    / |      |
    /        |
             | '''),
(f'''
      +======+
      0      |
    / |      |
             |
             | '''),
(f'''
      +======+
      0      |
      |      |
             |
             | '''),
(f'''
      +======+
      0      |
             |
             |
             | '''),
(f'''
      +======+
             |
             |
             |
             | ''')
]
lista_palavras = ['camelo', 'paralelo', 'celular', 'nomes']
palavra_escolhida = lista_palavras[cw]
tamanho = len(palavra_escolhida)
segredo = ''
lista = []
vida = 6
for para in range(tamanho):
    segredo += '*'
print(segredo)
while True:
    letra_do_player = str(input('Guess a letter:')).lower()
    display = ''
    for letra in palavra_escolhida:
        if letra == letra_do_player:
            display += letra
            lista.append(letra)
        elif letra in lista:
            display += letra
        else:
            display += '*'
    if letra_do_player not in palavra_escolhida:
        vida -= 1
    print(corpo[vida])
    print(display)  
    if '*' not in display:
        print('You win')
        break
    elif vida == 0:
        print(corpo[vida], 'You lose')
        break