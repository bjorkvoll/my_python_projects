# NUMBER GUESSING GAME
# The user is asked to guess a in the range of 1 to 100.
# The program will then say if the guess is too high, too low, or correct.

import random;

generated_number = random.randrange(1,11)
winning = 0

while winning == 0:
    print("-" * 30)
    print("Guess a number")

    try:
        guess = int(input())
    except ValueError:
        print("You must enter a integer")
        continue

    if guess is generated_number:
        print(f"You guessed: {guess}, and it was correct!")
        winning = 1
    elif guess < generated_number:
        print(f"You guessed: {guess}, but the generated number is higher.")
    elif guess > generated_number:
        print(f"You guessed: {guess}, but the generated number is lower.")
    else:
        print("wow, you broke it")
        break