#Use of this page is optional. If you use code here, make sure either import page4 or from page4 import * appear on your main.py page.
import random
import time

print("Welcome to the game of war! as the real game takes too long, this is a modified version of the game with only 10 cards each. Get your enemy down to their last card to win.")
time.sleep(5)
playerhand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
comphand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while len(playerhand) < 19 and len(comphand) < 19:
    playercard = random.choice(playerhand)
    compcard = random.choice(comphand)
    if playercard > compcard:
      print("your card was", playercard, "and the computers card was", compcard, "meaning you win the computers card.")
      playerhand.append(compcard)
      comphand.remove(compcard)
    elif compcard > playercard:
      print("your card was", playercard, "and the computers card was", compcard, "meaning the computer wins your card.")
      comphand.append(playercard)
      playerhand.remove(playercard)
    elif compcard == playercard:
      print("your card was", playercard, "and the computers card was", compcard, "meaning it is a draw, no cards are won.")
if len(playerhand) == 19:
  print("Congrats! You beat the computer!")
elif len(comphand) == 19:
  print("Unlucky today. The computer wins.")