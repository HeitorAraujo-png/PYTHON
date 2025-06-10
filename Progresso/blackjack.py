def BlackJack2():
    '''Jogue um jogo de blackjack também conhecido como 21'''
    import random, time
    def soma(deck):
        '''Conta e soma quantas cartas tem e se o As vale 11 ou 1'''
        total = sum(deck)
        ases = deck.count(11)
        while total > 21 and ases > 0:
            total -= 10
            ases -= 1
        if total > 21:
            total = 0
        return total
    def cards_deal():
        '''Escolhe uma carta aleatoria do baralho'''
        cart = random.choice(cards)
        return cart
    blackjack_player1 = blackjack_dealer = blackjack_player2 = False
    p1 = p2 = True
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards_dealer = [cards_deal(), cards_deal()]
    if cards_dealer == [11, 11]:
        cards_dealer[1] = 1
    total_dealer = soma(cards_dealer)
    if total_dealer == 21 and len(cards_dealer) == 2:
        blackjack_dealer = True
    cards_player1 = [cards_deal(), cards_deal()]
    if cards_player1 ==[11, 11]:
        cards_player1[1] = 1
    total_player1 = soma(cards_player1)
    if total_player1 == 21 and len(cards_dealer) == 2:
        blackjack_player1 = True
    cards_player2 = [cards_deal(), cards_deal()]
    if cards_player2 == [11, 11]:
        cards_player2[1] == 1
    total_player2 = soma(cards_player2)
    if total_player2 == 21 and len(cards_player2) == 2:
        blackjack_player2 == True
    player1 = input('Qual é o seu nome Player1? ')
    print('\n' * 20)
    player2 = input('Qual é o seu nome Player2? ')
    print('\n' * 20)
    def jogo(player, total):
        card_random = cards_deal()
        player.append(card_random)
        total = soma(player) 
        if total > 21:
            print(f'Você estourou! Você fez uma pontuação de {total} (Maior que 21)')
            print('\n' * 20)
            total = 0
            return False, player, total
        return True, player, total
    while p1 and p2:
        while p1:
            if total_player1 == 0:
                print(f'{player1} Estourou! ')
                p1 = False
            condicao1 = input(f'PLAYER 1\nAs cartas do dealer são: {cards_dealer[0]}\nAs cartas do {player2} são: {cards_player2}, total: {total_player2}\nSuas cartas são: {cards_player1}, Pontos {player1} {total_player1}\nDeseja pegar mais uma carta? [S/N] ').lower().strip()
            if condicao1 == 's':
                p1, cards_player1, total_player1 = jogo(player=cards_player1, total=total_player1)
                print('\n' * 20)
            elif condicao1 == 'n':
                p1 = False
                print('\n' * 20)
            else:
                print('Opção invalida! Tente novamente.')
                print('\n' * 20)
        while p2:
            if total_player2 == 0:
                print(f'{player2} Estourou! ')
                p2 = False
            condicao2 = input(f'PLAYER 2\nAs cartas do dealer são: {cards_dealer[0]}\nAs cartas do {player1} são: {cards_player1}, total : {total_player1}\nSuas cartas são: {cards_player2}, Pontos {player2} {total_player2}\nDeseja pegar mais uma carta? [S/N] ').lower().strip()
            if condicao2 == 's':
                p2 , cards_player2, total_player2 = jogo(player=cards_player2, total=total_player2)
                print('\n' * 20)
            elif condicao2 == 'n':
                p2 = False
                print('\n' * 20)
            else:
                print('Opção invalida! Tente novamente.')
                print('\n' * 20)
    while soma(cards_dealer) < 17:
        cards_dealer.append(random.choice(cards))
    total_dealer = soma(cards_dealer)
    print(f'Cartas do dealer {cards_dealer}, {total_dealer} Pontos.\nCartas do(a) {player1}: {cards_player1}, {total_player1} Pontos.\nCartas do(a) {player2}: {cards_player2},{total_player2} Pontos.')
    if blackjack_dealer and blackjack_player1 and blackjack_player2:
        print(f'Todos da mesa tem um blackjack!!!\nEmpate')
    elif blackjack_dealer and blackjack_player2:
        print(f'O dealer e o {player2} tem blackjack!!!\n {player1} perder\nDelaer e {player2} ficam empatados')
    elif blackjack_dealer and blackjack_player1:
        print(f'O dealer e o {player1} tem blackjack!!!\n {player2} perder\nDelaer e {player1} ficam empatados')
    elif blackjack_player1 and blackjack_player2:
        print(f'O {player2} e o {player1} tem blackjack!!!\nDealer perder\nPlayer2 e {player1} ficam empatados')
    elif blackjack_dealer:
        print(f'O dealer ganhou com um blackjack!')
    elif blackjack_player1:
        print(f'O {player1} ganhou com um blackjack!')
    elif blackjack_player2:
        print(f'O {player2} ganhou com um blackjack!')
    elif total_player2 < total_player1 > total_dealer:
        print(f'O {player1} ganhou!')
    elif total_player1 < total_player2 > total_dealer:
        print(f'O {player2} ganhou!')
    elif total_player1 < total_dealer > total_player2:
        print(f'O dealer ganhou!')
    elif total_player2 == total_player1 > total_dealer:
        print('Empate entre os jogadores!')
    elif total_dealer == total_player1 > total_player2:
        print(f'Empate entre o {player1} e o Dealer!')
    elif total_dealer == total_player2 > total_player1:
        print(f'Empate entre o {player2} e o Dealer!')
    else:
        print('Empate')
BlackJack2()