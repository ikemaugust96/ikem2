import random


def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I picked a number between 1 and 50. Try and guess!")

    # Generate a random number between 1 and 50
    random_number = random.randint(1, 50)

    tries = 0
    user_guess = None

    while user_guess != random_number:
        # Get user input and ensure it is a valid integer
        user_input = input("Enter your guess: ")

        # Validate the input to ensure it's an integer
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue  # Skip to the next iteration if input is invalid

        user_guess = int(user_input)  # Convert input to an integer
        tries += 1

        # Calculate the absolute difference
        difference = abs(random_number - user_guess)

        print(f"You guessed {user_guess}")

        # Determine how far off the guess is and give feedback
        if difference == 0:
            print(f"Congratulations! You figured it out in {tries} tries.")
            break  # Exit the loop when the correct guess is made
        elif difference == 1:
            print("Your guess is scalding hot")
        elif difference == 2:
            print("Your guess is extremely warm")
        elif difference == 3:
            print("Your guess is very warm")
        elif difference <= 5:
            print("Your guess is warm")
        elif difference <= 8:
            print("Your guess is cold")
        elif difference <= 13:
            print("Your guess is very cold")
        elif difference <= 20:
            print("Your guess is extremely cold")
        else:
            print("Your guess is icy freezing miserably cold")

        # Provide additional feedback on whether the guess is too high or too low
        if user_guess > random_number:
            print("Your guess is too high")
        elif user_guess < random_number:
            print("Your guess is too low")


# Start the game
guessing_game()
