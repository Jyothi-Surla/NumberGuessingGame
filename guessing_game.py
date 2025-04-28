
import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0
    max_attempts = 7

    print("\n🎯 I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it!")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("📉 Too low!")
            elif guess > number_to_guess:
                print("📈 Too high!")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} tries!")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

    else:
        print(f"\n❌ Sorry! You've used all {max_attempts} attempts.")
        print(f"The correct number was {number_to_guess}.")

def main():
    play_again = "yes"
    while play_again.lower() in ("yes", "y"):
        number_guessing_game()
        play_again = input("\nDo you want to play again? (yes/no): ")
    print("\n👋 Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main()

