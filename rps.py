#Use of this page is optional. If you use code here, make sure either import page3 or from page3 import * appear on your main.py page.
import random

rounds = int(input("Welcome to Rock Paper Scissors!\nhow many rounds would you like to play? "))
round = 1
print("Round", round)
pts = 0
comppts = 0
while rounds > 0:
  rps = input("Would you like to play rock, paper, or scissors? ")
  rps = rps.lower()
  comprps = random.random()
  if rps == "rock":
    if comprps <= (1/3):
      print("Computer picks paper. Computer wins.")
      comppts += 1
    elif (1/3) <= comprps and comprps <= (2/3):
      print("Computer picks scissors. You win.")
      pts += 1
    else:
      print("Computer picks rock. It's a draw.")
  elif rps == "scissors":
    if comprps <= (1/3):
      print("Computer picks rock. Computer wins.")
      comppts += 1
    elif (1/3) <= comprps and comprps <= (2/3):
      print("Computer picks paper. You win.")
      pts += 1
    else:
      print("Computer picks scissors. It's a draw.")
  elif rps == "paper":
    if comprps <= (1/3):
      print("Computer picks scissors. Computer wins.")
      comppts += 1
    elif (1/3) <= comprps and comprps <= (2/3):
      print("Computer picks rock. You win.")
      pts += 1
    else:
      print("Computer picks paper. It's a draw.")
  else:
    print("That's not an option. Computer wins because you couldn't choose.")
    comppts += 1
  rounds -= 1
  round += 1
print("The match is over. You got", pts, "points. The computer got", comppts, "points.")
if comppts > pts:
  print("The computer wins.")
elif pts > comppts:
  print("You win.")
else:
  print("It's a draw!")