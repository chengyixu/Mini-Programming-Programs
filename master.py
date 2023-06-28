# Mastermind

# This is a simulation of the game Mastermind.
# There is a secret combination of four colored pegs,
# and then a series of guesses at that combination.
# Correctness is evaluated by a black peg indicating
# that there is a correctly-colored peg in a correct
# position, and a white peg indicating that there is
# a correctly-colored peg in an incorrect position.

# Combinations and guesses in this program will be
# indicated by four-letter strings, where each letter
# is the initial of a color:
# Red, Yellow, Blue, Green, Purple, White

# There will be some randomness in producing
# solutions to guess at, or to make random guesses
import random

# This is a list of the valid colors for general use.
colors = ['R', 'Y', 'B', 'G', 'P', 'W']

# Some functions relating to generating and
# validating combinations

def is_valid(combination):
    '''identifies whether combination is valid:
       four letters from the list defined above
       Returns True or False accordingly'''
    if len(combination) != 4:
        return False
    else:
        valid = True
        for letter in combination:
            if letter not in colors:
                valid = False
        return valid

def random_combination():
    '''A random combination of four letters for this simulation
       random.select() is NOT chosen, because it disallows duplicaties'''
    return (random.choice(colors) + random.choice(colors)
         +  random.choice(colors) + random.choice(colors))

def input_combination():
    '''asks the user for a combination,
       and continues to ask if the input is invalid'''
    combination = input("What would you like to guess? ")
    while not is_valid(combination):
        print("Guess must be four letters from RYBGPW.")
        combination = input("Try again: ")
    return combination

def all_combinations():
    '''generates a list of all valid combinations'''
    combo_list = []
    for first in colors:
        for second in colors:
            for third in colors:
                for fourth in colors:
                    combo_list.append(first+second+third+fourth)
    return combo_list

#  Functions to see if the check_guess function works correctly

def test_check_guess(guess,answer,result,message):
    response = check_guess(guess,answer)
    if response == result:       # It worked!
        return True
    elif len(response) != 2:
        print('Did not get black and white pegs comparing',guess,'to',answer)
        return False
    else:
        print('Got responnse of',response,'comparing',guess,'to',answer)
        print('Correct result would be',result,'--',message)
        return False

def test_checker():
    test_check_guess('RBBB','RGGG',(1,0),'cannot find the black peg')
    test_check_guess('BBBR','GGGR',(1,0),'cannot find the black peg')
    test_check_guess('RRBB','RRGG',(2,0),'did you find both black pegs?')
    test_check_guess('RBBR','RGGR',(2,0),'two black pegs cannot also be white')
    test_check_guess('RRRR','RRRR',(4,0),'four black pegs cannot also be white')
    test_check_guess('RRBB','GGRR',(0,2),'only one white peg per guess peg')
    test_check_guess('RBBB','GGRR',(0,1),'only one white peg per guess peg')
    test_check_guess('RRBB','GGGR',(0,1),'only one white peg per answer peg')
    test_check_guess('RBYW','BYWG',(0,3),'must be able to find all the colors')
    test_check_guess('RBYW','WRBY',(0,4),'must be able to find all the colors')
    test_check_guess('RBYW','RYWB',(1,3),'do not count black peg as white also')
    test_check_guess('RRRR','RGGG',(1,0),'do not count black peg as white also')
    test_check_guess('RGGG','RRRR',(1,0),'do not count black peg as white also')
    test_check_guess('RRRR','GGGR',(1,0),'do not count black peg as white also')
    test_check_guess('GGGR','RRRR',(1,0),'do not count black peg as white also')

# Student work begins below

import random

COLORS = ['R', 'Y', 'B', 'G', 'W', 'P']

# ... other helper functions ...

def check_guess(guess, solution):
    black_pegs = 0
    white_pegs = 0
    guess_copy = list(guess)
    solution_copy = list(solution)

    for i in range(len(guess)):
        if guess[i] == solution[i]:
            black_pegs += 1
            guess_copy[i] = None
            solution_copy[i] = None

    for i in range(len(guess_copy)):
        if guess_copy[i] is not None and guess_copy[i] in solution_copy:
            white_pegs += 1
            solution_copy[solution_copy.index(guess_copy[i])] = None

    return black_pegs, white_pegs

def user_guesses():
    secret_combination = random_combination()
    # print(secret_combination)  # Uncomment this line for debugging purposes
    attempts = 0

    while True:
        user_input = input_combination()
        attempts += 1
        black_pegs, white_pegs = check_guess(user_input, secret_combination)

        if black_pegs == 4:
            print("You got it!")
            break

        print(f"{black_pegs} pegs (correct color in correct location)")
        print(f"{white_pegs} pegs (correct color in incorrect location)")

    print(f"Number of attempts: {attempts}")

def computer_guesses():
    user_combination = input("Choose a secret combination: ").upper()
    viable_candidates = all_combinations()
    attempts = 0

    while True:
        computer_guess = random.choice(viable_candidates)
        print(f"My guess is {computer_guess}")
        attempts += 1

        black_pegs = int(input("How many black pegs (correct color in correct location)? "))
        white_pegs = int(input("How many white pegs (correct color in incorrect location)? "))

        if black_pegs == 4:
            print(f"I guessed your combination in {attempts} attempts!")
            break

        viable_candidates = [
            candidate for candidate in viable_candidates
            if check_guess(computer_guess, candidate) == (black_pegs, white_pegs)
        ]

 
    # Report the solution when found
    if len(pool) == 0:
        print("I could not find any answer that matches your responses.")
    else:
        print("I think I have it!  Your combination is ",pool[0])


#  The 'main' part of this code just alternates
#  between the player guessing and the computer guessing.

#  Once the check_guess function is all correct,
#  the following function call will have no output
test_checker()

print("Welcome to Mastermind!")
yesno = 'y'
while yesno in ['y','Y']:
    print("Try to guess my combination!")
    user_guesses()
    print("My turn, to guess at yours!")
    computer_guesses()
    yesno = input("Play again? ")





