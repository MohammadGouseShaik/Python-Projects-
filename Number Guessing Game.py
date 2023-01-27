import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Prompt the user to guess the number
guess = int(input("Guess a number between 1 and 100: "))

# Keep track of the number of guesses
guesses = 1

# Loop until the user guesses the correct number
while guess != number:
    if guess > number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    guess = int(input("Guess a number between 1 and 100: "))
    guesses += 1

# Let the user know they've guessed the correct number
print("Congratulations! You guessed the number in", guesses, "tries.")
