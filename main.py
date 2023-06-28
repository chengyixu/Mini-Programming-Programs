import random
from hangman import draw_hangman

# Define the word bank and initialize variables:

words = ["programming", "python", "language", "hangman", "game"]
word = ""
tiles = []
remaining_letters = 0
guesses = 5
guessed_letters = []

# Handle the seed input:

def get_seed_input():
    while True:
        seed_choice = input("Would you like to enter a seed? (y/n): ").lower()
        if seed_choice == "y" or seed_choice == "n":
            break
        else:
            print("Error: answer must be y or n")
    return seed_choice

seed_choice = get_seed_input()

if seed_choice == "y":
    while True:
        seed = input("Please enter a seed: ")
        if seed.isdigit() and int(seed) >= 0:
            random.seed(int(seed))
            break
        else:
            print("ERROR: Invalid seed.")

# Select the random word and create the initial tiles list:

word = random.choice(words)
tiles = ["_" for _ in word]
remaining_letters = len(word)

# Implement the game loop:

while remaining_letters > 0 and guesses > 0:
    draw_hangman(tiles, f"Letters remaining: {remaining_letters:^30}", guesses, ", ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if guess.isalpha() and len(guess) == 1:
        if guess not in guessed_letters:
            guessed_letters.append(guess)

            if guess in word:
                letter_count = 0
                for i, letter in enumerate(word):
                    if letter == guess:
                        tiles[i] = guess
                        letter_count += 1
                remaining_letters -= letter_count
            else:
                guesses -= 1
        else:
            print("You have already guessed that letter!")
    else:
        guesses -= 1


# Display the game result:

if remaining_letters == 0:
    print("You win!")
else:
    print("You lost!")

print(f"The word was {word}!")