# Number Guessing Game --- Python

A simple and fun command-line **Number Guessing Game** written in
Python.\
The computer randomly selects a number, and the player must guess it in
the fewest tries possible.

## Features

-   Random number generation\
-   User input validation\
-   Hint system (higher/lower)\
-   Counts number of attempts\
-   Clean and beginner-friendly Python code

## How the Game Works

1.  The computer selects a random number within a given range (e.g., **1
    to 100**).\
2.  You enter your guess.\
3.  The program tells you whether your guess is **too high**, **too
    low**, or **correct**.\
4.  The game ends when you guess correctly, and it shows how many
    attempts you took.

## Example Code

``` python
import random

number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have picked a number between 1 and 100. Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed the number in {attempts} attempts.")
        break
```

## How to Run the Game

1.  Install Python (if not installed).\
2.  Save the script as `number_guessing_game.py`\
3.  Run it using:

```{=html}
<!-- -->
```
    python number_guessing_game.py

## License

This project is free to use for learning or personal projects.
