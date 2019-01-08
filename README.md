# blackjack
BlackJack competition on kaggle https://www.kaggle.com/borisalekseev/blackjack-microchallenge/edit
discussion https://www.kaggle.com/learn-forum/58735#latest-348767

blackjack.py is a description of game realization. Could be used to check the rules of the game.

Currently, dealer++.py consists an algorithm to calculate distribution of probabilities for dealer to get total of 17-21 or 22 (when dealer get more than 21) on each stage)

Folder js contains the port of dealer++.py to Javascript (thanks, Serg!)

Next goal - calculation of the best strategy for player.

The overall idea is (not finished yet!!):

def PlayerStrategy(total, aces = False):

  """

  total - current total sum of cards
  
  aces - is True if Aces are among the cards, False  if not
  
  should return
  
  [Stop, Prob]
  
  Stop - True - if the best decision is to stop, False - if not
  
  Prob - probability if win
  
  """
  
  dealer_distr = {17:0, 18:0, 19:0, 20:0, 21:0, 22:0}
  
  dealer_distr = dealer()
  
  player_win_if_stop = dealer_distr[22]
  
  player_win_if_continue = 0
  
  for c in range(1,11):
  
    if total+c > 21:
    
      # player in fire
    
    elif aces and total+c<12:
    
      # player use aces
      
      stop, prob = PlayerStrategy(total+c+10, aces or c == 1)
      
      if prob > player_win_if_continue:
      
        prob = player_win_if_continue
      
    else:
    
      stop, prob = PlayerStrategy(total+c, aces or c == 1)
      
      if prob > player_win_if_continue:
      
        prob = player_win_if_continue

  if player_win_if_stop > player_win_if_continue:
  
    return [True, player_win_if_stop]
  
  else:
  
    return [False, player_win_if_continue]
  
