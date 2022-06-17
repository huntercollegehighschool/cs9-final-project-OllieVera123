#Use of this page is optional. If you use code here, make sure either import page2 or from page2 import * appear on your main.py page.
import random
import urllib.request

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = urllib.request.urlopen(word_site)
txt = response.read().decode()
WORDS = txt.splitlines()

word = random.choice(WORDS)
wordnum = len(word)
spaces = "_ "*wordnum
hangmanlevel = {
  0: """
    ~~~~~~||
          ||
          ||
          ||
          ||
          ||
  {}{}{}{}{}""",
  1: """
    ~~~~~~||
    0     ||
          ||
          ||
          ||
          ||
  {}{}{}{}{}""",
  2: """
    ~~~~~~||
    0     ||
    |     ||
    |     ||
          ||
          ||
  {}{}{}{}{}""",
  3: """
    ~~~~~~||
    0     ||
    |--   ||
    |     ||
          ||
          ||
  {}{}{}{}{}""",
  4: """
    ~~~~~~||
    0     ||
  --|--   ||
    |     ||
          ||
          ||
  {}{}{}{}{}""",
  5: """
    ~~~~~~||
    0     ||
  --|--   ||
    |     ||
     \    ||
          ||
  {}{}{}{}{}""",
  6: """
    ~~~~~~||
    0     ||
  --|--   ||
    |     ||
   / \    ||
          ||
  {}{}{}{}{}"""}
def split(word):
  return [char for char in word]
print("\n", spaces, "\n")

lettersfound = 0 #number of letters which have been found
letterswrong = 0 #number of letters guessed which were wrong
lettersguessedright = {}
alllettersguessed = []
for x in range(0,wordnum): #which letters have been guessed
  lettersguessedright[x] = " _ "

while lettersfound < wordnum and letterswrong < 7: #testing for if we found all the words
 
  letterguessed = input("\nGuess a letter: ") #current letter being guessed
  if letterguessed not in alllettersguessed:
    alllettersguessed.append(letterguessed)
    if letterguessed in split(word):
      lettertest = 0
      while lettertest < wordnum: ##program that checks each spot for the letter
        if letterguessed == (split(word)[lettertest]):
          lettersfound += 1
          print("letter found")
          print(lettertest+1)
          lettersguessedright[lettertest] = letterguessed
        lettertest += 1
    else:
      print("letter not found")
      letterswrong += 1
    print("\n",''.join(list(lettersguessedright.values())))
    print("you have guessed the letters:", alllettersguessed)
    if letterswrong < 7:
      print(hangmanlevel[letterswrong])
  else:
    print("You have already entered that letter! Pick another one.")

if letterswrong == 7:
  print("The Computer wins! Better luck next time")
elif lettersfound == wordnum:
  print("Congrats! You guessed the word!")
print("The word was", word)