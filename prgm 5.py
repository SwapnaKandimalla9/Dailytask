#write a program that generates a random number btw 1 and 100 and asks user to guess 
import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guess the Number Game!")

    while True:
        # Get user input
        user_guess = input("Enter your guess (or 'q' to quit): ")

        # Allow the user to quit
        if user_guess.lower() == 'q':
            print("Thanks for playing!")
            break
        try
            user_guess = int(user_guess)
            attempts += 1

            # Check the user's guess
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")

# Run the game
guess_the_number()
