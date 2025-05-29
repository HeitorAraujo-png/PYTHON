from random import randint; cw = randint(0, 3)
list_words = ['camelo', 'paralelo', 'celular', 'thays']
chosed_word = list_words[cw]
print(chosed_word)
lifes = 7
true_player = []
while lifes > 0:
    chosed_player = (input('Guess a letter:')).lower()
    true_player.append(chosed_player)
    for i in chosed_word:
        if i in true_player:
            print(True)
        else:
            print(False)