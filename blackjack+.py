from blackjack import BlackJack

def should_hit(player_total, dealer_card_val, player_aces):
    return player_total <=17

g = BlackJack(should_hit, True, True)
#g.play()
g.simulate(n_games=10)
