#Use of this page is optional. If you use code here, make sure either import page1 or from page1 import * appear on your main.py page.
"""
Unfortunately we weren't able t complete this, but here is our work so far:
"""

import random
import time

print("Welcome to blackjack! Here are the rules: you will be dealt two cards. You will  add the value of those two cards to gether and then determine if you want extra cards (hit) or if you are done collecting cards (stay). The goal of the game is to get your cards to equal 21, but if you go over 21, you lose. All face cards are worth 10 points except for aces which are 11 points.")
time.sleep(2)
jack = king = queen = 10
ace = 11
deck = [ace, ace, ace, ace, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, jack, jack, jack, jack, queen, queen, queen, queen, king, king, king, king]
playerhand = random.sample(deck, 2)
comphand = random.sample(deck, 2)
finalhand = 0
game = 0
possibilities = []
print(playerhand)
print(comphand)
playerval = sum(playerhand)
compval = sum(comphand)
y = random.random()
print(y)



while compval < 21 and y > (1-(len(possibilities)/len(deck))):
  for x in deck:
    if x <= (21-compval) and x not in possibilities:
      possibilities.append(x)
      print(possibilities)
  if y > (1-(len(possibilities)/len(deck))):
    comphand.extend(random.sample(deck, 1))
    print(comphand)
    compval = sum(comphand)

if compval <= 10:
  comphand.extend(random.)


while playerval <= 21 and game != "stay":
  if playerval == 21:
    print("Blackjack! Player wins.")
  game = input("Would you like to hit or stay? ")
  if game == "hit":
    playerhand.extend(random.sample(deck, 1))
    print(playerhand)
    playerval = sum(playerhand)
    if compval > 21:
      print("Computer's total is above 21. You win. Game over.")
      break
    elif compval == 21:
      print("Computer got blackjack! Computer wins.") 
      break
    elif playerval > 21:
      print("Your total is above 21. Game over.")
      break
    elif playerval == 21:
      print("Blackjack!! Player wins.")
      break
  elif game == "stay":
    finalhand = playerhand
    if playerval > compval and playerval <= 21 or compval > 21:
      print("Player wins!")
    elif compval > playerval and compval <= 21 or playerval > 21:
      print("Computer wins!")
print("Player total is", playerval, "Computer total is", compval)