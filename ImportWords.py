import random


class RandomWordGenerator:
    def RandomWord():
        with open('hangman_words (2).py', 'r') as input_file:
            words_raw = input_file.readlines()
            words = random.choice(words_raw)
            map(str.strip, words)
            words = (words.translate({ord("'"): None}))
            words = (words.translate({ord(","): None}))
            words = (words.strip())

        return words
