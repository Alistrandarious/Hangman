import time
from ImportWords import *

class HangManGame:
    GameOver = False

    def hangman(name):
        word = RandomWordGenerator.RandomWord()  # From the 47k, uses a word from the list generated randomly.
        validLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Set to this so I can print after invalid guesses. + alpha only.
        turns = 10  # sets the amount of 'lives' a player has to play the game. ASCII code is based around this number.
        guessed = []  # appends guesses to a list.

        while len(word) > 0:  # This makes sure we have a word to use.
            msg = ""
            missed = 0
            for letter in word:  # for loop is used to check if a letter is in the word.
                if letter in guessed:
                    msg = msg + letter  # if it is, then we print that letter in the spot.
                else:
                    msg = msg + "_" + " "  # otherwise we print a blank, to keep it consistent. '_ ' used to break up.
                    missed += 1
            if msg == word: # condition 1 win, where the completed word via individual input equals the word.
                print(msg)
                print(f"\n*** CONGRATULATIONS!!! *** {name}, you have guessed correctly with {turns} remaining lives! "
                      f"The word was " + word + "\n")
                global GameOver
                GameOver = True
                break

            GameOver = False
            print(f"\n" + msg + " Guess the executioner's word (" + str(len(word)) + ") :")
            guess = input().upper()
            if guess == word:  # condition 2 win, where completed word is completed via whole input. GG!
                print(msg)
                print(f"\n*** CONGRATULATIONS!!! *** {name}, you have guessed correctly with {turns} remaining lives! "
                      f"The word was " + word + "\n")
                GameOver = True
                break
            if guess in guessed:  # if the letter is already guessed, this is printed, but splits off:
                print(f"You've already guessed {guess}!")
                if guess in word: # as you don't lose a life after a correct guess, no reimbursement.
                    pass
                elif guess not in word: # but as you lose a life after an incorrect guess, reimbursement.
                    turns += 1  # this is to stop plays from spamming a correct letter to gain more lives.
            if guess == "HELP":  # I created this to allow the player to take a pause and reread the rules ingame.
                print("########################################################################")
                print("Don't worry. This game can be tricky.\n\n"
                      "The objective is, within ten lives as removed by incorrect guesses, to correctly identify "
                      "the word that will stop the executioner from killing AliMan."
                      "\n\nYour guesses should be alphabetical and one character per turn (but typing help,"
                      "as you've done, is fine).\n\n"
                      "If you think you know the correct word, you can type this out also. If correct, you will "
                      "save Ali Man.\n\nSo, to recap; one letter guesses. Wrong guesses remove a life. There are "
                      "no hints to the word.\n\nBest of luck! Type help any time to recap this information.")
                print("########################################################################\n")
                turns += 1  # adds a turn to cancel out the minus turns.
            if guess == "EXIT":
                turns += 1
                leave = input("Are you sure you want to exit Hangman?:\n").lower()
                if leave in ["yes", "ye", "y", "yeah", "ok", "end this hell", 'yeah boi', "gg im out"]:
                    print("Thanks for playing!")
                    exit()
                if leave in ["no", "nah", "n", "never", "nope", "negative", "noo", "nooo", "stop", "exit"]:
                    print("Resuming game...")
            if guess in validLetters:
                guessed.append(guess)
            if guess not in validLetters and not ("HELP" or "EXIT"):  # guess not added
                print("You have lost a life. Please enter valid letters: " + validLetters)
                print("Type in one letter at a time from the above list or the whole word when you are ready to guess.")
                print("When you are ready, input below.")
            elif guess is not word and not ("HELP" or "EXIT"):  # if the guess is not the word and not help, lose a life.
                guessed.append(guess)
                print("You have lost a life Please enter valid letters: " + validLetters)
                print("Type in one letter at a time from the above list or the whole word when you are ready to guess.")
                print("When you are ready, input below.")
            if guess not in word:
                turns -= 1  # This is like, the Global turns/lives loss function i've been referencing.
                print(f"You have guessed {guessed} so far.\n")
                if turns == 9:  # Cycles through the hangman ASCII as turns/lives are reduced.
                    print(f"Oh no! {turns}/10 remaining!\n")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                if turns == 8:
                    print(f"Oh no! {turns}/10 remaining!\n")
                    print("________")
                    print("|/")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                if turns == 7:
                    print(f"Oh no! {turns}/10 remaining!\n")
                    print("________")
                    print("|/")
                    print("|")
                    print("|")
                    print("|")
                    print("|_________")
                if turns == 6:
                    print(f"Oh no! The noose has been built, {turns}/10 remaining!\n")  # builds special line.
                    print("________")
                    print("|/     |")
                    print("|")
                    print("|")
                    print("|")
                    print("|_________")
                if turns == 5:
                    print(f"Oh no! {turns}/10 remaining!\n")
                    print("________")
                    print("|/     |")
                    print("|      O  ")
                    print("|")
                    print("|")
                    print("|_________")
                if turns == 4:
                    print(f"Oh no! {turns}/10 remaining!\n")
                    print("________")
                    print("|/     |")
                    print("|      O")
                    print("|      |")
                    print("|")
                    print("|_________")
                if turns == 3:
                    print(f"Oh no! {turns}/10 remaining!\n")
                    print("________")
                    print("|/     |")
                    print("|      O")
                    print("|      |\\ ")
                    print("|")
                    print("|_________")
                if turns == 2:
                    print(f"Oh no! {turns}/10 remaining!\n")
                    print("________")
                    print("|/     |")
                    print("|      O")
                    print("|      |\\ ")
                    print("|       \\ ")
                    print("|_________")
                if turns == 1:
                    print(f"Oh no! {turns}/10 remaining!\n")
                    print("________")
                    print("|/     |")
                    print("|      O")
                    print("|     /|\\ ")
                    print("|       \\ ")
                    print("|_________")
                if turns == 0:
                    print(f"Oh no! {turns}/10 remaining!\n")
                    print("________")
                    print("|/     |   ")
                    print("|      ⓧ  ")
                    print("|     /|\\ ")
                    print("|     / \\ ")
                    print("|_________")
                    print(f"\nOh no! AliMan is a gonner! {name}, you have failed to guess the word. The word was: "
                          f"\n {word} !")
                    input("Press 'F' to press respects:\n").upper()  # does nothing.
                    GameOver = True
                    break

    def restart(name):  # restarts game. Came up with as many ways to say yes or no as I could.
        while GameOver is True:
            restart = input("I hope you've enjoyed the game! Try a new word? :\n").lower()
            if restart in ["yes", "ye", "y", "yeah", "ok", "yeah boii"]:
                HangManGame.hangman(name)
            if restart in ["no", "nah", "n", "never", "nope", "negative", "noo", "nooo", "stop", "exit"]:
                print("Come back soon!")
                exit()
            else:
                print("Please type y/N to continue or exit AliMan v1")

class WelcomeScreen: # Rules:
    def greetings():
        print("########################################################################")
        print("Hello and Welcome to AliMan!\n")
        time.sleep(1)
        print("AliMan (v1) is an iteration on the famous Hangman series for Python 3.4.\n")
        time.sleep(1.75)
        print("Try to guess the executioner's word (randomly chosen by the computer) in ten lives or less.\n")
        time.sleep(2)
        print("The game works by typing one letter in per turn. With each letter you guess wrong, a life is removed.\n ")
        time.sleep(2.2)
        print("The game is over when you save AliMan by typing the correct letters in the random word, or when you run"
              "out of lives from incorrect guesses.\n")
        time.sleep(2.5)
        print("If you are stuck, type help at any time.")
        print("########################################################################")
        time.sleep(2)
        name = input("\nLet's begin, what is your name? :\n").capitalize()
        if name == "David": # How could I not :)
            print(f"Ah, {name}! Spearhead of data 4. Welcome!")
        else:
            print(f"\nWelcome, {name}! To AliMan v1!\n")
        time.sleep(0.3)
        print("...")
        time.sleep(0.3)
        print("...")
        time.sleep(0.3)
        print("...")
        time.sleep(0.85)
        HangManGame.hangman(name)
        HangManGame.restart(name)
