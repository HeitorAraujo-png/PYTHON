def BlackJack2():
    '''Jogue um jogo de blackjack também conhecido como 21'''
    import random, time
    def soma(deck):
        '''Conta e soma quantas cartas tem e se o As vale 11 ou 1'''
        total = sum(deck)
        ases = deck.count(11)
        while total > 21 and ases > 0:
            total -= 11
            ases -= 1
        return total
    def cards_deal():
        '''Escolhe uma carta aleatoria do baralho'''
        cart = random.choice(cards)
        return cart
    blackjack_player = blackjack_dealer = False
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards_dealer = [cards_deal(), cards_deal()]
    if cards_dealer == [11, 11]:
        cards_dealer[1] = 1
    total_dealer = soma(cards_dealer)
    if total_dealer == 21 and len(cards_dealer) == 2:
        blackjack_dealer = True
    cards_player = [cards_deal(), cards_deal()]
    if cards_player ==[11, 11]:
        cards_player[1] = 1
    total_player = soma(cards_player)
    if total_player == 21 and len(cards_dealer) == 2:
        blackjack_player = True
    while True:
        condicao = input(f'As cartas do dealer são: {cards_dealer[0]}\nSuas cartas são: {cards_player}, Pontos Player {total_player}\nDeseja pegar mais uma carta? [S/N] ').lower()
        if condicao == 's':
            card_random = cards_deal()
            if card_random == 11 and (total_player + card_random) > (21):
                card_random = 1
                cards_player.append(card_random)
            else:
                cards_player.append(card_random)
            total_player = soma(cards_player)
            if total_player > 21:
                print(f'Você estourou! Você fez uma pontuação de {total_player} (Maior que 21)')
                return
        elif condicao == 'n':
            while soma(cards_dealer) < 17:
                cards_dealer.append(random.choice(cards))
            total_dealer = soma(cards_dealer)
            if blackjack_dealer and blackjack_player:
                print('Ambos tinham blackjack! Jogo empatado.')
            elif blackjack_dealer:
                print('Dealer com blackjack! Dealer vence.')
            elif blackjack_player:
                print('Player com blackjack! Player vence!')
            elif total_dealer > 21:
                print(f'Dealer tem o total de {total_dealer}\nPlayer tem o total de {total_player}\nO delaer estourou! Player Vence.')
            elif total_dealer > total_player:
                print(f'Dealer tem o total de {total_dealer}\nPlayer tem o total de {total_player}\nDealer Vence!')
            elif total_dealer < total_player:
                print(f'Dealer tem o total de {total_dealer}\nPlayer tem o total de {total_player}\nPlayer Vence!')
            else:
                print(f'Dealer tem o total de {total_dealer}\nPlayer tem o total de {total_player}\nJogo empatado!')
            time.sleep(1.5)
            return
        else:
            print('Opção invalida! Tente novamente.')
BlackJack2()
