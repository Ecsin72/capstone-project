# Import necessary libraries
import math
from collections import Counter
import random
word_file = 'word-list.txt'

# Define the wordle game class


class WordleGame:
    """Class to handle the Wordle game logic, it will load the words from the word text file, pick a random target word and provide functionality for the game."""

    def __init__(self, filename):
        """Constructor method to initialise the game with a file of words."""
        self.filename = filename
        self.words = self.load_words()
        self.target = self.pick_random_word()

    def load_words(self):
        """Loads all the words from the text file into a list we can access."""
        with open(self.filename, 'r') as file:
            return file.read().splitlines()

    def pick_random_word(self):
        """Picks a random word from the new list of loaded words."""
        return random.choice(self.words)


# Initialise WordleGame with the file of words we downloaded from github and pick a target word
game = WordleGame(word_file)
target = game.target

# Define the playable Wordle game as a function


def Wordle(target, guess):
    """Evaluates a player's guess against the randomised target word.
    INPUT - target: hidden word to be guesses
            guess: the word guessed by the player
    OUTPUT - A string representing the correct letters in the guess word where:
                'G' = Green, correct letter in correct position
                'Y' = Yellow, correct letter in incorrect position
                'R' = Red, incorrect letter"""
    assert len(target) == 5 and len(
        guess) == 5, "Both words must be 5 letters long"
    # Initialise list of colours, all Red
    colours = ['R'] * 5
    # Initialise list of target word letters to track for yellow marking
    target_remaining = list(target)
    # First pass through the guess, marking green letters
    for i, letter in enumerate(guess):
        if letter == target[i]:
            colours[i] = 'G'
            target_remaining[i] = None
    # Second padd through the guess, marking yellow letters
    for i, letter in enumerate(guess):
        if colours[i] == 'R' and letter in target_remaining:
            colours[i] = 'Y'
            target_remaining[target_remaining.index(letter)] = None
    # Return the final colour string
    return ''.join(colours)


# Initialise empty lists to track guesses and outputs in case the player needs reminding
guesses = []
outputs = []
tracker = [guesses, outputs]

# Create a function so you can interact with the Wordle game as a player


def wordle_guess(guess, target, tracker):
    """Allows the player to make a guess and updates our trackers
    INPUT - guess: the word guessed by the player
            target: the randomised target word
            tracker: list of two sublists, guesses so far and their corresponding outputs"""
    while True:
        guess = input("Please make a guess of a 5 letter word: ").lower()
        output = Wordle(target, guess)
        tracker[0].append(guess)
        tracker[1].append(output)
        print(f"The output for {guess} is {output}")
        print(f"Your current guesses have been {tracker[0]}")
        print(f"The corresponding outputs have been {tracker[1]}")
        if guess == target:
            print(f"Yay! You found the hidden word is {target}")
            break


wordle_guess("", target, tracker)
