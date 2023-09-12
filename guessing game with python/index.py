import random

point = 100
print("You have 100 points")
while True:
    secret_number = random.randint(0, 100)
    max_attempts = 5
   
    
    print("You have 5 attempts to guess the number")

    for attempt in range(max_attempts):
        try:
            guess = int(input("Guess the number (between 1 and 100): "))
        except ValueError:
            print("Invalid input")
            continue  # Skip the rest of this iteration and go to the next attempt

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            point += 10
            print(f"+10 points: {point}")
            break  # Exit the loop if the guess is correct

    if guess != secret_number:
        print(f"Sorry, you're out of attempts. The secret number was: {secret_number}")
        point -= 10
        print(f"-10 points: {point}")

    if point <= 0:
        print("You're out of points. Game over.")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break