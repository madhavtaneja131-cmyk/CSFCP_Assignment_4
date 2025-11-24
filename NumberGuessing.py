import random #importing the random module to generate a random number 
a = int(input("enter a number:")) #taking input from the user to set the range for the random number
secret_number = random.randint(1, a)
# This line generates a random number between 1 and the user-defined number 'a'
print(f"I am thinking of a number between 1 and {a}.") # This line informs the user about the range of the secret number

while True: 
    guess = int(input("Guess the number:- "))# Taking input from the user to guess the secret number
    if guess == secret_number:
        print("You won! Great job.")# If the guess is correct, this line congratulates the user
        break  
    elif guess < secret_number:
        print("Too low!")# If the guess is too low, this line informs the user
    else:
        print("Too high!") # If the guess is too high, this line informs the user

# The loop continues until the user guesses the correct number and also provide feedback on each guess.