#1/17/19
#This program will simulate a hangman game

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   | 
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDFILELIST = ["nouns.txt","adjectives.txt","adverbs.txt","verbs.txt","animals.txt"]
CATAGORIES = ["Nouns","Adjectives","Adverbs","Verbs","Animals"]

import random

def CreateList(file):
    infile = open(file,"r")
    filelist = []
    for each_line in infile:
        current = each_line.strip()
        filelist.append(current)
    infile.close()
    return filelist

def AddGuess(alist,letter):
    alist.append(letter.upper())

def GetValidInput(missedlist,prompt,hint):
    print(prompt)
    letter = input()
    valid = False
    while not valid:
        if letter.lower() == "help":
            print("The catagory is:",hint+"!")
        elif letter.isalpha():
            if len(letter) == 1:
                if letter.upper() not in missedlist:
                    return letter
                else:
                    print("You have already guess that letter. Choose again.")
            else:
                print("Please enter a single letter.")
        else:
            print("Please enter a LETTER.")
        print(prompt)
        letter = input()

def DisplayMissed(missedlist):
    print("Missed Letters:")
    for x in range(len(missedlist)):
        print(missedlist[x],end = " ")
    print()

def DisplayWord(word,correctlist):
    for achar in word:
        
        if achar in correctlist:
            print(achar,end = " ")
        else:
            print("_",end = " ")
    print()
    print()

def CheckForWin(word,correctlist):
    for achar in word:
        if achar not in correctlist:
            return False
    return True

def GenerateCatagory(filelist):
    catagory = random.randrange(len(filelist))
    return catagory
    
def main():
    response = "y"

    while response.lower() != "n":
        print("H A N G M A N")
        print("(Enter 'HELP' for a hint!)")
        #initialize lists, the boolean variable, and select a new word
        gameover = False
        missedlist = []
        correctlist = []
        catagory = GenerateCatagory(WORDFILELIST)
        wordlist = CreateList(WORDFILELIST[catagory])
        hint = CATAGORIES[catagory]
        word = wordlist[random.randrange(len(wordlist))]

        while not gameover:
            #displays
            print(HANGMANPICS[len(missedlist)])
            print()
            DisplayMissed(missedlist)
            print()
            DisplayWord(word,correctlist)
            letter = GetValidInput(missedlist,"Guess a letter.",hint)

            #check if guess is correct; add to respective list
            if letter.upper() in word:
                AddGuess(correctlist,letter)
            else:
                AddGuess(missedlist,letter)

            #check for a 'gameover' situation
            if (len(missedlist)+1) == len(HANGMANPICS):
                print(HANGMANPICS[len(missedlist)])
                print("After",len(missedlist),"and",len(correctlist),
                      "correct guesses, the word was '"+word+"'")
                gameover = True
            elif CheckForWin(word,correctlist):
                print("Yes! The secret word is '"+word+"'! You have won!")
                gameover = True
                
        #check if to repeat the game
        response = input("Do you want to play again? (y/n) ")
        while response.lower() != "y" and response.lower() != "n":
            response = input("Do you want to play again? (y/n) ")
        print()
main()
