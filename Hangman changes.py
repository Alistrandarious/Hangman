import random
import time


class HangManGame:
    GameOver = False

    def hangman(name):
        word_list = ["arctic", "beans", "commando", "directly", "ending", "fruition", "gravy", "Harmony", "zebra",
                     "idiosyncratic", "villain", "heroism", "communism", "war", "chocolate", "vanilla",
                     "strawberry", "pizza"]  # change to multiple lists
        word = random.choice(word_list)
        validLetters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        attempt = 0
        turns = 10
        guessed = ''  # append to list

        while len(word) > 0:
            msg = ""
            missed = 0
            for letter in word:
                if letter in guessed:
                    msg = msg + letter
                else:
                    msg = msg + "_" + " "
                    missed += 1
            if msg == word:
                print(msg)
                print(f"Congratulations, {name} you have guessed correctly after {attempt} turns!! The word was "
                      + word + "\n")
                global GameOver
                GameOver = True
                break

            print("Guess the word: " + msg)
            guess = input().lower()
            if guess in validLetters:
                guessed = guessed + guess
            else:
                print("Valid Letters: " + validLetters)
                print("The aim of the game is to type in one letter at a time from the above list.")
                print("when you are ready, input a new letter.")
                turns += 1
            if guess not in word:
                turns -= 1
                print(f"You have guessed {guessed} so far. {turns} turns remaining.\n")
                if turns == 9:
                    print(f"Oh no! {turns}/10 remaining!")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                if turns == 8:
                    print(f"Oh no! {turns}/10 remaining!")
                    print("_______")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                if turns == 7:
                    print(f"Oh no! {turns}/10 remaining!")
                    print("_______")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("|_________")
                if turns == 6:
                    print(f"Oh no! {turns}/10 remaining!")
                    print("_______")
                    print("|     |")
                    print("|")
                    print("|")
                    print("|")
                    print("|_________")
                if turns == 5:
                    print(f"Oh no! {turns}/10 remaining!")
                    print("_______")
                    print("|     |")
                    print("|     o")
                    print("|")
                    print("|")
                    print("|_________")
                if turns == 4:
                    print(f"Oh no! {turns}/10 remaining!")
                    print("_______")
                    print("|     |")
                    print("|     o")
                    print("|     |")
                    print("|")
                    print("|_________")
                if turns == 3:
                    print(f"Oh no! {turns}/10 remaining!")
                    print("_______")
                    print("|     |")
                    print("|     o")
                    print("|     |\ ")
                    print("|")
                    print("|_________")
                if turns == 2:
                    print(f"Oh no! {turns}/10 remaining!")
                    print("_______")
                    print("|     |")
                    print("|     o")
                    print("|     |\ ")
                    print("|      \ ")
                    print("|_________")
                if turns == 1:
                    print(f"Oh no! {turns}/10 remaining!")
                    print("_______")
                    print("|     |")
                    print("|     o")
                    print("|    /|\ ")
                    print("|      \ ")
                    print("|_________")
                if turns == 0:
                    print(f"Oh no! {turns}/10 remaining!")
                    print("_______")
                    print("|     |")
                    print("|     o")
                    print("|    /|\\  ")
                    print("|    / \\ ")
                    print(f"|___________ Oh no! {name} You have failed to guess the word! The word was: "
                          f" {word} !") # carry over welcome name code.
                    GameOver = True
                    break
    def restart():
        while GameOver is True:
            restart = input("I hope you've enjoyed the game! Try a new word? :\n").lower()
            if restart in ["yes", "ye", "y", "yeah", "ok"]:
                HangManGame.hangman()
            if restart in ["no", "nah", "n", "never", "nope", "negative"]:
                print("Come back soon!")
                exit()

class WelcomeScreen:
    def greetings():
        print("\nHello and Welcome to AliMan!\n")
        time.sleep(1)
        print("AliMan (v1) is an iteration on the famous Hangman series for Python 3.4.\n")
        time.sleep(1.75)
        print("Try to guess the computer's word in ten tries or less.\n")
        time.sleep(1.5)
        print("If you are stuck, type help at any time.\n")
        time.sleep(1.5)
        name = input("What is your name? :\n")
        if name == "help":
            print("Don't worry. The aim of the game is to type in one letter at a time from a-z.")
            print(f"your have 10 turns to correctly guess the word, else AliMan goes bye-bye!")
            print("when you are ready, type your name:")
            name = input()

        print(f"welcome, {name}! Let's begin!\n\n")
        HangManGame.hangman(name)
        HangManGame.restart()

# Create instance of hangman game.


