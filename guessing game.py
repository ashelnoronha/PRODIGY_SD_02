import random
def guessing_game():
    num = random.randint(1,100)
    attempts = 0
    print("Welcome to the guessing game!\n")
    print("How to play: \n I'll pick a number between 1 and 100 \n Try to guess the number with the least number of attempts. \n Good luck! \n")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < num:
                print("Too low. Try again!")
            elif guess > num:
                print("Too high. Try again!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
guessing_game()