# blackjack
BlackJack competition on kaggle https://www.kaggle.com/borisalekseev/blackjack-microchallenge/edit
discussion https://www.kaggle.com/learn-forum/58735#latest-348767

blackjack.py is a description of game realization. Could be used to check the rules of the game.

Currently, dealer++.py consists an algorithm to calculate distribution of probabilities for dealer to get total of 17-21 or 22 (when dealer get more than 21) on each stage)

Folder js contains the port of dealer++.py to Javascript (thanks, Serg!)

Next goal - calculation of the best strategy for player.

The overall idea is:

def PlayerStrategy(total, aces = False):
  """
  total - current total sum of cards
  aces - is True if Aces are among the cards, False  if not
  should return
  [Stop, Prob]
  Stop - True - if the best decision is to stop, False - if not
  Prob - probability if win
  """
  return []
  
  --- to continue ---
