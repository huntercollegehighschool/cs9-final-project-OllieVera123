"""
Name(s): Oliver Flor, Jordan Bose
Name of Project: Fun Mini-Games
"""
#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
print("Hello, welcome to Fun Mini-Games!")
game = input("Pick Your Game: \n 1. rock paper scissors \n 2. the game of war \n 3. hangman \n 4. blackjack \n 5. tournament (all the games one after the other) \n ")
if game == "rock paper scissors" or game == "1":
  import rps
if game == "the game of war" or game == "2":
  import gow
if game == "hangman" or game == "3":
  import hangman
if game == "blackjack" or game == "4":
  import blackjack
if game == "tournament" or game == "5":
  import rps
  import gow
  import hangman
  import blackjack