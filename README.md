# Hangman Game in Python

This is a simple command-line Hangman game written in Python.  
The player tries to guess a randomly chosen word letter by letter before running out of lives.

## Features

- Words are loaded from an external JSON file (`data.json`), making it easy to customize the word list.
- Displays progress of the word with correctly guessed letters revealed and unknown letters shown as underscores.
- Limits the number of wrong guesses (lives) based on word length plus extra chances.
- Validates user input to accept only single alphabetical characters.
- Handles repeated guesses and invalid inputs gracefully.
- Prints messages to guide the player and show game status.
