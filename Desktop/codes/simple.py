"""Simple number guessing game."""

import random


def play():
    secret = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?\n")

    while True:
        guess = input("Your guess: ")

        if not guess.isdigit():
            print("Please enter a whole number.\n")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("Too low!\n")
        elif guess > secret:
            print("Too high!\n")
        else:
            print(f"Correct! You got it in {attempts} attempt(s).")
            break


if __name__ == "__main__":
    play()
