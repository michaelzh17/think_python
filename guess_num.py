#!/urs/bin/env python3

# A simple guess game

import random

rng = random.Random()

# 'rng' stands for 'random number generator'
# get random number between 1 and 1000
number = rng.randrange(1, 1000)

guesses = 1

message = ''

while True:
    guess = int(input(message + "Guess the number I have: "))
    guesses += 1

    if guess > number:
        print(str(guess) + " is too high.\n")
    elif guess < number:
        print(str(guess) + " is too low.\n")
    else:
        break

input("\n Great. You've got the number in "+str(guesses)+" guesses!\n")




