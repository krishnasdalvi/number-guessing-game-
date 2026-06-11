import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game")
    print("I am thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess_input = input("Enter your guess (or type 'quit' to exit): ").strip()
        
        if guess_input.lower() == 'quit':
            print("The number was " + str(secret_number) + ". Thanks for playing.")
            break
            
        if not guess_input.isdigit():
            print("Invalid input. Please enter a whole number between 1 and 100.")
            continue
            
        guess = int(guess_input)
        attempts += 1
        
        if guess < 1 or guess > 100:
            print("Out of bounds. Please guess a number between 1 and 100.")
        elif guess < secret_number:
            print("Too low. Try a higher number.")
        elif guess > secret_number:
            print("Too high. Try a lower number.")
        else:
            print("Correct. You guessed it in " + str(attempts) + " attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()