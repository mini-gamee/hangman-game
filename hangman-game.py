import random as rd
import json

# Load words from a JSON file named 'data.json'
with open('data.json', 'r') as file:
    data = json.load(file)
words = data['words']

# Letters guessed correctly are shown; others as underscores.


def progress(word, guessletter):
    display = ""
    for letters in word:
        if letters in guessletter:
            display += f"{letters} "
        else:
            display += "_ "
    print(display.strip())


def play_game():

    rdword = rd.choice(words)
    max_life = len(rdword) + 5
    guessletter = set()

    print("Guess Words")
    progress(rdword, guessletter)

    while max_life > 0:
        guessword = player()

        # Handle invalid input
        if guessword is None:
            print("Invalid Input.")
            max_life -= 1
            progress(rdword, guessletter)
            print(f"lives left: {max_life}")
            continue

        # Handle repeated guesses
        if guessword in guessletter:
            print("word already guess")
            continue

        # Add guessed letter to set
        guessletter.add(guessword)

        # Check if guess is correct
        if guessword in rdword:
            print("ok")
        else:
            print("not ok")
            max_life -= 1

        progress(rdword, guessletter)
        print(f"lives left: {max_life}")

        # Check if all letters have been guessed
        if all(letters in guessletter for letters in rdword):
            print("Congrat")
            break
    else:
        print("Game over!")

    print(f"The words was: {rdword}")


def player():

    # Prompt the player to input a single letter
    guess = input("Guess a letter: ")
    if len(guess) == 1 and guess.isalpha():
        return guess.lower()  # Return lowercase letter
    else:
        return None


print(play_game())
