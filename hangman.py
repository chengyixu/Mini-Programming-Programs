import os
import random

def read_data_file(file_name):
    """
    Reads the data file and creates a list of tuples with category and secret word/phrase pairs.
    """
    with open(file_name, 'r') as f:
        data_list = [tuple(line.strip().split(',')) for line in f]
    return data_list

def select_random_entry(data_list):
    """
    Selects a random tuple (category and secret word/phrase) from the list.
    """
    return random.choice(data_list)

def initialize_partial_word(secret_word):
    """
    Initializes the list representing the partially revealed secret word/phrase, with underscores for unguessed letters.
    """
    return ['_' if char.isalnum() else char for char in secret_word]

def process_user_guess(guess, correct_guesses, incorrect_guesses, partial_word, secret_word):
    """
    Processes the user's guess, updates the lists of correct and incorrect guesses, and updates the partially revealed secret word/phrase.
    """
    if guess in secret_word.lower() and guess not in correct_guesses:
        correct_guesses.append(guess)
        for i, char in enumerate(secret_word.lower()):
            if char == guess:
                partial_word[i] = secret_word[i]
        return True, f"There are {secret_word.lower().count(guess)} {guess}'s"
    else:
        if guess not in incorrect_guesses:
            incorrect_guesses.append(guess)
        return False, f"Incorrect guess ({len(incorrect_guesses)} incorrect guesses)"

def play_round(category, secret_word):
    """
    Plays one round of the Hangman game, using the provided category and secret word/phrase.
    """
    partial_word = initialize_partial_word(secret_word)
    correct_guesses = []
    incorrect_guesses = []

    print(f"This one is looking for a {category}:")
    print(' '.join(partial_word))

    while '_' in partial_word and len(incorrect_guesses) < 6:
        guess = input("What is your guess? ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        correct, message = process_user_guess(guess, correct_guesses, incorrect_guesses, partial_word, secret_word)
        print(message)
        print(' '.join(partial_word))

    if '_' not in partial_word:
        print(f"You've guessed the word: {secret_word}")
    else:
        print(f"You've lost! The correct {category} was: {secret_word}")

def main():
    file_name = input("What file will the words come from? ")
    if not os.path.isfile(file_name):
        print("File not found.")
        return

    data_list = read_data_file(file_name)

    play_again = True
    while play_again:
        category, secret_word = select_random_entry(data_list)
        play_round(category, secret_word)
        user_input = input("Would you like to play again? (yes/no): ").lower()
        play_again = user_input == "yes"

if __name__ == "__main__":
    main()
